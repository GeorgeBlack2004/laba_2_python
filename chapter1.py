def is_digit(q):
    while True:
        x = input(q)
        if x.isdigit():
            return int(x)
        else:
            print("This is not a digit. Try again")


def check(x):
    if x == 1:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


while True:
    a = 1
    b = 0
    try:
        a = int(input("Enter a lower: "))
        b = int(input("Enter a upper: "))
    except ValueError:
        print("This is not a digit!")
    finally:
        print("Values are introduced!")
    if a > b:
        print("Lower and upper are uncorrected!!!")
    else:
        break

for e in range(a, b + 1):
    if check(e):
        print(e, end=", ")
