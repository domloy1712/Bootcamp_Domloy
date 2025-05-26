const express = require('express');
const app = express();
const Router = require('./routes/routes');
const PORT = 3000;

app.use(express.json());

app.use('/mongo', Router)

app.listen(PORT, () =>{
    console.log(`El Servidor de Mongodb http://localhost:${PORT}`)
});