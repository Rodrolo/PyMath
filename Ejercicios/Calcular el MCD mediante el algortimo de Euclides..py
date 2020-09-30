#Calcular el MCD mediante el algortimo de Euclides.
#1.) Es m�s efectivo que el m�todo mediante fuerza bruta.

print("<==Calcular el MCD mediante el algortimo de Euclides.==>")

x = int(input("-N�mero X: ")) #Creamos un campo para insertar nuestro n�mero en la consola.
y = int(input("-N�mero Y: ")) #Creamos un campo para insertar nuestro n�mero en la consola

def euclides(x, y): #Definimos la funci�n "euclides". As� mismo indicamos "x" e "y" como variables.
    
    while True:     #Si el resto de la divisi�n entre "x" e "y" es igual a 0, entonces "y" es el MCD. Sino "x" pasa a ser "y", e "y" pasa ha ser el resto que nos daba antes.
        resto = x % y
        if resto == 0:
            return y
        else:
            x = y
            y = resto

print(euclides(x, y)) #Imprimimos el resultado final.
