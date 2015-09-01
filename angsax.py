from flask import Flask, render_template, request
from random import randint, choice
from narrativa import secciones

app = Flask(__name__)

def imagen_aleatoria(y):
    ''' elige una imagen aleatoria de una lista si no se ha establecido ninguna
    '''
    if (not y['imagen-arriba'] ) and (not y['imagen-abajo']):
        ilustraciones = ["bosque", "doll", "escudo", "hut", "kidsplay", "lira",
                        "mousy", "oak_leaf_illustration", "sceata"]
        lugar = ["imagen-abajo", "imagen-arriba"]
        y[choice(lugar)] = choice(ilustraciones) + ".png"
    return y

def prueba(y):
    ''' devuelve la sección que debe ir a continuación de acuerdo a la
    probabilidad que tiene asignada'''
    m = 1
    if randint(1,10) <= y["r"]:
        m = 0
    return y["s"][m]

def siguiente_seccion(x,z):
    try:
        y = x[z]
        try:
            if y["prueba"]:
                z = prueba(y)
                try:
                    y = x[z]
                except KeyError:
                    y = x['error']
                    y['KeyError'] = z
        except KeyError:
            y = x['error']
            y['KeyError']= "Prueba no inicializada"
    except KeyError:
        y = x['error']
        y['KeyError']= z
    return y

@app.route('/', methods=['GET'])
def inicio():
    return render_template('index.html', y = secciones['0'])

@app.route('/', methods=['POST'])
def section():
    opcion_elegida = request.form['opciones']
    y = siguiente_seccion(secciones, opcion_elegida)
    y = imagen_aleatoria(y)
    return render_template('index.html', y = y)