const functions = require("firebase-functions");
// const firebase = require("firebase");
const express = require("express");
const { initializeApp } = require("firebase-admin");
const { getDatabase } = require("firebase-admin/database");
const app = express();
const firebaseConfig = {
  apiKey: "AIzaSyCH0gyZ9RUUdHsLHEM7hYhyYHqmQoVJsKY",
  authDomain: "crowdwatch-ce5b8.firebaseapp.com",
  projectId: "crowdwatch-ce5b8",
  storageBucket: "crowdwatch-ce5b8.appspot.com",
  messagingSenderId: "267648106581",
  appId: "1:267648106581:web:3a11c1688282768f4cd4dc",
  measurementId: "G-9GVLV3ZJNE",
  databaseURL: "https://crowdwatch-ce5b8-default-rtdb.firebaseio.com/",
};
const appinit = initializeApp(firebaseConfig);
const db = getDatabase(appinit);
var database = firebase.database();

//Connecting to the Emulators for testing
if (location.hostname === "localhost") {
  // Point to the RTDB emulator running on localhost.
  firebase.functions.useEmulator("localhost", 4000);
  db.useEmulator("localhost", 50);
}

// Attach an asynchronous callback to read the data at our posts reference
ref.on(
  "value",
  (snapshot) => {
    console.log(snapshot.val());
  },
  (errorObject) => {
    console.log("The read failed: " + errorObject.name);
  }
);
// const fs = require("fs");
// const data = fs.readFileSync("data.json");
// const words = JSON.parse(data);

// let database = firebase.database();

// database.ref("/Yep").set(obj, function (error) {
//   if (error) {
//     console.log("failed with error: " + error);
//   } else {
//     console.log("Sucess");
//   }
// });

app.listen(3000, () => console.log("Connecting to Port: 3000"));
app.use(express.static("public"));
app.use(express.json());

app.get("/", (req, res) => {
  res.status(200).send({ data: "Sucess" });
});

app.post("/endpoint", (request, response) => {
  const data = request.body;
  data.timestamp = Date.now();
  //   database.insert(data);
  response.json({
    status: "successful",
  });
});

app.get("/currentvalues", (req, res) => {
  // res.json(words);
  res.json({ Users: "Current" });
});

app.patch("/DataChange/:location/:number?", (request, response) => {});

// app.get("/logs", (request, response) => {
//   //   database.insert({ action: "Login", date: Date.now() });
//   //   database.find({}, (err, data) => {
//   //     if (err) {
//   //       response.end();
//   //       return;
//   //     }
//   //     response.json(data);
//   //     console.log(data);
//   //   });
// });
// // Create and deploy your first functions
// // https://firebase.google.com/docs/functions/get-started
//
exports.app = functions.https.onRequest(app);

// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", { structuredData: true });
//   response.send("Hello from Firebase!");
// });
