#Descomponer un n�mero en n�meros primos.
#1.) No insertar m�s de 10 n�meros.

print("<==Descomponer o factorizar un n�mero en n�meros primos. (Max. 10 cifras)==>") #El t�tulo. Para que quede bonito solo :)

x = int(input("-N�mero X: ")) #Creamos un campo para insertar nuestro n�mero en la consola.
        
def descomponer(x): #Definimos la funci�n "descomponer". As� mismo indicamos "x" como variable. Perd�n :)

    primos = [] #Lista donde iremos guardando los n�meros primos

    for i in range(2, x+1): #Buscamos todos los n�meros primos desde 2 hasta x+1
        while x % i == 0: #Si el resto de la divisi�n entre "x" y un n�mero primo es igual a cero significa que es divisible.
            primos.append(i) #Se insertan los divisores en la lista.
            x = x / i #Si "x" en la primera divisi�n da como resto 0, seguiremos dividiendo los cocientes mientras d� 0 como resto (ej.: 60/2 -> 30 R:0 | 30/2 -> 15 R:0)
    return primos #Vuelve a ejecutar la b�squeda cambiando de divisor (ej.: Divisor 2 -> Divisor 3).

print(descomponer(x)) #Imprimiremos el resultado final.

