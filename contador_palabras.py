from narrativa import secciones
from re import findall

def conpal(x):
    # Find all non-whitespace patterns.
    list = findall("(\S+)", x)
    return len(list)
    # http://www.dotnetperls.com/word-count-python

def conpal_seccion(seccion):
    #ignora las palabras de las opciones
    try:
        y = seccion['prueba']
    except:
        y = False

    if y:
        x = 0
    else:
        try:
            x = conpal(seccion['titulo'])
            x += conpal(seccion['texto'])
        except:
            print("Error en ", seccion)
            x=0
    return x

def con_pal_secciones(secciones):
    cuenta = 0
    for seccion_index in secciones:
        #print(secciones[seccion_index])
        cuenta += conpal_seccion(secciones[seccion_index])
    return cuenta

print(con_pal_secciones(secciones))