const express = require('express');
const app = express();
const datastore = require('nedb');

app.listen(3000, ()=> console.log("Listening at 3000"));
app.use(express.static('public'));
app.use(express.json())//can add different options in the parameter, will do this later

const database = new datastore('database.db')
database.loadDatabase();

app.post('/endpoint', (request, response) => {
    console.log(request.body);
    response.json({
        status : 'successful'
    })
});