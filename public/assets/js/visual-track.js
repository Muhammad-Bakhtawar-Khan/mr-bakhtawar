/* One dependency-free controller for the static pages' compact author archive. */
;(() => {
  const host = document.querySelector("[data-portrait-track]")
  if (host) {
    fetch("/assets/data/portrait-track.json")
      .then((r) => {
        if (!r.ok) throw Error("Archive unavailable")
        return r.json()
      })
      .then((images) => {
        const section = document.createElement("section")
        section.className = "global-archive"
        section.setAttribute("aria-label", "Personal image archive")
        const heading = document.createElement("div")
        heading.className = "archive-heading"
        const title = document.createElement("h2")
        title.textContent = host.dataset.caption
        const link = document.createElement("a")
        link.href = "/gallery.html"
        link.textContent = "Personal gallery ↗"
        const toggle = document.createElement("button")
        toggle.type = "button"
        toggle.textContent = "Pause motion"
        toggle.setAttribute("aria-pressed", "false")
        heading.append(title, link, toggle)
        const viewport = document.createElement("div")
        viewport.className = "archive-viewport"
        viewport.tabIndex = 0
        viewport.setAttribute(
          "aria-label",
          "Personal photographs; scroll horizontally to explore",
        )
        const track = document.createElement("div")
        track.className = "archive-track"
        for (let copy = 0; copy < 2; copy++) {
          const set = document.createElement("div")
          set.className = "archive-set"
          if (copy) set.setAttribute("aria-hidden", "true")
          for (const image of images.slice(0, 4)) {
            const img = document.createElement("img")
            img.src = image.src
            if (image.srcset) {
              img.srcset = image.srcset
              img.sizes = "160px"
            }
            img.alt = copy ? "" : image.alt
            img.width = image.width
            img.height = image.height
            img.loading = "lazy"
            img.decoding = "async"
            set.append(img)
          }
          track.append(set)
        }
        viewport.append(track)
        section.append(heading, viewport)
        host.replaceWith(section)
        toggle.addEventListener("click", () => {
          const paused = section.classList.toggle("is-paused")
          toggle.setAttribute("aria-pressed", String(paused))
          toggle.textContent = paused ? "Resume motion" : "Pause motion"
        })
        viewport.addEventListener(
          "touchstart",
          () => {
            section.classList.add("is-paused")
            toggle.setAttribute("aria-pressed", "true")
            toggle.textContent = "Resume motion"
          },
          { passive: true },
        )
        // Do not spend animation work on an offscreen footer.
        const observer = new IntersectionObserver((entries) => {
          track.style.animationPlayState = entries[0].isIntersecting
            ? ""
            : "paused"
        })
        observer.observe(section)
      })
      .catch(() => host.remove())
  }
  const search = document.getElementById("note-search")
  if (search) {
    const notes = [...document.querySelectorAll(".note-card")]
    const update = () => {
      const q = search.value.trim().toLowerCase()
      let count = 0
      notes.forEach((n) => {
        n.hidden = !n.textContent.toLowerCase().includes(q)
        if (!n.hidden) count++
      })
      document.getElementById("note-count").textContent = `${count} notes found`
    }
    search.addEventListener("input", update)
    update()
  }
})()
