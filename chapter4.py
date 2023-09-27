a = int(input("Enter digit number one: "))
b = int(input("Enter digit number two: "))

try:
    c = a / b
    print(f"Answer: {c}")
except ZeroDivisionError:
    print("Impossible")
finally:
    print("End the program")
