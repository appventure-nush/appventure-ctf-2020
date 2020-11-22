const app = require("express")();
const crypto = require("crypto");
const xss = require("xss");
const pup = require("./puppeteer")
const fs = require("fs")

app.use(require('body-parser').urlencoded({extended: true}));

const state = new Map();
app.get("/", (req, res) => {
  const id = crypto.randomBytes(16).toString("hex")
  state.set(id, []);
  res.redirect("/" + id);
});

app.get("/:uid", (req, res) => {
  const id = req.params.uid;
  if (!state.has(id)) {
    res.redirect("/");
    return;
  }
  const notes = state.get(id);
  let html = "<h1>Your notes</h1><ul>"
  for (const note of notes) {
    html += `<li><a href="/${id}/${note.id}">${xss(note.title)}</a></li>`
  }
  if (notes.length === 0) {
    html += "<li>You currently have no notes.</li>"
  }
  html += `</ul><a href="/${id}/new">Create a new note</a>`
  res.send(html);
});

app.get("/:uid/new", (req, res) => {
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

app.post("/:uid/new", (req, res) => {
  const id = req.params.uid;
  if (!state.has(id)) {
    res.redirect("/");
    return;
  }
  const {content, title} = req.body;
  if (content && title) {
    const noteId = crypto.randomBytes(16).toString("hex")
    const notes = state.get(id);
    state.set(id, [...notes, {content, title, id: noteId}]);
    res.redirect(`/${id}/${noteId}`)
  } else {
    res.end("Bad")
  }
});
app.get("/:uid/:noteId", (req, res) => {
  const id = req.params.uid;
  if (!state.has(id)) {
    res.redirect("/");
    return;
  }
  const notes = state.get(id);
  const note = notes.filter(note => note.id == req.params.noteId);
  if (note.length === 0) {
    res.redirect("/" + id);
    return;
  }
  res.send(`
  <h1>${xss(note[0].title)}</h1>
  ${note[0].content}<br><br>
  <a href="/${id}">Back to notes</a><br>
   <a href="/${id}/${note[0].id}/report">Report this note to the admin</a>
  `);
});

app.get("/:uid/:noteId/report", async (req, res) => {
  const id = req.params.uid;
  if (!state.has(id)) {
    res.redirect("/");
    return;
  }
  const notes = state.get(id);
  const note = notes.filter(note => note.id == req.params.noteId);
  if (note.length === 0) {
    res.redirect("/" + id);
    return;
  }
  const origin = "http://34.68.146.67:1238"
  const url = origin + `/${id}/${req.params.noteId}`;

  const cookies = [{
    name: "flag",
    value: fs.readFileSync("flag.txt").toString().trim(),
    url: origin
  }];
  console.log(url)
  await pup(url, cookies);
  res.end("The admin has visited your note. It has been removed to prevent spam.")
  state.set(id, notes.filter(note => note.id !== req.params.noteId))
})

app.listen(1238);
