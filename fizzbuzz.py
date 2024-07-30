# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

def is_multiplo(numero, multiplo)->bool:
    if numero % multiplo == 0:
        return True
    return False

for i in range(1,101):
    if is_multiplo(i,3) and is_multiplo(i,5):
        i = "fizzbuzz"
    elif is_multiplo(i,3):
        i = "fizz"
    elif is_multiplo(i,5):
        i = "buzz"
    print(i)
