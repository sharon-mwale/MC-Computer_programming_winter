def find_maximum(numbers):
    if len(numbers) == 0:
        return None

    maximum = max(numbers)
    return maximum

numbers_list = [4, 9, 2, 50, 1, 10]
print("Maximum value:", find_maximum(numbers_list))
