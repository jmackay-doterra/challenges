from functools import lru_cache

class Fibonacci():

    @lru_cache(maxsize = 1000)
    def generate_fibonacci(num):
        if num == 1:
            return 0
        elif num == 2:
            return 1
        elif num > 2:
            return (Fibonacci.generate_fibonacci(num - 1) + Fibonacci.generate_fibonacci(num - 2))