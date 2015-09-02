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
            imagen_arriba:False,
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
            opciones:{"Sí":"angel-saber-mas", #/47/?
                      "No":"angel-no-saber-mas", #/133/?
                      },
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
            'opciones':{"Luchas entre los thengs.":"thengs", #170?
                        "Corres a recuperar la milicia.":"milicia",  #180-
                        "Huyes.":"huyes-batalla-conde-ian"}, #190-
            'prueba':False,
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
            opciones:{"Te das la vuelta y atacas al enemigo, esperando servir de ejemplo.":"ejemplo-milicia",
                        "Alineas las filas personalmente, tan rápido como puedes.":"milicia-filas", #-
                        "Arrebatas el estandarte del santo y lo lanzas contra el enemigo, esperando animar a tus tropas a recuperarlo":"milicia-estandarte"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
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
            r:5,
            s:["disparas-arco-victoria","disparas-arco-fallo"] # 60- 70?
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
                      "Buscas la fuerza principal.":"fuerza-principal", #/80/
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
                      "Viajas a avisar a tu familia.":"avisar-familia-16", #/16/
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
            opciones:{"Descubre la decisión del Conde":"p-avisar-ian-62"},
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
                      "Convocas a tus mejores hombres para llevar una guerra de guerrillas en el camino; mientras la milicia se ocupa del fuerte.":"guerrilla-camino-norte", #/69/?
                      },
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
                      "Esperas a la noche para intentar una salida":"salida-noturna-113", #/113/
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
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
            opciones:{"Descubre el resultado de la batalla":"p-atacar-inmediato-109"},
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
            },

        "p-atacar-inmediato-109":{
            prueba:True,
            r:3,
            s:["117","119"] # 117 119
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
            opciones:{"Ordenas un ataque inmediato":"ataque-132", #/132/?
                      "Esperáis aquí a su ataque":"esperas-ataque-137", #/137/?
                      "Te retiras en orden de combate, sin huir pero sin dejar que se acerquen":"retirada-combate-146", #/146/?
                      },
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
                      "Te escondes en el margen del camino.":"escondes-camino", #/141/?
                      "Te internas en el bosque.":"internas-bosque", #/99/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
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
                      "Si corréis para agruparos al grupo principal.":"agruparos-principal", #/46/
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
            opciones:{"El plan tradicional.":"plan-batalla-tradicional", #/68/
                      "El plan radical.":"plan-batalla-radical", #/74/
                      "Si no sabes qué decisión tomar.":"no-decision", #/85/
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:False
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
            opciones:{"Tratas de sacar la cruz de su sitio":"tomar-mi-cruz-literal", #/89/
                      "Rezas":"mi-cruz-rezar", #/91/-
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
                      "Convocas a tus mejores hombres para llevar una guerra de guerrillas en el camino; mientras la milicia se ocupa del fuerte.":"guerrilla-camino-norte", #/69/?
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
            opciones:{"Vas a investigar tú solo con el vigía.":"investigar-con-vigia", #/55/
                      "Alertas a toda la tropa.":"alerta-toda-tropa", #/56/
                      },
            prueba:False,
            imagen_arriba:"bosque.png",
            imagen_abajo:False
            },

        "investigar-con-vigia":{
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
                      "Los retrasas con tus jóvenes, para ganar tiempo a que escapen los civiles.":"operacion-dilatoria", #/58/
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
            opciones:{"Corres a la alquería con tus últimas fuerzas.":"ultimas-fuerzas-122", #/122/
                      "Te escondes como puedes tras un arbusto cercano.":"escondes-arbusto", #/181/?
                      },
            prueba:False,
            imagen_arriba:False,
            imagen_abajo:"hut.png"
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
            opciones:{"Si vas con los exploradores.":"guerreros-exploradores", #/43/
                      "Si fuerzas la marcha con una sola formación.":"guerreros-forzar-marcha", #/44/
                      },
            imagen_arriba:False,
            imagen_abajo:"escudo.png"
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
            s:["giro-espadas","muerte-milicia"]
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
            opciones:{"Sigue adelante":"oscuridad"}, #/82/
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
            opciones:{"Sigue adelante":"oscuridad"}, #/82/
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
            opciones:{"Saquearemos a los vikingos.":"14", #/14/
                      "Primero tenemos que reconstruir el fuerte.":"reconstruir-fuerte", #/114/
                      "Tenemos que explorar esta tierra. Quién sabe, igual haya caza.":"explorar-caza", #/162/
                      },
            prueba:False,
            imagen_arriba:"hut.png",
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
            opciones:{"Si corres a atender al chico":"atender-nino-herido", #/98/?
                      "Si prefieres escapar":"huir-nino-herido" #/43/?
                      },
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
            opciones:{"Intentas un disparo entre las ramas":"disparo-ramas", #/186/?
                      "Llamas la atención de los vikingos a gritos":"gritar-vikingos", #/194/?
                      "Aprovechas para escapar":"escapar-vikingos-8" #/8/?
                      },
            imagen_arriba:False,
            imagen_abajo:False
            },


   }