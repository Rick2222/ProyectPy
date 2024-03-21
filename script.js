document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Verificar las credenciales
    if (username === 'admin' && password === 'admin') {
        window.location.href = 'Pag admin.html'; 
      } else if (username === 'User' && password === '1234') {
        window.location.href = 'Pag user.html'; 
      } else {
        document.getElementById('error-msg').innerText = 'Credenciales incorrectas. Por favor, intente de nuevo.';
      }
});

