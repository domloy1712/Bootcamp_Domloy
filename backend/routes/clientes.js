const express = require('express');
const Router = express.Router();
const clientesController = require('../controller/clientesController');

Router.get('/', clientesController.mostrar);

Router.post('/', clientesController.crear);

Router.delete('/:id',clientesController.borrar)



module.exports = Router;