def calculate_square(number):
    square = number ** 2

    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    return square

num1 = 5
num2 = 8

print(f"Square of {num1} is {calculate_square(num1)}")
print(f"Square of {num2} is {calculate_square(num2)}")
