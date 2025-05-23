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