const express = require('express');
const path = require('path');
const session = require('express-session');
const app = express();

// Configuración para servir archivos estáticos desde la carpeta 'public'
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: true }));

// Configuración de sesión
app.use(session({
    secret: 'mySecret',
    resave: false,
    saveUninitialized: true
}));

// Rutas de autenticación
const authRoutes = require('./routes/auth');
app.use('/', authRoutes);

// Iniciar el servidor
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});


