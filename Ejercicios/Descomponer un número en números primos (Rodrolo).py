#Descomponer un número en números primos.
#1.) No insertar más de 10 números.

print("<==Descomponer o factorizar un número en números primos. (Max. 10 cifras)==>") #El título. Para que quede bonito solo :)

x = int(input("Número X: ")) #Creamos un campo para insertar nuestro número en la consola.
        
def descomponer(x): #Definimos la función "descomponer". Así mismo indicamos "x" como variable. Perdón :)

    primos = [] #Lista donde iremos guardando los números primos

    for i in range(2, x+1): #Buscamos todos los números primos desde 2 hasta x+1
        while x % i == 0: #Si el resto de la división entre "x" y un número primo es igual a cero significa que es divisible.
            primos.append(i) #Se insertan los divisores en la lista.
            x = x / i #Si "x" en la primera división da como resto 0, seguiremos dividiendo los cocientes mientras dé 0 como resto (ej.: 60/2 -> 30 R:0 | 30/2 -> 15 R:0)
    return primos #Vuelve a ejecutar la búsqueda cambiando de divisor (ej.: Divisor 2 -> Divisor 3).

print(descomponer(x)) #Imprimiremos el resultado final.

