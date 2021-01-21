#Sacar el mínimo común multiplo de 2 números

#Variables. Creamos dos campos donde podremos insertar los números.
x = int(input("Número X: "))
y = int(input("Número Y: "))

#Definimos la función "mcm" con nuestras dos variables: "x" e "y".
def mcm(x, y):

    if x < y: #Si "x" es menor que "y", entonces "z" es "x". Si no, lo contrario.
        z = x
    else:
        z = y

    while not (x % z == 0 and y % z == 0): #Modulo (%): resto de división.
        z -= 1
    else:
        return z
    
print(mcm(x, y))
