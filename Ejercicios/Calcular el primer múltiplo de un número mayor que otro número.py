#Calcular el primer m�ltiplo de X mayor que Y.

#El t�tulo
print("<==Calcular el primer m�ltiplo de un n�mero mayor que otro n�mero.==>")

#Variables
x = int(input("N�mero X: "))
y = int(input("N�mero Y: "))
resultado = y / x
resto = y % x
final1 = resultado * x
final2 = final1 + x

#Condici�n: si el resto es igual a 0, entonces mostraremos el cociente de la divis�n. Sino, multiplicamosel cociente de la divisi�n, y al resultado le sumaremos X
if resto == 0:
    print(resultado)
else:
    print(final2)
