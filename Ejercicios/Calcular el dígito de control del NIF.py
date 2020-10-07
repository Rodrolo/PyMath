#Calcular el dígito de control del NIF.

#El título
print("<==Calcular el dígito de control del NIF.==>")

#Variables
nif = int(raw_input("Introduce los 8 dígitos del NIF: ")) #Campo donde introduciremos los 8 dígitos del NIF.
letra = nif % 23

#Condición: Depende del resto que obtengamos de la división entree el NIF y 23, nos dará una letra diferente.
if letra == 0:
    print("T")
elif letra == 1:
    print("R")
elif letra == 2:
    print("W")
elif letra == 3:
    print("A")
elif letra == 4:
    print("G")
elif letra == 5:
    print("M")
elif letra == 6:
    print("Y")
elif letra == 7:
    print("F")
elif letra == 8:
    print("P")
elif letra == 9:
    print("D")
elif letra == 10:
    print("X")
elif letra == 11:
    print("B")
elif letra == 12:
    print("N")
elif letra == 13:
    print("J")
elif letra == 14:
    print("Z")
elif letra == 15:
    print("S")
elif letra == 16:
    print("Q")
elif letra == 17:
    print("V")
elif letra == 18:
    print("H")
elif letra == 19:
    print("L")
elif letra == 20:
    print("C")
elif letra == 21:
    print("K")
elif letra == 22:
    print("E")
