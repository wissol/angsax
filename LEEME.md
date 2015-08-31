### Introducción

El Primer Rey de Angsax es un librojuego escrito al estilo de los librojuegos 
clásicos de los 80 que aprovecha las capacidades del ordenador para superar 
algunas de las limitaciones del papel.

En concreto, básicamente sigue el estilo ETPA (el que popularizó la serie 
"Elige tu propia aventura") con el texto dividido en secciones que terminan 
en una o más opciones que se dan al lector/jugador continuando la lectura en el 
punto adecuado.

La diferencia está es que secretamente la aplicación "tira los dados" para 
determinar el éxito o fracaso de la acción que decidió el jugador, en base a la 
probabilidad que el autor ha determinado al crear el juego.

Está desplegado en www.angsax.com (aunque a 1 de septiembre de 2015 aún 
incompleto)

## Estructura:


### angsax.py -> "Controlador"

Angsax.py contiene las instrucciones necesarias para que el servidor tome los 
datos del modelo y los mande a las vistas (views).

No quiero comentar demasiado sobre él porque todavía tengo que "refactorizarlo" 
(mejorarlo). De momento funcionar, funciona, pero debo mejorarlo para que r
esulte más fácil de entender.

### narrativa.py -> "Modelo"

Contiene el modelo, los datos de la aplicación; básicamente el texto y los 
enlaces. Todos los datos vienen en un diccionario de diccionarios llamado x.

Una sección típica tiene esta estructura


    "nombre-seccion-1":{
    					titulo:"Mi titulo",
    					texto:'''
    					<p>Texto de la sección.</p>
    					''',
    					opciones:{"opcion1":"nombre-seccion-2",
    							  "opcion2":"p-nombre-seccion-1"},
    					prueba:False,
    					imagen_abajo:False,
        				imagen_arriba:"sceata.png"
        				},

Cuando prueba vale False, el controlador interpreta que tiene que desplegar 
el contenido en la vista ("la página web"), cuando vale True, le toca elegir 
una de las salidas como veremos más adelante.

imagen_abajo e imagen_arriba pueden contener el nombre de un fichero de imagen o 
False. Si ambas son False el controlador selecciona automáticamente una 
ilustración de relleno entre las de una lista.

Las secciones con las pruebas tienen esta estructura:

    "p-emboscar-vikingos":{
                prueba:True,
                r:3,
                s:["nombre-seccion-4","nombre-seccion-5"] 
                },


Al ser prueba true, angsax.py "tira un dado de 10 caras" Si el resultado es 
menor o igual a r (lo que en rol llamamos número objetivo) elige desplegar 
la primera de las salidas que aparecen en la lista s. Si el resultado es mayor 
que r el controlador desplegará la segunda de las salidas.

Obviamente podría haber complicado esto mucho más. Quizás en un nuevo librojuego 
lo haga así.

### Templates

Esta carpeta contiene las plantillas que usa Flask para crear las páginas web. 
Básicamente lo que ponga {{ algo }} significa que ese algo es una variable. 
Cuando ponga {% programa %} son trocitos de código. La documentación de Flask 
está en Internet.

### Static


Contiene archivos auxiliares: las imágenes y la información de estilo CSS.