#El t�tulo
print("<==Calcular el �ndice de variaci�n.==>")

# Imprimimos el men� en pantalla
print("""
    1) Aumentar
    2) Disminuir
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona algo:")

# Seg�n lo que ingres�, c�digo diferente
if eligio=="1":
    print ("\n" * 1)
    print("Aumentar")
    x1 = float(input("Valor inicial: ")) #Campo para ingresar variable.
    y1 = float(input("Indice de variaci�n (porcentaje a aumentar): ")) #Campo para ingresar variable.
    a1 = 1 + y1/100
    r1 = x1 * a1
    print(r1)
    
elif eligio=="2":
    print ("\n" * 1)
    print("Disminuir")
    x2 = float(input("Valor inicial: ")) #Campo para ingresar variable.
    y2 = float(input("Indice de variaci�n (porcentaje a aumentar): ")) #Campo para ingresar variable.
    a2 = 1 - y2/100
    r2 = x2 * a2
    print(r2)
