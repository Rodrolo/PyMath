#Calcular el factorial de un número.
#1.) Máx. números de 9 cifras

print("<==Calcular el factorial de un número. Máx. números de 10 cifras==>")

x = int(input("-Número X: ")) #Creamos un campo para insertar nuestro número en la consola.

def factorial(x): #Definimos la función "factorial" y definimos "x" como variable.
    f = 1 #Creamos la variabe "f" para ir guardando el producto. Partimos de 1 para que al multiplicar, si pusieramos 0 darian todo el rato 0.

    for i in range(1, x+1): #Buscamos todos los números de 1 hasta x+1, debido a que esta función siempre busca hasta x-1.
        f *= i #Indicamos que "f" va ha ser igual que "f" * "i"
    return f #Volvemos ha ejecutar hasta terminar.

print(factorial(x)) #Imprimimos el resultado.
