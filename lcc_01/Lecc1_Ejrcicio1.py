'''
1. Crea una funcion que pida por pantalla un número al usuario y que 
controle mediante excepciones lo siguiente:
a. Solo se podrá introducir numeros enteros
b. Si el numero es mayor de 10 lanza una excepción con raise la 
cual hayas creado previamente mediante ‘class 
Miexcepcion(Exception):’
'''
def mi_funcion(n):
    class valor_mayor_10(Exception):
        pass
    
    try:
        n=int(n)
        if n>10:
            raise valor_mayor_10
    except ValueError as err:
        print("El número debe ser un entero: ", err)
    except valor_mayor_10:
        print("El número debe ser <=10")
    
    else:
        print("Has introduzido el número: ", n)
    finally:
        print("La función se ha completado sin interrupciones")
entrada=input("Inroduce un número entero menor que 10 :")
mi_funcion(entrada)

   
