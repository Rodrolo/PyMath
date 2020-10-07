#Calcular el MCD mediante el algortimo de Euclides.
#1.) Es más efectivo que el método mediante fuerza bruta.

print("<==Calcular el MCD mediante el algortimo de Euclides.==>")

x = int(input("Número X: ")) #Creamos un campo para insertar nuestro número en la consola.
y = int(input("Número Y: ")) #Creamos un campo para insertar nuestro número en la consola

def euclides(x, y): #Definimos la función "euclides". Así mismo indicamos "x" e "y" como variables.
    
    while True:     #Si el resto de la división entre "x" e "y" es igual a 0, entonces "y" es el MCD. Sino "x" pasa a ser "y", e "y" pasa ha ser el resto que nos daba antes.
        resto = x % y
        if resto == 0:
            return y
        else:
            x = y
            y = resto

print(euclides(x, y)) #Imprimimos el resultado final.

