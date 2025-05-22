const express = express();
const router = express.router;
const prcontroller = require('../controller/productosController');

router.get('/',prcontroller.productos);
router.post('/',prcontroller.crearproductos);

export default router;