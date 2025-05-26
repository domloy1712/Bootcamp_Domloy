const express = require('express');
const Router = express.Router();
const Controller = require('../controller/controller');

Router.get('/coleccion', Controller.coleccion);



module.exports = Router;
