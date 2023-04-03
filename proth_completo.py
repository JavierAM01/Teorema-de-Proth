"""
Fecha:  03 / 11 / 2022
Título: Teorema de Proth
Autor:  Francisco Javier Abollado
"""

from time import time
from matplotlib import pyplot as plt
import random

def jacobi(a, p):
    a = a % p
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = p % 8
            if r == 3 or r == 5:
                t = -t
        a, p = p, a
        if a % 4 == 3 and p % 4 == 3:
            t = -t
        a = a % p
    if p == 1:
        return t
    return 0

# a^((p-1)/2) mod (p)
def prueba_potencia(a, p):
    k = (p-1) // 2
    mod = pow(a,k,p)
    # ver si es -1
    mod -= p
    return mod

# encontrar un 'a' tal que: jacobi(a,p) == -1
def encontrar_a(p):
    i = 0
    a = 2
    while i < 10:  # prob. de error = 0.00097
        jac = jacobi(a, p)
        if jac == -1:
            return (True, a)
        i += 1
        a = random.randint(2,p-1) 
    return (False, a)

# comprueba si un cierto 'a' cumple el test de que: a^((p-1)/2) mod (p) = -1 mod (p)
def proth(a, p):
    mod = prueba_potencia(a, p)
    if mod == -1:
        return True
    return False

# Test que propone el teorema:
# realiza k (= 5 en este caso) pruebas para encontrar un 'a' que cumpla
# con el Tª de Proth:
# 1) Si lo encuentra: True  (100%)
# 2) Si no:           False (prob. de error = 0.03125)
def test_proth(p):
    for k in range(5):
        a = random.randint(2,p-1)
        if proth(a,p):
            return True
    return False

# Test que funciona mejor en la practica:
# 1) busca un 'a' tal que: jacobi(a,p) == -1
# 2) con ese 'a' aplica y retorna el valor de: proth(a,p)
# 3) en caso de no encontrar 'a': False
def test_rapido(p):
    _es_primo, a = encontrar_a(p)  
    if _es_primo:
        _es_primo = proth(a, p)
    return _es_primo


# primos de proth del tipo: 7*2**n + 1 (en la lista esta el 'n')
p7 = [2, 20, 92, 120, 190, 390, 432, 1804, 2256, 6614, 13496, 15494, 16696, 22386]
# compuestos de proth (+1 a los anteriores)
c7 = [n+1 for n in p7]

def pruebas_primos():
    tiempos_rapido = []
    tiempos = []
    k = 7
    print("\nTest para numeros primos, p = k*2**n + 1:")
    for n in p7:
        p = k*2**n + 1
        # test supuestamente rapido
        t = time()
        _es_primo = test_rapido(p) 
        t2 = time()
        tiempos_rapido.append(t2-t)
        # test del teorema
        t = time()
        _es_primo_2 = test_proth(p)  
        t2 = time()
        tiempos.append(t2-t)
        if _es_primo == _es_primo_2:
            print(f" (k,n) = ({k},{n}) -> {_es_primo}")
        else:
            print(f" (k,n) = ({k},{n}) -> {_es_primo} (tras 5 test no ha consegido un 'a' correcto)")
    
    x = list(range(len(p7)))
    plt.title("Primos de Proth")
    plt.xlabel("pruebas")
    plt.ylabel("tiempos")
    x2 = list(range(len(tiempos_rapido)))
    plt.plot(x, tiempos,"k-" , x2, tiempos_rapido,"b-")
    plt.legend(["aplicando teorema", "aplicando truco"])
    plt.show()

def pruebas_compuestos():
    tiempos_rapido = []
    tiempos = []
    k = 7
    print("\nTest para numeros compuestos, p = k*2**n + 1:")
    for n in c7:
        p = k*2**n + 1
        # test supuestamente rapido
        t = time()
        _es_primo, a = encontrar_a(p)  
        if _es_primo:
            _es_primo = proth(a, p)  
        t2 = time()
        tiempos_rapido.append(t2-t)
        # test del teorema
        t = time()
        _es_primo_2 = test_proth(p) 
        t2 = time()
        tiempos.append(t2-t)
        if _es_primo == _es_primo_2:
            print(f" (k,n) = ({k},{n}) -> {_es_primo}")
        else:
            print(f" (k,n) = ({k},{n}) -> {_es_primo} (tras 5 test no ha consegido un 'a' correcto)")
    
    x = list(range(len(c7)))
    plt.title("Compuestos de Proth")
    plt.xlabel("pruebas")
    plt.ylabel("tiempos")
    x2 = list(range(len(tiempos_rapido)))
    plt.plot(x, tiempos,"k-" , x2, tiempos_rapido,"b-")
    plt.legend(["aplicando teorema", "aplicando truco"])
    plt.show()


def ask_number(string):
    x = input(string)
    try:
        return int(x)
    except:
        print("Error! Introduce un numero entero positivo valido")
        return ask_number(string)
    

if __name__ == "__main__":
    
    print("\nComparar los tiempos entre la aplicación del teorema de proth tal cual, frente a hacerlo con alguna diferencia (para numeros pequeños no hay mucha diferencia), las pruebas no tardan más de 3 minutos.\n")
    
    while True:

        print("PROBAR EL TEST:")
        print(" 1) test_proth()")
        print(" 2) test_rapido()")
        print("PRUEBAS POR DEFECTO:")
        print(" 3) pruebas_primos()")
        print(" 4) pruebas_compuestos()")
        x = input(" > ")
        
        if x == "1": 
            p = ask_number("\nNumero: ")
            if test_proth(p):
                print("Es primo")
            else:
                print("Es compuesto")
        elif x == "2": 
            p = ask_number("\nNumero: ")
            if test_rapido(p):
                print("Es primo")
            else:
                print("Es compuesto")
        elif x == "3": 
            pruebas_primos()
        else: 
            pruebas_compuestos()

        x = input("\nContinuar? (y/n) \n > ")
        if x.lower() != "y":
            break