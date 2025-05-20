const pool = require('../config/db');

exports.createCategory = async (req, res) => { 
    const { name } = req.body;
    console.log('Creando categoría:', name);
    if (!name) {
        return res.status(400).json({ message: 'El nombre de la categoría es requerido' });
    }

    try {
    const [existing] = await pool.query('SELECT * FROM categories WHERE name = ?', [name]);
    if (existing.length > 0) return res.status(409).json({ msg: 'La categoría ya existe.' });

    await pool.query('INSERT INTO categories (name) VALUES (?)', [name]);
    res.status(201).json({ msg: 'Categoría creada correctamente.' });
  } catch (error) {
    res.status(500).json({ msg: 'Error al crear categoría.', error: error.message });
  }
};


exports.getCategories = async (req, res) => {
    try {
        const [categories] = await pool.query('SELECT * FROM categories ');
        res.status(200).json(categories);
    } catch (error) {
        res.status(500).json({ msg: 'Error al obtener categorías.', error: error.message });
    }
};

exports.borrar = async (req,res) => {
    const borrar = req.params.id;
    try {
        await pool.query('DELETE FROM categories WHERE id = ?', [borrar]);
        res.status(200).json({message: 'Categoria Borrada!!!'})
    } catch (error) { 
        res.status(500).json({msg: 'Error a eliminar categorias', error: error.massage});
    }
};

exports.actualizar = async (req,res) => {
    const id_categoria = req.params.id;
    const { nombre } = req.body;
    try {
        const [rows] = await pool.query('SELECT * FROM categories WHERE id = ? ', [id_categoria]);
        if (rows.length == 0){
            res.status(404).json({massage: "No existe"});
        }
        await pool.query('UPDATE categories SET name = ? WHERE id = ? ', [nombre,id_categoria]);
        res.status(200).json({message: "Vale"});
    } catch (error) {
        res.status(500).json({message: "No funciona", error: error.message});
    };
};
