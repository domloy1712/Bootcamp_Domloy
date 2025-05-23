const express = require('express');
const router = express.Router();
const prcontroller = require('../controller/productosController');

router.get('/', prcontroller.productos);
router.post('/', prcontroller.crearproductos);
router.delete('/:id', prcontroller.eliminar);
module.exports= router;