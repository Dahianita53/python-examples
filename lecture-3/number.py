# 1
x = int(input("what's x? "))
print(f"x is {x}")

# 2
try:
    x = int(input("what's x? "))
    print(f"x is {x}")

except ValueError:
    print("x is not a integer")

# 3
try:
    x = int(input("what's x? "))
    print(f"x is {x}")

except ValueError:
    print("x is not a integer")

print(f"x is {x}")

# 4 
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not a integer")
else:
    print(f"x is {x}")

# 5 
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")

# 6
while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an integer")
    
print(f"x is {x}")

# 7
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("what's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
        return x
    
main()

# 8
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass

main()
    
# 9
def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()