/** Build-time rendering of the existing React homepage; no server or requests. */
import fs from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"
import ts from "typescript"
import React from "react"
import { renderToString } from "react-dom/server"

const root = fileURLToPath(new URL("../", import.meta.url))
let source = await fs.readFile(path.join(root, "src/App.tsx"), "utf8")
for (const name of ["directory", "galleryImages"]) {
  const filename =
    name === "directory" ? "page-directory.json" : "gallery-showcase.json"
  const data = JSON.parse(
    await fs.readFile(path.join(root, "src", filename), "utf8"),
  )
  source = source.replace(
    new RegExp(`import ${name} from ["']\\./${filename}["'];?`),
    `const ${name} = ${JSON.stringify(data)};`,
  )
}
let compiled = ts.transpileModule(source, {
  compilerOptions: {
    target: ts.ScriptTarget.ES2022,
    module: ts.ModuleKind.ESNext,
    jsx: ts.JsxEmit.ReactJSX,
  },
}).outputText
for (const name of ["react", "react/jsx-runtime"]) {
  compiled = compiled.replaceAll(
    `"${name}"`,
    JSON.stringify(import.meta.resolve(name)),
  )
}
const { default: App } = await import(
  `data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`
)
const rendered = renderToString(React.createElement(App))
if (!rendered.includes("<h1") || !rendered.includes("<main")) {
  throw new Error("Homepage prerender did not produce its primary content.")
}
const filename = path.join(root, "dist/index.html")
const shell = await fs.readFile(filename, "utf8")
if (!shell.includes('<div id="root"></div>')) {
  throw new Error("Expected the unrendered Vite root; refusing to overwrite.")
}
await fs.writeFile(
  filename,
  shell.replace('<div id="root"></div>', `<div id="root">${rendered}</div>`),
)
console.log("Prerendered the existing React homepage into dist/index.html.")
