const db = require('../db');

exports.verventas = async (req,res) => {
    try {
        const [rows] = await db.query ('SELECT * FROM ventas');
        res.json(rows);
    } catch (error) {
        console.log({error: error })
        res.status(500).json({message: 'no funciona'})

    }
};

exports.crearventas = async (req,res) => {

    const { fecha  } = req.body;
    
    try{ await db.query('INSERT INTO ventas (fecha) VALUES (?)',[fecha])
        res.json({ message: 'Producto creado correctamente' });
    } catch (error) {
       console.log('Error al crear producto:', error);
       res.status(500).json({ error: 'Error al crear producto' });
    }
};