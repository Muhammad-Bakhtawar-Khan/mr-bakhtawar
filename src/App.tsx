import { useEffect, useMemo, useState } from "react"
import directory from "./page-directory.json"
import galleryImages from "./gallery-showcase.json"
const photo = "/assets/images/optimized/"
const paths = [
  {
    number: "01",
    title: "Build for the web",
    description:
      "From semantic HTML to responsive interfaces. Start with the foundations, then make something real.",
    route: "/web-performance-and-ux-guide.html",
    topics: "WEB DEVELOPMENT / UX",
    mark: "</>",
  },
  {
    number: "02",
    title: "Connect the dots",
    description:
      "Explore APIs, practical automation, and responsible AI workflows—with people in the loop.",
    route: "/automation-and-ai-workflows-guide.html",
    topics: "APIS / AI / AUTOMATION",
    mark: "↔",
  },
  {
    number: "03",
    title: "Make your work discoverable",
    description:
      "Clear content, technical SEO, and a consistent digital identity. Help the right people find your work.",
    route: "/technical-seo-checklist-mbk.html",
    topics: "SEO / CONTENT / IDENTITY",
    mark: "Aa",
  },
]
export default function App() {
  const [galleryPaused, setGalleryPaused] = useState(false)
  const [shareStatus, setShareStatus] = useState("")
  const [menu, setMenu] = useState(false),
    [query, setQuery] = useState(""),
    [category, setCategory] = useState("All")
  useEffect(() => {
    const closeMenu = (event: KeyboardEvent) => {
      if (event.key === "Escape" && menu) {
        setMenu(false)
        document.querySelector<HTMLButtonElement>(".academy-menu")?.focus()
      }
    }
    document.addEventListener("keydown", closeMenu)
    return () => document.removeEventListener("keydown", closeMenu)
  }, [menu])
  const pages = useMemo(
    () =>
      directory.filter(
        (p) =>
          (category === "All" || p.family === category) &&
          `${p.title} ${p.description}`
            .toLowerCase()
            .includes(query.toLowerCase()),
      ),
    [query, category],
  )

  const shareProfile = async () => {
    const shareData = {
      title: "Mr Bakhtawar | Bakhtawar Khan Portfolio",
      text: "Explore Bakhtawar Khan’s digital portfolio, projects, and work through MBK Global.",
      url: new URL("/about.html", window.location.href).href,
    }

    try {
      if (navigator.share) {
        await navigator.share(shareData)
        setShareStatus("Profile shared")
      } else if (navigator.clipboard) {
        await navigator.clipboard.writeText(shareData.url)
        setShareStatus("Profile link copied")
      } else {
        window.location.href = `mailto:?subject=${encodeURIComponent(shareData.title)}&body=${encodeURIComponent(`${shareData.text}\n\n${shareData.url}`)}`
        setShareStatus("Opening your email app")
      }
    } catch (error) {
      if (error instanceof DOMException && error.name === "AbortError") return
      setShareStatus("Unable to share right now")
    }
  }

  return (
    <div className="academy home master-refresh">
      <a className="skip-link" href="#main-content">
        Skip to content
      </a>
      <header className="academy-header" id="top">
        <a className="academy-brand personal-brand" href="/">
          <span>
            Bakhtawar Khan<small>Personal Digital Portfolio · MBK Global</small>
          </span>
        </a>
        <button
          className="academy-menu"
          aria-expanded={menu}
          onClick={() => setMenu(!menu)}
          aria-controls="academy-nav"
        >
          {menu ? "Close" : "Menu"} <span>{menu ? "−" : "+"}</span>
        </button>
        <nav
          id="academy-nav"
          className={menu ? "open" : ""}
          aria-label="Main navigation"
        >
          <a href="/" aria-current="page">
            Home
          </a>
          <a href="/about.html">About</a>
          <a href="/projects.html">Projects</a>
          <a href="/services.html">Services</a>
          <a href="/hire-me.html" className="header-cta">
            Let’s talk <span aria-hidden="true">↗</span>
          </a>
          <details className="portfolio-more">
            <summary>More</summary>
            <div className="portfolio-panel">
              <section>
                <h2>Professional work</h2>
                <a href="/case-studies.html">Case Studies</a>
                <a href="/changelog.html">Projects Changelog</a>
                <a href="/delivered-project.html">Process</a>
                <a href="/resources.html">Resources</a>
                <a href="/news.html">Notes</a>
              </section>
              <section>
                <h2>Contact & career</h2>
                <a href="/book-a-call.html">Book a Call</a>
                <a href="/resume.html">Resume / CV</a>
                <a href="/hire-me.html">Hire Me</a>
              </section>
              <section>
                <h2>Content & media</h2>
                <a href="/gallery.html">Gallery</a>
                <a href="/blog.html">Blog & Articles</a>
                <a href="/faq.html">FAQs</a>
              </section>
              <section>
                <h2>Personal brand</h2>
                <a href="/about.html">Founder Profile</a>
                <a href="/social.html">Social Profiles</a>
                <a href="/official-links.html">Official Links</a>
              </section>
            </div>
          </details>
          <button
            className="theme-toggle"
            type="button"
            aria-label="Switch color theme"
          >
            ◐
          </button>
        </nav>
      </header>
      <main id="main-content">
        <div className="home-edition">
          <span>MR. BAKHTAWAR PORTFOLIO</span>
          <span>INDEPENDENT THINKING. PURPOSEFUL MAKING.</span>
        </div>
        <section className="home-hero">
          <div className="home-hero-copy">
            <p className="academy-kicker">
              <span className="status-dot" /> THE PERSON. THE PROCESS. THE
              PORTFOLIO.
            </p>
            <h1>
              Thoughtful code.
              <br />
              Human <em>purpose.</em>
            </h1>
            <p className="home-lede">
              I’m Bakhtawar Khan, known online as Mr Bakhtawar and founder of
              MBK Global. My work connects web development, APIs and practical
              automation—with a curiosity for how software works beneath the
              surface.
            </p>
            <div className="home-actions">
              <a className="button" href="/projects.html">
                Explore my work <span>↗</span>
              </a>
              <a className="academy-text-link" href="/about.html">
                Meet the founder <span aria-hidden="true">↗</span>
              </a>
            </div>
            <div className="hero-subnote">
              <span className="tiny-line" />
              <p>
                Independent projects. Thoughtful development.
                <br />
                Modern JavaScript · React · APIs · AI & automation
              </p>
            </div>
          </div>
          <figure className="home-hero-portrait">
            <div className="portrait-mat">
              <img
                src={photo + "bakhtawar-standing-white-portrait-960.webp"}
                srcSet={`${photo}bakhtawar-standing-white-portrait-480.webp 480w, ${photo}bakhtawar-standing-white-portrait-960.webp 960w`}
                sizes="(max-width: 760px) calc(100vw - 68px), (max-width: 1100px) 42vw, 540px"
                alt="Bakhtawar Khan, founder of MBK Global, standing in a professional portrait"
                width="960"
                height="1440"
                decoding="async"
                fetchPriority="high"
              />
              <span className="portrait-index">THE FOUNDER / MBK GLOBAL</span>
            </div>
            <figcaption>
              <span>
                Bakhtawar Khan
                <small>Founder of MBK Global</small>
              </span>
              <span className="portrait-actions">
                <button
                  type="button"
                  className="profile-share"
                  onClick={shareProfile}
                  aria-label="Share Bakhtawar Khan’s founder profile"
                  title="Share founder profile"
                >
                  <svg viewBox="0 0 24 24" aria-hidden="true">
                    <circle cx="18" cy="5" r="2.5" />
                    <circle cx="6" cy="12" r="2.5" />
                    <circle cx="18" cy="19" r="2.5" />
                    <path d="m8.2 10.8 7.5-4.4M8.2 13.2l7.5 4.4" />
                  </svg>
                </button>
                <a
                  href="/about.html"
                  aria-label="Open Bakhtawar Khan’s founder profile"
                >
                  ↗
                </a>
              </span>
            </figcaption>
            <span className="share-status" role="status" aria-live="polite">
              {shareStatus}
            </span>
          </figure>
        </section>
        <div className="home-topics">
          <span>THE THREADS THAT CONNECT MY WORK</span>
          <a href="/web-development.html">Web & design</a>
          <b>·</b>
          <a href="/ai-api-integration.html">AI & APIs</a>
          <b>·</b>
          <a href="/automation-and-ai-workflows-guide.html">Automation</a>
          <b>·</b>
          <a href="/technical-seo.html">Search & discovery</a>
        </div>
        <section className="home-section learning" id="learning">
          <div className="home-heading">
            <div>
              <p className="academy-kicker">01 / FOLLOW YOUR CURIOSITY</p>
              <h2>
                A good place
                <br />
                to <em>begin.</em>
              </h2>
            </div>
            <p>
              You don’t need to know everything.
              <br />
              Start with a question. Follow a thread.
              <br />
              Learn something you can use.
            </p>
            <a className="academy-text-link" href="/resources.html">
              The resource library ↗
            </a>
          </div>
          <div className="learning-paths">
            {paths.map((p) => (
              <a href={p.route} className="learning-path" key={p.number}>
                <div className="path-top">
                  <span>{p.number} / LEARNING PATH</span>
                  <span className="path-symbol">{p.mark}</span>
                </div>
                <p className="path-topics">{p.topics}</p>
                <h3>{p.title}</h3>
                <p>{p.description}</p>
                <span className="path-link">
                  Explore the essentials <b>↗</b>
                </span>
              </a>
            ))}
          </div>
        </section>
        <section className="home-section home-work" id="work">
          <div className="home-heading">
            <div>
              <p className="academy-kicker">
                02 / KNOWLEDGE, PUT INTO PRACTICE
              </p>
              <h2>
                Ideas are good.
                <br />
                <em>Making is better.</em>
              </h2>
            </div>
            <p>
              Each experiment starts with a question.
              <br />
              These are a few of the answers so far.
            </p>
            <a className="academy-text-link" href="/projects.html">
              All projects ↗
            </a>
          </div>
          <div className="home-projects">
            <a href="/article-mbk-tv.html" className="home-project-feature">
              <div className="home-tv-art">
                <span>MBK / DIGITAL MEDIA EXPLORATION</span>
                <div>
                  MBK<span>TV</span>
                  <small>A WINDOW TO WHAT’S ON.</small>
                </div>
                <span className="project-art-corner">01 ↗</span>
              </div>
              <div className="home-project-caption">
                <div>
                  <span>MEDIA / WEB PLATFORM</span>
                  <h3>MBK TV</h3>
                  <p>
                    A digital destination for exploring available live channels.
                  </p>
                </div>
                <b>↗</b>
              </div>
            </a>
            <div className="home-project-side">
              <a href="/article-mbk-markets.html">
                <span className="mini-project-index">
                  02 / DATA & DISCOVERY
                </span>
                <div className="mini-market">
                  <span>MBK Markets</span>
                  <div className="mini-bars">
                    {[35, 55, 42, 75, 60, 92, 80, 110].map((_, i) => (
                      <i key={i} />
                    ))}
                  </div>
                </div>
                <h3>
                  A clearer view of the market. <b>↗</b>
                </h3>
                <p>
                  Exploring how to make complex market information easier to
                  navigate.
                </p>
              </a>
              <a className="handwriting-project" href="/article-mbk-tools.html">
                <span className="mini-project-index">
                  03 / SMALL TOOLS, USEFUL OUTCOMES
                </span>
                <h3>
                  Make text feel
                  <br />
                  <em>a little more human.</em>
                  <b>↗</b>
                </h3>
                <p>Text to Handwriting & MBK Downloader</p>
              </a>
            </div>
          </div>
          <a className="quran-strip" href="/article-noor-e-quran.html">
            <span>ALSO IN THE PROJECT JOURNAL</span>
            <strong>Noor-e-Quran</strong>
            <p>Exploring a calmer digital learning experience.</p>
            <b>↗</b>
          </a>
        </section>
        <section className="home-section home-story" id="about">
          <div className="story-photo">
            <img
              src={photo + "bakhtawar-seated-navy-portrait-960.webp"}
              srcSet={`${photo}bakhtawar-seated-navy-portrait-480.webp 480w, ${photo}bakhtawar-seated-navy-portrait-960.webp 960w`}
              sizes="(max-width: 760px) calc(100vw - 68px), 410px"
              width="960"
              height="960"
              decoding="async"
              alt="Portrait of Bakhtawar Khan"
              loading="lazy"
            />
            <span>THE PERSON BEHIND THE PROJECTS</span>
          </div>
          <div className="home-story-copy">
            <p className="academy-kicker">03 / THE PERSON BEHIND THE WORK</p>
            <h2>
              Bakhtawar Khan.
              <br />A builder, <em>by nature.</em>
            </h2>
            <p className="story-intro">
              Founder of MBK Global. Curious about technology. Serious about
              making it useful.
            </p>
            <div className="founder-interests" aria-label="Technical interests">
              <span>Web development</span>
              <span>AI & APIs</span>
              <span>Automation</span>
              <span>Technical SEO</span>
            </div>
            <p>
              I’m Bakhtawar Khan, the person behind MBK Global. My work spans
              websites, APIs, practical AI, automation, and the many small
              details that make digital experiences useful.
            </p>
            <p>
              Some projects work on the first try. Most teach me something. This
              is a living record of that process: the work, the thinking, and
              the person behind it.
            </p>
            <div
              className="story-process"
              aria-label="My six-step project process"
            >
              {[
                "Understand",
                "Plan",
                "Design",
                "Develop",
                "Test",
                "Deliver",
              ].map((step, index) => (
                <span key={step}>
                  <b>{String(index + 1).padStart(2, "0")}</b>
                  {step}
                </span>
              ))}
            </div>
            <div className="founder-links">
              <a className="academy-text-link" href="/about.html">
                My story & approach ↗
              </a>
              <a className="academy-text-link" href="/contact.html">
                Discuss a project ↗
              </a>
            </div>
            <div className="story-signoff">
              <span>Bakhtawar Khan</span>
              <small>FOUNDER, MBK GLOBAL</small>
            </div>
          </div>
        </section>
        <section className="home-section home-journal">
          <div className="home-heading">
            <div>
              <p className="academy-kicker">04 / FROM THE NOTEBOOK</p>
              <h2>
                Useful thoughts.
                <br />
                <em>Not just more noise.</em>
              </h2>
            </div>
            <a className="academy-text-link" href="/blog.html">
              Browse the journal ↗
            </a>
          </div>
          <div className="journal-feature-layout">
            <a className="journal-lead" href="/article-ai-automation.html">
              <span className="academy-kicker">
                AI & AUTOMATION / PRACTICAL NOTES
              </span>
              <div className="journal-diagram">
                <span>Understand</span>
                <i>→</i>
                <span>Build</span>
                <i>→</i>
                <span>Review</span>
              </div>
              <h3>
                Design the workflow.
                <br />
                <em>Then write the prompt.</em>
              </h3>
              <p>
                Good automation begins with understanding the task—not choosing
                the tool. A practical starting point for responsible AI.
              </p>
              <span className="academy-text-link">Read the field notes ↗</span>
            </a>
            <div className="journal-list">
              {[
                [
                  "01",
                  "WEB CRAFT",
                  "React performance: measure before you optimize.",
                  "/article-react-performance.html",
                ],
                [
                  "02",
                  "SEARCH & DISCOVERY",
                  "Technical SEO, without the mystery.",
                  "/technical-seo-checklist-mbk.html",
                ],
                [
                  "03",
                  "THE BIGGER PICTURE",
                  "One person. One identity. Connected work.",
                  "/generative-search-entity-clarity.html",
                ],
              ].map(([n, c, t, r]) => (
                <a href={r} key={n}>
                  <span>{n}</span>
                  <div>
                    <small>{c}</small>
                    <h3>{t}</h3>
                  </div>
                  <b>↗</b>
                </a>
              ))}
            </div>
          </div>
        </section>
        <section className="home-section home-principles">
          <div>
            <p className="academy-kicker">05 / THE WAY I WORK</p>
            <h2>
              Technology should
              <br />
              work <em>for people.</em>
            </h2>
            <p>Useful outcomes matter. So does how we get there.</p>
            <a className="academy-text-link" href="/services.html">
              Explore services & approach ↗
            </a>
          </div>
          <div className="principle-list">
            {[
              [
                "01",
                "Respect privacy",
                "Collect only what’s needed. Be clear about how information is used.",
              ],
              [
                "02",
                "Make room for everyone",
                "Readable content, keyboard access, and layouts that work across devices.",
              ],
              [
                "03",
                "Keep humans in the loop",
                "Check automated outputs, protect sensitive information, and be honest about limits.",
              ],
            ].map(([n, t, d]) => (
              <div key={n}>
                <span>{n}</span>
                <div>
                  <h3>{t}</h3>
                  <p>{d}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
        <section className="home-section complete-directory">
          <div className="home-heading">
            <div>
              <p className="academy-kicker">06 / THE COMPLETE COLLECTION</p>
              <h2>
                Keep <em>exploring.</em>
              </h2>
            </div>
            <p>
              Every project, practical guide, and page.
              <br />
              Find the thread that interests you.
            </p>
          </div>
          <label htmlFor="directory-search">Search the MBK collection</label>
          <input
            id="directory-search"
            type="search"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Try “accessibility”, “APIs”, or “projects”…"
          />
          <div className="directory-filters" aria-label="Filter collection">
            {[
              ["All", "Everything"],
              ["lesson", "Learning notes"],
              ["case-study", "Project journal"],
              ["service", "Services"],
              ["profile", "About MBK"],
            ].map(([v, l]) => (
              <button
                key={v}
                aria-pressed={category === v}
                onClick={() => setCategory(v)}
              >
                {l}
              </button>
            ))}
          </div>
          <p className="collection-count" aria-live="polite">
            {pages.length} pages to explore
          </p>
          <div className="collection-list">
            {pages.length ? (
              pages.map((p) => (
                <a href={p.route} key={p.route}>
                  <span>{p.family.replace("-", " ")}</span>
                  <h3>{p.title}</h3>
                  <b>↗</b>
                </a>
              ))
            ) : (
              <p>No matching pages. Try another keyword.</p>
            )}
          </div>
        </section>
        <section
          className="home-section gallery-showcase"
          aria-labelledby="showcase-title"
        >
          <div className="home-heading">
            <div>
              <p className="academy-kicker">
                BEYOND THE SCREEN / PERSONAL GALLERY
              </p>
              <h2 id="showcase-title">
                A few moments,
                <br />
                <em>from my world.</em>
              </h2>
            </div>
            <div className="showcase-controls">
              <button
                type="button"
                onClick={() => setGalleryPaused(!galleryPaused)}
                aria-pressed={galleryPaused}
              >
                {galleryPaused ? "Resume motion" : "Pause motion"}
              </button>
              <a className="academy-text-link" href="/gallery.html">
                Open the gallery ↗
              </a>
            </div>
          </div>
          <div
            className={
              galleryPaused ? "gallery-window paused" : "gallery-window"
            }
          >
            <div className="gallery-track">
              {[0, 1].map((copy) => (
                <div
                  className="gallery-set"
                  key={copy}
                  aria-hidden={copy === 1 ? true : undefined}
                >
                  {galleryImages.map((image, index) => (
                    <figure key={image.src}>
                      <img
                        src={image.src}
                        srcSet={image.srcset}
                        sizes="180px"
                        alt={copy ? "" : image.alt}
                        width={image.width}
                        height={image.height}
                        loading="lazy"
                        decoding="async"
                      />
                      <figcaption>
                        <span>FRAME {String(index + 1).padStart(2, "0")}</span>
                        <span>PERSONAL ARCHIVE</span>
                      </figcaption>
                    </figure>
                  ))}
                </div>
              ))}
            </div>
          </div>
        </section>
        <section className="home-connect">
          <p className="academy-kicker">
            HAVE A QUESTION, A PROJECT, OR A “WHAT IF”?
          </p>
          <h2>
            Good things begin
            <br />
            with <em>a conversation.</em>
          </h2>
          <div>
            <a className="button" href="/contact.html">
              Tell me what’s on your mind ↗
            </a>
            <a className="academy-text-link" href="/book-a-call.html">
              Request a call ↗
            </a>
          </div>
          <span>BASED IN PAKISTAN · OPEN TO REMOTE COLLABORATION</span>
        </section>
      </main>
      <footer className="academy-footer">
        <div>
          <a className="academy-brand personal-brand" href="/">
            <span>
              Bakhtawar Khan
              <small>Personal Digital Portfolio · MBK Global</small>
            </span>
          </a>
          <p>Thoughtful technology. Useful knowledge. Work in progress.</p>
        </div>
        <nav aria-label="Footer">
          <a href="/resources.html">Resources</a>
          <a href="/official-links.html">Official links</a>
          <a href="/gallery.html">Gallery</a>
          <a href="/resume.html">Resume</a>
          <a href="/faq.html">FAQ</a>
          <a href="/privacy-policy.html">Privacy</a>
        </nav>
        <div className="academy-colophon">
          <span>© {new Date().getFullYear()} Bakhtawar Khan · MBK Global</span>
          <a href="#top">Back to top ↑</a>
        </div>
      </footer>
    </div>
  )
}
