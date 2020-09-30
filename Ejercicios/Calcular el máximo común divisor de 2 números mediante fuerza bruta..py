#Calcular el máximo común divisor de 2 números mediante fuerza bruta.

#Variables
x = int(input("Número X: "))
y = int(input("Número Y: "))

#Definimos la función "mcd" con nuestras dos variables: "x" e "y".
def mcd(x, y):

#Establecemos una condición, la cuál es la siguiente: "Si "x" es menor que "y", entonces "z" es igual que "x". Sino "z" es igual que "y".
    if x < y:
        z = x
    else:
        z = y

#Mientras que "x" e "y" partido entre "z", no de como resto 0, le iremos restando 1 a "z".
    while not (x % z == 0 and y % z == 0):
        z -= 1
    else:
        return z
    
#Imprimiremos el resultado una vez lo tengamos.   
print(mcd(x, y))
