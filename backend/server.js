const express = express('express');
const app = express();
const cors = require('cors');
require('dotenv').config();
app.use(cors());
app.use(express.json());

app.use('/api/clientes', require('./routes/clientes'));
app.use('/api/productos', require('./routes/productos'));
app.use('/api/ventas', require('./routes/ventas'));


app.listen(process.env.PORT, () =>
console.log (`Servidor volando en http://localhost:${process.env.PORT}`)
);