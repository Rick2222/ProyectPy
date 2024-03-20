from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Clave secreta para el manejo de sesiones

class SistemaLogin:
    def __init__(self):
        self.usuarios = {'estudiante': {'contraseña': 'est123'},
                         'profesor': {'contraseña': 'prof456'},
                         'admin': {'contraseña': 'admin789'}}  

    def login(self, rol, usuario, contraseña):
        if usuario in self.usuarios and contraseña == self.usuarios[usuario]['contraseña']:
            return True
        return False

sistema = SistemaLogin()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        rol = request.form['rol']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        if sistema.login(rol, usuario, contraseña):
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Credenciales incorrectas', 'error')
    
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return "¡Bienvenido! Has iniciado sesión correctamente."

if __name__ == '__main__':
    app.run(debug=True)
