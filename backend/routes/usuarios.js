const express = require('express');
const Router = express.Router();
const { login, logout, register } = require('../controller/usuariosController');
const { verificacion } = require('../middleware/auth')

Router.post('/Registrar' , register );
Router.post('/Login', login );
Router.post('/logout', logout, verificacion );



module.exports = Router;