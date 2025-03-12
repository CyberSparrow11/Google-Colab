import timeit

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)
n = 500 
execution_time = timeit.timeit(lambda: recursive_factorial(n), number=10)

print("Factorial calculated!")
print("Execution time:", execution_time, "seconds")
