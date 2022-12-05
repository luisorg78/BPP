try:
    fichero=open('fichero.txt','r')
    print("El fichero se ha abierto")

except IOError:
    print("No se ha encontrado el fichero o no se ha podido abrir")

else:
    fichero.close()
    print("El fichero se ha cerrado")
finally:
    print("No se ha cerrado de forma inesperada")