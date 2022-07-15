print("\t>< SIMPLE CALCULATOR ><")


def addition():
    n = float(input("Enter the number: "))
    ans, t = 0, 0
    while n != 0:
        ans = ans + n
        n = float(input("Enter another number (Enter 0 for Answer): "))
        t = t + 1
    return [ans, t]


def subtraction():
    print("\tSubtraction")
    n = float(input("Enter the number: "))
    ans = n
    while n != 0:
        n = float(input("Enter another number (Enter 0 for Answer): "))
        ans = ans - n
    return ans


def multiplication():
    print("\tMultiplication")
    n = float(input("Enter the number: "))
    ans = 1
    while n != 0:
        ans = ans * n
        n = float(input("Enter another number (Enter 0 for Answer): "))
    return ans


def division():
    print("\tDivision")
    n = float(input("Enter the number: "))
    ans = n
    while True:
        n = float(input("Enter another number (Enter 0 for Answer): "))
        if n == 0:
            return ans
        ans = ans / n


def remainder():
    print("\tRemainder")
    a = float(input("Enter Dividend: "))
    b = float(input("Enter Divisor: "))
    ans = a % b
    return ans


def square():
    print("\tSquare")
    n = float(input("Enter the number: "))
    ans = n ** 2
    return ans


def squareroot():
    print("\tSquare Root")
    n = float(input("Enter the number: "))
    ans = n ** (1 / 2)
    return ans


def cube():
    print("\tCube")
    n = float(input("Enter the number: "))
    ans = n ** 3
    return ans


def cuberoot():
    print("\tCube Root")
    n = float(input("Enter the number: "))
    ans = n ** (1 / 3)
    return ans


def average():
    print("\tAverage")
    a = addition()
    ans = (a[0] / a[1])
    return ans


while True:
    print("\nChoose one to proceed")
    print("'a' for addition")
    print("'s' for subtraction")
    print("'m' for multiplication")
    print("'d' for Division")
    print("'r' for Remainder")
    print("'sq' for Square")
    print("'sqr' for Square Root")
    print("'c' for Cube")
    print("'cr' for Cube Root")
    print("'av' for Average")
    print("'q' for quit")
    c = input()
    if c != 'q':
        if c == 'a':
            print("\tAddition")
            print("Sum= ", addition()[0])
        elif c == 's':
            print("Difference= ", subtraction())
        elif c == 'm':
            print("Product= ", multiplication())
        elif c == 'd':
            print("Quotient= ", division())
        elif c == 'r':
            print("Remainder= ", remainder())
        elif c == 'sq':
            print("Square= ", square())
        elif c == 'sqr':
            print("Square Root= ", squareroot())
        elif c == 'c':
            print("Cube= ", cube())
        elif c == 'cr':
            print("Cube Root= ", cuberoot())
        elif c == 'av':
            print("Average= ", average())
        else:
            print("Sorry! invalid character")
    else:
        break
