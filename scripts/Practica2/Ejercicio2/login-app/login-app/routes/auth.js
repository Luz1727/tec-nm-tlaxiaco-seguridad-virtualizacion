const express = require('express');
const path = require('path');
const router = express.Router();

// Simulación de base de datos
const users = [];

// Middleware de autenticación
function isAuthenticated(req, res, next) {
    if (req.session.user) {
        return next(); 
    }
    res.redirect('/login'); 
}

// Middleware de autorización de administrador
function isAdmin(req, res, next) {
    if (req.session.user && req.session.role === 'admin') {
        return next();
    }
    res.send('Acceso Denegado. Solo administradores.'); 
}

// Registro de usuarios
router.post('/register', (req, res) => {
    const { username, password, confirmPassword, role } = req.body;

    if (password !== confirmPassword) {
        return res.send('Las contraseñas no coinciden');
    }

    const userExists = users.find(user => user.username === username);
    if (userExists) {
        return res.send('El usuario ya existe');
    }

    const newUser = { username, password, role };
    users.push(newUser);

    res.redirect('/login');
});

// Inicio de sesión
router.post('/login', (req, res) => {
    const { username, password } = req.body;

    const user = users.find(user => user.username === username && user.password === password);

    if (user) {
        req.session.user = user.username;
        req.session.role = user.role;

        if (user.role === 'admin') {
            res.redirect('/admin');
        } else {
            res.redirect('/profile');
        }
    } else {
        res.send('Nombre de usuario o contraseña inválidos');
    }
});


router.get('/admin', isAuthenticated, isAdmin, (req, res) => {
    res.sendFile(path.join(__dirname, '../public/admin.html'));
});


router.get('/profile', isAuthenticated, (req, res) => {
    res.sendFile(path.join(__dirname, '../public/profile.html'));
});


router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/index.html'));
});


router.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/login.html'));
});

 M
router.get('/register', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/register.html'));
});

module.exports = router;


