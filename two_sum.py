def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    seen = {}
    for i, num in enumerate(numbers):
        try:
            #If we reached this point, then we know where the index would be for seen[num] + seen[target_sum-num]
            return (seen[num], i)
        except KeyError:
            #Add the index to the list of seen indexes for this number
            seen[target_sum-num] = i
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))