const db = require('../db');

exports.productos = async (req,res) => {
    try { const [rows] = await db.query('SELECT * FROM Productos');
        res.json(rows);
    } catch (error) {
        console.log('Error al obtener productos', error);
        res.status(500).json({error: 'Error al obtener productos'})
    };
};

exports.crearproductos = async (req,res) =>{
    const { nombre, precio, stock, stock_minimo } = req.body;
    try{ await db.query('INSERT INTO productos (nombre, precio, stock, stock_minimo) VALUES (?, ?, ?, ?)',[nombre, precio, stock, stock_minimo]);
        res.json({ message: 'Producto creado correctamente' });
    } catch (error) {
       console.log('Error al crear producto:', error);
       res.status(500).json({ error: 'Error al crear producto' });
    };

};
