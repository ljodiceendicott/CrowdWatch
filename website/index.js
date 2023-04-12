const express = require("express");
const app = express();
const Datastore = require("nedb");
const mysql = require("mysql");
const fs = require("fs");
var data = fs.readFileSync("data.json");
var words = JSON.parse(data);

//parse all objects with first
//Put history in its own file

// console.log(words)
var DataChange = false;

// console.log(data);

app.listen(3000, () => console.log("Connecting to Port: 3000"));
app.use(express.static("public"));
app.use(express.json()); //can add different options in the parameter, will do this later

const database = new Datastore("database.db");
database.loadDatabase();

database.insert({ action: "Login", date: Date.now() });

// var con = mysql.createConnection({
//     host:"localhost",
//     user:"ljodice",
//     password: ""
// });

// con.connect(function(err){
//     if(err) throw err;
//     console.log("Connected!");
// })

app.post("/endpoint", (req, res) => {
  const data = req.body;
  data.timestamp = Date.now();
  database.insert(data);
  res.json({
    status: "successful",
  });
});

app.post("/test", (req, res) => {
  const data = req.body;
  console.log(data);
  res.json({
    status: "IT  Worked",
  });
});

app.post("/logs", (req, resp) => {
  const data = req.body;
  database.insert(data);
  resp.json({
    status: "100 Data sent to DB",
  });
});

app.get("/currentvalues", (req, res) => {
  res.json(words);
});

app.get("/getfullhistory", (req, res) => {
  history = [];
  for (var i = 0; i < words.account.locations.length; i++) {
    var lochistory = { name: words.account.locations[i].name, lochist: [] };
    for (var j = 0; j < words.account.locations[i].history.length; j++) {
      lochistory.lochist.push(words.account.locations[i].history[j]);
    }
    history.push(lochistory);
  }
  res.json(history);
  console.log(history);
});

app.get("/isUpdated", (req, res) => {
  res.json({
    isChanged: DataChange,
  });
});

app.get("/logs", (req, res) => {
  database.insert({ action: "Login", date: Date.now() });
  database.find({}, (err, data) => {
    if (err) {
      res.end();
      return;
    }
    res.json(data);
    console.log(data);
  });
});

app.patch("/DataChange/:location/:number?", (req, res) => {
  words[req.params[0]] = req.params[1];
  conscole.log(words);
});

app.get("/isupdatedReset", (req, res) => {
  DataChange = false;
  res.json({
    isChanged: DataChange,
  });
  console.log("Working");
});

app.put("/valuechange/:location/:number?", (req, res) => {
  DataChange = true;
  update_location = req.params[0];
  update_number = req.params[1];

  res.json({
    isChanged: DataChange,
  });
});

// router.get('/pages/dashboard.html', function(req, res, next) {
//     res.send('respond with a resource')
// });
