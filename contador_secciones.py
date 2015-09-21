from narrativa import secciones

pruebas = 0
fines = 0
for seccion in secciones:
    x = secciones[seccion]
    try:
        if x['prueba']:
            pruebas += 1
        else:
            x = secciones[seccion]
            try:
                if x['opciones'] == False:
                    fines += 1
            except:
                print(x)
    except:
        print("Fallo en", seccion)

print("secciones: ", len(secciones))
print("pruebas: ",pruebas)
print("visibles: ", len(secciones) - pruebas)
print("finales: ", fines)