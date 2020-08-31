def pipeline(*funcs):
    def helper(arg):
        # loop through all the functions
        for func in funcs:
            # pass in the arguement for each function. updating it as we go along
            arg = func(arg)
        # return the final result
        return arg
    return helper


fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3))  # should print 5.0
