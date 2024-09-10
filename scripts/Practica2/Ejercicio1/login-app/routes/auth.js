const express = require('express');
const path = require('path');
const router = express.Router();

// Simulación de base de datos
const users = [];

// Registro de usuarios
router.post('/register', (req, res) => {
    const { username, password, confirmPassword, role } = req.body;

    // Verificación de coincidencia de contraseñas
    if (password !== confirmPassword) {
        return res.send('Las contraseñas no coinciden');
    }

    // Verificar si el usuario ya existe
    const userExists = users.find(user => user.username === username);
    if (userExists) {
        return res.send('El usuario ya existe');
    }

    // Crear un nuevo usuario
    const newUser = { username, password, role };
    users.push(newUser);

    // Redirigir al inicio de sesión
    res.redirect('/login');
});

// Inicio de sesión
router.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Verificar si el usuario existe y la contraseña es correcta
    const user = users.find(user => user.username === username && user.password === password);

    if (user) {
        req.session.user = user.username;
        req.session.role = user.role;

        // Redirigir según el rol del usuario
        if (user.role === 'admin') {
            res.redirect('/admin');
        } else {
            res.redirect('/profile');
        }
    } else {
        res.send('Nombre de usuario o contraseña inválidos');
    }
});

// Página de administración (solo accesible para administradores)
router.get('/admin', (req, res) => {
    if (req.session.user && req.session.role === 'admin') {
        res.sendFile(path.join(__dirname, '../public/admin.html'));
    } else {
        res.send('Acceso Denegado. Solo administradores.');
    }
});

// Página de perfil (solo accesible para usuarios logueados)
router.get('/profile', (req, res) => {
    if (req.session.user) {
        res.sendFile(path.join(__dirname, '../public/profile.html'));
    } else {
        res.redirect('/login');
    }
});

// Página de inicio
router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/index.html'));
});

// Página de inicio de sesión
router.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/login.html'));
});

// Página de registro
router.get('/register', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/register.html'));
});

module.exports = router;
