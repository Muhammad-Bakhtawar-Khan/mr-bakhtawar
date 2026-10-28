;(() => {
  const button = document.querySelector(".academy-menu")
  const nav = document.getElementById("academy-nav")
  button?.addEventListener("click", () => {
    const open = nav.classList.toggle("open")
    button.setAttribute("aria-expanded", String(open))
    button.querySelector("span").textContent = open ? "−" : "+"
  })
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && nav?.classList.contains("open")) {
      nav.classList.remove("open")
      button.setAttribute("aria-expanded", "false")
      button.querySelector("span").textContent = "+"
      button.focus()
    }
  })
  const search = document.getElementById("library-search")
  if (search) {
    const entries = [...document.querySelectorAll(".journal-article")]
    const results = document.getElementById("library-results")
    const update = () => {
      const query = search.value.trim().toLowerCase()
      entries.forEach(
        (entry) =>
          (entry.hidden = !entry.textContent.toLowerCase().includes(query)),
      )
      const count = entries.filter((entry) => !entry.hidden).length
      results.textContent = count
        ? `${count} articles to explore`
        : "No matching articles. Try a broader topic."
    }
    search.addEventListener("input", update)
    update()
  }
})()
