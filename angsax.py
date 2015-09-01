from flask import Flask, render_template, request
from random import randint, choice
from narrativa import x

app = Flask(__name__)

def imagen_aleatoria(y):
    if (not y['imagen-arriba'] ) and (not y['imagen-abajo']):
        ilustraciones = ["bosque", "doll", "escudo", "hut", "kidsplay", "lira",
                        "mousy", "oak_leaf_illustration", "sceata"]
        lugar = ["imagen-abajo", "imagen-arriba"]
        y[choice(lugar)] = choice(ilustraciones) + ".png"
    return y

def prueba(y):
    m = 1
    if randint(1,10) <= y["r"]:
        m = 0
    return y["s"][m]

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html', y = x['0'])

@app.route('/', methods=['POST'])
def section():
    z = request.form['opciones']
    try:
        y = x[z]
        try:
            if y["prueba"]:
                z = prueba(y)
                try:
                    y = x[z]
                except KeyError:
                    return render_template('404.html', z = z)
        except KeyError:
            pass
    except KeyError:
        return render_template('404.html', z = z)
    y = imagen_aleatoria(y)
    return render_template('index.html', y = y)