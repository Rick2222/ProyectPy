document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Verificar las credenciales
    if (username === 'estudiante' && password === '123') {
        // Redirigir a la página de inicio después de iniciar sesión
        window.location.href = 'dashboard.html'; // Cambia aquí a la página de dashboard
    } else {
        // Mostrar mensaje de error si las credenciales son incorrectas
        document.getElementById('error-msg').innerText = 'Credenciales incorrectas. Por favor, intente de nuevo.';
    }
});
