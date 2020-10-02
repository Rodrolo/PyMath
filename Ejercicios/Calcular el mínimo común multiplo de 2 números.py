#Sacar el m�nimo com�n multiplo de 2 n�meros

#Variables. Creamos dos campos donde podremos insertar los n�meros.
x = int(input("N�mero X: "))
y = int(input("N�mero Y: "))

#Definimos la funci�n "mcm" con nuestras dos variables: "x" e "y".
def mcm(x, y):

    if x < y:
        z = x
    else:
        z = y

    while not (x % z == 0 and y % z == 0):
        z -= 1
    else:
        return z
    
print(mcm(x, y))
