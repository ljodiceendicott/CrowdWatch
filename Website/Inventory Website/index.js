const express = require('express');
const app = express();
const Datastore = require('nedb');
const mysql = require('mysql')


app.listen(3000, ()=> console.log("Listening at 3000"));
app.use(express.static('public'));
app.use(express.json())//can add different options in the parameter, will do this later

const database = new Datastore('database.db')
database.loadDatabase();

database.insert({action: 'Login', date : Date.now()})

var con = mysql.createConnection({
    host:"localhost",
    user:"ljodice",
    password: ""
});

con.connect(function(er){
    if(err) throw err;
    console.log("Connected!");
})

app.post('/endpoint', (request, response) => {
    const data = request.body;
    data.timestamp = Date.now();
    database.insert(data);
    response.json({
        status : 'successful'
    })
});

app.get('/logs', (request,response) => {
    database.insert({action: 'Login', date : Date.now()})
    database.find({},(err, data) =>{
        if(err){
            response.end();
            return;
        }
        response.json(data);
        console.log(data);
    });
});

router.get('/', function(req, res, next) {
    res.send('respond with a resource')
});