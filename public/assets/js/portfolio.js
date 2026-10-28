;(() => {
  document.addEventListener("click", (e) => {
    const b = e.target.closest(".theme-toggle")
    if (b) {
      const t =
        document.documentElement.dataset.theme === "dark" ? "light" : "dark"
      document.documentElement.dataset.theme = t
      try {
        localStorage.setItem("portfolio-theme", t)
      } catch {}
      b.setAttribute(
        "aria-label",
        "Switch to " + (t === "dark" ? "light" : "dark") + " theme",
      )
    }
    document.querySelectorAll(".portfolio-more[open]").forEach((d) => {
      if (!d.contains(e.target)) d.open = false
    })
  })
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape")
      document.querySelectorAll(".portfolio-more[open]").forEach((d) => {
        d.open = false
        d.querySelector("summary").focus()
      })
  })
})()
;(() => {
  const input = document.getElementById("resource-filter")
  if (!input) return
  const entries = [...document.querySelectorAll("[data-resource]")]
  const count = document.getElementById("resource-count")
  const update = () => {
    const term = input.value.trim().toLowerCase()
    let visible = 0
    entries.forEach((entry) => {
      entry.hidden = !entry.textContent.toLowerCase().includes(term)
      if (!entry.hidden) visible++
    })
    count.textContent = visible
      ? `${visible} resources to explore`
      : "No resources match. Try another topic."
  }
  input.addEventListener("input", update)
  update()
})()
