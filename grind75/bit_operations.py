# Counting Bits
def countBits(num):
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1  # same as n // 2
        print(num)
    return count


if __name__ == '__main__':
    # AND
    n = 1 & 1
    print(n)

    # OR
    n = 1 | 0
    print(n)

    # XOR
    n = 0 ^ 1
    print(n)

    # NOT (negation)
    n = ~1
    print(n)

    # Bit shifting
    n = 1
    n = n << 1
    n = n << 1
    n = n << 1
    print(n)
    n = n >> 1
    print(n)
    print(f'----')
    print(countBits(23))
