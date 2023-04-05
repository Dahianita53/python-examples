# 1
print("#")
print("#")
print("#")

# 2
for _ in range(3):
    print("#")

# 3
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# 4 
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

# 5
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# 6 
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()

# 7
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
            print("#" * size)


main()

# 8
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
            print_row(size)

def print_row(width):
    print("#" * width)


main()
