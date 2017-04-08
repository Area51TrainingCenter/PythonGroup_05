from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    contexto = {'otra': 'cosa'}

    if request.method == 'POST':
        contexto['nombre'] = request.form.get('nombre', '')

    return render_template('hello.html', **contexto)

lista_de_tareas = ['uno', 'dos', 'tres']


@app.route('/tareas', methods=['GET', 'POST'])
def tareas():
    if request.method == 'POST':
        tarea = request.form.get('tarea', '')
        if tarea:
            lista_de_tareas.append(tarea)

    contexto = {'tareas': lista_de_tareas}
    return render_template('tareas.html', **contexto)


@app.route('/saludo/<nombre>')
def hola(nombre):
    contexto = {
        'nombre': nombre,
        'apellido': 'cachay',
        # 'numeros': [x ** 2 for x in range(100)]
    }
    return render_template('index.html', **contexto)


@app.route('/<operacion>/<float:uno>/<float:dos>')
def operar(operacion, uno, dos):
    if operacion == 'suma':
        return str(uno + dos)
    elif operacion == 'resta':
        return str(uno - dos)
    elif operacion == 'producto':
        return str(uno * dos)
    elif operacion == 'cociente':
        return str(uno / dos)

if __name__ == '__main__':
    app.run(debug=True)
