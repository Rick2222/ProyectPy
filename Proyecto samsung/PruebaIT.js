document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('submit').addEventListener('click', function () {
        var respuestas = [];
        var preguntas = document.querySelectorAll('.question');
        preguntas.forEach(function (pregunta, idx) {
            var seleccion = pregunta.querySelector('input[type="radio"]:checked');
            if (seleccion) {
                respuestas.push({
                    id: idx,
                    seleccion: seleccion.value
                });
            }
        });

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(respuestas)
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            document.getElementById('result').innerText = 'Tu puntaje es: ' + data.puntaje;
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
    });
});
