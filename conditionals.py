x = 40
color = "blue"

if x < 30:
    print(f"{x} es menor que 30")
else:
    print(f"{x} es mayor que 30")

if color == "red":
    print("El color es rojo")
elif color == "blue":
    print("El color es azul")
else:
    print("El color no es azul ni rojo")

if x > 20 and x < 50:
    print("x está entre 20 y 50")

if x == 30 or x == 40:
    print(f"Esto vale x: {x}")

if not x == 30:
    print("X es distinto de 30")
