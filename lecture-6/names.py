#1 
name = input("what's your name? ")
print(f"hello, {name}")

#2
"""lo que hace este ejercicio es que guarda los nombres que pones 
y despues pones code names.txt y hay se crea un archivo e imprimen los 
nombres que ya escribiste antes"""

name = input("what's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

#3 
"""lo que hace este ejercicio es que guarda los nombres que pones 
y despues pones vas a names.txt y hay se imprimen los nombres que vas escribiendo"""

name = input("what's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

#4 
"""lo que hace este ejemplo es que va a saludar a todos los nombres que estan en el names.txt
y se ejecuta con python3 names.py"""

with open("names.txt", "r") as file:
    lines= file.readlines()

for line in lines:
    print("hello,", line)

#5
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")

#6 
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
