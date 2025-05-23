const db = require('../db');

exports.mostrar = async (req,res) => {
    
    try { const [rows] = await db.query('SELECT * FROM Clientes');
        res.json(rows);
    } catch (error) {
        console.log('Error al obtener clientes', error);
        res.status(500).json({error: 'Error al obtener clientes'})
    }
};

exports.crear = async (req,res) =>{
    
    const { nombre, email, telefono } = req.body;
    
    try{ await db.query('INSERT INTO clientes (nombre, email, telefono) VALUES (?,?,?)',[nombre, email, telefono]);
        res.json({ message: 'Producto creado correctamente' });
    } catch (error) {
       console.log('Error al crear producto:', error);
       res.status(500).json({ error: 'Error al crear producto' });
    }
};

exports.borrar = async (req,res) => {
   const { id } = req.params;
    try{
        await db.query('DELETE FROM Clientes WHERE id_cliente= ?', [id])
        res.json({ message:'Borrado correctamente' })

    }  catch (error) {
       console.log('Error al borar el producto:', error);
       res.status(500).json({ error: 'Error al borrarlo producto' });
    }
};