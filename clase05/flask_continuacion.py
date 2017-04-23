from flask import Flask, render_template, request, redirect
from modelos import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@db_session
def index():
    if request.method == 'POST':
        tarea = request.form.get('tarea')
        if tarea:
            t = Tarea(texto=tarea)

    contexto = {'tareas': select(t for t in Tarea)}
    return render_template('index.html', **contexto)


@app.route('/eliminar/<int:indice>')
@db_session
def eliminar(indice):
    tarea = Tarea[indice]
    tarea.delete()
    return redirect('/')


@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
@db_session
def editar(indice):
    tarea = Tarea[indice]
    if request.method == 'POST':
        texto = request.form.get('tarea')
        if texto:
            tarea.texto = texto
            return redirect('/')
    return render_template('editar.html', tarea=tarea)

if __name__ == '__main__':
    app.run(debug=True)
