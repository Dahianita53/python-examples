# 1 
def main():
    heigth = int(input("Height: "))
    pyramid(heigth)

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

if __name__ == "__main__":
    main()
