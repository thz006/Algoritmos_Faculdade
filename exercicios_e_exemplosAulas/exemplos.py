num1 = int(input("num1: "))
num2 = int(input("num1: "))
num3 = int(input("num1: "))
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f"maior: {num1}, menor: {num3}")
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f"maior: {num1}, menor: {num2}")
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(f"maior: {num2}, menor: {num3}")
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f"maior: {num2}, menor: {num1}")
elif num3 > num1 and num3 > num2 and num1 > num2:
    print(f"maior: {num3}, menor: {num2}")
elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f"maior: {num3}, menor: {num1}")