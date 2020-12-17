#El título
print("<==Calcular la diferencia porcentual.==>")

#Variables
x = int(input("Valor nuevo: ")) #Campo para ingresar variable.
y = int(input("Valor antiguo: ")) #Campo para ingresar variable.
p1 = x - y #Valor antiguo menos valor nuevo (4000 - 3600).
p2 = p1 / y #Var. P1 partido del valor antiguo.
r = p2 * 100 #Var. P2 multiplicada por 100.

#Imprimimos el resultado, truncando a 2 decimales.
print("Resultado: %.2f" %r+"%")
