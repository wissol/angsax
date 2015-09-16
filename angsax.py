from flask import Flask, render_template, request
from random import randint, choice
from narrativa import secciones

app = Flask(__name__)

def annade_imagen_aleatoria(seccion):
    ''' elige una imagen aleatoria de una lista si no se ha establecido ninguna
    '''
    z = seccion
    if (not z['imagen-arriba'] ) and (not z['imagen-abajo']):
        ilustraciones = ["ancient_nordic_borre_beasts", "bosque", "doll",
                         "escudo", "hut", "kidsplay", "lira",
                         "molaise", "mousy",
                         "oak_leaf_illustration", "sceata",
                         "viking_shield_style_brooch_by_eveyd-d38na6a"]
        lugar = ["imagen-abajo", "imagen-arriba"]
        z[choice(lugar)] = choice(ilustraciones) + ".png"
    return z

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
    return render_template(
        'index.html',
        y = annade_imagen_aleatoria(
            siguiente_seccion(secciones, request.form['opciones'])
        )
    )
"""
@app.errorhandler(404)
def no_econtrada(e):
    return render_template('404.html'), 404
"""