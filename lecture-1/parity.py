# 1
x = int(input("what's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

    
# 2
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()


# 3
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False

main()


# 4 
def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0 

main()