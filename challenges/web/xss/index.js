const app = require("express")();
const crypto = require("crypto");
const xss = require("xss");
const pup = require("./puppeteer")
const fs = require("fs")

app.use(require('body-parser').urlencoded({extended: true}));

const state = new Map();
app.get("/", (req, res) => {
  res.redirect("/1");
});

app.get("/:level/", (req, res) => {
  const id = crypto.randomBytes(16).toString("hex")
  state.set(id, []);
  res.redirect("/" + req.params.level + "/" + id);
});

app.get("/:level/:uid", (req, res) => {
  const id = req.params.uid;
  const level = req.params.level;
  if (!state.has(id)) {
    res.redirect("/" + level);
    return;
  }
  const notes = state.get(id).filter(note => note.level === level);
  let html = "<h1>Your notes</h1><ul>"
  for (const note of notes) {
    html += `<li><a href="/${level}/${id}/${note.id}">${xss(note.title)}</a></li>`
  }
  if (notes.length === 0) {
    html += "<li>You currently have no notes.</li>"
  }
  html += `</ul><a href="/${level}/${id}/new">Create a new note</a>`
  if (parseInt(level) === 3) {
    res.set("Content-Security-Policy", "default-src 'self'; script-src https://*.google.com; object-src 'none'; frame-src 'none'")
  }
  res.send(html);
});

app.get("/:level/:uid/new", (req, res) => {
  res.send(`
  <form method="post">
  <label>Title:</label>
  <input name="title"><br>
  <label>Content:</label><br>
  <textarea name="content"></textarea><br>
  <button type="submit">Create</button>
  </form>
  `);
});

app.post("/:level/:uid/new", (req, res) => {
  const id = req.params.uid;
  const level = req.params.level;
  if (!state.has(id)) {
    res.redirect("/" + level);
    return;
  }
  let {content, title} = req.body;
  if (parseInt(level) === 2) {
    while (content.includes("script")) {
      content = content.replace("script", "");
    }
  }
  if (content && title) {
    const noteId = crypto.randomBytes(16).toString("hex")
    const notes = state.get(id);
    state.set(id, [...notes, {content, title, level, id: noteId}]);
    res.redirect(`/${level}/${id}/${noteId}`)
  } else {
    res.end("Bad")
  }
});

app.get("/:level/:uid/:noteId", (req, res) => {
  const id = req.params.uid;
  const level = req.params.level;
  if (!state.has(id)) {
    res.redirect("/" + level);
    return;
  }
  const notes = state.get(id);
  const note = notes.filter(note => note.id === req.params.noteId && note.level === level);
  if (note.length === 0) {
    res.redirect("/" + level + "/" + id);
    return;
  }
  if (parseInt(level) === 3) {
    res.set("Content-Security-Policy", "default-src 'self'; script-src https://*.google.com; object-src 'none'; frame-src 'none'")
  }
  res.send(`
  <h1>${xss(note[0].title)}</h1>
  ${note[0].content}<br><br>
  <a href="/${level}/${id}">Back to notes</a><br>
   <a href="/${level}/${id}/${note[0].id}/report">Report this note to the admin</a>
  `);
});

app.get("/:level/:uid/:noteId/report", async (req, res) => {
  const id = req.params.uid;
  const level = req.params.level;
  if (parseInt(level) < 1 || parseInt(level) > 3) {
    return res.end("Invalid level");
  }
  if (!state.has(id)) {
    res.redirect("/" + level);
    return;
  }
  const notes = state.get(id);
  const note = notes.filter(note => note.id === req.params.noteId && note.level === level);
  if (note.length === 0) {
    res.redirect("/" + level + "/" + id);
    return;
  }
  const origin = "http://localhost:1238"
  const url = origin + `/${level}/${id}/${req.params.noteId}`;

  const cookies = [{
    name: "flag",
    value: fs.readFileSync(`flag${level}.txt`).toString().trim(),
    url: origin
  }];
  console.log(url, level);
  await pup(url, cookies);
  res.end("The admin has visited the note.")
})

app.listen(1238);
