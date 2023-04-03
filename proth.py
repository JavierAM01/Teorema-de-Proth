"""
Fecha:  03 / 11 / 2022
Título: Teorema de Proth
Autor:  Francisco Javier Abollado
"""

import random

# a^((p-1)/2) mod (p)
def prueba_potencia(a, p):
    k = (p-1) // 2
    mod = pow(a,k,p)
    # ver si es -1
    mod -= p
    return mod


# Test del teorema:
# realiza k (= 5 en este caso) pruebas para encontrar un 'a' que cumpla
# con el Tª de Proth:
# 1) Si lo encuentra: True (100%)
# 2) Si no: False (hay una prob. de 2**(-k) de que en realidad sea primo)
#  ---> para k = 5: prob de fallo = 0.03125
def test_proth(p):
    for k in range(5):
        a = random.randint(2,p-1)
        mod = prueba_potencia(a,p)
        if mod == -1:
            return True
    return False