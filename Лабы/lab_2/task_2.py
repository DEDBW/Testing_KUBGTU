from functools import lru_cache

INT32_MIN = -2**31
INT32_MAX = 2**31 - 1


@lru_cache
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


def sum_of_factorials(limit):
    total_sum = 0
    for i in range(1, limit + 1):
        fact = factorial(i)
        try:
            assert 0 <= fact < INT32_MAX, f"Overflow at factorial({i})"
        except AssertionError as e:
            print(f"Total sum of factorials up to {i}: {total_sum}")
            return e
        total_sum += fact
        print(f"Factorial of {i} is {fact}, Sum is {total_sum}")
    return total_sum

limit = int(input("Enter num\n"))
total = sum_of_factorials(limit)
print(f"Total sum of factorials up to {limit}: {total}") if not isinstance(total, Exception) else print(total)
