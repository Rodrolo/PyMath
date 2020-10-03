#Calcular el primer múltiplo de X mayor que Y.

#El título
print("<==Calcular el primer múltiplo de un número mayor que otro número.==>")

#Variables
x = int(input("Número X: "))
y = int(input("Número Y: "))
resultado = y / x
resto = y % x
final1 = resultado * x
final2 = final1 + x

#Condición: si el resto es igual a 0, entonces mostraremos el cociente de la divisón. Sino, multiplicamosel cociente de la división, y al resultado le sumaremos X
if resto == 0:
    print(resultado)
else:
    print(final2)
