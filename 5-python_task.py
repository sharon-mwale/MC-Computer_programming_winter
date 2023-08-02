def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

numbers_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers_list)

bubble_sort(numbers_list)
print("Sorted list:", numbers_list)
