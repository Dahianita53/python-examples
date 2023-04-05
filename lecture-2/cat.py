# 1
print("meow")
print("meow")
print("meow")

# 2
i = 3
while i != 0:
    print("meow")
    i = i - 1
    i = 3

# 3
i = 0
while i <= 3:
    print("meow")
    i = i + 1
    
# 4
i = 0
while i < 3:
    print("meow")
    i = i + 1
    
# 5 
i = 0
while i < 3:
    print("meow")
    i += 1

# 6
for i in [0, 1, 2]:
    print("meow")

# 7
for i in range(3):
    print("meow")

# 8 
for _ in range(3):
    print("meow")

# 9
print("meow\n" * 3, end="")

# 10
while True:
    n = int(input("what's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# 11
def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("meow")

main()