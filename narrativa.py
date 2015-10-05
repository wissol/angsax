# -*- coding: utf-8 -*-
titulo = "titulo"
texto = "texto"
opciones = "opciones"
prueba = "prueba"
imagen_abajo = "imagen-abajo"
imagen_arriba = "imagen-arriba"
r = "r"
s = "s"

secciones = {

        "error":{
            titulo:"Error :(",
            texto:'''
            <p>Lo siento mucho, pero se ha generado un error en esta página. Lo
            más probable es que me haya olvidado de algo, o tenga un punto y
            coma donde no debería o que simplemente no hay todavía escrito la
            sección que habías elegido para continuar la aventura.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_abajo:False,
            imagen_arriba:'404.png',
        },

        "0":{titulo:"El Primer Rey de Angsax",
        texto:
            '''
            <p>Te llamaré Dever.</p>
            <p>Eres un joven guerrero de Angsax, en la época de la furia de los Vikingos.
            Angsax es una gran isla dividida entre pequeños señores de la guerra. Las antiguas
            ciudades son ruinas desde los tiempos de tus abuelos. Cada verano cientos de
            mujeres y niños desaparecen en un barco invasor para no volver nunca. La tierra
            y el cielo claman por un héroe, como el los tiempos de las gestas, ¿podrías
            serlo tú?</p>

            <p>Si te atreves es posible que te conviertas en el primer rey de Angsax o en un
            montón de huesos en el fondo de un pantano.</p>
            ''',
        opciones:{"Comienza tu aventura":"1"},
        prueba:False,
        imagen_abajo:False,
        imagen_arriba:"sceata.png"
        },

        "1":{titulo: "Resplandor al Amanecer",
         texto:
         '''
           <p>Dever, despiertas entre los resplandores de la mañana, que surgen
           los abetos, al este y al oeste. ¿Al oeste? Tu cerebro se termina de
           despertar, al este debe ser el sol pero, ¿qué podría causar un
           resplandor al oeste? Decidido a investigar, calzas tus pies, te ciñes
           tu gambesón y corres a la aventura. Tras media hora entre carrera y
           marcha, tus oídos escuchan el rápido huir de los animales del bosque
           y el lejano crepitar de las llamas. Aún así, continuas en tu empeño
           hasta alcanzar la cima de una pequeña colina sin nombre.</p>

           <p>Desde allí, contemplas la cercana playa atestada de las largas
           galeras vikingas y un pequeño número de prisioneros y guardias. A su
           lado, el viejo monasterio de San Brenan se ha transformado en una
           gran hoguera y desde ellas se extiende una estela de llamas y
           destrucción que llega hasta los bosques de la colina. Súbitamente
           comprendes que los guerreros enemigos deben estar muy cerca.
           El corazón se te acelera, mientras intentas aclarar tu mente.
           ¿Qué deberías hacer?
           ''',

           opciones: {"Puedes ir ahora mismo a avisar al Conde Ian":"deliberacion", #7-
                        "Decides ir a avisar a tu familia":"avisar-familia", #16-
                        "O podrías primero ir a investigar entre los abetos para saber exactamente a qué se enfrenta tu pueblo":"investigar-abetos" #-
                        },

            prueba:False,
            imagen_arriba:'Sword.png',
            imagen_abajo:False,

            },

        "deliberacion":{#7
         titulo: "La Deliberación del Conde Ian",
         texto:
         '''
         <p>Crees que la gran hilera de barcos no puede mentir. Angsax no se
         enfrenta a otra de las muchas correrías vikingas sino a un gran ejército.
         La única esperanza de tu pueblo es que los condes se pongan de acuerdo
         en convocar el Gran Ejército, reuniendo hasta el último de los campesinos.</p>

         <p>Pero eso son pensamientos para reyes. Tú solo te preocupas en correr,
         primero entre los árboles, más tarde en el camino, hasta casi desfallecer
         y luego descender a una marcha larga. Por fin, cuatro horas más tarde,
         totalmente exhausto, alcanzas la corte del Conde Ian: una ciudadela de
         piedra, superviviente de un fuerte imperial, rodeada por un laberinto
         de cabañas protegidas por un foso y una empalizada.</p>

         <p>Al llegar al portón, los guardias te reciben con la cortesía habitual;
         pero los cortas inmediatamente. &mdash;Traigo noticias urgentes. He de
         ver al conde. &mdash;dices. Tu cuerpo cubierto de sudor y polvo y tu dura
         mirada les convence de la seriedad de tu misión, sin que sea necesaria
         ni una palabra más. Pronto estás en el Gran Salón de la Torre Alta,
         donde el Conde recibe a sus vasallos cubierto de de cuero y hierro.</p>

         <p>&mdash;Han quemado San Brenan.</p>
         <p>&mdash;¿Qué son esta vez? ¿Bandidos?</p>
         <p>&mdash;No, Señor, Vikingos, un ejército.</p>
         <p>&mdash;¿Cómo qué un ejército? ¿Qué quieres decir?</p>
         <p>&mdash;Señor, sus barcos cubrían las playas hasta donde pude ver.</p>
         <p>&mdash;¿Cómo eran sus guerreros? Pudiste verlos.</p>
         <p>&mdash;Solo desde lejos, en cuanto vi lo que vi supe que tenía que dar la alarma.</p>
         <p>&mdash;Lo que dices, significa que...</p>

         <p>Las manos del conde van desde su barbilla al pomo de su espada. Sus
         pensamientos le atraviesan el cuerpo hasta hacer derribarle en su asiento,
         debatiéndose en una decisión fatal:</p>
           ''',
           opciones: {"Enfréntate a la decisión del Conde":"p-conde", #-
                       },

            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,

            },

        "p-conde":{
            prueba:True,
            r:5,
            s:["conde-huye","conde-lucha"] # las dos hechas
            },

        "conde-huye":{titulo:"Huye, está huyendo",
            texto:'''
            <p>El conde no cambia la expresión de su rostro pero tartamudea. &mdash;Muy, muy bien,
            gracias. He de retirarme a reflexionar. Senescal, ofrezca alimentos
            a este joven, vendrá fatigado.</p>

            <p>Dicho eso desaparece de tu vista. Tras él van sus thengs, mientras
            a ti te conducen a una mesa donde te sirven apresuradamente pan,
            vino e hígado de cerdo. Notas que todo el mundo está nervioso, como
            niños con ganas de orinar y enseguida un cuchicheo con alma de grito
            os confirma a todos vuestros peores temores.</p>

            <p>&mdash;Está huyendo, el conde está huyendo.</p>

            <p>Los thengs le siguen, al honor o al deshonor, porque su suerte
            está ligada a su señor desde el día en que le juraron lealtad. Los
            sirvientes, los campesinos y el resto de la gente se precipitan a huir
            también, cada uno para salvar su propia vida. La cuestión es qué harás tú.</p>
            ''',
            opciones: {"Terminas tu comida tranquilamente y luego emprendes camino al lejano norte, a avisar a tu familia":"comida-familia", #193-
                         "Huyes también, de momento, para salvar tu vida":"huyes-tambien"}, #9-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"hen.png",
            },

        "comida-familia":{ #193
            titulo:"Una Comida Estupenda",
            texto:'''
            <p>Derrúmbese el mundo, toquen los ángeles las trompetas del
            Apocalipsis, ábrase el cielo, venga el mismo demonio que tú no vas a
            dejar la comida enfriarse. Es una comida bastante solitaria; hasta
            las moscas han salido huyendo y no escuchas más que a tus propias
            tripas relamiéndose de gusto. Una vez que has terminado, bien
            rebañado el plato, y descansados tus huesos, sales de la fortaleza
            ahora vacía y te diriges directamente a tu casa. Muy ufano y muy
            complacido con tu gesta, lo único que lamentas es que no haya
            quedado nadie para apreciar tu valor.</p>
            ''',
            opciones:{"Ve a avisar a tu familia":"avisar-familia"}, #/16/-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "huyes-tambien":{#9
            titulo:"También Huyes",
            texto:'''
            <p>Viendo que todo el mundo huye, tú decides hacer lo mismo. El
            fuerte queda enseguida abandonado y vacío y tú te unes a la columna
            de refugiados que se apresura por el camino, tan rápido como pueden.
            Por supuesto, en ese tan rápido como pueden, algunos pueden más que
            otros y los ancianos y las mujeres a cargo de niños pequeños se van
            quedando atrás. Son solo una docena, veinte contando los niños y
            acabarán muertos o esclavos; quizás tú también con ellos. No puedes
            quitarte de la cabeza el pensamiento de que, a ese ritmo, los
            vikingos os alcanzarán sin remedio.</p>
            <p>Tienes un arco, y en torno al camino hay arboledas y matorrales
            donde esconderse. Quizás podrías entretener al ejército enemigo el
            tiempo suficiente para que todos puedan escapar. Pero por otro lado,
            lo que te persigue es un ejército. ¿Acaso eres un héroe de la talla
            de Alejandro, Hércules, Héctor o Lisandro?</p>
            ''',
            opciones:{"Te preparas para emboscar a los vikingos.":"emboscar-vikingos", #/54/-
                      "Les dices a los rezagados que abandonen el camino y se escondan contigo en el monte.":"escondemos-monte", #/118/-
                      "Apresuras la marcha para salvarte":"resto-tu-vida", #33-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "escondemos-monte":{#118
            titulo:"Tenemos que Escondernos",
            texto:'''
            <p>Te diriges a ellos con toda la seguridad que puedes fingir —Los
            niños no podrán escapar. —Tenemos que escondernos.</p>
            <p>&mdash;¿Escondernos? ¿En el monte? Algunas somos demasiado viejas
            para dormir al raso.</p>
            <p>&mdash;¿Y para ser esclavas de los vikingos?</p>
            <p>Después de esas palabras abandonáis el camino y os metéis entre
            los matorrales hasta internaros en el bosque. Todavía andáis más
            despacio que antes y cuando el inconfundible sonido de un ejército
            en marcha se os acerca, os tiráis todos al suelo de puro miedo.
            Pasáis así tres horas más, temiendo a cada momento ser encontrados;
            llega la noche y todavía la lenta retaguardia del enemigo no ha
            acabado de pasar por el camino.</p>
            <p>&mdash;¿Tendremos que dormir aquí? &mdash;Te cuchichea una de las
            madres.</p>
            <p>&mdash;¿Dormir? No, &mdash;le respondes. &mdash;Vamos a
            aprovechar esta noche de infierno. Seguidme ahora.</p>
            <p>A eso de la madrugada, en medio del bosque, descubrís un lago y
            en ese lago hay una isla cubierta de árboles. &mdash;Ahí,
            &mdash;dices, &mdash;ahí tendremos nuestro refugio. La isla es
            pequeña, pero somos pocos. Tendremos pescado y en el centro campos
            de avena. De momento haremos una balsa.</p>
            <p>Los sirvientes, acostumbrados a toda clase de trabajos, no tienen
            problema en hacer la balsa y, llegados a la isla, una primera choza,
            donde dormís apiñados unos junto a otros, derrumbados de los
            esfuerzos y las emociones. Los niños ni siquiera lloran por el
            hambre.</p>
            <p>A la mañana siguiente los primeros peces caen en vuestras
            primeras redes, tejidas a toda prisa. El bosque os provee del
            resto de la despensa y no tenéis que tocar la simiente de avena.</p>
            <p>A los días van siguiendo las semanas y poco a poco, escondida de
            la orilla, habéis levantado siete chozas y una pequeña casa.
            Los vikingos no os han molestado y hasta os podéis imaginar que
            vivís en un mundo aparte, un lugar bueno y tranquilo, aunque
            extrañamente deshabitado desde los tiempos de Adán.</p>
            <p>Esta noche quizás descubras por qué.</p>
            <p>&mdash;Dever, soy la voz que llamó a Samuel en los tiempos que
            eran pobres en milagros, despierta y atiéndeme.</p>
            <p>Sabes que es un sueño, estás durmiendo y sabes que esa voz no
            corresponde con la de nadie que hayas conocido, aunque al mismo
            tiempo es tan familiar como la voz de tu madre. Sí, todo debe ser
            una fantasía.</p>
            ''',
            opciones:{"Te levantas":"angel-samuel", #/6/-
                      "Dejas que se vaya el sueño":"sigue-durmiendo", #/199/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "angel-samuel":{#6
            titulo:"Caminas sobre Aguas",
            texto:'''
            <p>Abandonas tu choza y te sobrecoge el manto de estrellas. Muchas
            otras veces has mirado el cielo, pero esta vez bulle en él un hálito
            del espíritu. Entonces desde el mismo cielo ves bajar una estrella
            al lago, sumergirse en ella y reaparecer convertida en un ángel.</p>
            <p>&mdash;No tengas miedo, ven, camina.</p>
            <p>Y caminas, ¿qué otra cosa puedes hacer? Tus pies tocan el agua
            sin hundirse y aún así el líquido retiene toda su humedad y hasta el
            frío de esta noche. Sin saber como, tu ropa y tu equipo te ha
            encontrado a ti: tus ropas se han puesto solas, tu bolsa y tu espada
            cuelgan del cinto, y todo lo que necesitarías para una aventura está
            en su sitio. Pero eso tampoco te maravilla y sin embargo ya no
            tienes la sensación de estar soñando.</p>
            <p>Camináis, el ángel y tú, envueltos en luz, hasta llegar al mismo
            centro del lago. &mdash;El Señor Nuestro Dios te ha elegido para que se
            cumpla su voluntad. La bendición de Cristo y de todos los Santos
            está contigo. Y ahora, que sabes eso, ¿necesitas saber algo más?</p>
            <p>¿Qué respondes al ángel?</p>
            ''',
            opciones:{"Sí":"angel-saber-mas", #/47/-
                      "No":"sigue-durmiendo", #199-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "angel-saber-mas":{
            titulo:"Saber más",
            texto:'''
            <p>El ángel sonríe: &mdash;Está bien, lo que Dios te pide es que guíes
            a tu pueblo. Abandona la gente con la que estás ahora que yo la cuidaré
            y ve al lugar que yo te mostraré. Toma tus armas pero deja el casco que
            tu cabeza ha de quedar libre.</p>
            ''',
            opciones:{"Te disculpas y dices que no":"sigue-durmiendo",
                      "Tiras tu casco al agua y dices que sí":"si-Dios-24-9-15"}, # - | -
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "si-Dios-24-9-15":{
            titulo:"Offawick",
            texto:'''
            <p>Aunque te parece extraña la petición del ángel, no vas a discutir con
            un mensajero de Dios y despojándose de tu casco lo arrojas al agua. Inmediatamente
            se abre un túnel en las aguas que continúa bajo la superficie de la tierra.
            En su interior brota la luz y antes incluso de que el ángel diga nada ya sabes
            lo que tienes que hacer.</p>
            <p>&mdash;Ve.</p>
            <p>Y vas, solo pues el ángel ha desaparecido de tu lado, por el túnel
            que atraviesa las aguas y el interior de la tierra y extrañamente sin
            miedo. Dos días después, o eso crees, emerges en el interior de una
            gruta en el otro extremo de Angsax, junto a la ciudad de Offawick,
            antaño colonia romana y hoy un abigarrado bulto de casas y chozas, enclaustradas
            por un cercado de viejos muros y toscas empalizadas, donde se esconde una
            temblorosa muchedumbre sin rey ni jefe.</p>
            <p>Cuando llegas ante la puerta de Adriano Imperator, el guardia te grita: &mdash;¿Quién vive?
            Y tú respondes...</p>
            ''',
            opciones:{"El Rey que Dios nuestro Señor os manda":"rey-Señor-1-10-15",
                      "Dever, un guerrero del norte":"Dever-guerrero-norte-1-10-15"},#
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "Dever-guerrero-norte-1-10-15":{
            titulo:"Guerrero entre guerreros",
            texto:'''
            <p>El guardia te da la bienvenida &mdash;Adelante, bien sabe Dios que
            necesitamos brazos fuertes.</p>
            <p>Antes que te quieras dar cuenta te has unido a la <em>Fyrd</em> de
            Offawick. Las noticias que te llegan a través de tus compañeros son
            peores de lo que pudieras imaginar. No es solo que el ejército vikingo
            se acerque, es que las peleas entre los housecarles son constantes para
            ver quién es el jefe. <em>Sólo un rey podría salvarnos.</em></p>
            <p>No te atreviste a proclamar la obra que Dios había hecho en ti y
            ahora te toca esperar entre las lanzas la hora fatal de los fuertes
            invasores.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "sigue-durmiendo":{#199
            titulo:"Paz y Naturaleza",
            texto:'''
            <p>Este sueño, como tantos otros, se va y a la mañana siguiente no
            te queda ni el recuerdo vago de sus palabras. Abandonadas las
            fantasías, os espera otro día más de duro trabajo para la
            supervivencia.</p>
            <p>Las semanas paren meses y estos van construyendo los años.
            Durante todo este tiempo habéis permanecido separados de la
            civilización. Solo muy de vez en cuando, y a hurtadillas, has
            liderado a un puñado de los tuyos a intercambiar caza por
            herramientas, siempre ocultando de dónde venís y que no servís a
            ningún señor.</p>
            <p>Las tierras de Angsax las gobierna ahora un señor pagano, pero a
            vosotros esos asuntos os llegan demasiado grandes. Tú ya has casado
            con una joven viuda, has adoptado sus hijos, ya en la frontera de la
            adolescencia y en dos semanas tendrás dos preciosas gemelas.</p>
            <p>La vida te ha regalado un sitio tranquilo de paz y naturaleza
            donde pasarás tus días en espera de tiempos mejores. Pero después de
            todo, la felicidad solo requiere sabiduría y unas pocas cosas muy
            simples. Mientras se acerca el otoño de tus días esperas ser capaz
            de transmitir estas verdades a la gente de tu pueblo.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "emboscar-vikingos":{#54
            titulo:"La prueba del Héroe",
            texto:'''
            <p>Sin dar una palabra de explicación, procurando no ser visto, te
            escurres por el margen del camino hasta desaparecer en la espesura.
            Ves pasar sus caras de miedo y esfuerzo mientras te escondes y
            buscas las mejores posiciones para disparar y las rutas de
            huída.</p>
            <p>Cuando al fin los rezagados desaparecen de tu vista, el mundo
            recupera los tenues sonidos de la naturaleza. El tiempo pasa tan
            tranquilamente que la guerra se te antoja una fantasía. Pero el
            tiempo sigue pasando hasta que revela que la fantasía era esa paz.
            Ante ti, como un dragón armado de hierro, se desliza la hueste de
            Espada Negra, llenando el camino hasta el horizonte. Quizás lo
            hubiera dicho así, o con palabras parecidas, algún poeta, pero hoy
            vas a molestar algo más peligroso que un dragón.</p>
            <p>En tu escondiste clavas dos flechas en un tronco cercano, cierras
            tu corazón al miedo y dejas que se acerquen. Ya pasan los primeros
            guerreros delante tuya y esperas; la mayor confusión se consigue si
            la emboscada llega de espaldas. Después comienzas a dudar, ¿es este
            el momento? ¿Es este? Hasta que, sin saber si ha llegado el momento
            perfecto descargas la primera flecha.</p>
            ''',
            opciones:{"Lanza esa flecha":"p-emboscar-vikingos"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-emboscar-vikingos":{
            prueba:True,
            r:3,
            s:["victoria-emboscada","espadas-flechas"] # 2?    3-
            },

        "espadas-flechas":{
            titulo:"Red de Espadas y Flechas",
            texto:'''
            <p>Fallas. Una segunda acierta el cuello de un gigantón barbudo, que
            se derrumba en silencio. Antes de que lleguen los gritos disparas
            una tercera que se rompe contra el casco de un cobarde.
            Gritos, carreras, pero ya estás huyendo a otra posición.</p>
            <p>Vuelves a disparar, pero esta vez solo una de las tres flechas
            encuentra el pecho de un enemigo. Ya están preparados los guerreros
            y listos los escudos. Uno de ellos señala, te han localizado y han
            traído sus propios arqueros. Ahora cada intento de disparar o huir
            se topa con una lluvia de flechas. Intentas escurrirte entre los
            árboles, pero ahora los guerreros no tienen dificultades para correr.
            Pronto te rodean hasta que una red de espadas y flechas te atrapa.
            Resignado, dejas caer tus armas al suelo esperando haber ganado el
            suficiente tiempo para esos niños que quizás no conocerás nunca.
            En cuanto a ti, te espera una vida de esclavitud.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "resto-tu-vida":{#33
            titulo:"El Resto de tu Vida",
            texto:'''
            <p>Asumiendo lo inevitable decides que lo mejor es no sacrificarte
            de forma estúpida y, después de rezar por ellos y desearles buena
            suerte, apresuras tu marcha tanto como puedes. Pronto dejas atrás
            sus miradas de reproche y empiezas tu huída en el camino hasta que
            llega la noche.</p>
            <p>Te quedan muchos días como este, de huidas, saqueos y lamentos.
            Aunque algunos nobles oponen resistencia la mayoría huye con todo lo
            que tiene más allá del mar en medio de la noche. Tú quisieras hacer
            lo mismo pero no tienes suficiente dinero para embarcar en los pocos
            barcos que pueden hacer esa travesía. Cada día los vikingos son más
            fuertes y cada vez hay menos lugares donde esconderse. ¿Pasarás el
            resto de tu vida como un forajido o acabarás llevando las argollas
            de un esclavo?</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "conde-lucha":{
            titulo:"Atacaremos",
            texto:'''
            <p>El Conde Ian, infla su voz con coraje. &mdash; ¡Atacaremos! Y esta
            misma noche, voto a San Iurmín, nuestras espadas se alimentaran de su
            carne.</p>
            <p>La estancia se llena de vítores orgullosos y ansiosos de pelea.
            Una energía contagiosa se propaga por toda la corte, aprestando a guerreros
            y a gente común al combate. En media hora todos os habéis pertrechado
            para la pelea.</p>
            <p>La columna de guerreros parte con el conde a la cabeza, sobre un
            glorioso caballo que, según él cuenta, desciende de Bucéfalo y Aura.
            Detrás, y a pie, sus thengs, soldados nacidos con la espada.
            Más atrás queda la milicia de lanceros y entre todos, esclavos descalzos
            armados de hondas, cuchillos y miedo.</p>

            <p>Cuando se acerca la noche callan los pájaros y entonces, silenciosos
            entre los árboles cargan los vikingos. Al instante se os para el corazón.
            Son muchos más que vosotros y no hay rastro de campesinos entre sus filas.
            Estos, los que os han sorprendido en el bosque, sonríen al atacar. Ya
            está huyendo vuestra milicia, vuestros thengs tratan de formar un
            círculo con sus escudos.  Y tú, ¿qué vas a hacer?</p>
            ''',
            'opciones':{"Luchas entre los thengs.":"thengs", #170-
                        "Corres a recuperar la milicia.":"milicia",  #180-
                        "Huyes.":"huyes-batalla-conde-ian"}, #190-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "thengs":{#170
            titulo:"¿Ángeles?",
            texto:'''
            <p>Cuando los vikingos llegan a vuestras líneas todavía no habéis
            podido cerrar las filas con un muro de escudos. Ya nunca tendréis
            otra oportunidad. Aún lucháis con desesperado valor, alejando la
            hora de muerte, haciendo pagar cada vida con sangre.</p>
            <p>Enfrascado en defenderte de un bruto cubierto de una piel de oso
            que enarbola un hacha gigantesca, una lanza de dolor se introduce en
            un costado. Caes, casi sin vida, regando sangre, mientras la horda
            pasa sobre ti. La muerte te trata con desprecio, entregándote a una
            angustia que no termina, pero en el último momento, los oscuros
            cielos parecen abrirse al azul y crees ver ángeles, que te llaman
            por tu nombre. ¿Podría ser esto cierto?</p>
            ''',
            opciones:{"Respondes a los ángeles.":"respondes-angeles", #/11/-
                      "Ignoras la visión y te concentras en conservar tus pocas fuerzas.":"conservas-fuerzas-200", #/200/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "respondes-angeles":{ #11
            titulo:"Tu Luz",
            texto:'''
            <p>Gritas desesperado, pero la voz se te corta entre estertores de
            sangre. Enseguida se te va la vista y ya, pronto, duermes hasta que
            una dulce voz te despierta.</p>
            <p>&mdash;Levántate y resplandece, porque ha llegado tu luz. La
            gloria de Dios brilla sobre ti.</p>
            <p>Abres los ojos. Amanece. Trescientos cuervos levantan el vuelo
            entre graznidos. Un halcón, que da vueltas en el cielo, los ha
            espantado. Te incorporas temblando de cansancio y una onza de dolor.
            Seiscientos cuerpos cubiertos solo de sangre y rocío yacen ante ti.
            Tu estás igual, descalzo y sin más ropa que los calzones; vuestros
            conquistadores os han robado a conciencia.</p>
            <p>Pero estás vivo.</p>
            <p>&mdash;No tengas miedo.</p>
            <p>Te das la vuelta. Quien te habla es un niño moreno, vestido con
            una leve túnica egipcia que crees egipcia, el pelo cortado a la
            manera de los esclavos, sus pies descalzos.</p>
            <p>&mdash;No... ¿puedes ayudarme? &mdash;Todavía no piensas con
            claridad.</p>
            <p>&mdash;Quien me envía ya te ha ayudado, Devir. Ahora debes ir a
            la abadía de San Cuthbert. Le pedirás a su abad que te confiese y él
            te recibirá y te ungirá y tú servirás a Dios, como mejor puedas.</p>
            <p>&mdash;¿Quién eres?</p>
            <p>El dolor de la herida te sobrecoge de nuevo y caes de rodillas y
            brazos sobre la tierra. Cuando te levantas, el chico ha desaparecido
            y en su lugar aparece el caballo del conde caminando tranquilamente
            hacia ti. Esperas, lo coges de la brida y andas junto a él, pasando
            entre las filas de muertos que te llenan de lágrimas. Solo cuando
            los dejas te atreves a afrontar el dolor que te trae subir a la
            grupa del caballo.</p>
            <p>Ya montado, te concentras en mantenerte erguido sobre la silla,
            agradeciendo al viento que te aviva los sentidos. Luchas contra la
            tentación de seguir el viejo camino romano y te adentras por una
            senda de cazadores, difícil pero discreta y te dejas llegar.</p>
            <p>Y va llegando, tras horas eternas la primera noche, al monte
            solitario donde te encuentras, un animal entre animales, fatigado y
            herido, hambriento, descalzo y casi desnudo, vivo solo por un
            milagro o, tal vez, un sueño. Quisieras seguir, abandonar estos
            parajes, pero desconfías de tu resistencia.</p>
            ''',
            opciones:{"Sigues Adelante.":"p-sigues-adelante-31", #/31/-
                      "Buscas un refugio para la noche.":"refugio-noche-21", #/21/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-sigues-adelante-31":{
            prueba:True,
            r:5,
            s:["monasterio-iv","cadaver-bosque-iv"],
            },
        "cadaver-bosque-iv":{
            titulo:"Un cuerpo en el bosque",
            texto:'''
            <p>El frío se recrudece según van pasando las horas. Te pegas al
            cuerpo de tu caballo buscando su calor mientras tratas de mantener
            la dirección del norte. Pero pronto cae la oscuridad, la oscuridad
            atroz del bosque nocturno que junto con el cansancio acumulado
            conspiran contra ti hasta que acabas perdido.</p>
            <p>Sin poderlo evitar, sin ni siquiera poder luchar contra ello,
            acabas dormido bajo las lágrimas del cielo.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "refugio-noche-21":{
            titulo:"El Carro",
            texto:'''
            <p>Apresuras los ojos, mirando a lo lejos, buscando cualquier cosa
            que pueda servirte de abrigo. Con una pala podrías excavar un
            refugio, con una hacha pequeña hacerte una cabaña, pero estás
            demasiado cansado y herido para conseguirte construirte algo antes
            de que caiga la noche. Pronto se va a hacer el invierno para ti;
            casi desnudo y si no tiemblas ya de frío, es por miedo. A momentos
            te pegas a la piel de tu caballo, buscando su calor y a momentos
            vuelves a erguirte, con las pocas fuerzas que te quedan.</p>
            <p>Es entonces cuando vislumbras a lo lejos una luz ambarina
            tambaleándose por el camino. Te paras, te apresuras, dudas y en
            medio de todo el dolor que te revienta el cuerpo. ¿Quién llevará esa
            luz solitaria? La sigues por esperanza y desesperación; si Dios
            hubiera querido tu aliento, ya lo habría tomado. Al poco comienzas a
            escuchar una embriagadora música de liras y cantos en una lengua que
            te parece tan lejana a tu idioma como a la jerga de los vikingos.
            ¿Serán monjes cantando en Latín? ¿Pero qué harían unos monjes en
            medio del campo y, sobre todo, en este día de tristezas?</p>
            <p>Por fin los ves, sobre las primeras oscuridades de la noche.
            Cuatro ciervos, con herrajes de bronce, tiran de un largo carro azul
            cubierto con una lona blanca, ambarina ahora por la acción de un
            farol. Un niño de pelo verde, abrigado de cabeza a tobillos con
            ropas de plumas, da el so a las bestias. Desde el carro salen otras
            diez personas, de niños a viejas, empuñando instrumentos de música y
            cuernos de vino.</p>
            <p>&mdash; Madre, madre, un pobre. &mdash;Dice el niño. &mdash;¿Nos
            dejas ayudarle?</p>
            <p>&mdash;Ese permiso lo tendrá que dar el señor pobre.</p>
            <p>&mdash;Señor pobre, si nos deja ayudarle se lo agradeceríamos
            mucho. ¿Quiere quedarse con nosotros? Pronto dormiremos; nos queda
            pan caliente, hidromiel y pastel de chirivías. Pero si no quiere
            quedarse con nosotros también podemos darle ropa, comida y un beso.
            Déjenos, señor pobre por favor.</p>
            <p>Dudas, estás tentado de huir ante lo estrafalario de la
            situación. Hasta te preguntas si no serán duendes, de esos que
            engañan a los viajeros para matarlos, comerlos y hervir sus huesos
            en caldos mágicos.</p>
            ''',
            opciones:{"Te quedas con ellos en el carro.":"carro-41", #/41/-
                      "Aceptas la comida y la ropa, pero te vas.":"comida-ropa-adios-51", #/51/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "comida-ropa-adios-51":{
            titulo:"",
            texto:'''
            <p>&mdash;Ne...necesito la ropa, muchas gracias, pero sé cuidarme
            solo.</p>
            <p>Tus palabras decepcionan un poco a los extraños viajeros e insisten
            en su ofrecimiento de ayuda mientras te pasan una túnica blanca de una
            tela que no has visto nunca, pantalones de cuero, botas y una bolsa
            llena de pan negro recién horneado.</p>
            <p>¿Recién horneado? ¿Cómo podrían tener un honor dentro del carro?
            No puedes rechazar la idea de que esto se deba a la magia y, si es
            así, estás en la presencia de elfos, como en las leyendas antiguas.
            Elfos, a los que quizás hayas ofendido...</p>
            ''',
            opciones:{"Te disculpas y te alejas lentamente":"alejarse-lento-14-9", #
                      "Sales corriendo":"sales-corriendo-14-9"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "carro-41":{
            titulo:"",
            texto:'''
            <p>De alguna manera has acabado bajo mantas de lana en medio del
            carro, rodeado de los viajeros que apretujados junto a ti, han
            quedado dormidos. De la misma manera el cansancio de las horas te
            lleva al mundo de los sueños.</p>
            <p>El carro se ha convertido en un barco volador, suspendido de una
            bolsa gigante de tela gris, por encima de un extraño mar gris y
            debajo del mismo cielo. Todos tus compañeros son elfos y, en verdad
            tú también te has convertido en un elfo, y te sientes seguro y feliz
            y…</p>
            <p>Despiertas solo, tumbado sobre una estera multicolor de extraña
            trama, con tu herida cubierta con una especie de tela de araña,
            aunque más limpia, más tersa y más suave. Junto a ti tienes regalos:
            botas recias, ropas de cuero y lana, una capa y una cota de malla
            digna de un noble. Hay también una bolsa con un gran pan negro y una
            tablilla de madera con algo escrito cuyo contenido descubrirías si
            supieras leer. Por último y, quizás más importante, una extraña
            espada, más bien corta, con forma de hoja de sauce, que primero
            crees de oro, pero pronto concluyes que es de bronce.</p>
            <p>Cerca, sobre los árboles, ves descollar la torre de la abadía de
            San Cuthbert. Solo lamentas la pérdida de tu caballo.</p>
            ''',
            opciones:{"Buscas a tu caballo.":"buscas-caballo-81", #/81/-
                      "Vas a la Abadía de San Cuthbert.":"san-cuthbert-72", #/72/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "buscas-caballo-81":{
            titulo:"",
            texto:'''
            <p>Desde luego que tu caballo era demasiado importante como para
            perderlo sin lucha. ¿Se habrán cobrado los extraños viajeros tu
            caballo en pago de su ayuda? ¿O sencillamente le han dejado
            abandonado en medio del campo?</p>
            ''',
            opciones:{"Intentas buscar las huellas del carro":"carro-17-sep", #-
                      "Buscas tu caballo por los alrededores":"caballo-17-sep"},#
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "carro-17-sep":{
            titulo:"El interior de la tierra",
            texto:'''
            <p>Solo tienes dar cien pasos para descubrir las cicatrices que las
            ruedas del carro han dejado en la tierra cubierta de hierba. Desde
            entonces puedes avanzar a buen ritmo sin perder la pista. De hecho
            hasta notas un detalle peculiar, casi insignificante: allí donde las
            ruedas han tocado la hierba, han dejado un hilillo de polvo brillante
            que muy bien podría ser bronce. Tanto tus ojos como tus dedos te
            dicen que es real. ¿Serán estos los sembradores de bronce de los más
            antiguos mitos? Y aún te resta una sorpresa mayor llegado a un punto
            donde las huellas desaparecen, pero no como cabría esperarse, cada
            vez más leves, sino como si todo el carro se hubiera zambullido en
            el inframundo.</p>
            ''',
            opciones:{"Escarbas en la tierra en busca de pistas":"escarbas-17-sep", #
                      "Abandonas la búsqueda y vas a la abadía":"san-cuthbert-72", #-
                      "No pierdes la esperanza de enconrar tu caballo":"p-caballo-17-sep"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "san-cuthbert-72":{
            titulo:"San Cuthbert",
            texto:'''
            <p>Eras niño la última vez que visitaste la abadía de San Cuthbert
            pero sigue asombrándote. De sus doce construcciones, cinco son de
            piedra: la hospedería, sus dos iglesias, la residencia de novicios
            y el gran salón, inmenso con sus dos plantas. Por lo demás, salvo
            por la ausencia de mujeres, que no de niños, el lugar se parece a
            cualquier otro pueblo: los mismos campos de avena, los mismos
            cercados de ovejas y cerdos y la misma empalizada.</p>
            <p>Uno de los siete guardias te conduce desde la puerta a la
            hospedería. No quiere saber nada de tus asuntos, le basta con tener
            tu espada y saber que no eres un bandido. &mdash;Los afanes que traigas
            se los llevará un monje, a mí no me eches cuentas, que yo no
            cuento.</p>
            <p>Pronto te atiende un novicio y tu historia le hace traer a un
            monje profeso y así entrevista tras entrevista, llegas ante el mismo
            abad.</p>
            <p>&mdash;¿Te han dicho los ángeles que debo confesarte y
            ungirte?</p>
            <p>&mdash;Sí. &mdash;La voz te tiembla, pensando que todo lo vivido
            desde la batalla parece el resultado de un saludable golpe en la
            cabeza.</p>
            <p>&mdash;Nada me anima a ungirte todavía, pero la misericordia me
            urge a que me entregues tus pecados. Después rezaremos juntos y
            después ya se verá.</p>
            <p>Tras la confesión, viene una misa y tras ella el oficio de la
            Canción de la Tarde, que el ritmo lento del monasterio os lleva dos
            horas. Ya terminando el cuarto de los salmos, el abad se levanta en
            medio de todos los monjes y te señala.</p>
            <p>&mdas;¡Es cierto! Traédme los santos óleos, he de ungir a un
            Rey.</p>
            <p>Las miradas de todos los monjes y de los novicios, hasta de los
            niños que se han unido al monasterio se mueven del abad a ti y de ti
            al abad. Solo eres un visitante, uno de tantos otros, no
            especialmente fuerte, ni piadoso, ni dotado de una voz especialmente
            clara. ¿Se habrá vuelto loco el abad?</p>
            <p>Dudas si decir algo, si rechazar este honor y esta carga, rey,
            ¿pero de qué? Si nunca ha tenido Angsax un rey, ¿por qué habría de
            tenerlo ahora que todo parece perdido?</p>
            <p>&mdash;Dever, &mdash;se dirige a ti el Abad, &mdash;¿Aceptas de
            mis manos el encargo que Dios te hace de regir y proteger al pueblo
            de Angsax? ¿Aceptar ser su rey en sus horas más oscuras?</p>
            ''',
            opciones:{"Sí.":"si-rey", #/53/?
                      "No.":"no-rey", #/83/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "conservas-fuerzas-200":{
            titulo:"Horrible Hora",
            texto:'''
            <p>Todavía aguantas dolores durante una horrible hora de siglos.
            Después un minuto de angustia luchando en agonía contra la oscuridad
            hasta que por fin duermes.</p>
            <p>Cuando despiertas vistes de túnica blanca y estás entre una
            multitud inmensa que proclama: Santo, Santo, Santo es el Señor, Rey
            del Universo...</p>
            <p>Desde entonces todo es felicidad.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },


        "milicia":{ #180
            titulo:"Salvar la milicia",
            texto:'''
            <p>La milicia empezaron a agitarse, como la hierba al viento, tan pronto
            como vieron aparecer a los vikingos. Su bandera, el viejo estandarte
            de lino de la parroquia, tiembla con el miedo de su portador. Corres,
            a alcanzarlos, antes de que huyan, interceptándolos, mirándolos a la
            cara y alzando tu espada al cielo.</p>
            <p>&mdash;¡Angsax y San Iurmín! &mdash;gritas, no hay tiempo para discursos,
            y golpeas el filo del escudo con la espada, como han hecho miles de guerreros antes de ti.
            <em>"Contra caos, orden"</em>, recuerdas el consejo de tu padre y lo
            sigues literalmente. &mdash;¡Muro de Escudos! ¡Venga deprisa!.</p>
            <p>Ya están luchando los thengs contra los vikingos. Ya se acercan
            sus espadas a las lanzas de tu milicia; pero no puedes darte la vuelta
            y refugiarte entre sus filas. Todavía no, todavía tiemblan y ante el
            choque contra el acero se derrumbarían sin lucha. Tienes que hacer
            algo. Sientes que decidas lo que decidas no tienes garantizado nada,
            pero sabes que no tienes tiempo para preocuparte. Así que, sonríes,
            ruges como un león y…</p>
            ''',
            opciones:{"Te das la vuelta y atacas al enemigo, esperando servir de ejemplo.":"ejemplo-milicia", #-
                        "Alineas las filas personalmente, tan rápido como puedes.":"milicia-filas", #-
                        "Arrebatas el estandarte del santo y lo lanzas contra el enemigo, esperando animar a tus tropas a recuperarlo":"milicia-estandarte"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "ejemplo-milicia":{
            prueba:True,
            r:3,
            s:["carga-gloriosa-24-9-15","muerte-estupida-24-9-15"], # carga - muerte -
            },

        "muerte-estupida-24-9-15":{
            titulo:"Solo",
            texto:'''
            <p>Solo cargas contra el enemigo. Corres con ferocidad pero nadie te
            sigue y antes de que puedas cambiar de opinión una nube de lanzas descarga
            su muete sobre tu pecho.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "carga-gloriosa-24-9-15":{
            titulo:"Carga Gloriosa",
            texto:'''
            <p>¡Raaarghf! No sabes ni lo que gritas, pero, despreciando tu vida y la
            inteligencia te lanzas tú solo al enemigo, como los dioses guerreros
            paganos. Y por milagro quizás, toda la milicia te sigue embebida del
            mismo espíritu salvaje que anima a usar el escudo como otra arma.</p>
            <p>Y cuando chocáis contra el enemigo los guerreros vikingos no saben
            cómo reaccionar y, maravillas de las maravillas, rompéis su muro de
            escudos y se dispersan, huyendo como conejos.</p>
            <p>Gritáis victoria, pero desde el bosque nuevas hordas vikingas se
            unen a sus compañeros y desplazan a los cobardes. Detrás de ellos cada
            árbol parece acoger un nuevo vikingo y te queda claro que con las fuerzas
            locales del Conde es del todo imposible que los detengáis.</p>
            <p>Además los <em>thengs</em> no han tenido tanta gloria como vosotros
            y todavía están luchando contra sus propios vikingos.</p>
            <p>Mientras, todos los milicianos miran a su nuevo héroe. ¿Qué ordenas?</p>
            ''',
            opciones:{"Unes tus tropas a las del Conde Ian":"milicia-y-thengs-24-9-15", #
                      "Ordenas una retirada inmediata":"retirada-milicia-inmediata-24-9-15"}, #-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "retirada-milicia-inmediata-24-9-15":{
            titulo:"Retirada",
            texto:'''
            <p>Ante la disparidad de fuerzas decides volver a la razón y retirarte.
            En cuanto a los <em>thengs</em>, deseas lo mejor para ellos pero no vas
            a arriesgar a toda una hueste de campesinos a una guerra de verdad. En
            vez de eso ordenas una rápida retirada mientras una docena de vikingos,
            exploradores sin duda, os siguen a caballo sin acercarse demasiado.</p>
            <p>El tiempo pasa con la rapidez del miedo hasta que vuestros pasos os
            alejan de la batalla, pero no de los exploradores vikingos que os vienen siguiendo.
            Sopesas tus opciones y solo se te ocurren tres maneras de conseguir que sobrevivan:
            resguardaros bajo las empalizadas del fuerte, huir a la tierra de los
            pantanos donde los caballos no podrán seguiros o intentar un ataque
            contra el puñado de exploradores que están tras vuestra pista.</p>
            ''',
            opciones:{"Ordenas ir al fuerte del conde para defenderlo.":"al-fuerte", #/92-
                        "Ordenas ir a por las mujeres y los niños para emprender luego la huida a la Tierra de los Pantanos.":"tierra-pantanos", #/187-
                        "Atacar a los exploradores":"atacar-exploradores-25-9-15", #-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "atacar-exploradores-29-9-15":{
            titulo:"Rodeados por diez mil enemigos",
            texto:'''
            <p>Los exploradores se retiran lentamente en cuanto cargáis contra
            ellos y cuando estáis a punto de alcanzarlos, dan la vuelta a sus
            monturas y aceleran hasta galopar. Uno de ellos reacciona demasiado
            tarde y tu espada se cobra primero su montura y después al jinete sobre
            el frío suelo del campo de batalla.</p>
            <p>Pero va a dar igual: las hordas vikingas han avanzado hacia tu
            unidad sin que os hubieráis percatado de ello, nublados por las ansias
            de victoria y ahora estáis rodeados por diez mil enemigos y solo podéis
            elegir entre esclavitud o muerte.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "huyes-batalla-conde-ian":{#190
            titulo:"Triste Juglar",
            texto:'''
            <p>Decides que no hay salvación posible y huyes para salvar tu vida.
            Tu caballo no es tan poderoso como el del Conde, pero es ligero y
            se basta para escapar de los vikingos.</p>
            <p>De lo que no te escapas es de las maldiciones del conde Ian, ni
            de los gritos de dolor de tus compañeros. También los de la milicia
            son alcanzados. Treinta minutos después solo escuchas los latidos de
            tu corazón y el casco de los caballos y entonces sabes que Angsax
            está perdido.</p>
            <p>Aún tardan tres años, pero poco a poco los vikingos imponen su
            conquista y establecen un reino. Tu familia pierde sus tierras y
            propiedades, como la mayoría de los nobles de Angsax, pero consiguen
            sobrevivr dedicándose al comercio. En cuanto a ti, desmoralizado
            tras tu huída, has vivido de acá para allá, haciendo de juglar
            para vuestros conquistadores, ocultando tu nombre</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "investigar-abetos":{ # /17/
            titulo:"Entre los Abetos",
            texto:'''
            <p>Haces la señal de la cruz sobre tu frente y te internas en el bosque.
            La reliquia que pende de tu cuello te araña la piel. Se te
            achica la garganta mientras tus ojos y oídos se agudizan como los de un lobo.
            Pronto escuchas los pasos de un puñado de guerreros sobre la hojarasca.
            Sabes que sólo pueden ser una avanzadilla de una gigantesca horda.</p>

            <p>Paras. Junto a un abeto preparas tu arco y esperas. Necesitas ver
            a tus enemigos y el resto del universo parece enmudecer. Todas tus
            preocupaciones han desaparecido; mientras tu corazón sigue moviendo
            los segundos.</p>

            <p>¡Ahí están! A treinta pasos, entre las ramas y matorrales. Son siete,
            lanzas y escudos viejos, sin armadura, con el lino de sus ropas manchadas
            de sangre y andares despistados. Si todos sus guerreros fueran así los
            vikingos no merecería su fama.</p>
            ''',
            opciones:{"Disparas con tu arco y huyes.":"disparas-arco", # 30-
                        "Intentas retirarte a escondidas para ir a avisar al Conde Ian.":"avisar-conde-40", #/40/-
                        "Te quedas quieto hasta que pasen para poder internarte más en el bosque y en el peligro hasta encontrar la fuerza principal.":"internarte-bosque" #50/-
                        },
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "disparas-arco":{
            titulo:"Todo en una Flecha",
            texto:'''
            <p>No quieres fallar este tiro. Te concentras en el último y dejas
            que camine hasta que te ofrezca su espaldas. Éste es el momento
            definitivo.</p>
            ''',
            opciones:{"¿Acertarás?":"p-disparas-arco"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-disparas-arco":{
            prueba:True,
            r:7,
            s:["disparas-arco-victoria","disparas-arco-fallo"] # 60- 70-
            },

        "disparas-arco-fallo":{
            titulo:"A cubierto",
            texto:'''
            <p>Tu flecha casi roza el cuello de uno de los vikingos y se pierde
            entre los bosques. Tus enemigos reaccionan levantando sus escudos y
            agrupándose mientras miran en todas direcciones. Dentro de muy poco
            hasta ellos comprenderán que estas solo.</p>
            ''',
            opciones:{"Vuelves a disparar":"p-vuelves-disparar-15-sep",
                      "Huyes":"huyes-15-sep"}, #vuelves disparar - |  huyes-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "huyes-15-sep":{
            titulo:"Huyes",
            texto:'''
            <p>Aprovechas tu oportunidad y antes de que los vikingos puedan
            darse cuenta de lo que está pasando has puesto mucho terrerno por
            delante. Aún corres durante tanto tiempo como te permiten tus piernas
            hasta que te sientes seguro de que no te han seguido.</p>
            <p>Mientras recuperas resuello decides que lo más prudente es ir a
            dar la alarma.</p>
            ''',
            opciones:{"Ve a avisar al conde":"avisar-conde-40"}, #-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-vuelves-disparar-15-sep":{
            prueba:True,
            r:5,
            s:["ahora-aciertas-15-sep","nuevo-fallo-15-sep"], #ahora aciertas - | nuevo fallo -
            },

        "ahora-aciertas-15-sep":{
            titulo:"Un guerrero muerto",
            texto:'''
            <p>La flecha le entró desde arriba, burlando su escudo, hundiéndose
            en su pecho de arriba abajo y ahora cae entre estertores y muere
            rodeado de la zozobra de sus compañeros. Has ganado la oportunidad
            que necesitabas para poder huir y, consciente de que no tendrás otra
            asi, no pierdes un instante hasta desaparecer entre los árboles.</p>
            ''',
            opciones:{"Ve a avisar al conde de lo que has encontrado":"avisar-conde-40",
                      "Intenta dar un rodeo y busca la fuerza principal":"fuerza-principal",
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "nuevo-fallo-15-sep":{
            titulo:"Ataque",
            texto:'''
            <p>Tu seguda flecha se estrella ahora contra uno de sus escudos.
            Gritan y se acercan a ti, tan rápido como pueden sin romper su muro
            de protección. Calculas que todavía puedes disparar una flecha más
            antes de que te alcancen.</p>
            ''',
            opciones:{"¿Un último intento?":"p-nueva-flecha-16-sep", #-
                      "Huyes":"p-huyes-16-sep"}, #nueva flecha-, #p-huyes
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-nueva-flecha-16-sep":{
            prueba:True,
            r:4,
            s:["acierto-muerte-16-sep","fallo-muerte-16-sep"], # 1- 2-
            },

        "p-huyes-16-sep":{
            prueba:True,
            r:7,
            s:["escapas-vikingos-17-sep","te-pillan-vikingos-17-sep"], # ambos hechos
            },

        "escapas-vikingos-17-sep":{
            titulo:"Escapas",
            texto:'''
            <p>Aprovechando la confusión de los vikingos y su poca inclinación al
            heroísmo consigues enseguida poner tierra de por medio y desaparecer
            de su vista. En este mismo momento tienes que tomar una decisión, o
            avisas inmediatamente al Conde Ian del peligro o intentas investigar
            más.</p>
            ''',
            opciones:{"Avisa al Conde Ian":"avisar-conde-40", #-
                      "Da un rodeo y busca la fuerza principal":"fuerza-principal"}, #-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "te-pillan-vikingos-17-sep":{
            titulo:"",
            texto:'''
            <p>Había un líder entre ellos, para tu mala suerte, un líder que
            despertó justo cuando disparaste esa flecha. Él fue quien rehizo a
            sus compañeros y les dio la audacia para perseguirte sin descanso y
            quien, cuando te tuvo a tres metros, arrojó su lanza contra tu
            espalda...</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "fallo-muerte-16-sep":{
            titulo:"Última derrota",
            texto:'''
            <p>Maldices tu puntería cuando ves a tu última flecha estrellarse de
            nuevo contra sus escudos. Están demasiado cerca y envalentonados por
            tu puntería ya no huirán. Desesperado, tratas de cambiar tu arco por
            espada y escudo, pero para cuando estás listo ya estás rodeado por
            sus lanzas, que te atacan una y otra vez.<p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "acierto-muerte-16-sep":{
            titulo:"Última victoria",
            texto:'''
            <p>No puedes evitar una sonrisa de triunfo cuando ves desplomarse a
            uno de los vikingos; pero ya están demasiado cerca como para huir y
            ofrecerte sus espaldas. En vez de eso arremeten con sus lanzas.</p>
            <p>Intentas defenderte, pero apenas tienes tiempo para intercambiar
            arco por espada. Para entonces estás rodeados por sus lanzas...</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "disparas-arco-victoria":{
            titulo:"Huyen como conejos",
            texto:'''
            <p>Un grito apagado y el guerrero se desploma en el suelo, manchado
            esta vez con su propia sangre. Sus compañeros no tienen tiempo a
            comprender lo que ha pasado cuando la segunda de tus flechas
            atraviesa el pecho de otro de los suyos. El pánico les hace huir
            como conejos entre los árboles y tú tomas una rápida decisión.</p>

            <p>¿Debes volver inmediatamente a avisar al Conde Ian de los
            vikingos que has encontrado? ¿O sería mejor arriesgarte a descubrir
            la fuerza principal de los vikingos aunque tardes más?</p>
            ''',
            opciones:{"Te retiras a avisar al Conde Ian.":"avisar-conde-40", #/40/-
                      "Buscas la fuerza principal.":"fuerza-principal", #/80/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "fuerza-principal":{#80
            titulo:"Te internas en la espesura",
            texto:'''
            <p>Convencido de que ese grupo de botarates son lo peor de los
            vikingos, te internas en el bosque para descubrir a sus verdaderos
            guerreros; primero apartándote de su dirección para luego tratar de
            adivinar dónde podría moverse el grupo.</p>
            <p>El breve silencio de tus pasos queda pronto interrumpido por los
            crujidos de las carretas. Tienen que estar cerca, pero hasta un
            ejército puede ser invisible en medio de esta espesura.</p>
            <!-- Descripción con niños, hombres, mujeres, etc -->
            <p>Ahora mismo descubres dos grupos de guerreros, armados con
            espadas y grandes escudos que intentan cazarte como a un conejo.</p>
            <p>Ya te han visto, están demasiado cerca para disparar y no podrías
            sobrevivir a un combate contra tantos enemigos. Tus opciones se
            reducen a una, huir.</p>
            ''',
            opciones:{"¡Intenta escapar!":"p-fuerza-principal"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-fuerza-principal":{
            prueba:True,
            r:7,
            s:["escapas-90","te-pillan-100"] # 90-  100-
            },

        "escapas-90":{
            titulo:"Escapas",
            texto:'''
            <p>Estorbados por sus escudos los fieros guerreros vikingos no
            pueden sobreponerse a tu agilidad al sortear los obstáculos del
            bosque. Tras una hora de carrera y marcha decides que los has
            dejado atrás y te paras un momento a consolidar en tu cerebro la
            información adquirida.</p>
            <p>La primera pista es la inmensa hilera de barcos, la segunda es la
            presencia de varias clases de guerreros. Durante toda tu infancia
            has vivido con el miedo a los saqueos y asaltos de los bárbaros,
            pero esta vez han venido para conquistar la tierra y, quizás, para
            exterminar al pueblo de Angsax.</p>
            <p>Tu mente y tu corazón se revuelven con las imágenes que la
            memoria mezcla con la imaginación. Tus padres muertos, tus primos
            pequeños sirviendo de esclavos con cadena al cuello y tu pueblo
            quemado hasta los cimientos. Sabes que en dos semanas este podría
            ser el futuro.</p>
            ''',
            opciones:{
                "Avisas al Conde para que convoque a los guerreros.":"avisar-ian-62", #/62/-
                "Emprendes camino hasta el fuerte de tu familia, en el lejano norte.":"avisar-familia", #/16/-
                },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "te-pillan-100":{
            titulo:"Segundos Fatales",
            texto:'''
            <p>Corres con todas tus fuerzas, esquivando los troncos y las raíces
            que salen a tu paso. Crees que lo estás consiguiendo y de hecho, al
            principio consigues dejar atrás a los guerreros que tienen
            dificultades para seguirte enarbolando sus largos escudos. Sin
            embargo la mala suerte se topa contigo en la forma de un viejo lobo,
            que demasiado asustado para ignorarte y demasiado cansado para huir
            se cruza en tu camino enseñando sus colmillos.</p>
            <p>Te paras solo diez segundos para mostrarle tus armas y dejar que
            se vaya; pero son diez segundos fatales. Antes de que puedas volver
            a emprender la carrera el filo de una espada se hunde entre tus
            costillas.</p>
            <p>Caes al suelo, te falta el aire y los ojos se te llenan de
            oscuridad y muerte.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },


        "avisar-conde-40":{#40
            titulo:"La Decisión de un Conde",
            texto:'''
            <p>Te agachas y lentamente deshaces tu pasos caminando hacia
            atrás hasta estar seguro de que no te han visto. Entonces te das la
            vuelta y te deslizas entre los árboles para luego emprender la
            carrera. Solo entonces se dan cuenta de tu presencia pero ya es
            demasiado tarde para ellos.</p>
            <p>Tú solo te preocupas en correr, primero entre los árboles, más
            tarde en el camino, hasta casi desfallecer y luego descender a una
            marcha larga. Por fin, cuatro horas más tarde, alcanzas la corte del
            Conde Ian: una ciudadela de piedra, superviviente de un fuerte
            imperial, rodeada por un laberinto de cabañas protegidas por un foso
            y una empalizada.</p>
            <p>Al llegar al portón, los guardias te reciben con la cortesía
            habitual; pero los cortas inmediatamente. --Traigo noticias
            urgentes. He de ver al conde, -- les dices. Tu cuerpo cubierto de
            sudor y polvo y tu dura mirada les convence de la seriedad de tu
            misión, sin que sea necesaria ni una palabra más. Pronto estás en el
            Gran Salón de la Torre Alta, donde el Conde te recibe cubierto de de
            cuero y hierro.</p>
            <p>-- Han quemado San Brenan.</p>
            <p>-- ¿Qué son esta vez? ¿Bandidos?</p>
            <p>-- No, Señor, Vikingos, un ejército.</p>
            <p>-- ¿Cómo qué un ejército? ¿Qué quieres decir?</p>
            <p>-- Señor, sus barcos cubrían las playas hasta donde pude ver.</p>
            <p>-- ¿Cómo eran sus guerreros? ¿Pudiste verlos?</p>
            <p>-- Los que vi no eran nada más que milicia, pero solo alcancé a
            ver un grupo pequeño; estaban en el bosque y...</p>
            <p>-- Muy malo...</p>
            <p>Las manos del conde van desde su barbilla al pomo de su espada,
            que desenvaina enseguida para tomar una decisión fatal.</p>
            ''',
            opciones:{"Descubre la decisión del conde":"p-avisar-conde-40"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-avisar-conde-40":{
            prueba:True,
            r:6,
            s:["conde-lucha","conde-huye"] # hechos los dos
            },

        "internarte-bosque":{#50
            titulo:"Serpiente de Carne y Hierro",
            texto:'''
            <p>Decides que no vale la pena cruzar tus armas con estos imberbes y
            los dejas pasar, oculto por la maleza y tu capa. Enseguida
            comprendes que no tenías motivo de preocupación; esos vikingos ni se
            molestan en observar sus alrededores; orgullosos como están de sus
            propias fuerzas. Al poco primero ellos y después su rastro
            desaparecen.</p>
            <p>Caminas cuidando tus paso, vigilando ruidos y silencios y hasta
            aprestando tu olfato a cualquier olor extraño. Media hora después
            los pájaros callan y tras su silencio llegan un rumor de carretas,
            mulas y palabras recias nacidas de vientos y fiordos. Entre zarzales
            te buscas una atalaya y contienes el corazón hasta que por fin ves
            al gran monstruo, la serpiente de carne e hierro, el dragón de los
            reyes salvajes, formado por cientos de guerreros que huelen a sudor
            y sangre; tan distintos de los que viste anteriormente que se diría
            son de otro país. Tus ojos se concentran en extraer toda información
            útil: hay mujeres y niños entre sus filas, casi ningún caballo,
            todos tienen escudos; cuando otro par de ojos miran fuertemente en
            tu dirección.</p>
            ''',
            opciones:{"Corres.":"corres-serpiente-carne-hierro", #/12/-
                      "Te quedas quieto.":"quieto-serpiente-carne-hierro", #/22/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "corres-serpiente-carne-hierro":{#12
            titulo:"Oriente",
            texto:'''
            <p>Saltas de tu escondite y corres. Eres más rápido que la mayoría y
            al principio lo pruebas arañando distancia a tus perseguidores. Pero
            entonces llega el sonido más amenazador que hayas escuchado en tu
            vida: los cascos de los caballos nórdicos sobre el manto del bosque.
            Los pocos jinetes que viste, no podían ser más de veinte, muy pocos
            para un ejército, demasiados para un fugitivo.</p>
            <p>Pero sigues corriendo hasta que tu corazón se rinde y tienes que
            sostenerte contra un árbol mientras tus pulmones tratan de devorar
            el aire. Apenas recuperas tu alma te das cuenta que estás rodeado.
            Delante tuya y a los lados, la veintena de jinetes; detrás todo un
            ejército de vikingos.</p>
            <p>Quizás con tu arco podrías matar a alguno, pero sabes que estás
            perdido y alzas las manos vacías en rendición. Te espera una vida de
            esclavo. No lo sabrás hasta dentro de tres, pero tras muchos viajes
            y sufrimientos, acabarás como guardia de la corte de un príncipe
            oriental y nunca volverás a ver tu tierra.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "quieto-serpiente-carne-hierro":{#22
            titulo:"Eres un Ratón",
            texto:'''
            <p>Ahora eres un ratón. Esas palabras fueron de tu abuelo, un viejo
            cincuentón y tú entonces un niño de diez. Te las susurró mientras
            esperabas agazapado a que la <em>señora liebre</em> se acercara hasta donde
            no pudiste fallar. Esas mismas palabras te han venido ahora mientras
            esperas agazapado a que los ojos que han mirado en tu dirección se
            aparten hasta donde no puedan verte. Tardan el tiempo de rezar diez
            padrenuestros, pero al final la columna de vikingos se separa lo
            suficiente como para que puedas desaparecer de nuevo en el
            bosque.</p>
            <p>En cuanto te sientes seguro, apresuras la marcha con la energía
            de la desesperación. Tienes una información preciosa sobre la
            grandeza de este ejército, que ya es malo, pero la presencia de
            mujeres y niños es peor. Indica, no puede ser de otra manera, que
            han venido aquí para conquistar y subyugar. Nadie en todo Angsax
            está a salvo. Pero tu información solo servirá de algo si llega a
            tiempo para que los señores de cada aldea llamen a todo el pueblo a
            las armas. Después, incluso en el mejor de los casos, estaréis en
            manos de Dios.</p>
            <p>Esos son tus pensamientos mientras sales del bosque y tomas una
            decisión de la que penderá tu aventura.</p>
            ''',
            opciones:{"Puedes ir ahora mismo a avisar al Conde Ian.":"avisar-ian-62", #/62/-
                      "Viajas a avisar a tu familia.":"avisar-familia-16", #/16/-
                        },
            prueba:False,
            imagen_arriba:"mousy.png",
            imagen_abajo:False
            },

        "avisar-ian-62":{
            titulo:"En la fortaleza del Conde Ian",
            texto:'''
            <p>Solo te preocupas en correr, primero entre los árboles, más tarde
            en el camino, hasta casi desfallecer y luego descender a una marcha
            larga. Por fin, cuatro horas más tarde, alcanzas la corte del Conde
            Ian: una ciudadela de piedra, superviviente de un fuerte imperial,
            rodeada por un laberinto de cabañas protegidas por un foso y una
            empalizada.</p>
            <p>Al llegar al portón, los guardias te reciben con la cortesía
            habitual; pero los cortas inmediatamente. --Traigo noticias
            urgentes. He de ver al conde. --dices. Tu cuerpo cubierto de sudor
            y polvo y tu dura mirada les convence de la seriedad de tu misión,
            sin que sea necesaria ni una palabra más. Pronto estás en el Gran
            Salón de la Torre Alta, donde el Conde recibe a sus vasallos
            cubierto de de cuero y hierro.</p>
            <p>&mdash;Han quemado San Brenan.</p>
            <p>&mdash;¿Qué son esta vez? ¿Bandidos?</p>
            <p>&mdash;No, Señor, Vikingos, un ejército.</p>
            <p>&mdash;¿Cómo qué un ejército? ¿Qué quieres decir?</p>
            <p>&mdash;Señor, sus barcos cubrían las playas hasta donde pude ver.</p>
            <p>&mdash;¿Cómo eran sus guerreros? Pudiste verlos.</p>
            <p>&mdash;Sí, vienen con sus nobles, sus hombres de armas, las levas
            de granjeros, todo, también sus mujeres y hasta sus niños.</p>
            <p>&mdash;Lo que dices, significa que...</p>
            <p>Las manos del conde van desde su barbilla al pomo de su espada.
            Sus pensamientos le atraviesan el cuerpo hasta hacer derribarle en
            su asiento, debatiéndose en una decisión fatal:</p>
            ''',
            opciones:{"Descubre la decisión del Conde":"p-avisar-ian-62"},#-
            prueba:False,
            imagen_arriba:"mousy.png",
            imagen_abajo:False
            },

        "p-avisar-ian-62":{
            prueba:True,
            r:3,
            s:["conde-lucha","conde-huye"] # hechos los dos
            },


        "avisar-familia":{ #16
            titulo:"El Camino del Norte",
            texto:'''
            <p>Decides que tu primera obligación es con tu familia y tu clan. Te
            espera un viaje largo, de más de una semana a pie, pero precisamente
            por eso debes apresurarte. Entre antes esté avisada tu familia mayores
            serán sus probabilidades de sobrevivir.</p>
            <p>Sales al camino, trotando al principio, andando después, desgastando
            todas las horas del día hasta que cae la noche. Buscas refugio escondido
            entre los matorrales, tal como te han enseñado, lejos de las miradas
            indiscretas, pero con un pequeño fuego que mantenga alejados, por su
            olor, a los lobos.</p>
            <p>A la mañana siguiente despiertas todavía inmerso en la soledad de
            esta región remota, casi desierta de seres humanos tras cinco siglos
            de guerras. Aún así sabes que los vikingos, tras su probable victoria,
            vendrán por aquí y los pensamientos de espadas y fuego dan alas a tus
            pies. No paras sino para comer algo de carne seca y queso y ya con el
            sol atravesando la tarde, te llegan los olores y sonidos de una aldea:
            ovejas, cabras, campos de avena, humo de las chimeneas, hombre, mujeres
            y niños. Puedes imaginarte lo que les pasará dentro de muy poco tiempo.
            Lo único que te hace dudar de avisarlos es que tendrías que desviarte
            de tu camino y aún te quedan al menos cinco días de dura marcha.
            Además, seguramente su desaparición no pasará inadvertida a los vikingos.
            </p>
            ''',
            opciones:{"Avisas al pueblo":"avisar-pueblo", #/128/-
                        "Sigues tu camino":"sigues-camino" #/179/-
                        },
            prueba:False,
            imagen_arriba:"kidsplay.png",
            imagen_abajo:False
            },

        "avisar-pueblo":{ #128
            titulo:"El Pueblo de Piedra",
            texto:'''
            <p>Esta aldea es peculiar en que se ha levantado aprovechando las
            ruinas de una antigua población romana. Todas las casa tienen las
            formas familiares de Angsax, pero solo los techos son de madera. El
            resto es de piedras sacadas de algún antiguo templo o fortificación.
            Pero prefieres no detenerte en nada hermoso, dado que todo tiene que
            ser abandonado.</p>
            <p>Tus noticias originan un revuelo inmediato en la comunidad. Todos
            los hombres tienen espadas y escudos y no dudarían en luchar contra
            una partida de vikingos, pero son demasiado pocos para enfrentarse a
            un ejército. Te preguntan insistentemente que dónde está el conde y
            a dónde tienen que ir para unirse a la milicia, y no les gustan tus
            respuestas. Ni sabes dónde está ni crees que pueda detenerlos.</p>
            <p>&mdash; ¡Que huyan las mujeres y los niños! Nosotros iremos con
            el conde. Nadie de Angsax debe morir sin haber intentado vivir
            primero.</p>
            <p>Y tú solo puedes mirar y responderles:</p>
            ''',
            opciones:{"— Haced lo que queráis, yo ya he cumplido avisando.":"cumpli-avisando", #/169/-
                        "— No, debemos huir al norte, todos juntos.":"p-al-norte-42", #/42/-
                        "— Está bien, trataremos de encontrar al conde y unirnos a su ejército.":"buscamos-conde" #/105/-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "sigues-camino":{#179
            titulo:"Conde Dever",
            texto:'''
            <p>No te hace muy feliz tomar este tipo de decisiones; pero sabes
            que cada momento cuenta. Solo piensas en salvar a tu familia y a
            ti mismo. Eso es en lo que crees, aunque la conciencia te remuerde
            un poco, la verdad es que no lo puedes todo. En fin, tampoco tienes
            tiempo para lamentarte ni para compadecerte de ti mismo. Así que
            sigues en el camino con la mayor de las energías.</p>
            <p>Los días se van sucediendo sin que nada turbe tu tranquilidad.
            Sabes que solo es una ilusión pasajera, pero es una ilusión con la
            que engañas el cansancio y un hambre mal engañado con una comida
            cada vez más seca y pobre. Lluvia, sol y viento son tus compañeros
            durante el día, y el frío se pega cruelmente a tus huesos durante
            la noche.</p>
            <p>La alegría no llega hasta que divisas la Piedra de las Urracas,
            un monolito tallado en memoria de las tres reinas que en tiempos
            remotos ganaron aquí el respeto del Emperador de Roma y quizás algo
            más. Según tu abuela, tú mismo desciendes de una de estas tres, lo
            que supondría que tu estirpe tiene sangre antigua y, si has de creer
            a las leyendas, también del mismo emperador. Pero más allá de todo
            eso, lo único cierto es que estás en casa.</p>
            <p>Desde la Piedra de las Urracas, un corto camino te lleva ante la
            fortaleza de tu familia. De niño, antes de que vieras mundo, te
            impresionaba. Se trata de una colina artificial, rodeada por un foso
            y rodeada de estacas y dos anillos de empalizadas y atalayas. En el
            centro de todo, un pequeño fuerte romano que una vez alojó a una
            cohorte, y que ahora ha sido transformado en una torre de piedra.
            Ahí naciste, junto al fuego de la chimenea.</p>
            <p>Tu llegada provoca una revolución de alegría. A pesar de tu
            estado todos están impacientes por las noticias que traigas,
            esperando escuchar historias de tus viajes, los chismes de los
            condes y las nuevas maravillas que hayan traído los mercaderes del
            sur desde oriente.</p>
            <p>Cuando finalmente tienes el valor de compartir la terrible
            invasión, todo el mundo se queda frío. Miran hacia tu padre
            esperando que tome una decisión, pero éste, ante tus ojos cae
            privado del conocimiento, como alcanzado por un rayo invisible, para
            convulsionar en el suelo ante la desdicha de todos y luego
            morir.</p>
            <p>Los pesares y las lamentaciones duran toda la noche, y solo son
            interrumpidos por la fórmula tradicional: &mdash;Larga vida al conde
            Dever.</p>
            <p>Hablan de ti. Ahora tienes una responsabilidad. Lo primero es
            atender al funeral y entierro de tu padre; a quien llevaréis al
            monasterio para que lo cuiden los monjes. Pero incluso ahora tu
            cabeza no puede dejar de pensar en el monstruo que se acerca.</p>
            ''',
            opciones:{"Preparas tu fortaleza para un asedio, reclutando todas las milicias que puedas":"preparar-fortaleza-conde-dever", #/27/-
                      "Convocas a tus mejores hombres para llevar una guerra de guerrillas en el camino; mientras la milicia se ocupa del fuerte.":"guerrilla-camino-norte", #/69/-
                      },#hechos los dos
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "preparar-fortaleza-conde-dever":{#27
            titulo:"Reclutas",
            texto:'''
            <p>Pasáis una semana de frenética actividad mandando mensajeros a
            los cuatro puntos cardinales para convocar a cualquiera que pueda
            empuñar un arma. Jóvenes, viejos, hombres, mujeres, extranjeros, os
            da igual siempre que sepan que extremo de la lanza pincha. El
            resultado es una hueste impresionante, en tamaño similar al del
            ejército vikingo que se os acerca, pero mucho peor entrenado. Peor
            aún, no tenéis suministros si quiera para alimentarlos más allá de
            un mes, y en esos pensamientos estás cuando uno de los exploradores
            te anuncia que la horda enemiga se acerca.</p>
            <p>Por lo que te cuenta, solo os ha alcanzado la mitad de sus
            números; por lo que o se han separado o han perdido alguna batalla.
            En cualquier caso interesa saber lo que vas a ordenar tú.</p>
            ''',
            opciones:{"Defender la fortaleza.":"defender-fortaleza-101", #/101/-
                      "Presentar batalla en los bosques.":"batalla-bosques-103", #/103/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "defender-fortaleza-101":{
            titulo:"Defender la Fortaleza",
            texto:'''
            <p>Sabes perfectamente que tus tropas, por numerosas que sean, no
            están preparadas para enfrentarse a un ejército de la gloria y
            envergadura del ejército vikingo. Tampoco puedes confiar
            demasiado en tus habilidades de general; después de todo eres
            completamente novato en liderar una batalla de esta envergadura.
            Quizás por esto optas por encerrarte en la fortaleza.</p>
            <p>Todo va bien los primeros cuatro días. Los vikingos se estrellan
            contra las murallas del fuerte familiar y los muros dan la
            suficiente confianza a tus soldados como para rechazar al enemigo.
            Sin embargo las cosas se ponen más difíciles al amanecer del quinto
            día. Tal como se te advirtió las provisiones empiezan a ser escasas.
            No durarán más de un día, dos como mucho y después tendrás que
            enfrentarte a cientos de hombres, mujeres y niños hambrientos.</p>
            <p>Sabes que rodeado como estás, y teniendo que pasar tus tropas por
            un portón, no puedes maniobrar fácilmente. Un ataque ahora será
            incluso más difícil que a campo abierto y tu única esperanza
            puede que sea...</p>
            ''',
            opciones:{"Empiezas a racionar la comida":"racionar-comida-107", #/107/-
                      "Atacas inmediatamente":"atacar-inmediato-109", #/109/-
                      "Esperas a la noche para intentar una salida":"salida-nocturna-113", #/113/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "salida-nocturna-113":{
            titulo:"Salida Nocturna",
            texto:'''
            <p>No dejas pasar ociosamente las horas cuando ordenas dormir a la
            mayoría de tu gente. Disfrazas a adolescentes y ancianos para que
            con un puñado de hombres guarden las murallas.</p>
            <p>Despertáis silencionsamente, al abrigo de la noche. Mediante
            susurros y gestos se transmiten tus órdenes y pronto toda la hueste
            está formada junto a la puerta magna. Solo vuestras respiraciones y
            el rumor de las puertas al abrirse rompe la calma de la noche.</p>
            <p>Gritos de alarma; los retenes vikingos han detectado vuestra
            salida y los paganos, como avispas, corren a formar en sus cuadros.
            Corréis, no les dejarás tiempo para ganar cohesión.</p>
            ''',
            opciones:{"aquí comienza vuestra única y última oportunidad":"p-salida-nocturna-113"},#-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-salida-nocturna-113":{
            prueba:True,
            r:5,
            s:["ruptura-117","derrota-119"] # 119 - 117 -
            },

        "racionar-comida-107":{
            titulo:"Hambruna",
            texto:'''
            <p>Racionando la comida consigues estirarla para que dure dos
            semanas más, aunque lo comido sea tan minúsculo que no sirve para
            acallar el dolor de los estómagos. Los vikingos, por su parte siguen
            fuertes afuera y tienes que resignarte a la idea de la
            rendición. Tu futuro está entre los esclavos.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "atacar-inmediato-109":{
            titulo:"Ataque Desesperado",
            texto:'''
            <p>Consciente de lo desesperado de vuestra situación, reúnes a los
            <em>husecarls</em>, las tropas de élite de tu padre ante la puerta
            magna. Junto a ti encabezarán la carga final en la que precederán a
            todo la hueste.</p>
            <p>Vuestros cuernos rompen el silencio, las puertas se abren y una
            avalancha de furia se estrella contra la línea vikinga. Solo tenéis
            una mínima oportunidad.</p>
            ''',
            opciones:{"Descubre el resultado de la batalla":"p-atacar-inmediato-109"},#-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-atacar-inmediato-109":{
            prueba:True,
            r:3,
            s:["ruptura-117","derrota-119"] # 117- 119-
            },

        "ruptura-117":{
            titulo:"Ruptura",
            texto:'''
            <p>Tras un furioso combate tus guerreros se abren paso entre los
            enemigos rompiendo sus filas, obligando a los vikingos a retirarse
            para no verse atacados por la espalda. Te das cuenta de que has
            llegado a un momento crítico; podrías huir y asegurarte la
            salvación, si quiera temporal de tu ejército, tu gente y tu familia,
            o podrías atreverte a intentar dar un golpe decisivo con tu milicia
            antes que los guerreros profesionales de los vikingos se recuperen,
            aprovechando la brecha para atacar a su espalda.</p>
            <p>Tuya es la decisión, Conde Dever.</p>
            ''',
            opciones:{"Ordenas seguir avanzando hacia el monte":"avanzar-al-monte-120", #/120/-
                      "¡A la carga!":"a-la-carga-126", #/126/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "derrota-119":{
            titulo:"Derrota",
            texto:'''
            <p>Cuando la lucha termina hace tiempo que yaces muerto. Tu
            sacrificio y el de los <em>husecarls</em> ha servido para permitir
            escapar a la mitad de vuestra hueste desde una esclavitud cierta a
            la desesperada vida de un animal acosado en el bosque. En cualquier
            caso ya no te queda nada de lo que preocuparte.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "avanzar-al-monte-120":{
            titulo:"Al monte",
            texto:'''
            <p>Decides que la vida de tu gente es demasiado importante como para
            arriesgarlo todo jugando a ser Alejandro Magno. Aprovechas la brecha
            para dejar que todo el mundo huya mientras tú y tus husecarles la
            mantienen abierta, conteniendo a la feroz bestia que más que un
            fuerte o las tierras ansía esclavos.</p>
            <p>Al final conseguís vuestra pequeña victoria y escapáis todos a
            las tierras salvajes. Desde allí, durante los años siguientes,
            observáis a los vikingos imponer su ley en todo Angsax. Los años y
            la necesidad de establecer su reino vuelve práctico al rey de los
            vikingos, con quienes firmáis la paz. Tú te conviertes en su
            vasallo, otro conde más al servicio del señor y a cambio mantenéis
            vuestra libertad y vuestras tierras. No es ciertamente la mejor de
            las suertes, pero mucho mejor que la mayoría de tus compatriotas han
            podido conseguir.</p>
            <p>Tu gente recordará tus esfuerzos durante generaciones.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:'dance.png'
            },

        "batalla-bosques-103":{
            titulo:"Batalla en el Bosque",
            texto:'''
            <p>Con suministros insuficientes lo último que quieres es encerrarte
            en una fortaleza a esperar al hambre. Por eso, aún sabiendo que tus
            soldados tienen pocas posibilidades contra los vikingos, decides
            encontrarles en los bosques. Tu ejército forma a la manera
            tradicional, con los jóvenes y los adolescentes delante, armados con
            arcos, jabalinas y hondas y el grupo principal detrás, un muro de
            escudos y lanzas. En el centro de todo estás tú y tus husecarles,
            los hombres escogidos de tu padre, los únicos protegidos por
            armaduras y con experiencia en batalla.</p>
            <p>No mucho después de que lográis formar llegan los vikingos, que
            despliegan sus tropas de forma similar. Ni ellos ni vosotros pueden
            ver hasta donde llegan vuestros respectivos ejércitos, porque el
            bosque oculta gran parte de vuestras líneas.</p>
            <p>¿Cuáles son tus órdenes?</p>
            ''',
            opciones:{"Ordenas un ataque inmediato":"p-ataque-132", #/132/-
                      "Esperáis aquí a su ataque":"esperas-ataque-137", #/137/-
                      "Te retiras en orden de combate, sin huir pero sin dejar que se acerquen":"retirada-combate-146", #/146/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "retirada-combate-146":{
            titulo:"Resentimiento",
            texto:'''
            <p>Los guerreros desconfían de ti. No entienden qué pretendes retirándote
            sin combatir y su explicación es simple: eres un cobarde; pero obedecen.
            La lenta retirada tampoco complace al enemigo que tiene la misma
            opinión de ti. Esta no es forma de hacer la guerra. Con todo y de momento
            no se atreven a acercarse, no sea que les conduzcas a alguna trampa, pero
            al mismo tiempo tratan de abrirse camino hacia tu castillo.</p>
            <p>Las horas van dando paso al primer día y durante las horas de la noche
            calculas que, de seguir con esta táctica podrás ganar dos o tres días para
            los defensores de la fortaleza, y durante todo este tiempo no puedes ver
            sino caras de desilusión en tus hombres. Todos quieren combatir y tú
            eres lo único que se lo impide.</p>
            ''',
            opciones:{"Mantienes la táctica":"mantienes-tactica-18-9", #-
                      "Atacas a la primera oportunidad":"p-atacas-oportunidad-18-9", #-
                      "Intentas negociar con los vikingos":"intentas-negociar-18-9", #-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "mantienes-tactica-18-9":{
            titulo:"Una decisión incómoda",
            texto:'''
            <p>Mantenerla táctica ha sido, desde luego la decisión más incómoda.
            Nada hay de gloria para los guerreros que cada vez se sienten más
            defraudados con tus decisiones. Con todo has tenido la recompensa de
            retener a los vikingos una semana entera, siguiéndote de acá para allá,
            siempre con el temor de que les tendieras una emboscada. Los enemigos
            te han puesto un mote: <em>el mirlo</em> y escupen al pronunciarlo,
            llenándote de maldiciones.</p>
            <p>Ademsás, tu éxito te ha traído un problema más serio:, tu ejército improvisado
            apenas salió con raciones y poco a poco van escaseando. Quizás sea
            el momento de volver al fuerte</p>.
            ''',
            opciones:{"Vuelves al fuerte":"al-fuerte-26-9-15",
                      "Ordenas una incursión nocturna para robar comida a los vikingos":"robar-comida-26-9-15",},
                      # volver fuerte  | incursión nocturna
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "p-atacas-oportunidad-18-9":{
            prueba:True,
            r:5,
            s:["victoria-atacas-oportunidad-22-9-15", "derrota-batalla-generica"],
            },


        "intentas-negociar-18-9":{
            titulo:"Largas negociaciones",
            texto:'''
            <p>Mandas a tu heraldo quien maneja las negociaciones mientras echas un
            ojo al ejército enemigo que continua su despliegue pero sin avanzar.
            Tras dos horas vuelves con las condiciones del enemigo: quieren que tú
            negocies directamente con su jefe, en una cabaña de pastores a media
            hora de camino, tú y él solos.</p>
            ''',
            opciones:{"Aceptas sus condiciones":"aceptas-condiciones-21-9-15", #-
                      "Mantienes al táctica dilatoria":"mantienes-tactica-18-9", #
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "aceptas-condiciones-21-9-15":{
            titulo:"",
            texto:'''
            <p>Tras aceptar sus condiciones, te diriges a la cabaña a caballo sin
            que nadie te moleste durante el camino. Cuando llegas a ella te encuentras
            al vikingo ya esperándote a la entrada. Os saludáis y acordáis llevar
            las conversaciones en el exterior.
            </p>
            <p>Las horas se alargan hasta llegar a la noche. El vikingo apenas habla
            tu idioma y tampoco parece hablar el suyo demasiado bien. Todo lo tiene
            que pensar tres y cuatro veces y cada palabra que da se pelea con la
            anterior. Pero no te ha preocupado demasiado, después de todo, cada hora
            negociado es una hora ganada para la fortaleza.</p>
            <p>Sin embargo, justo a la caída de la noche te llega el rumor de una
            batalla. Alarmado, cortas las negociaciones inmediatamente pero entonces
            siete arqueros salen de la cabaña.</p>
            <p>&mdash;Idiota, no soy ningún rey, mi rey está matando a tu ejército.
            Yo soy asesino de reyes y ahora te mataré a ti.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "esperas-ataque-137":{
            titulo:"",
            texto:'''
            <p>Decides no arriesgarte a luchar en el interior del bosque y ordenas
            esperar afuera, aprovechando el tiempo para organizar tus líneas. El
            enemigo duda en salir y cuando al fin lo hace, está visiblemente falto
            de entusiasmo. Avanzan como cobardes, escondiendo sus espadas y
            mostrando sus escudos, concentrados como conejos, obedeciendo a
            regañadientes las órdenes de sus jefes.</p>
            <p>No les faltan razones, aunque veteranos son inferiores en número,
            quizás la mitad de tus tropas.</p>
            ''',
            opciones:{"No dejas pasar esta oportunidad y atacas":"atacar-17-sep", #atacar
                      "Decides mantener la distancia, no huyes pero tampoco permites que se acerquen":"retirada-combante-146"},#146
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-ataque-132":{
            prueba:True,
            r:3,
            s:["batalla-bosques-16-sep","derrota-bosques-16-sep"], #victoria- derrota-
            },

        "batalla-bosques-16-sept":{
            titulo:"Últimas esperanzas",
            texto:'''
            <p>Tu grito de ataque se junta a un millar de vítores que impulsan al
            ejército de Angsax hacia la hueste pagana. Corréis, la muerte y el
            dolor acallada por los cuernos de guerra, hasta que arremetéis al
            enemigo. Desde ese momento solo se escucha el silbido del acero y el
            entrechocar de los escudos. Lucháis tan bien como los vikingos y
            conseguís hacerles retroceder hacia el interior del bosque.</p>
            ''',
            opciones:{"Ordenas seguir adelante":"adelante-16-sep",
                      "Detienes a tu ejército y reformas sus líneas":"parar-16-sep"}, #adelante-, parar-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "parar-16-sep":{
            titulo:"La Horda",
            texto:'''
            <p>Te cuesta controlar a tus hombres, y puedes ver algo más que
            desconfianza en sus caras. Tenían a mano la victoria y tú y tu
            prudencia se la habéis hurtado. Solo tu linaje y los juramentos les
            impiden rebelarse.</p>
            <p>Pero momentos más tarde, una horda vikinga, el doble de los que
            habiaís vencido antes, si no más, surge de los bosques en formación
            de cabeza de jabalí, listos para cargar y destrozar a tu ejército.</p>
            ''',
            opciones:{"Ordenas un ataque, lo que nunca esperarían":"ataque-inesperado-17-sep", #-
                      "Ordenas aguantar":"aguantar-17-sep", #-
                      "Ordenas huir":"huir-ejercito-carga-17-sep"}, #-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "huir-ejercito-carga-17-sep":{
            titulo:"Cacería",
            texto:'''
            <p>Sí, cacería, la batalla se ha transformado en una sangrienta
            cacería en la que vosotros sois los ciervo. Aún así la mayoría
            sobreviviréis para ver otro día, pero quedaréis dispersos y rotos
            entre los bosques, cada uno ocupado por salvar su propia vida. Peor
            aún, tus guerreros ya no confían en ti y buscarán un mejor señor
            entre los vikingos. Tu futuro está con los forajidos, los muertos o
            los esclavos.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "aguantar-17-sep":{
            titulo:"Aguantaremos",
            texto:'''
            <p>¡Muro de escudos! Aguantaremos.</p>
            <p>La orden tradicional de tu pueblo ha unido a tus guerreros y
            ahora están listos para lo que venga. Y lo que viene es una máquina
            traicionera y astuta que también sabe convertirse en un gigante cuando
            le conviene, como ahora.</p>
            <p>Y cargan contra vosotros los vikingos, bajo el sonido de los cuernos,
            y los aullidos de quienes quieren imponeros el miedo. Ganar o morir,
            ahora es cosa de segundos.</p>
            ''',
            opciones:{"Trata de resistir como sea":"p-resistir-19-sep"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-resistir-19-sep":{
            prueba:True,
            r:6,
            s:["victoria-resistir-20-sep","derrota-resistir-20-sep"], # victoria -, derrota -
            },

        "victoria-resistir-20-sep":{
            titulo:"Seguimos aquí",
            texto:'''
            <p>Tras el primer choque entre los ejércitos el muro de escudos
            resiste bien. Los vikingos no consiguen penetrar tu formación por
            mucho que se esfuerzan y aunque tus flancos son débiles el general
            enemigo no es capaz de aprovecharse de la situación. En vez de eso,
            enrabietado por su fracaso, lanza más y más tropas contra tu centro,
            pero el centro resiste.</p>
            <p>A la caída de la tarde, los vikingos, ya extenuados, se retiran
            dejando el campo sembrado de cadáveres. Tus tropas, cubiertas de sangre
            y sudor, no tienen fuerzas ni para celebrar la victoria.</p>
            <p>¿Cuáles serán tus órdenes?</p>
            ''',
            opciones:{"Un supremo esfuerzo, la carga final":"carga-final-20-sep", #
                      "Os mantenéis aquí, clavados a la tierra de la victoria":"tierra-victoria-20-sep"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "derrota-resistir-20-sep":{
            titulo:"Derrota",
            texto:'''
            <p>El ejército anglosajón puso toda su fuerza en contener a la horda
            vikinga y el muro de escudos resistió, pero poco a poco los vikingos,
            superiores en números, lo envolvieron por sus flancos.</p>
            <p>Trataste de contraatacar pero tus fuerzas fueron rechazadas dos
            veces seguidas y, antes de que pudieras organizar un último ataque
            el ejército principal se rompió en dos, y luego en tres para ser
            masacrados hasta el amargo final.</p>,
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "ataque-ineperado-17-sep":{
            titulo:"Ataque Inesperado",
            texto:'''
            <p>Das la orden y la alegría bulle en vuestro ejército que corre al
            encuentro del acero enemigo. Las espadas y las lanzas cortan a los
            guerreros de ambos bandos con la misma velocidad y durante unos
            gloriosos cinco minutos se hace épica sobre el campo de la sangre.
            Después se imponen los números en la confusa meleé y con rapidez cada
            vez mayor son tus hombres los que más caen a la muerte. Y justo cuando
            empiezas a preocuparte una traicionera lanza que llegó como del cielo
            atraviesa tus pulmones.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "adelante-16-sep":{
            titulo:"",
            texto:'''
            <p>Das la orden y tu ejército triunfante se interna en el bosque,
            arrollando a los regazados entre los vikingos. Los árboles van
            revolviendo tu ejércitos según pasáis entre ellos. Entonces os
            envuelven los rugidos de los vikingos, que cargan desde tres
            direcciones, llenando el bosque de confusión y muerte. Deben
            triplicaros en número y os tienen completamente rodeados. Ha llegado
            el...</p>
            ''',
            prueba:False,
            opciones:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "derrota-bosques-16-sep":{
            titulo:"Derrota",
            texto:'''
            <p>Tu ejército golpea el centro de la línea enemiga que resiste su
            presión desde los primeros momentos. Ambos ejércitos bregan sin que
            ninguno sea capaz de hacer retroceder al otro, hasta que a la
            derecha de tu ejército surge una gigantesca columna de vikingos.
            Alarmado, reúnes a todos los que puedes encontrar en las últimas
            filas, y rugiendo órdenes consigues formar un muro de escudos que
            pare la nueva amenaza. Milagrosamente resistís, pagando con sangre
            cada minuto que dáis a vuestra fuerza principal para que consiga la
            victoria.</p>
            <p>Pero no habrá de ser, porque otra ola vikinga surge por el flanco
            izquierdo. Solo entonces te das cuenta de la fuerza de un enemigo
            experto que no solo te triplica en número, sino que también te ha
            superado en astucia. Tu última esperanza es morir con la espada en
            la mano.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "a-la-carga-126":{
            titulo:"A la Carga",
            texto:'''
            <p>Aprovechas el momento para dar la orden; tu hueste victoriosa se
            divide en dos grupos, a derecha e izquierda, y cae sobre la
            retaguardia enemiga. Sorprendidos ante tu inesperada victoria al
            salir del castillo, los vikingos reaccionan cada uno por su cuenta,
            permitiéndote ganar segundos preciosos.</p>
            <p>Corres y gritas con tus hombres, en el puesto de honor, al frente
            de todo, junto al estandarte. Tu espada surge entre un bosque de
            brillante acero y cae envuelta y sangre. Adelante, adelante, no
            puedes dejar al enemigo recomponerse. Ahora todo es una pantomima;
            durante tres minutos tus campesinos van a creerse soldados y los
            vikingos no van a creer lo que están viendo. Si algo se retrasa,
            el enemigo se recomprondará y será el fin de está última y cara
            esperanza.</p>
            ''',
            opciones:{"Nunca lo permitirás.":"p-a-la-carga-126"},#-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-a-la-carga-126" :{
            prueba:True,
            r:8,
            s:["victoria-127","victoria-muerte-129"] # 127- 129-
            },

        "victoria-127":{
            titulo:"Victoria",
            texto:'''
            <p>Tras una furiosa batalla tus fuerzas ponen en fuga a la mitad de
            los vikingos, aplastando contra los muros a los supervivientes.
            Habéis triunfado y la fama de vuestra victoria se extiende por toda
            la tierra, alcanzando a todos aquellos que buscan una esperanza
            contra la opresión.</p>
            <p>De todas partes llegan refugiados, aumentando vuestros números.
            Poco a poco váis constituyendo lo que con el tiempo acabará por
            llamarse el Reino del Norte, del que tú serás coronado como primer
            Rey.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "victoria-muerte-129":{
            titulo:"Victoria y Muerte",
            texto:'''
            <p>Vuestra victoria, sí, victoria es absoluta e incontestable.
            Esta batalla será recordada el resto de la historia del pueblo de
            Angsax. Tú no vivirás para verlo, pero el eco de vuestra victoria
            resonará en todo el país atrayendo a todos los que anhelaban una
            esperanza.</p>
            <p>Con el tiempo la situación se estabilizará y nacerá un reino de
            Angsax independiente, y tú, el Conde Dever, formarás parte de sus
            leyendas, con el jefe guerrero que en las horas tan amargas pagó con
            su dolor y su vida la libertad de un pueblo.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "cumpli-avisando":{ # 169
            titulo:"Camino Solitario",
            texto:'''
            <p>Tenías las ideas claras desde el principio; no conoces a esta
            gente de nada y solo querías avisarles para que tuvieran una
            oportunidad. No es que fueras su hermano ni nada de eso; es en tu
            verdadera familia en quienes piensas. Y ya has perdido demasiado
            tiempo. Así que, a pesar de sus protestas, los abandonas y te
            apresuras al camino, antes de que lo dejen colapsado con sus
            carretas.</p>
            <p>El camino todavía está solitario, pero ya no tranquilo. Ya se
            escucha la bulla de la gente y las bestias mientras intentan
            organizarse para la huída, que ha hecho desaparecer el murmullo
            habitual del monte.</p>
            <p>Van pasando las horas y con el tiempo dejas la bulla atrás, a
            costa de cansancio y esfuerzo. Pero entonces, proviniendo del sur,
            escuchas otro sonido más familiar: el de los cascos de caballos.
            Quizás sean de los vuestros; después de todo los vikingos llevan
            pocos caballos en sus correrías, salvo para un puñado de
            exploradores y nobles, debido al espacio que ocupan en los barcos.
            Rápidamente sopesas tus opciones.</p>
            ''',
            opciones:{"Apresuras la marcha.":"huida-desesperada-121", #/121/-
                      "Te escondes en el margen del camino.":"escondes-camino", #/141/-
                      "Te internas en el bosque.":"internas-bosque", #/99/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "internas-bosque": {#99
            titulo:"Lo profundo",
            texto:'''
            <p>Hace ya horas que te escondiste de los vikingos en esta
            oscuridad húmeda. No podrías saber dónde estás sino decir que estás
            rodeado por árboles que escalan hasta el cielo, que la tierra está
            cubierta de una hierba corta y húmeda, que cede ante tus pies y que
            brilla en los puntos donde el sol consigue abrirse camino entre las
            ramas. Hay un rumor de aguas entre el píar de los pajarillos y el
            susurro de la brisa que acaricia las copas de los árboles, y más allá
            de todo esto, una sensación inefable, a la vez misteriosa y fascinante
            que te inquieta y te atrae.</p>
            ''',
            opciones:{"Te quedas aquí para pasar esta noche":"te-quedas-14-sep",
                      "Te diriges a dónde suena el agua":"al-agua-14-sep"}, #te-quedas-  al-agua-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "al-agua-14-sep":{
            titulo:"El rastro de luz",
            texto:'''
            <p>Las huellas que el rumor del agua deja en el aire te conduce a
            una parte del bosque donde la luz nunca queda extinta. El tiempo ha
            pasado lo suficiente como para que caiga la noche y ni la luna ni
            las estrellas deberían ser capaces de atravesar este techo de ramas
            y hojas. Sin embargo queda un rastro de luz que fluye sobre el suelo
            como si fuera agua.</p>
            ''',
            opciones:{"Te acercas para tocarla":"agua-luz-tocar-19-9-15", #-
                      "Te alejas de este lugar":"alejas-agua-luz-19-9-15"}, #-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "agua-luz-tocar-19-9-15":{
            prueba:True,
            r:8,
            s:["tacto-infinito-21-9-15","iluminacion-21-9-15"], # tacto - ilumniación-
            },

        "iluminacion-21-9-15":{
            titulo:"Iluminación",
            texto:'''
            <p>Lo primer que notas al acariciar el agua de luz con tus dedos es un fluir
            natural que en nada se distingue del agua corriente. Sin embargo, al mismo
            tiempo tienes una sensación de bienestar que no se parece a nada que hayas
            sentido antes. Y entonces una fuerza te arrebata y cuando te das cuenta
            has bebido del agua de luz.</p>
            <p>Tu alma experimente un milagro, una conversión total y santidad. De pronto
            ya no te interesa nada sino servir a Dios. Y tomando una dirección al azar
            te pones en camino para unirte al primer monasterio que encuentres.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "tacto-infinito-21-9-15":{
            titulo:"El tacto infinito",
            texto:'''
            <p>El agua de luz entre tus dedos tiene el mismo tacto del agua y sin
            embargo llama a tu corazón a un mundo infinito, mucho más allá de éste.
            Siendo quien eres y viniendo de donde vienes, no puedes evitar hincar
            la rodilla y rezar.</p>
            <p>Al terminar un pensamiento te ha venido a la mente, no sabes si de
            tu propia imaginación o de Dios, pero en cualquier caso dice lo siguiente
            <em>"no te fies del mal, mientras mal sea"</em>, que no sabes cómo te
            podrá servir de ayuda.</p>
            ''',
            opciones:{"Buscas el norte, la dirección aproximada de tu familia":"norte-familia-20-sep", #
                      "Exploras los alrededores":"exploras-bosque-20-sep"},#
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "alejas-agua-luz-19-9-15":{
            titulo:"",
            texto:'''
            Silenciosamente te alejas de la luz hasta quedarte sobrecogida por la
            abisal oscuridad del bosque nocturno. Pronto debes renunciar a seguir
            avanzando y tu propio cansancio y la imposibilidad de avanzar cinco
            metros seguidos sin tropezar hace que caes dormido.</p>
            <p>Cuando despiertas, antes incluso de que estés despejado, te
            reconoces perdido en este bosque inmenso.</p>
            ''',
            opciones:{"Buscas el norte, la dirección aproximada de tu familia":"norte-familia-20-sep", #
                      "Exploras los alrededores para buscar una pista":"exploras-bosque-20-sep"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "te-quedas-14-sep":{
            titulo:"El boque sagrado",
            texto:'''
            <p>La noche pasa tranquila en el bosque sagrado; la humedad apenas
            te molesta mientras duermes encajado entre dos árboles hasta que
            despiertas, arropado por la penumbra de la madrugada. El rumor del
            agua sigue sonando como cuando llegaste aquí y nada indicaría que ha
            pasado el tiempo sino fuera por la sombra grisácea que vuela entre
            las ramas.</p>
            ''',
            opciones:{"Sigues esa sombra":"sigues-sombra-15-sep", #-
                      "No le prestas importancia":"paso-de-sombra-15-sep"}, # sigues sombra - pasas de sombra-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "paso-de-sombra-15-sep":{
            titulo:"Vuelta a casa",
            texto:'''
            <p>Olvidada la sombra, continuas con tu gran viaje de vuelta a casa.
            Solo que ahora no sabes dónde estás y te sientes como un viejo perdido
            e inútil.A cada paso que profundizas en el bosque sus sonidos familiares
            desaparecen. Te han visto, te han oído, sobre todo te han olido y
            callan esperando que te reveles como un cazador. La situación te
            alegra, porque significa que los próximos que vulneren la santidad
            de esta selva recibirán el mismo silencio delatador.</p>
            <p>Comienza así una aventura de supervivencia campo a través,
            caminando, buscando guía en el sol y en las estrellas, cazando
            cuando es necesaria, durmiendo cuando es posible, en alerta siempre.</p>
            <p>Un mes más tarde llegas ante tus tierras y lo que allí te recibe
            es una estampa de desolación. La tristeza te hace caer de rodillas
            atravesado de dolores. Porque la empalizada que protegía la
            fortaleza de tu padre está quebrada en tres partes y sobre la altiva
            torre de piedra vuela el cuervo de los vikingos, su bandera de
            sangre y noche.</p>
            ''',
            opciones:{"Buscas un lugar seguro para esconderte":"seguro-esconderte-26-9-15",
                      "Buscas a tu familia, si es que alguien ha sobrevivido.":"buscas-familia-superviviente-26-9-15"},
                      # lugar seguro | buscar familia
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "seguro-esconderte-26-9-15":{
            titulo:"Las tres brujas",
            texto:'''
            <p>Desde niño sabes agazaparte entre el matorral que brota por todo
            lo que no son campos de avena. Tu tierra te conoce y te guarda hasta
            que desapareces de la vista de todos. Ahora te sería muy fácil
            escapar y no volver a ser encontrado nunca, pero eso no te basta;
            necesitas saber qué ha pasado y sabes muy bien dónde dirigirte: la
            cabaña de las tres brujas. Son tres árboles que crecieron tan juntos que sus ramas
            entretejieron un techo y sus troncos forjaron paredes retorcidas,
            compitiendo unos contra otros por el espacio hasta solo dejar
            rendijas de aire entre ellos. Ya en los tiempos de tus abuelos los
            niños se desafiaban a pasar allí la noche de vísperas de los
            espíritus y casi ninguno acepta. Sin embargo, para otras ocasiones
            era muy buen escondite.</p>
            <p>Llegas y enseguidas recuerdas el truco: hay que subir a la bruja
            pálida, el árbol de corteza casi blanca, y desde su copa sorteas las
            ramas hasta descender a su interior. Hoy subir se te hace más fácil
            pero cuando llegas al centro un chillido te derriba al suelo.</p>
            <p>Es Aedelwina tu sobrina de rostro demacrado y cubierto de polvo,
            el pelo revuelto y un zapato perdido, que todavía abraza su muñeca
            de madera labrada cuando caes junto a ella.</p>
            ''',
            opciones:{"Le preguntas qué ha pasado.":"preguntas-Aedelwina-26-9-15",
                      "Escapas inmediatamente con ella.":"escapas-Aedelwina-26-9-15",
                      },
                      #preguntas | escapas
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


        "sigues-sombra-15-sep":{
            titulo:"Decepción",
            texto:'''
            <p>La sombra salta de una rama a otra como burlándose de ti. Cada vez
            que te aproximas vuela y luego se queda quieta como esperándote. El
            juego continúa durante quince minutos que parecen horas hasta que al
            fin te das cuenta de que lo que has seguido durante todo ese tiempo
            no era sino un pájaro.</p>
            ''',
            opciones:{"Olvídate de la sombra":"paso-de-sombra-15-sep"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "escondes-camino":{#141
            titulo:"Escondido en el camino",
            texto:'''
            <p>Rodeas unos &aacute;rboles y te tumbas entre troncos, junto a
            las flores. Extiendes tu capa, cubres tu cabeza y hasta esparces
            tierra por encima. Con ello esperas desaparecer de tus enemigos.</p>
            <p>Poca es tu espera, en seguida escuchas a los cascos de los
            caballos avanzando al trote haci&eacute;ndose cada vez m&aacute;s
            fuertes mientras toda la naturaleza a tu alrededor se calla en un
            suspiro. Falta ya muy poco, Dever, en un segundo estar&aacute;n
            junto a ti, listos para degollar.
            ''',
            opciones:{"Corres al interior del bosque":"al-interior-del-bosque-i",#-
                      "Te mantienes en tu escondite":"sigues-escondido-i",#-
                      },
            prueba:False,
            imagen_arriba: False,
            imagen_abajo: False,
            },

        "sigues-escondido-i":{
            titulo:"",
            texto:'''
            <p>Tienes que tragarte muchos miedos mientras el sonido de los
            caballos atronan la tierra; pero rechazas la tentación de levantarte
            y salir corriendo. Y así, confiado en tu escondite vislumbra su
            llegada entre los árboles. Apenas puedes distinguir que son vikingos
            y su número lo calculas entre cuatro y siete. No te ven, van al
            trote sobre caballos y tu eres poco más que una sombra entre los
            árboles. Siguen adelante y quince minutos después, el bosque
            recupera su discreta música.</p>
            <hr>
            <p>Los días se van sucediendo sin que nada turbe tu tranquilidad.
            Sabes que solo es una ilusión pasajera, pero es una ilusión con la
            que engañas el cansancio y un hambre mal engañado con una comida
            cada vez más seca y pobre. Lluvia, sol y viento son tus compañeros
            durante el día, y el frío se pega cruelmente a tus huesos durante
            la noche.</p>
            <p>La alegría no llega hasta que divisas la Piedra de las Urracas,
            un monolito tallado en memoria de las tres reinas que en tiempos
            remotos ganaron aquí el respeto del Emperador de Roma y quizás algo
            más. Según tu abuela, tú mismo desciendes de una de estas tres, lo
            que supondría que tu estirpe tiene sangre antigua y, si has de creer
            a las leyendas, también del mismo emperador. Pero más allá de todo
            eso, lo único cierto es que estás en casa.</p>
            <p>Desde la Piedra de las Urracas, un corto camino te lleva ante la
            fortaleza de tu familia. De niño, antes de que vieras mundo, te
            impresionaba. Se trata de una colina artificial, rodeada por un foso
            y rodeada de estacas y dos anillos de empalizadas y atalayas. En el
            centro de todo, un pequeño fuerte romano que una vez alojó a una
            cohorte, y que ahora ha sido transformado en una torre de piedra.
            Ahí naciste, junto al fuego de la chimenea.</p>
            <p>Tu llegada provoca una revolución de alegría. A pesar de tu
            estado todos están impacientes por las noticias que traigas,
            esperando escuchar historias de tus viajes, los chismes de los
            condes y las nuevas maravillas que hayan traído los mercaderes
            del sur desde oriente.</p>
            <p>Cuando finalmente tienes el valor de compartir la terrible
            invasión, todo el mundo se queda frío. Miran hacia tu padre
            esperando que tome una decisión, pero éste, ante tus ojos cae
            privado del conocimiento, como alcanzado por un rayo invisible, para
            convulsionar en el suelo ante la desdicha de todos y luego
            morir.</p>
            <p>&mdash;Larga vida al conde Dever.</p>
            <p>Hablan de ti. Ahora tienes una responsabilidad. Lo primero es
            atender al funeral y entierro de tu padre; a quien llevaréis al
            monasterio para que lo cuiden los monjes. Pero incluso ahora tu
            cabeza no puede dejar de pensar en el monstruo que se acerca.</p>
            ''',
            opciones:{"Preparas tu fortaleza para un asedio, reclutando todas las milicias que puedas":"preparar-fortaleza-conde-dever", #/27/-
                      "Convocas a tus mejores hombres para llevar una guerra de guerrillas en el camino; mientras la milicia se ocupa del fuerte.":"guerrilla-camino-norte", #/69/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "guerrilla-camino-norte":{#69
            titulo:"Pequeñas guerras",
            texto:'''
            <p>Reunidos los mejores guerreros junto a ti, salís de la fortaleza
            bajo el estandarte del santo. Los que quedan en el interior la
            preparan para lo que tenga que venir; tendrás que confiar en ellos
            si tu plan se tuerce.</p>
            <p>Este plan es muy sencillo, avanzar todo lo al sur que se pueda en
            la carretera, bloquearla en varios puntos y atacar desde los flancos
            al ejército vikingo para luego retiraos al interior del bosque. Y
            vuelta a empezar. Si sale bien quizás eso convenza a los invasores a
            ir a saquear a otra parte o al menos retrasar su avance para dar
            tiempo a que la fortaleza quede lista para todo.</p>
            <p>
            <p>Mientras preparas la primera emboscada te cruza la cabeza una
            idea arriesgada. Podrías dejar que todo ocurriera como siempre se ha
            hecho, pero unos cuantos hombres permanecerían escondidos en el
            bosque, mientras los vikingos pasan junto a ellos persiguiendo a la
            fuerza principal. Entonces, una vez pasara un buen grupo, estos
            hombres escondidos comenzarían un incendio dividiendo a los vikingos
            en un muro de fuego.</p>
            ''',
            opciones:{"Decides que es una idea desesperada":"idea-desesperada-iii", #-
                      "Decides de el riesgo merece la pena":"riesgo-ok-iii", #-
                      },
            prueba: False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "riesgo-ok-iii":{
            titulo: "Batalla en el bosque",
            texto:'''
            <p>Decidido a emplear cualquier medio necesario, reúnes a un pequeño
            grupo para hacer de incendiarios. Pero Dudda, el más viejo de ellos,
            se frota la cabeza y dice: &mdash;No es tiempo de fuego, la hoja está
            muy verde aún y no tenemos nafta ni nada con que alimentar el fuego.</p>
            <p>&mdash; El fuego nacerá, &mdash;le responde Aeldrid, uno de los
            jóvenes.</p>
            <p>&mdash; Nacerá, pero le costará nacer, ¿y quién cuidará del fuego
            recién nacido? ¿y qué harán los vikingos cuando lo vean nacer?
            ''',
            opciones:{"Abandonas la idea del fuego":"idea-desesperada-iii"},#-
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "idea-desesperada-iii":{
            titulo: "Batalla en el bosque",
            texto: '''
            <p>Tras rechazar la idea del fuego de tu cabeza, te concentras en
            poner el plan en marcha. Antes que nada destacas exploradores para
            evitar ser cogido por sorpresa precisamente mientras preparas la
            emboscada. Después, unos cuantos árboles caídos, estacas puntiagudas
            y un destacamento de guerreros veteranos harán de tapón; a cada lado
            despliegas los más rápidos y jóvenes escondidos entre los árboles.
            Por último solo queda esperar.</p>
            <p>Y esperáis con el silencio de vuestras armas y el sudor nervioso
            por compañía hasta que tres cantos de lagópodo rojo cruzan el
            silencio del bosque. Es la señal convenida con los exploradores y
            significa que los vikingos están a punto de llegar.</p>
            <p>Y llegan, en una columna larga y delgada, encabezada por el
            estandarte del cuervo y hombres cubiertos con el gris del acero y el
            rojo de las capas que os miran calculando que deberían hacer.</p>
            <p>Y tú, ¿qué deberías hacer?</p>.
            ''',
            opciones:{"Incitas la batalla con un desafío aderezado con una generosa cantidad de insultos":"insultas-emboscada-iv",
                      "Ordenas a algunos de tus guerreros a que, a la vista de los vikingos, abandonen las armas y pretendan huir":"p-huida-falsa-iv"
                      }, #insultas-emboscada-iv - huida-falsa-iv-
            prueba: False,
            imagen_arriba: False,
            imagen_abajo: False
            },

        "p-huida-falsa-iv":{
            prueba:True,
            r:7,
            s:["vikingos-atacan-v", "vikingos-prudentes-v"],
            },

        "insultas-emboscada-iv":{
                titulo:"Sarta de jamelgos",
                texto:'''
                <p>Sarta de jamelgos es lo m&aacute;s bonito que les dices. A partir de ah&iacute; desciendes a las oscuridades
                a las que solo tu antiguo lenguaje puede descender. Ciertamente los vikingos, siendo extranjeros, no pueden
                extraer todo su significado, pero por su reaccia&oacute;n puedes estar seguro que saben que no los quieres mucho.
                A cada instante se incrementa la agitaci&oacute;n en sus filas y probablemente no sea necesario que ninguno de sus jefes
                d&eacute; la orden de atacar.</p>
                ''',
                opciones:{"Prepárate para la furia de los vikingos":"p-insultas-emboscada-iv"},#-
                prueba: False,
                imagen_arriba: False,
                imagen_abajo: False,
                },

	    "p-insultas-emboscada-iv":{
    		prueba: True,
    		r: 5,
    		s: ["vikingos-atacan-v", "vikingos-prudentes-v"], #atacan -  prudentes-
    		},

    	"vikingos-prudentes-v":{
    	    titulo:"prudencia",
    	    texto:'''
    	    <p>El truco no ha funcionado y el ejército vikingo comienza a maniobrar,
    	    pasado de su estirada formación de viaje a disponerse para la batalla.
    	    Estás seguro de que os superan en número, aunque eso ellos no lo saben
    	    todavía porque no pueden contar los guerreros que has escondido en los
    	    bosques.</p>
    	    ''',
    	    opciones:{"Atacas":"p-atacar-ahora-20-9-15",#
    	              "Ordenas a los escondidos que hagan tanto ruido como puedas":"p-bulla-20-9-15",#
    	              "Mandas a los que hacen de tapón a que se dispersen y luchen también como guerrilla":"guerrilla-20-9-15",#
    	              "Te mantienes firme en este lugar":"p-Ferm-und-treu-20-9-15"},#
    	    prueba:False,
    	    imagen_arriba:False,
    	    imagen_abajo:False,
    	    },

    	"p-atacar-ahora-20-9-15":{
    	    prueba:True,
    	    r:6,
    	    s:["victoria-atacar-ahora-20-9-15", "derrota-batalla-generica"], #  victoria  derrota -
    	    },

    	"derrota-batalla-generica":{
    	    titulo:"Derrota",
    	    texto:'''<p>
    	    Tus soldados han combatido con valor pero la postre el ejército enemigo
    	    ha impuesto su voluntad sobre los tuyos. Casi la mitad de los hombres
    	    se han perdido y de los que sobreviven todos están dispersos en el campo
    	    y la mayoría completamente desmoralizados. Tu yaces ahora sobre la tierra
    	    herido y haciendo todo lo que puedes por respirar. Tus dolores se han ido
    	    apagando lentamente, quizás sea señal de que te estás muriendo. Pero aunque
    	    vivas pasarán días para que puedas incluso levantarte y durante semanas
    	    dependerás de la caridad de quien te encuentre.</p>
    	    <p>Mira, alguien se acerca, ¿ángeles o saqueadores de cadáveres?
    	    </p>''',
    	    opciones:False,
    	    prueba:False,
    	    imagen_arriba:False,
    	    imagen_abajo:False,
    	    },

	    "vikingos-atacan-v":{
	        titulo:"Emboscada",
	        texto:'''
	        <p>La batalla, ¿puede llamarse así? comienza cuando los excitados
	        vikingos, cargan hacia el destacamento que bloquea el bosque sin
	        cambiar su formación, ni prepararse para la batalla. Su pasión les
	        está llevando a la muerte. Los primeros caen ante las estacadas,
	        atravesados por las jabalinas de tus hombres. Otros más caen al
	        superar el obstáculo y, aún mejor, los que quedan llegan sin bríos,
	        sin el ímpetu necesario para romper la formación anglosajona. Lo que
	        iba a ser una carga ha degenerado en una lucha lenta en la que la
	        formación vikinga, estirada como una flecha, empieza a agolparse en
	        la cabeza. ¿Ha llegado el momento de atacar?
	        ''',
	        opciones:{"Ordenas atacar a los hombres escondidos a cada lado de la carretera":"flancos-20-9-15", #
	                  "Esperas la ocasión perfecta":"p-ocasion-perfecta-20-9-15"}, #
	        prueba:False,
	        imagen_arriba:False,
	        imagen_abajo:False,
	        },

        "al-interior-del-bosque-i":{
                titulo:"En el interior",
                texto:'''
                <p>No est&aacute;s dispuesto a guardar los miedos de la muerte
                hasta que te alcancen los jinetes. Antes si quiera de poder verlos
                surges de un salto y echas a correr.</p>
                <p>¡Justo a tiempo! El ruido de los cascos sigue acerc&acute;ndose
                y ahora sabes que van a por ti. Giras tu cabeza por medio segundo
                y los ves, a los siete, son vikingos, cargados de hierro y ansias
                de matar.</p>
                ''',
                opciones:{"¡Corre!":"p-al-interior-del-bosque-i"},
                prueba: False,
                imagen_arriba: False,
                imagen_abajo: False,
                },

        "p-al-interior-del-bosque-i":{
                prueba:True,
                r:5,
                s:["internas-bosque","pillado-ii"],
                imagen_arriba: False,
                imagen_abajo: False,
                },

        "pillado-ii":{
            titulo:"",
            texto:'''
            <p>La persecución salvaje terminó porque con la precipitación de la
            huida no acertarte a encontrar los más profundo del bosque. Los
            caballos pudieron seguirte, rodearte y batirte en velocidad para que
            sus dueños te encontraran y descargaran sobre ti sus flechas sin
            darte ni oportunidad ni gloria.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba: False,
            imagen_abajo: False,
            },

        "p-al-norte-42":{
            prueba:True,
            r:4,
            s:["convences-al-norte","no-convences-al-norte"]
            },

        "convences-al-norte":{#28
            titulo:"Te creen",
            texto:'''
            <p>Finalmente tus palabras tienen el resultado que buscabas, pero
            te ha llevado horas de debate; un tiempo que quizás tendréis que
            pagar con sangre más tarde. Tus órdenes vuelan aguijonando a diestro
            y siniestros pero ni tú ni el pueblo tenéis demasiada práctica en
            evacuaciones. Con todo al final tienes organizada la columna en tres
            grupos: ochenta con arcos y hondas, de entre trece y veinte años,
            la <em>fyrd</em>, de doscientos hombres y alguna mujer disfrazada
            con lanza y escudo, y otros cuatrocientos de gente desarmada.
            Mandas que estos últimos partan primero, con la <em>fyrd</em>
            detrás y, cerrando el paso a una milla del grupo principal,
            los más jóvenes, a los que acompañas.</p>
            <p>No pasa ni una hora en el camino que vislumbráis las siluetas de
            seis jinetes, que, en cuanto os ven, mucho antes de que podáis
            descubrir más detalles o hablar, se salen del camino y se abren
            hacia el oeste. ¿Quiénes serán y cuáles serán sus intenciones?</p>
            ''',
            opciones:{"Si intentas interceptarlos con tus jóvenes.":"interceptar-jovenes", #/45/-
                      "Si corréis para agruparos al grupo principal.":"agruparos-principal", #/46/?
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"escudo.png"
            },

        "no-convences-al-norte":{
            titulo:"No quieren escucharte",
            texto:'''
            <p>Tus palabras no logran hacerles entrar en razón. Tú solo eres un
            guerrero joven y desconocido y ellos, después de su familia, se
            deben a su señor, y no quieren dejarlo abandonado en estas horas
            trágicas.</p>
            ''',
            opciones:{"Sigues tu camino":"cumpli-avisando", #/169/-
                      "Les das la razón y vas con ellos a buscar al conde":"buscamos-conde" #/105/-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "interceptar-jovenes":{#45
            titulo:"Liebre y Caracol",
            texto:'''
            <p>Ochenta contra seis parecen buenos números cuando das la orden de
            empezar la carrera. Pero los jinetes, montados en sus veloces
            caballos, no tienen problemas en dejaros atrás muy rapidamente.
            Lo único que habéis conseguido es cansaros y dejar a tu gente
            dispersa por la llanura. Peor, antes de los vieras desaparecer,
            los jinetes habían vuelto a girar al norte, con un poco de mala
            suerte llegarán a donde están las mujeres y los niños a eso de la
            noche.</p>
            <p>Con el corazón temblando por la carrera, apenas ahora empiezas a
            pensar y a recordar la situación antes de tomar una decisión.</p>
            ''',
            opciones:{"Si corres hacia los civiles, dejando a tu gente descansar.":"corres-a-civiles", #/48/-
                      "Si mandas un mensajero a la fyrd.":"mensajero-a-fyrd", #/49/-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "corres-a-civiles":{#48
            titulo:"",
            texto:'''
            <p>Persigues a la noche y la oscuridad corre más que tu. Atrás has
            dejado a los jóvenes y ni siquiera has avisado a los guerreros. Tu
            mente fabrica pesadillas de emboscadas y hombres muerto y esa
            angustia acumulada te mantiene corriendo.</p>
            <p>Cuando llegas a los civiles, todos se giran desconcertados.
            ¿Quién es ese guerrero que nos persigue? Cuando te reconocen no
            acaban sus inquietudes. ¿Por qué está solo? ¿Por qué ha dejado a los
            demás? Sus preguntas se cruzan con las tuyas y al final parece ser
            que tus preocupaciones eran exageradas. Los seis jinetes ni siquiera
            han sido vistos por esta muchedumbre. Después la oscuridad os vence
            a todos y el cansancio te lleva a dormir.</p>
            <p>...</p>
            <p>Te despiertan poco después de la madrugada. Es uno de los chicos,
            cubierto de barro y sudor, la cara desencajada por el miedo.</p>
            <p>&mdash;Señor, nos alcanzan, nos alcanzan.</p>
            <p>&mdash;¿Cuántos son?</p>
            <p>&mdash;No lo sé, hay un gigante y Athrel dice que mil, pero
            Eodriwic dice que no pueden ser más que cien, y...</p>
            <p>&mdash;¿Dónde están? &mdash;Antes de que te pueda responder el
            cuerno vikingo hiela tus entrañas.</p>
            ''',
            opciones:{"Reunes todas tus tropa y presentas batalla.":"reunes-tropas-batalla", #/57/-
                      "Ordenas una huida inmediata.":"ordenas-huida-inmediata", #/61/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "reunes-tropas-batalla":{#57
            titulo:"Plan de Batalla",
            texto:'''
            <p>La decisión de presentar batalla ha sido dura. Todo puede
            terminar en este momento para los tuyos pues lucháis por la
            supervivencia. Lamentablemente no tienes tiempo para grandes
            preparativos, a lo más que puedes llegar es a establecer un plan de
            combate.</p>
            <p>Por lo que has podido ver todas sus tropas son guerreros que
            están formando en cuña, con el pagano estandarte en su vértice y los
            escudos como muros en sus lados. No pasará mucho tiempo antes de que
            carguen sobre vosotros. Entre ellos y vosotros el campo está limpio,
            nada hay que entorpezca sus pies ni retrase vuestras fuerzas.</p>
            <p>Consideras tus opciones. Podrías formar tu ejército en dos líneas
            separadas, con los escaramuceadores en vanguardia y la <em>fyrd</em>
            detrás, conforme a la tradición. La idea es que los escaramuceadores
            agoten y debiliten a la fuerza enemiga para que la fuerza principal
            pueda rematar la fanea.</p>
            <p>La segunda opción es más radical y solo la puedes recordar en
            leyendas antiguas. Consiste en disponer la <em>fyrd</em> en tres
            grupos, uno a cada flanco y otro más en retaguardia, dejando el
            centro para los escaramuceadores. Éstos no podrán resistir a los
            vikingos para siempre, pero cuando esto ocurra los tres grupos de la
            <em>fyrd</em> caerán sobre el enemigo, encerrándolo en un muro de
            escudos y lanzas.</p>
            ''',
            opciones:{"El plan tradicional.":"plan-batalla-tradicional", #/68/?
                      "El plan radical.":"plan-batalla-radical", #/74/?
                      "Si no sabes qué decisión tomar.":"no-decision", #/85/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "no-decision":{#85
            titulo:"¡Carga!",
            texto:'''
            <p>Al no tomar tú la decisión, el enemigo la toma por ti. Cargan
            gritando y antes de que puedas reaccionar la vanguardia de tus tropas
            se deshace sin luchar. A partir de ahí es una cacería. Cada uno
            intenta sobrevivir como puede; pronto el suelo queda alfombrado de
            armas y escudos.</p>
            ''',
            opciones:{"Corre tú también para salvar tu vida":"p-no-decision-v"}, #p-
            prueba: False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-no-decision-v":{
            prueba:True,
            r:5,
            s:["escapa-5-10-15","pillado-5-10-15"],
            },

        "escapa-5-10-15":{
            titulo:"Escapas",
            texto:'''
            <p>En la confusión de la huida has conseguido escapar con tu vida, tu
            espada y las ropas que llevas puesta. Todo lo demás ha quedado en el
            campo de batalla. Ni siquiera resta la esperanza en una victoria ahora
            que todos han perdido la moral. Te toca luchar por sobrevivir entre los
            campos dominados por el enemigo.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "pillado-5-10-5":{
            titulo:"Muerte",
            texto:'''
            <p>No sabes muy bien como vino, solo que una lanza, de repente te atravesó
            las costillas desde la espalda y acabaste en el suelo, entre cadáveres,
            esperando sin esperanza una muerte que ponga fin al dolor.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "ordenas-huida-inmediata":{#61
            titulo:"Todo parece perdido",
            texto:'''
            <p>No puedes evitar que tu voz contenga un timpre de pánico.
            &mdash;Rápido, tenemos que huir. Que nadie pierda un segundo.
            &mdash;Así comienzan tus órdenes y desde luego que nadie remolonea
            en cumplirlas. El aire vibra de angustia con los chillidos y lloros
            de los niños, los gritos impacientes de los hombres y la respiración
            entrecortada de todos.</p>
            <blockquote>Protégenos, Señor, de la furia de los hombres del norte.
            </blockquote>
            <p>Así comienza la oración que expresa esa angustia, pero nadie
            tiene el valor de rezarla hoy. El andar se transforma en carreras y
            las carreras en un caos conforme unas tropiezan con otros. Ya
            vienen, ya vienen, ya os alcanza la furia de los hombres del norte.
            En la retaguardia se cruzan flechas con lanzas y algunos de los
            jóvenes más valientes caen mientras los demás los abandona.
            La <em>fyrd</em> se disuelve, cada cual va a buscar a su familia o,
            los más cobardes, a desaparecer en el monte, a huir, a no ser nada.
            En este instante todo parece perdido.</p>
            ''',
            opciones:{"Descubre tu destino":"p-ordenas-huida-inmediata"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-ordenas-huida-inmediata":{
            prueba:True,
            r:3,
            s:["lanza-cuello","superviviente-cruz"] # 86- 88-
            },

        "lanza-cuello":{#86
            titulo:"Lanzas",
            texto:'''
            <p>La huida se transforma en un caos ensordecedor en el que te ves
            atrapado. Intentas correr, pero en vano, porque la gente se
            apelotona a tu alrededor. Una de los carneros de los campesinos,
            asustado como todos tropieza contigo y te derriba. Al levantarte
            crees estar en medio de un mar embravecido de personas, enseres y
            bestias, que te arrastran sin rumbo. Treinta segundos dura eso,
            después llueven lanzas.</p>
            <p>Comienzan los ayes, te das la vuelta, espada y escudo en mano,
            pero entonces, antes de que puedas ver la hueste pagana, una de las
            lanzas atraviesa tu cuello. Caes sobre el suelo inconsciente y
            comienzas a morir.</p>
            ''',
            prueba:False,
            opciones:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "superviviente-cruz":{#88
            titulo:"Superviviente",
            texto:'''
            <p>El caos en el que se transforma la huida te empuja fuera del
            grupo perseguido y antes de que te des cuenta te encuentras
            corriendo solo entre los matojos que surgen de un pantano. Por la
            sangre que te cae descubres una ceja rota. El agua te cubre hasta
            los tobillos, el sol ha llegado ya al mediodía y a tu alrededor ni
            se vislumbra un alma ni se escucha más que el silencio.</p>
            <p>Paras. Solo estás seguro de haberte perdido. Podrías desde luego
            intentar volver al camino, pero francamente ni tienes idea de en qué
            dirección estás, ni tienes ganas de tropezarte con más vikingos. Por
            otro lado y considerando la lejanía, tu familia tiene que estar
            vagamente al norte. Hacia allí te encaminas.</p>
            <p>El frío de las aguas te hiela el cuerpo comenzando por los pies.
            El barro te cansa, los cuervos son tu única compañía, quizás sueñen
            golosos con tu carne. El cielo va cubriéndose de nubes y estas
            descienden rapidamente hasta invadir la tierra. La niebla y la
            lluvia lo entreteje todo con lana de agua. Y es entonces, cayendo ya
            la tarde, que descubres, en medio de todo esto, clavada en el suelo,
            una cruz de ruda madera tan alta como un hombre, cubierta de letras
            formadas por los líquenes.</p>
            <p>Intrigado por tal prodigio, pero al mismo tiempo lleno de
            espanto, te aproximas y lees.</p>
            <blockquote>Toma tu cruz.</blockquote>
            ''',
            opciones:{"Tratas de sacar la cruz de su sitio":"tomar-mi-cruz-literal", #/89/-
                      "Rezas":"mi-cruz-rezar", #/91/-
                      },
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "tomar-mi-cruz-literal":{#89
            titulo:"Ángel de Luz y Majestad",
            texto:'''
            <p>Hinchas todos tus músculos para sacar la cruz que sale con
            inaudita facilidad. La carga en tus hombros y entonces desde el
            Cielo ves descender a un ángel vestido de luz y majestad. Sin que
            puedas evitarlo un fuerte temor se apodera de tu alma mientras al
            mismo tiempo te atrapa una inexplicable fascinación.</p>
            ''',
            opciones:{"Le sigues":"sigues-angel-93", #/93/?
                      "Vuelves a tu plan de volver a casa":"volver-casa-95", #/95/?
                      },
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "mi-cruz-rezar":{#91
            titulo:"",
            texto:'''
            <blockquote>Sálvame, Dios mío,<br>
            porque estoy a punto de ahogarme;<br>
            me estoy hundiendo en un pantano profundo<br>
            y no tengo dónde apoyar los pies.<br>
            He llegado a lo más hondo del agua<br>
            y me arrastra la corriente.<br>
            Ya estoy ronco de tanto gritar;<br>
            la garganta me duele;<br>
            ¡mis ojos están cansados<br>
            de tanto esperar a mi Dios!<br>
            <p>...</p><p>Apenas terminas de rezar el salmo la lluvia se seca y
            entre las nubes se abre un surco de cielo y luz. Enseguida te das
            cuenta de que está orientada al norte, a tu hogar. Dever, por ser
            quién eres y por lo que has vivido no puedes interpretar esto sino
            como un mensaje de Dios. El surco de cielo te indica un camino, como
            la columna de fuego guió a los israelitas en el éxodo. Este es Dever
            y este es el camino que debe seguir.</p>
            <p>Los días se van sucediendo sin que nada turbe tu tranquilidad.
            Sabes que solo es una ilusión pasajera, pero es una ilusión con la
            que engañas el cansancio y un hambre mal engañado con una comida
            cada vez más seca y pobre. Lluvia, sol y viento son tus compañeros
            durante el día, y el frío se pega cruelmente a tus huesos durante
            la noche.</p>
            <p>La alegría no llega hasta que divisas la Piedra de las Urracas,
            un monolito tallado en memoria de las tres reinas que en tiempos
            remotos ganaron aquí el respeto del Emperador de Roma y quizás algo
            más. Según tu abuela, tú mismo desciendes de una de estas tres, lo
            que supondría que tu estirpe tiene sangre antigua y, si has de creer
            a las leyendas, también del mismo emperador. Pero más allá de todo
            eso, lo único cierto es que estás en casa.</p>
            <p>Desde la Piedra de las Urracas, un corto camino te lleva ante la
            fortaleza de tu familia. De niño, antes de que vieras mundo, te
            impresionaba. Se trata de una colina artificial, rodeada por un foso
            y rodeada de estacas y dos anillos de empalizadas y atalayas. En el
            centro de todo, un pequeño fuerte romano que una vez alojó a una
            cohorte, y que ahora ha sido transformado en una torre de piedra.
            Ahí naciste, junto al fuego de la chimenea.</p>
            <p>Tu llegada provoca una revolución de alegría. A pesar de tu
            estado todos están impacientes por las noticias que traigas,
            esperando escuchar historias de tus viajes, los chismes de los
            condes y las nuevas maravillas que hayan traído los mercaderes
            del sur desde oriente.</p>
            <p>Cuando finalmente tienes el valor de compartir la terrible
            invasión, todo el mundo se queda frío. Miran hacia tu padre
            esperando que tome una decisión, pero éste, ante tus ojos cae
            privado del conocimiento, como alcanzado por un rayo invisible, para
            convulsionar en el suelo ante la desdicha de todos y luego
            morir.</p>
            <p>&mdash;Larga vida al conde Dever.</p>
            <p>Hablan de ti. Ahora tienes una responsabilidad. Lo primero es
            atender al funeral y entierro de tu padre; a quien llevaréis al
            monasterio para que lo cuiden los monjes. Pero incluso ahora tu
            cabeza no puede dejar de pensar en el monstruo que se acerca.</p>
            ''',
            opciones:{"Preparas tu fortaleza para un asedio, reclutando todas las milicias que puedas":"preparar-fortaleza-conde-dever", #/27/-
                      "Convocas a tus mejores hombres para llevar una guerra de guerrillas en el camino; mientras la milicia se ocupa del fuerte.":"guerrilla-camino-norte", #/69/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "mensajero-a-fyrd":{#49
            titulo:"Noche de Miedo",
            texto:'''
            <p>Tras una breve selección escoges a uno de los muchachos como
            mensajero y lo dejas marchar con la mejor de tus bendiciones. Justo
            después reorganizas tus hombres y los agrupas para pasar la noche.
            Con tanta sangre joven esperarías tener complicaciones de
            disciplina, pero el cansancio se sobrepone a todos: ni siquiera
            levantáis refugios, con mantas y la compañía de unos con otros
            tenéis suficiente.</p>
            <p>Solo te enfrentas al monstruo de los rumores. Hedrig, uno de los
            más jóvenes, no ha tenido más ocurrencia que preguntarte sobre el
            <em>devorador de reyes</em>, según las leyendas, un monstruo
            gigante, con forma de salamandra gigante, de carne "como el agua",
            y dientes de espadas. Por supuesto que tú no crees en tales cosas,
            pero antes de irte a dormir, notaste cierta expresión de miedo en
            los ojos de uno de los vigías de la primera guardia. Curiosamente el
            mismo que dos horas después te despierta contándote que ha visto
            algo.</p>
            ''',
            opciones:{"Vas a investigar tú solo con el vigía.":"investigar-con-vigia", #/55/-
                      "Alertas a toda la tropa.":"alerta-toda-tropa", #/56/?
                      },
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "investigar-con-vigia":{#55
            titulo:"Alivio y Peligro",
            texto:'''
            <p>Vuelves con el vigía hasta el lugar donde vió <em>algo:</em> una
            hilera de árboles en la margen de una charca.</p>
            <p>&mdash; Allí, allí, ¿no lo ve señor?</p>
            <p>Tardas en reconocerlo y no puedes estar muy seguro por la
            oscuridad, pero casi dirías que sobre el agua hay unos resplandores
            con forma de sapo. Notas al miedo sepulcral y ctónico infiltrándose
            en tus entrañas, corrompiendo pensamientos y emociones hasta que,
            rebelde ante todo, estallas en carcajas. Ríes y tus risas dispan el
            fantasma que tu propia mente había formado sobre el agua.</p>
            <p>Bueno, eso o puede que sea también cierta esa superstición que
            dice que los monstruos temen la risa de los niños. Y tengas la edad
            que tengas, mi querido Dever, tu joven acompañante no ha podido
            evitar unirse a tus carcajadas.</p>
            <p>...</p>
            <p>Despertáis y andáis antes del día. Casi os tropezáis con la
            milicia a la que, más amodorrada debéis azuzar para que se dé prisa.
            Ellos a su vez hacen lo mismo con los civiles hasta que toda la
            columna vuelve a su marcha. Es entonces cuando vuelves a la
            retaguardia y entonces también cuando temores peores que los de la
            noche te alcanzan. Son los ominosos sonidos de profundos pasos de
            gente de hierro y fuego. El estandarte del cuervo les precede y lo
            enarbola un garrido gigantón medio desnudo, que precede a una
            columna de cientos; quizás tantos como los tuyos, quizás más pero
            desde luego no la fuerza principal. Desde aquí, entre las brumas de
            la mañana, resulta demasiado difícil contarlos. Y de nuevo la eterna
            pregunta, ¿qué hacer?</p>
            ''',
            opciones:{"Reunes todas tus tropas y presentas batalla.":"reunes-tropas-batalla", #/57/-
                      "Los retrasas con tus jóvenes, para ganar tiempo a que escapen los civiles.":"operacion-dilatoria", #/58/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"hut.png"
            },

        "huida-desesperada-121":{
            titulo:"Huida Desesperada",
            texto:'''
            <p>Das a tus piernas todas las fuerzas que puedes hasta que vas
            dejando atrás los cascos de los caballos. Entonces, obligado por el
            cansancio, bajas un poco el ritmo hasta que vuelves a escuchar el
            ominoso sonido. Desfallecido, te apresuras ahora a buscar refugio,
            pero esta parte del camino es más rala de árboles y matorral y tu
            vista solo encuentras la ruinas de una alquería, que se yergue
            solitaria en medio del campo.</p>
            ''',
            opciones:{"Corres a la alquería con tus últimas fuerzas.":"ultimas-fuerzas-122", #/122/-
                      "Te escondes como puedes tras un arbusto cercano.":"escondes-arbusto", #/181/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"hut.png"
            },

        "p-ultimas-fuerzas-122":{
            prueba:True,
            r:5,
            s:["153","679"] # 153- 679
            },

        "153":{
            titulo:"En la alquería",
            texto:'''
            <p>Tras una agotadora carrera llegas a las ruinas de una alquería
            romana. Apenas tres edificios, de los cuales ninguno conserva el
            tejado y solo uno, el mayor, sus cuatro paredes. Te metes en ese y
            esperas, oteando desde un agujero. Tienes que esperar muy poco y en
            cuanto los ves te das cuenta de lo cercana que has tenido a la
            muerte.</p>
            <p>Porque lo que ves son seis jinetes vikingos, las calzas
            enrojecidas por lo que desde esta distancia se te antoja que es
            sangre. Llevan espada al cinto, sus grandes escudos colgados de la
            silla, demasiado grandes para usarse con efectividad. Por
            angustiosos momentos temes que se vuelvan a investigar las ruinas
            hasta que los ves alejarse por el camino.</p>
            <p>Pero una nueva angustia se une a la anterior.</p>
            <p>¿Y ahora qué? No puedes adelantar a gentes montadas y aunque por
            algún milagro o descuido de ellos lo hicieras, ¿cómo podrías
            enfrentarte a seis guerreros? Si todo sigue como hasta ahora los
            exploradores llegarán antes que tú hasta las tierras de tu familia.
            Afortunadamente son demasiado pocos como para representar una
            amenaza inmediata.</p>
            <p>Lo más sencillo, piensas, es seguir por el camino, dejándoles una
            saludable ventaja, para desviarte por el bosque cuando ya estés
            cerca de casa, confiando en que ellos estén ocupados con su tarea de
            exploración. Si eso no te convence, quizás lo más prudente sea
            internarte en el monte ahora mismo, buscando la protección de la
            naturaleza.</p>
            ''',
            opciones:{"Vuelves al camino, a buena distancia de los jinetes.":"camino-sin-jinetes", #35-
                      "Te internas en el bosque.":"internas-bosque-a", #a?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "679":{
            titulo:'',
            texto:'''
            <p>Corres con todas tus fuerzas, pero resultan escasas tras todas
            las fatigas por las que has pasado desde la llega de los vikingos.
            Consigues llegar a la alquería, pero te han visto. Son seis
            guerreros vikingos a caballo, con espadas, cota de malla, cascos y
            escudos y han concentrado todo su interés sobre ti. Sin prisa, se
            despliegan en forma de media luna, con los cuernos apuntando hacia
            ti, para que no tengas manera de escapar.</p>
            <p>Crees que la situación es desesperada. De los tres edificios que
            formaban la alquería, ninguno conserva el tejado y solo uno, el
            mayor, sus cuatro paredes. Quizás desde su interior pudieras
            rechazarlo a todos, pero te ríes de ti mismo ante tal ocurrencia.
            En cualquier caso ya cabalgan hacia ti. Decide rápido.</p>
            ''',
            opciones:{"Si decides luchar desde el interior del edificio mayor":"luchar-alqueria-18", #/18/
                      "Si te rindes":"te-rindes-123", #123
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "te-rindes-123":{
            titulo:'Malo Suerte',
            texto:'''
            <p>No te gusta tomar esta decisión, pero crees que luchar no tiene
            sentido. Son demasiados y nunca conseguirías vencerlos. Aún así
            odias tener que lanzar tus armas al suelo, ponerte de rodillas y
            levantar los brazos.</p>
            <p>Complacidos los vikingos desmontan y se te acercan, cuatro
            enarbolando sus espadas, los dos restantes asiendo hachas,
            preparados para lanzarlas a la mínima sospecha de una trampa.
            Pero tú no haces nada, comprendiendo que ya está todo perdido y les
            dejas acercarse. Cuando están junto a ti, dos de ellos te
            inmovilizan los brazos, un tercero te cierra los ojos con tu
            mano.</p>
            <p>&mdash;Malo suerte, &mdash;te dice una voz con fuerte acento
            extranjero. &mdash;No <em>pedemos</em> llevarnos a ti de
            <em>esclav</em>.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "luchar-alqueria-18":{
            titulo:'Desafío Final',
            texto:'''
            <p>Sean cuales sean las posibilidades, decides vender tu vida tan
            cara como sea posible. Y si tienes suerte de vencer a alguno, será
            uno menos contra los que tu pueblo tendrá que luchar. Animado por
            estos pensamientos, haces chocar en desafío espada contra escudo,
            finges una sonrisa y les esperas cantando ante el vano de la
            entrada. Si esta ha de ser tú última batalla al menos estás
            decidido a disfrutarla.</p>
            <p>Los vikingos no se arredran y optan por el asalto frontal,
            corriendo hacia ti mientras invocan a sus dioses paganos. Alzas tu
            espada, enarbola tu escudo y respondes a su choque.</p>
            ''',
            opciones:{"Vas a luchar contra tres vikingos, uno por uno, debido a lo estrecho de la puerta.":"p-luchar-alqueria-18"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-luchar-alqueria-18":{
            prueba:True,
            r:4,
            s:["65","144"] #65- 144-
            },

        "65":{
            titulo:"Lucha Sangrienta",
            texto:'''
            <p>La lucha ha sido sangrienta y no quieres recordarla, pero de
            algún modo tres de los vikingos yacen ahora muertos delante de lo
            que fue la puerta de la alquería. Tu espada ha bebido sangre, aunque
            también están manchadas tus ropas.</p>
            <p>Ahora los tres restantes no tienen intención de seguir intentando
            atravesar la entrada, sino que suben a sus caballos y se retiran.
            Sabes que no es por miedo sino que tienen una misión urgente que
            cumplir y no tienen tiempo de esperar el momento apropiado para
            vencerte; pero tu puedes contarlo como una pequeña victoria porque
            todavía estás vivo.</p>
            <p>Lo que cuenta ahora es ver cuál es tu siguiente movimiento.</p>
            <p>Lo más sencillo, piensas, es seguir por el camino, dejándoles una
            saludable ventaja, para desviarte por el bosque cuando ya estés
            cerca de casa, confiando en que ellos estén ocupados con su tarea de
            exploración. Si eso no te convence, quizás lo más prudente sea
            internarte en el monte ahora mismo, buscando la protección de la
            naturaleza.</p>
            ''',
            opciones:{"Si pruebas a ir por el camino.":"camino-94", #/94/-
                      "Si te internas ya mismo en el bosque.":"internar-bosque-172", #/172/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "camino-94":{
            titulo:"La Carreta",
            texto:'''
            <p>Decides arriesgarte a seguir por el camino considerando que la
            velocidad es tu primera consideración. Desde ahora tendrás que estar
            atento a dos peligros: que por cualquier causa se retrasen o que en
            cualquier momento decidan regresar a informar de cualquier cosa que
            hayan encontrado.</p>
            <p>Sin embargo, de momento, solo encuentras soledad. Durante otros
            dos días seguidos no pasa nada de interés, salvo que estás aún más
            cansado, sucio y hambriento; pero al atardecer del siguiente día,
            según reemprendes la marcha encuentras una carreta abandonada en
            medio del camino, con su carga de grano aún intacta; sin más merma
            que la que le están haciendo ahora los pájaros que se posan en
            ella.</p>
            ''',
            opciones:{"Intentas buscar a su propietario.":"propietario-carreta-58", #/58/-
                      "Te escondes.":"te-escondes-136", #/136/-
                      "Sigues adelante.":"sigues-adelante-164", #/164/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "te-escondes-136":{
            prueba:True,
            r:3,
            s:["te-descubren-30-9-15","tu-descubres-ellos-30-9-15"] # - | -
            },

        "tu-descubres-ellos-30-9-15":{
            titulo:"Los descubres",
            texto:'''
            <p>La carreta vacía te ha hecho sospechar que algo malo ha pasado.
            ¿A dónde ha podido ir el carretero? No se te ocurre ninguna razón lógica
            para dejar todo este cargamento de grano a merced de las bestias y los
            transeúntes salvo que haya tenido que huir para salvar la vida. Así que
            te escondes entre arbustos y esperas y pasas así la mejor parte de una
            hora hasta que los descubres: son tres vikingos acercándose por el camino,
            a unos veinte metros de distancia, con las ropas manchadas de sangre.</p>
            ''',
            opciones:{"Permaneces en tu escondite":"permaneces-escondido-1-10-15", #
                      "Les atacas con tu arco":"atacas-arco-1-10-15"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "te-descubren-30-9-15":{
            titulo:"Te han descubierto",
            texto:'''
            <p>La carreta vacía te parece lo suficientemente sospechosa para
            esconderte. ¿A dónde a ido el carretero? ¿A mear? ¿Acaso tiene alguien
            que guardar la intimidad en un camino poco transitado? Además en la
            carreta hay carga para un molino, ¿quién dejaría todo eso sin vigilancia?</p>
            <p>Así que te escondes entre arbustos y esperas y pasas así la mejor parte de una hora
            hasta que pierdes la paciencia y te levantas...</p>
            <p>Justo en el momento que tres vikingos con las ropas manchadas de sangre
            aparecen por el camino a unos veinte metros de ti, descubriéndote al instante.</p>
            ''',
            opciones:{"Huyes":"huyes-30-9-15",
                      "Te enfrentas a ellos con tu arco":"arco-30-9-15"}, #  huyes | arco
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },



        "propietario-carreta-58":{
            titulo:"Muerto",
            texto:'''
            <p>No tienes que caminar mucho tiempo hasta que, entre los árboles del
            margen izquierdo de la carretera, tendido de forma trágica sobre los
            arbustos, descubres un cuerpo. Te ahorraré los detalles, ha muerto a
            espada y la sangre todavía gotea sobre la hojarasca. Un arbusto está
            aplastado y en algunos lugares la hierba ha sido hollada hasta descubrir
            la tierra desnuda. Todo el bosque parece haber enmudecido ante el crimen
            que se ha cometido en su frontera.
            </p>
            ''',
            opciones:{"Sales corriendo de aquí":"p-corres-de-muerto-carreta-23-9-15", #-
                      "Investigas en profundidad":"investigas-profundo-23-9-15", #-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "p-corres-de-muerto-carreta-23-9-15":{
            prueba:True,
            r:8,
            s:["escapas-muerto-carreta-23-9-15","te-pillan-muerto-23-9-15"],
        },

        "te-pillan-muerto-23-9-15":{
            titulo:"Sin suerte",
            texto:'''
            <p>Deberías haber podido escapar. Saliste corriendo tan pronto como
            pudiste porque sabías que había algo peligroso por aquí. Ninguno de
            tus perseguidores era más rápido que tú y todos estaban agachados en
            la espesura, entre zarzales. Seguramente ni lo hubieran intentado.
            Pero es que corriste justo en su dirección, por un maldito azar del
            destino.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "investigas-profundo-23-9-15":{
            titulo:"Nuevo asesinato",
            texto:'''
            <p>Intranquilo por el desagradable encuentro empiezas a buscar por los
            alrededores una pista que te pueda llevar a los asesinos. Pero entonces,
            justo mientras examinas unas manchas de sangres, el filo de una espada
            te atraviesa la espalda.</p>
            <p>Caes muerto antes de poder sentir dolor.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "144":{
            titulo:"Sagas",
            texto:'''
            <p>Resistes los primeros embates del enemigos e incluso devuelves
            algún corte a sus espadas. Tres veces vienen a por ti y dos los
            rechazas; hasta que finalmente consiguen herirte y obligarte a
            retroceder. Contra-atacas, obligándoles a salir cuando ya tenían un
            pie dentro de las ruinas.</p>
            <p>Y otra vez empiezas el combate, más fatigado y con un hilo de
            sangre caliente bajándote por la pierna. ¿Dolor? No sientes nada.
            Tu espada se cruza con sus espadas, deteniéndolos una y otra vez
            durante una eternidad de gloria hasta que se apagan las fuerzas.
            Solo entonces consiguen empujarte otra vez al interior de las
            ruinas. Allí te rodean y esperan a que desfallezcas; pero la
            impaciencia se interpone en sus planes, y el primero que arremete
            contra ti, encuentra su fin en tu espada. Contra los otros cinco no
            tienes defensa y sus espadas hieren tu carne hasta que todo es
            primero oscuridad y después, y para siempre, luz.</p>
            <p>Has luchado con el valor de cien héroes y los vikingos te
            incluirán en sus sagas; pero tu cuerpo, incapaz de seguir de
            combatiendo, se desploma.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "buscamos-conde":{#105
            titulo:"¡Iremos!",
            texto:'''
            <p>Un bramido colectivo de asentimiento silencia todas las dudas que
            puedas tener. El entusiasmo incendia todo el pueblo y hasta las
            viejas buscan lanzas con las que unirse a la <em>fyrd</em>. Tarda un
            cuarto de hora para que se imponga un poco de razón y otras dos
            horas más para que el pueblo se organicen en dos grupos, lo que van
            a luchar y los que van a huir. Tu primera reacción como guerrero, y
            lo que todos esperan, es que lideres a los guerreros, pero por otra
            parte no puedes evitar pensar en los niños y los ancianos, cuyo
            destino es más que incierto.</p>
            ''',
            opciones:{"Si vas con los guerreros.":"vas-con-guerreros", #35-
                      "Si decides guiar a los refugiados.":"vas-con-refugiados", #/37/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "vas-con-guerreros":{#35
            titulo:"Guerreros",
            texto:'''
            <p>Conduces a la columna de la <em>fyrd</em> al camino. Dispones de
            doscientos lanceros con viejos escudos y unos ochenta adolescentes
            con hondas y arcos. Además de eso, dos carros de provisiones y la
            vaga idea de que debes dirigirte a la corte del Conde Ian en Offing
            para tratar de encontrar su ejército. En cuanto a los refugiados,
            confías que vuestra victoria les dé la oportunidad que
            necesiten.</p>
            <p>Piensas, no sin cierta emoción, que esta es la primera vez en tu
            vida que diriges a una especie de ejército y supones que sería bueno
            que empezaras a dar un par de órdenes para organizar todo esto. En
            tu cabeza bullen dos preocupaciones que parecen pelear entre ellas:
            seguridad y velocidad. Lo que te han enseñado es que las tropas
            ligeras deberían adelantarse para explorar, pero los tuyos no son
            sino campesinos adolescentes y para que hicieran algo de provecho
            tendrías que estar tú entre ellos, abandonando la fuerza principal.
            Lo más rápido, aunque a riesgo de caer en una emboscada, sería
            formar todo en una columna, forzar la marcha y rezar.</p>
            ''',
            opciones:{"Si vas con los exploradores.":"guerreros-exploradores", #/43/?
                      "Si fuerzas la marcha con una sola formación.":"guerreros-forzar-marcha", #/44/?
                      },
            imagen_arriba:False,
            imagen_abajo:"escudo.png",
            prueba:False,
            },

        "milicia-filas":{
            titulo:"Muro de Escudos",
            texto:'''
            <p>Extiendes tu espada a modo de barrera y con un atronador “en mi
            marca” alineas a toda una fila de campesinos que intentan hacerse
            pasar por guerreros. Tiemblan, esquivan tu mirada, se tropiezan con
            sus propios lanzas, pero finalmente forman en algo que se parece a
            una unidad.</p>
            <p>&mdash;¡Escudos! &mdash;Dada la orden, te integras en la columna.
            ¡Han llegado! Quien creas ser, ahora no importa. La salvaje horda de
            vikingos, aullando a sus ídolos paganos, corren alzando los filos que
            beberán vuestra sangre, brillantes sus nobles cubiertos de acero.
            Tres pasos, aprestas tu escudo; dos pasos, alejas tu espada. Un paso,
            te fijas un segundo eterno en el hombre que la suerte te ha puesto
            enfrente: barba de fuego, damasco en su espada, fuerte su aliento y
            fiera mirada. Los viejos poemas te traen recuerdos de los tiempos de
            los héroes que nunca viviste y a los cuales ahora te unes.</p>
            ''',
            opciones:{"A la batalla":"p-milicia-filas"},
            prueba:False,
            imagen_arriba:"escudo.png",
            imagen_abajo:False
            },

        "p-milicia-filas":{
            prueba:True,
            r:7,
            s:["giro-espadas","muerte-milicia"] # - -
            },

        "giro-espadas":{ #67
            titulo:"Muro de Escudos",
            texto:'''
            <p>Un giro de tu espada surca de sangre el pecho de tu enemigo, que se
            derrumba bajo los pies de sus compañeros. A tu alrededor el mismo
            drama se repite, con diverso resultado. No puedes atenderlo porque
            otro guerrero sucede al anterior y después otro; que acaban también
            derrumbados sobre la hierba que se está tiñendo de rojo. Alzas la
            mirada, tu milicia está aguantando por ahora, y está claro por qué:
            los mejores guerreros vikingos se están enfrentando a los thengs.
            Pero tus ojos te traen noticias peores; a vuestros flancos se están
            concentrando nuevas hordas de guerreros, y dentro de muy poco tiempo
            os rodearán.</p>
            <p>Sopesas la situación, mientras rechazas a un nuevo enemigo con el
            escudo, intentando ganar tiempo para dar una nueva orden, o decidir
            si eres tú quién debe hacerlo.</p>
            ''',
            opciones:{"Peleas como un león y Esperas una orden del Conde":"183", #,/183/?
                        "Haces que la milicia se retire peleando lentamente hacia el monte que tienes a tu espalda, esperando que los thengs tengan el mismo sentido común.":"digno-posible", #/131-
                        },
            prueba:False,
            imagen_arriba:"escudo.png",
            imagen_abajo:False
            },

        "muerte-milicia":{
            titulo:"El Final de un Valiente",
            texto:'''
            <p>Agonizas. Los viejos poemas se están acabando para tí, que yaces
            en el suelo entre heridos y moribundos. Su espada fue más rápida y la
            sangre abandona tu cuerpo en un rápido reguero mientras la vista y el
            dolor se nublan hasta desaparecer para siempre.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "digno-posible":{
            titulo:"Lo digno y lo posible",
            texto:'''
            <p>El ataque enemigo arrecia un tiempo más, pero de pronto se detiene.
            Ante los tuyos y entre los tuyos el campo está sembrado de lamentos
            y muertos. No muy lejos los thengs siguen combatiendo, sin decaer su
            ánimo, ni pensar en su vida.</p>
            <p>Pero junto a vosotros los vikingos están reformado sus líneas,
            alejando sus heridos, irguiendo sus estandartes, y gritando a sus
            ídolos que les traigan las fuerzas para mataros a todos. No puedes
            perder tiempo ni la oportunidad; cuchicheas la orden de retirada,
            que va pasando entre las filas a paso lento. Luchas a cada paso por
            mantener la formación, moviéndote de un lugar a otro, animando a
            uno, riñendo a otros y vigilando siempre tu espalda.</p>
            <p>Pronto te das cuenta que los vikingos te tienen a ti y a tus
            hombres por nada. Solo un grupo pequeño os sigue y os vigila a
            distancia. Mientras todo su ejército está rodeando a los thengs cuyo
            mal fin es seguro. La rabia y la culpa te atraviesan como a un niño
            pequeño que hubieran pillado robando, pero tú no tienes el lujo de
            poder llorar.</p>
            <p>Miras a tus soldados, que fueron siempre campesinos, sus rostros
            atemorizados que ahora te parecen acusadores mientras intentas
            discernir entre lo mejor, lo digno y lo posible.</p>
            ''',
            opciones:{"Ordenas ir al fuerte del conde para defenderlo.":"al-fuerte", #/92-
                        "Ordenas ir a por las mujeres y los niños para emprender luego la huida a la Tierra de los Pantanos.":"tierra-pantanos" #/187-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "tierra-pantanos":{#92
            titulo:"A la Tierra de los Pantanos",
            texto:'''
            <p>No estás seguro de que tu orden sea la que quisiera escribir un
            poeta, pero te parece la única posible. &mdash;¡Salgamos de aquí!
            Tenemos que salvar a nuestras familias.</p>
            <p>Nuestras… te gustaría que eso fuera verdad. La tuya vive lejos,
            al norte en un pueblo no muy diferente de este y con las mismas
            esperanzas de vencer a los bárbaros. Pero eso son preocupaciones de
            otro día y también de otra gente. Peleas contigo mismo hasta
            amordazar a tu corazón y escuchar solo a tu mente.</p>
            <p>Por lo menos los hombres responden con entusiasmo. En ningún
            momento tienes que dar una orden y, si tuvieras que animar a
            alguien, sería a ti mismo. Enseguida dejáis atrás a los vikingos que
            os seguían y ni siquiera tardáis en evacuar el pueblo: el grano, las
            piedras de molino, las mantas, las gallinas que puedan salvarse; lo
            demás no importa; y emprendéis juntos una larga marcha que encabezan
            los niños y que cierras tú, caminando lentamente, a media legua del
            grupo.</p>
            <p>&mdash;Uno para el cuervo, otro para el muerto, el último para el
            estúpido. ¿Quién eres tu?</p>
            <p>Te das la vuelta. Ante ti hay un joven delgado y bajito, vestido
            con ropas negras bordadas de oro, que te mira burlón. &mdash;Uno para el
            cuervo, otro para el muerto y tú eres el estúpido. &mdash;Te dice ahora.
            &mdash;¿Sabes una cosa? Moriréis todos, si todos no compráis mi hechizo de
            niñas. O sea que, abreviando, moriréis. Si lo prefieres tú puedes
            ser el primero.</p>
            ''',
            opciones:{"Te interesas por su hechizo de niñas":"hechizo", #/111/-
                        "Lo mandas a molestar a otra parte con palabras no demasiado educadas":"al-peo", #/151/-
                        },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"oak_leaf_illustration.png"
            },

        "al-fuerte":{#187
            titulo:"Nariz Azul",
            texto:'''
            <p>Viendo que está perdido el campo, diriges a tus tropas la única
            orden que te parece segura.</p>
            <p>&mdash;Volvamos al fuerte. En marcha. Vamos, rápido.</p>
            <p>La marcha comienza con la rapidez que pueden alcanzar los hombres
            cansados pero desesperados por la vida. A momentos perdéis de vista
            a los vikingos y te vas haciendo a la idea de que vas a llegar al
            fuerte sin problemas; pero cada vez que te das la vuelta notas como
            falta uno o dos de tus soldados. No hace falta ser un lince para
            concluir que han desertado para salvar sus vidas. Cuando llegas al
            fuerte no te quedan sino la mitad; y ya estáis todos rodeados.</p>
            <p>Atrancáis las puertas, reforzáis las empalizadas, preparáis hondas
            pero cuando la mañana sigue a la noche descubrís que todo está
            perdido. Una tormenta de hierro os rodea, una muralla de escudos
            circunda vuestra muralla y solo os queda esperar el momento del fin.</p>
            <p>Pero cuando esperáis que llegue el asalto, tus hombres aterrados
            ven llegar seis filas de mujeres y niños, con cadenas y cuerdas y
            cuchillos señalando sus entrañas. Un tal “Nariz Azul, hijo de
            Thortyr”, exige vuestra rendición. Al instante tus hombres tiran sus
            lanzas y ya sabes que nunca más serás su jefe, sino uno más entre
            los esclavos de los vikingos.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "hechizo":{#111
            titulo:"Hechizo de Niñas",
            texto:'''
            <p>Aunque el personajillo te ha irritado no puedes reprimir tu
            curiosidad. &mdash;¿Hechizo de niñas?, ¿Qué es eso del hechizo de
            niñas?</p>
            <p>&mdash;Hechizo de niñas, mi tonto amigo, son doce bailarinas en
            un corro que giran muy quietas hasta abrir una puerta y tras esa
            puerta a un reino de peligros y esperanzas, donde maravilla eres
            y maravillas vives.</p>
            <p>Y dicho eso desaparece ante tus ojos.</p>
            ''',
            opciones:{"Sigue adelante":"oscuridad"}, #/82/-
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "al-peo":{#151
            titulo:"",
            texto:'''
            <p>La criatura cierra los ojos y con voz llena de desprecio te
            escupe una frase &mdash;Sea como seas. &mdash;Y así, dejándote
            perplejo, desaparece de tu vista sin dejar el más remoto de los
            recuerdos.</p>
            ''',
            opciones:{"Sigue adelante":"oscuridad"}, #/82/-
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "oscuridad":{ #82
            titulo:"Extraña Oscuridad",
            texto:'''
            <p>Después de tu extraño encuentro, el mundo se abate en una extraña
            oscuridad. Dicen que las Tierras del Pantano son la última esperanza
            de los locos, cementerio de bandidos y ruina de amantes despechados.
            Es el reino de las leyendas amargas, habitadas por fantasmas paganos,
            asesinados en extraños ritos y el único país sobre la tierra que
            Dios no redimió del diluvio de Noé. Eres el único que siente esto;
            por ahora las mujeres, los niños y los campesinos solo piensan en
            esos vikingos en los que deberías pensar, pero tú estás abrumado por
            el sentimiento de derrota. Sientes más frío del que hace, más h
            umedad de la que se cuela por tus botas y no puedes centrar tu mente
            en la huída.</p>
            <p>La lluvia crece según os vais adentrando en vuestra ruta que poco
            a poco os lleva a un paisaje de árboles dispersos, matas de hierba,
            charcas, arroyos y en todo lo demás, barro y cieno. Cuando llega la
            noche los niños lloran, los viejos tosen y todos se encuentran
            helados de miedo. Por falta de mejor cama, os subís a los árboles,
            esperando que la mañana os traiga mejor afán.</p>
            <p>Llueve, ha llovido y seguirá lloviendo. No os queda nada seco; si
            no encontráis refugio pronto el grano se os pudrirá antes que
            vuestros huesos. También están los mosquitos disfrutando con
            vuestras carnes. Ya puedes escuchar las primeras voces de deserción
            que piden pedir la piedad de los vikingos. Los podrías pintar como
            monstruos, pero todos saben la verdad, no podéis confiar en que
            siempre digan la verdad, ni amen la paz, pero tampoco es cierto que
            maten por puro gusto. Para los más pobres de estos campesinos solo
            sería cambiar unos amos por otros. Pero también tienes conocimiento
            del viejo fuerte romano, en el centro de lo que los viejos llaman la
            isla en el pantano, un sitio sombrío y frío, apenas habitable para
            los duros legionarios y que nadie ha visto en treinta años.</p>
            <p>Oh, y está lo del cuento de los niños perdidos y un dragón que se
            los come y todas esas cosas de viejas que nunca dan miedo hasta que
            te ves envuelto en la bruma.</p>
            ''',
            opciones:{"Dejas que lo que quieran rendirse se rindan y guías los que queden te sigan al viejo fuerte":"al-fuerte", #/13/-]
                      "Ordenas a todos a ir al fuerte contigo":"todos-al-fuerte", #/34/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "todos-al-fuerte":{#34
            titulo:"La Isla del Pantano",
            texto:'''
            <p>Das la orden de ir al fuerte y la gente te sigue sin entusiasmo;
            por el mero hábito de seguir a un líder. Por sus caras, sin embargo,
            no puedes hacerte ninguna ilusión sobre su entusiasmo. Si los vikingos
            les prometieran respetar nada más que sus vidas te abandonarían
            ahora mismo.</p>
            <p>El viaje al fuerte es una larga batalla contra el barro y los
            mosquitos. Al esfuerzo se le une la tragedia de ver desfallecer de
            fatiga a una de las ancianas que muere muy cerca de ti. Las miradas
            de la gente se vuelven más duras, más amargas y hasta hacerte
            preguntar si te culpan del fin de esa vida.</p>
            <p>La llegada a la Isla del Pantano tampoco aporta gran alivio. El
            fuerte son restos de un pasado, apenas cuatro paredes, eso sí, bien
            recias que solo están resguardados por los restos de lo que alguna
            vez fuera un techo.</p>
            <p>Poco a poco, cada familia va haciéndose un refugio alrededor del
            fuerte: una “casa hundida”, la más modesta de todas, pero la más
            fácil de construir. Se excava en la tierra y se pone un techo
            encima.</p>
            <p>Cuando están por terminar, ya de noche, Eldwyn, un viejo de
            cincuenta años, manos grandes y mayores hombres, se dirige a ti
            —Aquí solo crecerá la avena. —Cuando ve que duda, porque al fin esta
            tierra no parece peor que ninguna otra, aclara —Apenas hay tierra
            para recoger avena para todos, si el año es bueno y llegamos a la
            cosecha. Con lo que tenemos no llegamos, habrá que conseguir más.</p>
            <p>¿Qué le respondes?</p>
            ''',
            opciones:{"Saquearemos a los vikingos.":"14", #/14/-
                      "Primero tenemos que reconstruir el fuerte.":"reconstruir-fuerte", #/114/?
                      "Tenemos que explorar esta tierra. Quién sabe, igual haya caza.":"explorar-caza", #/162/-
                      },
            prueba:False,
            imagen_arriba:"hut.png",
            imagen_abajo:False
            },

        "14":{
            titulo:"Saquearemos a los vikingos",
            texto:'''
            <p>En cuanto las palabras salen de tu boca la gente te mira como se
            mira a un loco. Se supone que son los vikingos quienes saquean angsax
            y no al revés. Pero tú no pierdes tu aplomo.</p>
            <p>&mdash;No es tan difícil y ya nada podemos perder. No tenemos casas
            ni fincas y ya somos forajidos. Hagamos lo que hagamos nos van a perseguir
            igual. Si no nos hacen más daño es que no pueden. Así que busquemos
            una noche o una trampa, entremos en sus campamentos y robemos. Así
            por una parte les hacemos la guerra, por otra les damos preocupación y
            por última engordamos.</p>
            <p>Poco a poco la gente se va convenciendo hasta que en la mente de
            todos se instala la idea de que la única forma de sobrevivir es robar
            a los vikingos. Una vez que eso pasa ya no hay miedo y sus preguntas
            se sustituyen por una sola: <em>¿cuál es tu plan?</em></p>
            ''',
            opciones:{"Salimos al alba, a encontrar su campamento":"al-alba-3-10-15", #
                      "Saldremos en cuanto caiga el sol, a saquearlos":"a-la-noche-3-10-15"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "al-alba-3-10-15":{
            titulo:"El campamento",
            texto:'''
            <p>Decides que os será más difícil encontrar el campamento vikingo
            en la oscuridad y mandas todo el mundo a dormir salvo a un retén de
            vigías. A la salida del sol tomas dos docentas de hombres y los
            divides en seis grupos, cada uno buscará el campamento vikingo por
            su cuenta.</p>
            <p>Al atardecer del segundo día, tu propio grupo, arrastrándose entre
            la hierba alta, descubre a los vikingos acampados junto a las marismas
            donde el caudaloso río Uhtceare se hunde en el barro. Su recinto es
            una bien ordenada trama de tiendas de campaña a la izquierda y toscos
            refugios de madera a la derecha, donde han dejado a sus caballos.</p>
            <p>Rápidamente das la orden a uno de los tuyos a que traiga a los demás
            grupos aquí para la noche. Hecho esto te pones a pensar en tu plan nocturno.
            </p>
            ''',
            opciones:{"Intentarás infiltrarte en la oscuridad, sencillo y limpio":"infiltrarse-3-10-15", #
                      "La mitad de tus hombres creará una distracción, mientras te infiltras con la otra mitad":"distraccion-3-10-15"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "explorar-caza":{#162
            titulo:"Barro y Frío",
            texto:'''
            <p>Tomas un pequeño grupo y os adentráis en el pantano hasta que se
            hace de noche. El ambiente se torna de repente en insufriblemente
            frío; el aire os araña el cuello y el barro congela vuestros pies.
            La Luna apenas se atreve a asomarse entre retales de niebla y
            lluvia. Pronto todo es oscuridad y frío.</p>
            <p>Decepcionados, volvéis al fuerte, dando por bastante no haberos
            perdido, cuando os sorprende un extraño chapoteo. Alzas la mano,
            pero no hace falta, ya han parado los tres campesinos y han erguido
            lanzas y escudos. Tiemblan, pero no es momento de palabras. Aguzas
            el oído y crees saber que se os acerca lo que se os acerque.</p>
            <p>Dudas, estáis completamente al descubierto, en terreno malo y
            embarrado y no tienes ni a los mejores guerreros, ni a los más
            valientes.</p>
            ''',
            opciones:{"Huís":"142","Esperáis":"32"}, #142- 32?
            prueba:False,
            imagen_arriba:"hut.png",
            imagen_abajo:False
            },

        "142":{
            titulo:"Combate en el barro",
            texto:'''
            <p>Desconcertado por el ruido, das la orden de huir. Os cuesta
            arrancar sobre el barro, y cuando lo hacéis destruís el silencio de
            la noche. Corréis con todas vuestras fuerzas, hundiéndoos en el
            barro; mientras la oscuridad os va separando unos de otros sin daros
            cuenta. Un mal paso te hace caer sobre la charca que llena tu cuerpo
            de frío y humedad. Luchas hasta levantarte y emprender de nuevo la
            huída, ahora más lentamente. Cuando te recuperas ya no distingues a
            tus compañeros. A tu alrededor la oscuridad solo se ve interrumpida
            por gritos, ayes y tres pares de pisadas. Te vuelves, apenas atinas
            a vislumbrar tres formas que adivinas que no son de tus hombres.
            Buscas las fuerzas para correr otra vez hasta que las nudosas raíces
            de la vegetación del pantano te hacen frenar. Tus perseguidores
            comparten tus dificultades, resultando en una persecución extraña,
            lenta, a trompicones y llena de fríos.</p>
            <p>De bruces tropiezas con un tronco. El golpe te hierve en los ojos
            y un pulso de dolor se instala en tu nariz. Con todo no es grave,
            salvo por el hecho de que has perdido toda esperanza de poder
            escapar. Desenvainas para desafiar a tu destino y los tres
            guerreros, que armados de hachas y escudos, se despliegan ante
            ti.</p>
            ''',
            opciones:{"Este va a ser un combate muy difícil.":"p-142"},
            prueba:False,
            imagen_arriba:"hut.png",
            imagen_abajo:False
            },

        "p-142":{
            prueba:True,
            r:5,
            s:["vences-84","derrota-175"] #84? 175-
            },

        "derrota-175":{
            titulo:"Ferocidad",
            texto:'''
            <p>Te defiendes con ferocidad; es lo único que haces porque se te
            hace imposible atacar a ninguno, en cuanto intentas arremeter con tu
            espada, otras dos te rechazan. El combate prosigue durante treinta
            segundos eternos hasta que una de las espadas muerde tu hombro, el
            dolor solo dura un instante, porque antes de caer al suelo descubres
            la guardia de tu escudo…</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "al-fuerte":{#13
            titulo:"Palabras Bonitas",
            texto:'''
            <p>El resentimiento te consume cuando te diriges a ellos. &mdash;Son
            y serán tiempos muy duros... ¡Bah!, ¿para qué os voy a engatusar con
            palabras bonitas? Que cada uno mire a su familia. ¿Queréis que vivan
            dónde os llevo? ¿Tanto os importa ser libres? —Tus palabras suenan
            más duras y amargas de lo que debieran pero la tristeza y la derrota
            te lleva a un ataque de sinceridad. Por otro lado y pensándolo mejor
            entre menos seáis más fácil será alimentar a todos.</p>
            <p>Estas y otras racionalizaciones te van cruzando la cabeza según
            te vas quedando completamente solo. Poco a poco vas comprendiendo
            que nunca te habían seguido a ti, sino que huían del miedo y el
            miedo al hambre ha resultado ser más terrible que el miedo a los
            vikingos. Con todo, cuando por fin pierdes de vista a la última de
            las familias, te parece imposible enfrentarte a lo que está pasando.
            </p>
            <p>Te encaminas hacia el viejo fuerte, más que nada para buscar un
            refugio para la noche. Batallas contra el barro y los mosquitos y un
            cansancio que te hace desear estar muerto, como seguro están todos
            los thengs.</p>
            <p>Cuando por fin llegas al fuerte, es poco más que un cuadrado de
            piedras agrietadas, una ruina sin techo, de la que huyen espantadas
            las alimañas. Allí, entre los cantos de una esquina, te improvisas
            un refugio donde duermes.</p>
            <p>Se hace el día. Despiertas a un mundo silencioso, donde hasta las
            ranas parecen estar durmiendo. La lluvia de ayer se ha condensado en
            niebla y te cuesta creer que estás despierto.</p>
            ''',
            opciones:{"Exploras los alrededores inmediatamente.":"explorar-alrededores", #/4/-
                      "Haces un fuego para calentarte":"fuego-calentarte", #/104/-
                },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "explorar-alrededores":{#4
            titulo:"Perdido en la Niebla",
            texto:'''
            <p>El día apenas ha empezado cuando sales a explorar para encontrar
            niebla ante tus ojos y cieno bajo tus pies. Todo el páramo se reduce
            al frío que entumece tus pies y un lienzo gris que sepulta todas tus
            esperanzas. Tras un rato no sabes dónde estás y tus miedos van
            recordando las historias de los puc que disfrutan confundiendo a los
            humanos.</p>
            <p>Cuando la niebla se dispersa, dos horas después, estás inmerso en
            lo más salvaje de la naturaleza. Hasta donde alcanza la vista no hay
            sino humedales entreverados de matorrales, arboledas e islas de
            arena que se funden al este lentamente con el mar. Tienes la
            sensación de haber caminado continuamente hacia el oeste, pero no
            puedes estar seguro. De hecho, ahora que lo piensas otra vez, puede
            que fueras un rato hacia el sur y luego, ¿hacia dónde fuiste?</p>
            ''',
            opciones:{"Te diriges al este":"este-26", #/26/-
                      "Vas al norte":"norte-38", #/38/
                      "Caminas en espiral, alejándote lentamente de donde te encuentras ahora":"camina-espiral", #/52/
                      "Caminas al oeste":"oeste-138", #/138/
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "fuego-calentarte":{ #104
            titulo:"Descansas a la Lumbre",
            texto:'''
            <p>El fuego nace de milagro en un nido de ramas que solo puedes
            llamar secas porque todo lo demás está empapado. Los naranjas y los
            ocres de las llamas van salpicando de calor la niebla y refrescan
            tus ganas de vivir. Hace mucho que no tenías un momento para pensar
            y es curioso que en la desgracia de tu penosa situación ni temes ni
            penas. Como los héroes de antaño has encontrado en estas piedras
            mohosos y en este fuego desvalido un santuario que te refugie hasta
            que, con fuerzas, acrecentadas puedas salvar el mundo.</p>
            <p>Salvar al mundo… te ríes de ese pensamiento, pero de algún modo
            casi milagroso te reconforta.</p>
            <p>Desayunas de tu avena y, a falta de cerveza, bebes agua hervida
            con flores de las llamadas de atardecer, como habría hecho tu madre
            hace la mitad de tus años. Y después de todo eso, el clima se
            despeja y puedes pensar en explorar.</p>
            ''',
            opciones:{"Sigue con tu misión":"sigue-mision-135"}, #/135/
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "este-26":{ #26
            titulo:"Hasta las Axilas",
            texto:'''
            <p>Las horas te van pasando por encima, desesperándote de barro.
            Finalmente llegas a un punto que lo que parece tierra firma no es
            más que plantas lacustres flotando sobre una superficie  cada vez
            más salada. En este momento el agua te llega a las axilas y sabes
            que tienes que desistir de continuar.</p>
            ''',
            opciones:{"Vuelves por dónde viniste":"vuelves-viniste", #/201/?
                      "Si vas al norte":"norte-185", #/185/-
                      "Si vas al sur":"norte-76", #/76/]
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "norte-185":{ #185
            titulo:"Fango",
            texto:'''
            <p>Después de una lucha eterna contra el fango te resignas a la
            terrible idea de que vas a tener que pasar la noche en los
            humedales. Ya piensas en el frío que te entrará en los huesos y
            anticipas la enfermedad que tomará tus pulmones. Lo peor de todo es
            que te parece inevitable, aunque quizás tuvieras una oportunidad
            si…</p>
            ''',
            opciones:{"Buscaras a un árbol para dormir entre sus ramas.":"arbol-dormir", #/191/-
                      "Siguieras adelante durante la noche.":"adelante-noche-64", #/64/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "arbol-dormir":{ #191
            titulo:"Otro Día de Frío",
            texto:'''
            <p>La noche pasa rápidamente en el árbol y te despiertas con las
            primeras luces, preocupado de encontrarte enfermo. Pero, a salvo de
            algo de tos, un ligero moqueo y algún estornudo parece que estás
            fuerte; lo que es afortunado, ya que te espera otro día más en este
            pantano desolado sin pista alguna de adónde ir, salvo que, al este,
            sigue desapareciendo en el mar.</p>
            ''',
            opciones:{"Al norte":"norte-29", #/29/-
                      "Al sur":"sur-63", #/63/-
                      "Al oeste":"oeste-102" #/102/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "sur-63":{#63
            titulo:"Sin Esperanza",
            texto:'''
            <p>Das media vuelta y, aunque al principio la ruta se te hace
            extrañamente familiar, al poco vas sintiendo la intranquilidad de
            haberte perdido. La sensación se acrecienta según pasan las horas y
            al llegar el confín del día pierdes toda esperanza.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "oeste-102":{#102
            titulo:"",
            texto:'''
            <p>Decides tomar la dirección del sol y dirigirte tierra a dentro,
            alejándote del mar. Tu andar, al principio difícil, se va tornando
            fácil a ratos, según tropiezas con tierra seca, pero enseguida esos
            respiros son interrumpidos por arroyos y más pantanos que te
            desesperan en su abrazo mortal. Si alguien te viera ahora
            descubriría un espantapájaros cansado y cubierto de barro hasta el
            cabello, pero determinado a sobrevivir.</p>
            <p>Aunque no hay quien te observe salvo las garzas que saltan de una
            charca a otra buscando ranas y peces. Ni siquiera se asustan cuando
            te acercas; no hacen ni un movimiento cuando preparas tu arco para
            procurarte algo de caza. Disparas a dos pasos, no puedes fallar, y
            el ave cae muerta ante tus pies. Solo entonces sus congéneres se
            dispersan a los cuatro vientos.</p>
            <p>Entonces te derrumbas sobre tus rodillas, comprendiendo al fin lo
            que pasa, estás en tierras tan remotas que jamás nadie las ha pisado
            antes, completamente perdido.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "norte-29":{#29
            titulo:"Extraño Animal",
            texto:'''
            <p>Te pones en marcha para bregar de nuevo contra el barro y los
            pantanos, dejando el mar a tu derecha. Tienes que hacer uso de todas
            tus fuerzas pero, al final, dan como resultado que alcanzas un
            bosque. Todavía no estás en la civilización, ni nada que se le
            parezca, pero al menos la tierra ya es firme y por unas horas todo
            te parece posible. Pronto, sin embargo, vuelve el recuerdo de la
            guerra y los vikingos y la realidad de que tu mundo se está
            desmoronando más allá de donde ven tus ojos.</p>

            <p>Sin embargo todo eso debería estar muy lejos todavía, a menos que
            ese bulto gris pálido que se mueve entre los árboles, sea alguna
            clase de extraño animal.</p>
            ''',
            opciones:{"Esperas a que se detenga y le disparas con tu arco a la primera oportunidad":"extrano-animal-arco", #/125/-
                      "Intentas seguirle para asegurarte a qué te enfrentas":"extrano-animal-seguir", #/178/
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "extrano-animal-arco":{#125
            titulo:"Pequeño Blanco",
            texto:'''
            <p>No tienes que esperar mucho, de hecho pierdes la primera
            oportunidad de disparar acercando la flecha al arco; pero para la
            segunda ya estás preparado. El objetivo no es más alto que un
            taburete, solo una parte de la espalda de alguien que se agazapa
            entre las sombras. Te preparas, apuntas, disparas y ves con
            esperanza cómo la flecha se aleja de tu arco…</p>
            ''',
            opciones:{"Descubre el resultado":"p-extrano-animal-arco"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-extrano-animal-arco":{
            prueba:True,
            r:4,
            s:["aciertas-p-extrano-animal-arco","fallas-p-extrano-animal-arco"] #139- #171-
            },

        "aciertas-p-extrano-animal-arco":{#139
            titulo:"Tragedia",
            texto:'''
            <p>Aciertas. Un grito agudo de dolor te hiela la espalda; no has
            herido a un guerrero acostumbrado al combate. Cuando el cuerpo de tu
            víctima se desploma puedes ver la cabeza de un muchacho entre diez y
            doce años, que en mira en tu dirección sin verte, atrapado por un
            miedo que le impide llorar. Quizás le quede muy poco de vida. La
            culpa te acongoja el alma, pero también y casi al mismo tiempo, el
            miedo a que la gente de su aldea o aquellos de quienes se escondía
            pudieran estar cerca. De ninguno de esos dos grupos puedes esperar
            ayuda, precisamente…</p>
            ''',
            opciones:{"Si corres a atender al chico":"atender-nino-herido", #/98/-
                      "Si prefieres escapar":"huir-nino-herido" #/43/-
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "huir-nino-herido":{
            titulo:"Huída",
            texto:'''
            <p>Decides no arriesgarte a enfrentarte a la furia de los padres y
            amigos del chico. Crees que si te encontraran nadie te creería y
            podrías acabar como cualquier forajido, aunque te remuerde la conciencia
            el que puedas dejar al chico así ya no hay vuelta atrás.</p>
            <p>De hecho, ahora lo que te preocupa es otro grupo de gente que se
            acerca entre los árboles.</p>
            ''',
            opciones:{"Te escondes":"te-escondes-22-9-15", #
                      "Les disparas":"p-disparas-otra-vez-22-9-15", #
                      "Huyes":"huyes-conejo-22-9-15"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "te-escondes-22-9-15":{
            prueba:True,
            r:3,
            s:["descubierto-26-9-15","vuelves-a-casa-27-9-15"], #  | casa-
            },

        "vuelves-a-casa-27-9-15":{
            titulo:"Vuelves a casa",
            texto:'''
            <p>Has conseguido librarte de los que te acechaban y, tras dejar un
            tiempoprudencial, no sea que te pase nada, te alejas hacia los más
            profundo del bosque. Aquí no tienes nada que temer, salvo las incomodidades
            porque estás acostumbrado a vivir en la naturaleza. Solo que ahora
            no sabes dónde estás y te sientes como un viejo perdido
            e inútil.A cada paso que profundizas en el bosque sus sonidos familiares
            desaparecen. Te han visto, te han oído, sobre todo te han olido y
            callan esperando que te reveles como un cazador. La situación te
            alegra, porque significa que los próximos que vulneren la santidad
            de esta selva recibirán el mismo silencio delatador.</p>
            <p>Comienza así una aventura de supervivencia campo a través,
            caminando, buscando guía en el sol y en las estrellas, cazando
            cuando es necesaria, durmiendo cuando es posible, en alerta siempre.</p>
            <p>Un mes más tarde llegas ante tus tierras y lo que allí te recibe
            es una estampa de desolación. La tristeza te hace caer de rodillas
            atravesado de dolores. Porque la empalizada que protegía la
            fortaleza de tu padre está quebrada en tres partes y sobre la altiva
            torre de piedra vuela el cuervo de los vikingos, su bandera de
            sangre y noche.</p>
            ''',
            opciones:{"Buscas un lugar seguro para esconderte":"seguro-esconderte-26-9-15",
                      "Buscas a tu familia, si es que alguien ha sobrevivido.":"buscas-familia-superviviente-26-9-15"},
                      # lugar seguro | buscar familia
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "atender-nino-herido":{#98-
            titulo:"Acechante Dama",
            texto:'''
            <p>Requiere una clase de valor especial acercarse a quien has
            herido, aunque sea por error y más aún cuando la víctima es tan
            pequeña. Este es el valor que has logrado agrupar en tu corazón,
            que ahora late con fuerza. Te has arrastrado entre las sombras,
            esquivando los ojos de quienes pudieran estar cerca y, a decir
            verdad, también de los ojos del chico. Quisieras que fuera
            ciego.</p>
            <p>Pero no va a poder ser; cuando llegas junto a él, sus ojos se
            retuercen de miedo y de dolor y te ofrece sus manos en señal de
            rendición. Tú, sin una palabra, —¿qué podrías decir?—, vas al muslo
            donde se clavó la flecha que ahora yace entre hojarasca
            ensagrentada. Sangra, pero no lo suficiente para llevarle a la
            muerte esta noche. Solo estaría en peligro si se lo llevara la
            fiebre.</p>
            <p>Tus manos van a buscar vendas, que empapas en la poca miel que te
            queda. Después recuestas al niño en tu cuerpo y mientras vendas
            cantas en susurros el conjuro de tu madre, de tu abuela y de tus
            antepasados hasta los tiempos de los gigantes.</p>
            <p>Aquí llega acechando la dama,</p>
            <p>Con vendas mágicas en su mano,</p>
            <p>Dijo que eras su hijo,</p>
            <p>Con ellas viste tu muslo</p>
            <p>Con mi mano cura tu muslo</p>
            <p>Ahora tu vida a su vida fijo,</p>
            <p>Aquí el frío llega a su mano,</p>
            <p>Allá se va llorando la dama,</p>
            <p>Pues tu dolor, suyo es</p>
            <p>Y también el mío,</p>
            <p>Así fué,</p>
            <p>Así es,</p>
            <p>Así será.</p>
            <p>Amén</p>
            <p>—Dilo tú también.</p>
            <p>—Amén.</p>
            <p>Nunca has creído demasiado en esas cosas antiguas, pero lo cierto
            es que tu propio muslo te empieza a doler y eso se interpreta como
            una buena señal. En cualquier caso, todavía estáis en peligro.</p>
            ''',
            opciones:{"Intentas escabullirte entre las sombras, con el niño entre tus brazos.":"escabullirte-106", #106
                      "Te quedas aquí, con el arco preparado.":"arco-listo-115"
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "escabullirte-106":{
            "titulo":"Recoges al Niño",
            "texto":'''
            <p>Recoges al niño con delicadeza y te sumerges de nuevo en las
            sombras del bosque. ¿Te han visto? No lo sabes. ¿Se atreverán a
            atacar a un guerrero quienes antes perseguían a un niño? Tampoco. Lo
            único que te concierne es caminar rápido y suavemente, y esperar lo
            mejor.</p>
            ''',
            opciones:{"Sé sigiloso":"p-escabullirte-106"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },


        "p-escabullirte-106":{
            prueba:True,
            r:5,
            s:["116","borrachos-con-espadas-124"] #116? 124-
            },

        "116":{
            titulo:"Nueva decisión",
            texto:'''
            <p>Habéis escapado. Este bosque desconocido os ha protegido, llevandóos
            a sus más profundas sombras. En este momento no sabes exactamente dónde
            estás, pero eso no te preocupa demasiado. Sabes que eres perfectamente
            capaz de sobrevivir en este entorno y que, con el tiemo, serás capaz de
            regresar a casa.</p>
            <p>El dilema se te presenta con el niño. Está mejor pero seguro que te
            va a retrasar; lo mejor sería dejarlo con su familia, pero dudas por lo
            que pasó antes con tu flecha. Además, tampoco estás seguro de que sea
            fácil encontrarla.</p>
            ''',
            opciones:{"Llevas al niño contigo":"nino-contigo-28-9-15", #
                      "Buscas a su familia":"buscas-familia-28-9-15",}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },

        "borrachos-con-espadas-124":{
            titulo:"Borrachos con Espadas",
            texto:'''
            <p>Os han escuchado. Este bosque desconocido te ha engañado hasta
            que has perdido tu dirección para caer casi en poder del enemigo.
            Son dos hombres los que salen a por vosotros, vikingos, borrachos de
            algo más que de victoria y armados solo con viejas espadas y joven
            bravuconería. Aún así, son dos contra uno y tu tienes a un niño que
            proteger.</p>
            ''',
            opciones:{"Defiéndete":"p-borrachos-con-espadas-124"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-borrachos-con-espadas-124":{
            prueba:True,
            r:8,
            s:["borrachos-victoria-134","143"] #134- 143-
            },

        "borrachos-victoria-134":{
            titulo:"Vences",
            texto:'''
            <p>No esperan ni a que te desprendan del niño. Uno de los vikingos
            lo arriesga todo a lanzarte su espada que, como cabría esperarse,
            llega casi sin fuerza a tu armadura. Toses del golpe, pero ríes
            también. Sin arredrarse su compañero ataca, mientras el otro se
            acerca a tu espalda, haciendo ver que pretende arrebatarte el
            escudo. Lo ignoras por un instante y es todo lo que necesitas para
            que tu acero beba sangre, rajando de lado a lado la cara de su
            amigo. Contra toda razón no huye sino que te lanza piedras, pero te
            basca con una carga y una corta carrera para acabar también con su
            vida. La cerveza que antes robaran te ha ayudado en esta victoria.
            </p>
            <p>Vencidos los vikingos, sin embargo, te espera otra decisión. ¿Qué
            vas a hacer con el niño? Si lo llevas contigo seguro que te retrasaría.
            Por otro lado tampoco sabes lo que tardarías en buscar a su familia
            para dejarlo a su cuidado.</p>
            ''',
            opciones:{"Llevas al niño a su familia":"buscas-familia-28-9-15", #
                      "Vas a buscar a tu familia con el niño":"nino-contigo-28-9-15" #
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },



        "143":{
            titulo:"Suerte Asquerosa",
            texto:'''
            <p>No has durado nada. Uno de los vikingos ha aprovechado el momento
            en que te desprendías del niño para lanzarte su espada. De haber
            fallado o, como suele suceder en estos casos, haber rebotado en tu
            armadura, estaría condenado a morir, pero el filo de su arma mal
            dirigido ha mordido tu rodilla.</p>
            <p>Todavía así intentas luchar, pero pronto tu pierna cede bajo el
            dolor. Desde entonces te hacen girar, esforzándote por ganar tu
            espalda. Doce veces lo intentan y once veces los encaras, pero al
            fin un filo tenebroso atraviesa tu lumbar.</p>
            ''',
            opciones:False,
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "fallas-p-extrano-animal-arco":{ #171
            titulo:"Feliz Error",
            texto:'''
            <p>Fallas. Tu flecha se clava en un árbol donde queda temblando como
            la cuerda de una lira. Tu objetivo ahora se levanta y corre; puedes
            verlo claramente, es solo un niño. El corazón se te acelera mientras
            te debates en el alivio de haber fallado y la congoja por el crimen
            que has estado a punto de cometer. Lo sigues con la mirada y tras un
            minuto vislumbras también dos guerreros, —desde aquí no puedes decir
            que sean vikingos— que se levantan para interceptarle. Sabes que no
            tiene ninguna oportunidad, a menos que intervengas.</p>
            ''',
            opciones:{"Intentas un disparo entre las ramas":"p-disparo-ramas", #/186/?
                      "Llamas la atención de los vikingos a gritos":"gritar-vikingos", #/194/?
                      "Aprovechas para escapar":"escapar-vikingos-8" #/8/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-disparo-ramas":{
            prueba:True,
            r:2,
            s:["herido-huye-18-sep","fallo-combate"], #muerto | fallo
            },

        "herido-huye-18-sep":{
            titulo:"El dios torcido",
            texto:'''
            <p>Creen que el mismo Loki, el dios de las trampas, les ha atacado
            cuando salen corriendo, tan rápido como puede cada uno. Al que has
            herido se queda atrás y cae varias veces, pero continua levantándose
            obstinadamente hasta que al fin desaparece de tus ojos. El bosque
            ha quedado tranquilo, ni siquiera el niño se atreve a hacer un
            movimiento.</p>
            ''',
            opciones:{"Vas a socorrer al niño":"socorrer-nino-18-sep",
                      "Sigues tu camino":"escapar-vikingos-8"}, #
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False,
            },


   }
