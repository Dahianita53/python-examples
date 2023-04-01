# Hay muchas maneras de calcular numeros y estas son algunas 

# Esto sirve solo para calcular numeros enteros 

x = int(input("what's x? "))
y = int(input("what's y? "))

print(x + y)

# y este sirve para calcular los numeros decimales (float)

x = float(input("what's x? "))
y = float(input("what's y? "))

print(x + y)


# calcula numeros enteros

x = input("what's x? ")
y = input("what's y? ")

z = int(x) + int(y)

print(z)


# Este redondea los numeros
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round (x + y)
print(z)

# Esto es una simple division
x = float(input("what's x? "))
y = float(input("what's y? "))

z = x / y

print(z)

# Esto es una division redondeada
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round (x / y, 2)

print(z)

# Esta calculadora usa cadena f
x = float(input("what's x? "))
y = float(input("what's y? "))

z = x / y

print(f"{z:.2f}")


# calcula numeros y los devuelve al cuadrado

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()

# calcula y eleva a potencia

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)


main()

