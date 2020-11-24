const app = require("express")();
const flag = require("fs").readFileSync("flag.txt");
const flag2 = require("fs").readFileSync("flag2.txt");

app.get("/", (req, res) => {
  res.end(require("fs").readFileSync("index.js"));
});

app.get("/flag", (req, res) => {
  try {
    console.log("1", req.query);
    const {a, b} = req.query;
    if (a.length != a.toString().length) {
      if (b.lol == 10) {
        console.log("Worked1", req.query)
        res.end(flag);
        return;
      }
    }
  } catch (e) {
    console.log(e.message)
    res.end("Something bad happened");
    return;
  }
  res.end("Ooops");
});

app.get("/flag2", (req, res) => {
  try {
    console.log("2", req.query);
    if (!(req.query.flag = "give flag")) {
      res.end(flag2)
      return;
    }
    if (req.query.flag.length + req.query.give.length + req.query.please == 420) {
      const query = req.query.flag + req.query.give + req.query.please;
      if (query.length == 69) {
        console.log("Worked2", req.query)
        res.end(flag2)
        return;
      }
    }
  } catch (e) {
    console.log(e.message)
    res.end("Something bad happened");
    return;
  }
  res.end("Ooops");
});


app.listen(1237)

