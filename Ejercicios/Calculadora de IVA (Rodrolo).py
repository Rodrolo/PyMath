#El título
print("<==Calculadora de IVA.==>")

# Imprimimos el menú en pantalla
print("""
    1) Añadir
    2) Quitar
    3) Calcular
    """)

# Leemos lo que ingresa el usuario
eligio=input("-Selecciona algo:")

# Según lo que ingresó, código diferente
if eligio=="1":
    print ("\n" * 1)
    print("Añadir")
    x1 = float(input("Valor inicial: ")) #Campo para ingresar variable.
    i1 = 1.21
    c1 = x1 * i1
    r1 = round(c1, 2)
    print(r1)
    
elif eligio=="2":
    print ("\n" * 1)
    print("Quitar")
    x2 = float(input("Valor inicial: ")) #Campo para ingresar variable.
    i2 = 1.21
    c2 = x2 / i2
    r2 = round(c2, 2)
    print(r2)

elif eligio=="3":
    print ("\n" * 1)
    print("Calcular")
    x3 = float(input("Valor inicial: ")) #Campo para ingresar variable.
    i3 = 0.21
    c3 = x3 * i3
    r3 = round(c3, 2)
    print(r3)
