/** Read-only built-artifact browser fixture; does not start a development server. */
const fs = require("node:fs/promises")
const path = require("node:path")
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || "playwright")

const root = path.resolve(__dirname, "..")
const dist = path.join(root, "dist")
const origin = "http://localhost:3000"
const types = {
  ".html": "text/html",
  ".js": "text/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".webp": "image/webp",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".webmanifest": "application/manifest+json",
}
;(async () => {
  const targets = JSON.parse(
    await fs.readFile(path.join(root, "research/page-targets.json")),
  )
  const browser = await chromium.launch({
    headless: true,
    ...(process.env.CHROMIUM_EXECUTABLE
      ? { executablePath: process.env.CHROMIUM_EXECUTABLE }
      : {}),
    args: ["--no-sandbox"],
  })
  const context = await browser.newContext({
    viewport: { width: 1440, height: 1000 },
    colorScheme: "light",
    permissions: ["clipboard-read", "clipboard-write"],
  })
  await context.route(`${origin}/**`, async (route) => {
    const url = new URL(route.request().url())
    const filename = path.resolve(
      dist,
      "." + (url.pathname === "/" ? "/index.html" : url.pathname),
    )
    if (!filename.startsWith(dist + path.sep))
      return route.fulfill({ status: 403, body: "Forbidden" })
    try {
      const body = await fs.readFile(filename)
      return route.fulfill({
        status: 200,
        body,
        contentType:
          types[path.extname(filename)] || "application/octet-stream",
      })
    } catch {
      return route.fulfill({ status: 404, body: "Missing built asset" })
    }
  })
  const page = await context.newPage()
  const result = {}
  let activeErrors = []
  page.on("pageerror", (e) => activeErrors.push(e.message))
  page.on("console", (m) => {
    if (
      m.type() === "error" &&
      /hydration|duplicate key|Minified React|unique.*key/i.test(m.text())
    ) {
      activeErrors.push(m.text())
    }
  })
  for (const route of Object.keys(targets).sort()) {
    activeErrors = []
    const row = {
      errors: [],
      overflow: false,
      viewports: [],
      method:
        "Built files served through a read-only Playwright route fixture, not production hosting",
    }
    for (const width of [1440, 390]) {
      await page.setViewportSize({ width, height: 1000 })
      const started = Date.now()
      await page.goto(origin + route, { waitUntil: "load" })
      await page.waitForSelector("main h1")
      await page.evaluate(async () => {
        // Exercise lazy delivery copies without permanently altering source.
        for (const img of document.images) img.loading = "eager"
        await Promise.all(
          [...document.images].map((img) => img.decode().catch(() => {})),
        )
      })
      const observed = await page.evaluate(() => ({
        h1: [...document.querySelectorAll("main h1")].map((e) =>
          e.textContent.trim(),
        ),
        title: document.title,
        overflow: document.documentElement.scrollWidth > innerWidth,
        missingImages: [...document.images]
          .filter(
            (e) =>
              (e.getAttribute("src") || e.getAttribute("srcset")) &&
              !e.naturalWidth,
          )
          .map((e) => e.currentSrc || e.src),
        forms: document.forms.length,
      }))
      row.viewports.push({
        width,
        ...observed,
        localFixtureLoadMs: Date.now() - started,
      })
      row.overflow ||= observed.overflow
      if (observed.h1.length !== 1) row.errors.push(`H1 count at ${width}`)
      if (observed.missingImages.length)
        row.errors.push(`Images failed at ${width}: ${observed.missingImages}`)
      if (width === 390) {
        const menu = page.getByRole("button", { name: /^(Menu|Close)/ })
        if (await menu.count()) {
          await menu.click()
          if ((await menu.getAttribute("aria-expanded")) !== "true")
            row.errors.push("Mobile menu did not open")
          await page.keyboard.press("Escape")
          if ((await menu.getAttribute("aria-expanded")) !== "false")
            row.errors.push("Mobile menu Escape did not close")
        }
      }
    }
    row.errors.push(...activeErrors)
    result[route] = row
    console.log(route, row.errors.length || row.overflow ? "REVIEW" : "PASS")
  }
  await page.setViewportSize({ width: 1440, height: 1000 })
  await page.goto(origin + "/")
  await page.locator("#directory-search").fill("API")
  const directoryCount = await page.locator(".collection-list a").count()
  if (!directoryCount)
    throw Error("Hydrated directory search returned no API matches")
  await page
    .getByRole("button", { name: "Share Bakhtawar Khan’s founder profile" })
    .click()
  await page.waitForFunction(() =>
    document.querySelector(".share-status")?.textContent.includes("copied"),
  )
  const share = await page.locator(".share-status").innerText()
  if (!share.includes("copied"))
    throw Error("Clipboard sharing fallback did not run")
  const pause = page.getByRole("button", { name: "Pause motion" }).first()
  await pause.click()
  if (
    (await page
      .getByRole("button", { name: "Resume motion" })
      .first()
      .getAttribute("aria-pressed")) !== "true"
  )
    throw Error("Homepage gallery pause did not update")
  result["/"].galleryMotion = "Pause control passed"
  await page.goto(origin + "/gallery.html")
  await page.locator("main a:has(img)").first().click()
  await page.locator("#mbk-image-preview[open]").waitFor()
  await page.getByRole("button", { name: "Close image preview" }).click()
  result["/gallery.html"].lightbox =
    "Open/close passed using the local delivery image"
  for (const route of ["/contact.html", "/hire-me.html", "/book-a-call.html"]) {
    await page.goto(origin + route)
    await page.evaluate(() => {
      window.__seoOpened = []
      window.open = (url) => {
        window.__seoOpened.push(String(url))
        return null
      }
      for (const e of document.querySelectorAll(
        "form input, form textarea, form select",
      )) {
        if (e.tagName === "SELECT") {
          e.value = [...e.options].find((o) => o.value)?.value || ""
        } else if (e.type === "checkbox") e.checked = true
        else
          e.value =
            e.type === "email"
              ? "seo-check@example.invalid"
              : e.name === "phone"
                ? "0000000000"
                : "Local SEO validation only"
        e.dispatchEvent(new Event("input", { bubbles: true }))
        e.dispatchEvent(new Event("change", { bubbles: true }))
      }
      document.querySelector("form").requestSubmit()
    })
    const opened = await page.evaluate(() => window.__seoOpened)
    if (!opened.some((u) => u.startsWith("https://wa.me/923200276941?text="))) {
      throw Error("WhatsApp compose preparation failed on " + route)
    }
    result[route].formCompose =
      "Passed with intercepted window.open; no message sent"
  }
  await page.goto(origin + "/about.html")
  await page.getByRole("button", { name: /Switch.*theme/ }).click()
  const theme = await page.locator("html").getAttribute("data-theme")
  if (theme !== "dark") throw Error("Theme toggle did not update")
  result["/about.html"].darkTheme = "Passed"
  result["/"].hydratedSearch = `Passed (${directoryCount} API results)`
  result["/"].clipboardShare = "Passed; OS native share delivery not tested"
  await fs.mkdir(path.join(root, "implementation/screenshots"), {
    recursive: true,
  })
  for (const [route, name] of [
    ["/", "home"],
    ["/about.html", "founder"],
    ["/article-api-integration.html", "api-guide"],
  ]) {
    await page.goto(origin + route)
    await page.setViewportSize({ width: 1440, height: 1000 })
    await page.screenshot({
      path: path.join(root, `implementation/screenshots/${name}-desktop.png`),
      animations: "disabled",
    })
    await page.setViewportSize({ width: 390, height: 844 })
    await page.screenshot({
      path: path.join(root, `implementation/screenshots/${name}-mobile.png`),
      animations: "disabled",
    })
  }
  await fs.writeFile(
    path.join(root, "implementation/rendered-validation.json"),
    JSON.stringify(result, null, 2),
  )
  await browser.close()
  if (Object.values(result).some((r) => r.errors.length || r.overflow))
    process.exitCode = 1
})().catch((error) => {
  console.error(error)
  process.exit(1)
})
