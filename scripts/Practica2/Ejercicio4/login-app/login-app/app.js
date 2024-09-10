const express = require('express');
const path = require('path');
const session = require('express-session');
const app = express();

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

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

