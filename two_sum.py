def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """

    numberSet=set(numbers)
    for i in numbers:
        j=target_sum-i
        if j in numberSet:
            return tuple([numbers.index(i),numbers.index(j)])
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))