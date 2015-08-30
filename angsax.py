from flask import Flask, render_template, request
from random import randint, choice
from narrativa import x
#1
app = Flask(__name__)

def imagen_aleatoria(y):
    if (not y['imagen-arriba'] ) and (not y['imagen-abajo']):
        ilustraciones = ["bosque", "doll", "escudo", "hut", "kidsplay", "lira",
                        "mousy", "oak_leaf_illustration", "sceata"]
        lugar = ["imagen-abajo", "imagen-arriba"]
        y[choice(lugar)] = choice(ilustraciones) + ".png"
    return y

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
                if randint(1,10) <= y["r"]:
                    m = 0
                else:
                    m = 1

                z = y["s"][m]
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