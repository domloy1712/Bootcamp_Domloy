const { connect } = require('../db');

exports.coleccion = async (req,res) =>{
    try {
        const db = await connect();
        const productos = await db.collection('productos').find().toArray();
        res.json(productos);
    }  catch (error) {
       res.status(500).json({ mensaje: "Error al obtener productos" });
  }
};