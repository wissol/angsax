from narrativa import secciones

pruebas = 0
for seccion in secciones:
    if seccion[0] == 'p':
        pruebas += 1

print("secciones: ", len(secciones))
print("pruebas: ",pruebas)
print("visibles: ", len(secciones) - pruebas)