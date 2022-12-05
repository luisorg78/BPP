from main_LRG import cuadrado, factorial, encuentra_maximo

#Tests con pytest
def test_cuadrado1():
    assert cuadrado(2)==4

def test_factorial1():
    assert factorial(3)==6

def test_factorial2():
    assert factorial(0)==1
    
def test_maximo1():
    assert encuentra_maximo(10,10.1,10.001)==10.1

def test_maximo2():
    assert encuentra_maximo(1,2,"A")=="Debes introducir números"