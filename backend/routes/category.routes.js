const express = require('express');
const router = express.Router();
const categoryController = require('../controllers/category.controller');
const { verifyToken } = require('../middleware/auth');


router.post('/create', categoryController.createCategory);
router.get('/', categoryController.getCategories);
router.delete('/borrar/:id', categoryController.borrar);
router.put('/actualizar/:id', categoryController.actualizar)
module.exports = router;