const express = require('express');
const Router = express.Router();
const clientesController = require('../controller/clientesController');

router.get('/', clientesController.mostrar);
router.post('/', clientesController.crear);
router.delete('/:id', )



module.exports = Router;