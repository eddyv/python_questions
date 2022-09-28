from collections import defaultdict
from typing import Dict

fb: Dict[int, int] = defaultdict(lambda: -1)


def fib_brute(num: int):
    if num < 0:
        return 0
    if num == 1:
        return 1
    return fib_brute(num - 1) + fib_brute(num - 2)


def fib(num: int):
    if num < 0:
        return 0
    if num == 1:
        return 1
    if fb[num] != -1:
        return fb.get(num, -1)
    else:
        fb[num] = fib(num - 1) + fib(num - 2)
        return fb[num]


if __name__ == '__main__':
    for i in range(100):
        print(fib(i))
    for i in range(100):
        print(fib_brute(i))
