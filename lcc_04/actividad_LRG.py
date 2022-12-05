#APARTADO 1

import pdb
pdb.set_trace()

def max_lista(list):
    maxi=list[0]
    for k in list:
        if k>maxi:
            maxi=k
    return maxi

lista=[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
list_maximos=[max_lista(l) for l in lista]
print(list_maximos)
'''
Indicando la orden break 11 y ejecutanto paso a paso, se observa que 
la función max_lista es llamada 3 veces, y que por tanto la ejecución
de la comprensión de lista, actúa como otro bucle for.
'''

#APARTADO 2
def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

lista=[3, 4, 8, 5, 5, 22, 13]
primos=list(filter(es_primo,lista))
print(primos)