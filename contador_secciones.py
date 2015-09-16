from narrativa import secciones

pruebas = 0
fines = 0
for seccion in secciones:
    if seccion[0] == 'p':
        pruebas += 1
    else:
        x = secciones[seccion]
        if x['opciones'] == False:
            fines += 1

print("secciones: ", len(secciones))
print("pruebas: ",pruebas)
print("visibles: ", len(secciones) - pruebas)
print("finales: ", fines)