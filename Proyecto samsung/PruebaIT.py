from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app = Flask("proyecto", static_url_path='', static_folder='static')
# Lista de preguntas y respuestas (para este ejemplo, se almacenan en memoria)
preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "opciones": ["Londres", "París", "Madrid", "Berlín"],
        "respuesta_correcta": "París"
    },
    {
        "pregunta": "¿Quién escribió 'El Quijote'?",
        "opciones": ["Miguel de Cervantes", "Gabriel García Márquez", "William Shakespeare", "Friedrich Nietzsche"],
        "respuesta_correcta": "Miguel de Cervantes"
    },
    {
        "pregunta": "¿En qué continente queda Egipto?",
        "opciones": ["Asia", "América", "Europa", "África", "Oceanía"],
        "respuesta_correcta": "África"
    }
]

@app.route('/')
def index():
    return render_template('PruebasInteractivas.html', preguntas=preguntas)

@app.route('/submit', methods=['POST'])
def submit():
    respuestas = request.json
    puntaje = 0
    for respuesta in respuestas:
        pregunta_id = respuesta['id']
        seleccion = respuesta['seleccion']
        respuesta_correcta = preguntas[pregunta_id]['respuesta_correcta']
        if seleccion == respuesta_correcta:
            puntaje += 1
    return jsonify({"puntaje": puntaje})

if __name__ == '__main__':
    app.run(debug=True)

