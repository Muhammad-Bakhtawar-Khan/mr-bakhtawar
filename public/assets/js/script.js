;(() => {
  const menuButton = document.querySelector(".menu-toggle")
  const nav = document.querySelector(".nav")
  if (menuButton && nav) {
    menuButton.addEventListener("click", () => {
      const open = nav.classList.toggle("open")
      menuButton.setAttribute("aria-expanded", String(open))
      menuButton.setAttribute(
        "aria-label",
        open ? "Close navigation" : "Open navigation",
      )
      menuButton.innerHTML = open
        ? "× <span>Close</span>"
        : "☰ <span>Menu</span>"
    })
    nav.querySelectorAll("a").forEach((link) =>
      link.addEventListener("click", () => {
        nav.classList.remove("open")
        menuButton.setAttribute("aria-expanded", "false")
        menuButton.setAttribute("aria-label", "Open navigation")
        menuButton.innerHTML = "☰ <span>Menu</span>"
        const more = nav.querySelector(".nav-more")
        if (more) more.removeAttribute("open")
      }),
    )
  }
  const year = document.getElementById("year")
  if (year) year.textContent = new Date().getFullYear()

  const projectForm = document.getElementById("whatsappProjectForm")
  if (projectForm) {
    projectForm.addEventListener("submit", (event) => {
      event.preventDefault()
      if (!projectForm.reportValidity()) return
      const data = new FormData(projectForm)
      const message = [
        "NEW PROJECT ENQUIRY — Bakhtawar Khan / MBK",
        "",
        "Name: " + data.get("name"),
        "Phone / WhatsApp: " + data.get("phone"),
        "Email: " + (data.get("email") || "Not provided"),
        "Service: " + data.get("service"),
        "Budget: " + (data.get("budget") || "Not specified"),
        "Timeline: " + (data.get("timeline") || "Flexible"),
        "",
        "Project details:",
        data.get("details"),
      ].join("\n")
      const success = document.getElementById("formSuccess")
      if (success) {
        success.hidden = false
        success.scrollIntoView({ behavior: "smooth", block: "nearest" })
      }
      const url =
        "https://wa.me/923200276941?text=" + encodeURIComponent(message)
      window.open(url, "_blank", "noopener,noreferrer")
    })
  }
})()

// Accessible, dependency-free image preview for the personal gallery.
;(() => {
  const gallery = document.querySelector(
    ".gallery-grid, .gallery-images, .photo-grid, .gallery, .photo-gallery",
  )
  if (!gallery || document.getElementById("mbk-image-preview")) return
  const links = Array.from(gallery.querySelectorAll("a:has(img)"))
  if (!links.length) return
  const dialog = document.createElement("dialog")
  dialog.id = "mbk-image-preview"
  dialog.setAttribute("aria-label", "Gallery image preview")
  dialog.innerHTML =
    '<div class="mbk-preview-bar"><p class="mbk-preview-caption" id="mbk-preview-caption"></p><button type="button" class="mbk-preview-close" aria-label="Close image preview">Close ×</button></div><img class="mbk-preview-image" alt="">'
  document.body.appendChild(dialog)
  const previewImg = dialog.querySelector("img")
  const caption = dialog.querySelector(".mbk-preview-caption")
  const close = dialog.querySelector(".mbk-preview-close")
  links.forEach((link) => {
    const img = link.querySelector("img")
    if (!img) return
    link.addEventListener("click", (event) => {
      if (typeof dialog.showModal !== "function") return
      event.preventDefault()
      previewImg.src = img.currentSrc || img.src
      previewImg.alt = img.alt || "Gallery photograph"
      caption.textContent = img.title || img.alt || "Gallery photograph"
      dialog.showModal()
      close.focus()
    })
  })
  close.addEventListener("click", () => dialog.close())
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) dialog.close()
  })
  dialog.addEventListener("close", () => {
    previewImg.removeAttribute("src")
  })
})()
