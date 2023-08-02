def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
num = 5
factorial = calculate_factorial(num)
print(f"The factorial of {num} is {factorial}")


def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        prev_series = fibonacci_series(n - 1)
        return prev_series + [prev_series[-1] + prev_series[-2]]
    
num_terms = 10
fib_series = fibonacci_series(num_terms)
print("Fibonacci series:", fib_series)
