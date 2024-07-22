from typing import Callable

# Returns function, which will calculate n'th Fibonacci number, using cache under the hood
def caching_fibonacci() -> Callable[[],int]:
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0: return 0
        elif n == 1: return 1
        elif n in cache: return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    try:
        n = int(input("Input index of fibonacci number you'd like to find out >>> "))
        calculate_fibonacci = caching_fibonacci()
        print(f"Fibbonacci {n}'th number is {calculate_fibonacci(10)}")
    except:
        print("Something went wrong with calculation. Make sure you input a number and its not very big")