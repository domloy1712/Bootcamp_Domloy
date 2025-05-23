const express = require('express');
const Router = express.Router();
const ventascontroller = require('../controller/ventasController')

Router.get('/', ventascontroller.verventas)
Router.post('/', ventascontroller.crearventas)

module.exports = Router;