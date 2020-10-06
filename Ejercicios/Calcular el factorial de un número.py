#Calcular el factorial de un n�mero.
#1.) M�x. n�meros de 9 cifras

print("<==Calcular el factorial de un n�mero. M�x. n�meros de 10 cifras==>")

x = int(input("-N�mero X: ")) #Creamos un campo para insertar nuestro n�mero en la consola.

def factorial(x): #Definimos la funci�n "factorial" y definimos "x" como variable.
    f = 1 #Creamos la variabe "f" para ir guardando el producto. Partimos de 1 para que al multiplicar, si pusieramos 0 darian todo el rato 0.

    for i in range(1, x+1): #Buscamos todos los n�meros de 1 hasta x+1, debido a que esta funci�n siempre busca hasta x-1.
        f *= i #Indicamos que "f" va ha ser igual que "f" * "i"
    return f #Volvemos ha ejecutar hasta terminar.

print(factorial(x)) #Imprimimos el resultado.
