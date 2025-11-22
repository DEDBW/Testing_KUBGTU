import numpy as np
from functools import lru_cache
import logging

logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def f(x):
    assert -1 <= x <= 1, f"This value x = {x} not in [-1, 1]"
    return np.sin(x ** 2 + x) / (0.4 + np.cos(x ** 2))


@lru_cache
def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)

    return result * h / 3


def runge_error(I2n, In):
    return abs(I2n - In) / (2 ** 4 - 1)


a, b = -3.0, 1.0
epsilon = 0.0001
n = 2
iterations = 0

try:
    In = simpsons_rule(f, a, b, n)
    I2n = simpsons_rule(f, a, b, 2 * n)

    while runge_error(I2n, In) > epsilon:
        iterations += 1
        logging.info(f"Iteration {iterations}: n={n}, In={In}, I2n={I2n}, Error={runge_error(I2n, In)}")
        print(f"Step {iterations}, value: {I2n}")
        n *= 2
        In = I2n
        I2n = simpsons_rule(f, a, b, 2 * n)

    logging.info(f"Final value: {I2n}, iterations amount: {iterations}")
    print(f"Final value: {I2n}, iterations amount: {iterations}")

except AssertionError as e:
    logging.error(f"AssertionError occurred: {e}")
    print(f"Error: {e}")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
    print(f"Unexpected error: {e}")

