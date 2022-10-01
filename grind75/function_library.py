from collections import defaultdict
from typing import List, Set, Dict


# Question:
#
# Suppose you are building a library and have the following definition of a function and two methods register and
# findMatches. Register method registers a function and its argumentTypes in the library and findMatches accepts an
# input argument list and tries to find all the functions that match this input argument list.
# Note:
# If a function is marked as isVariadic=true, then the last argument can occur one or more number of times.
#
# Example:
# FuncA: [String, Integer, Integer]; isVariadic = false
# FuncB: [String, Integer]; isVariadic = true
# FuncC: [Integer]; isVariadic = true
# FuncD: [Integer, Integer]; isVariadic = true
# FuncE: [Integer, Integer, Integer]; isVariadic = false
# FuncF: [String]; isVariadic = false
# FuncG: [Integer]; isVariadic = false
#
# findMatches({String}) -> [FuncF]
# findMatches({Integer}) -> [FuncC, FuncG]
# findMatches({Integer, Integer, Integer, Integer}) -> [FuncC, FuncD]
# findMatches({Integer, Integer, Integer}) -> [FuncC, FuncD, FuncE]
# findMatches({String, Integer, Integer, Integer}) -> [FuncB]
# findMatches({String, Integer, Integer}) -> [FuncA, FuncB]
class Function:
    def __init__(self, name: str, argument_types: List[str], is_variadic: bool):
        self.name = name
        self.argument_types = argument_types
        self.is_variadic = is_variadic

    def __repr__(self):
        return self.name


class FunctionLibrary:
    def __init__(self):
        self.non_variadic_function = defaultdict(list)
        self.variadic_function = defaultdict(list)

    def register(self, function_set: Set[Function]):
        for function in function_set:
            if function.is_variadic:
                self.variadic_function[tuple(function.argument_types)].append(function)
            else:
                self.non_variadic_function[tuple(function.argument_types)].append(function)

    def find_matches(self, argument_types: List[str]):
        non_variadic = self.non_variadic_function.get(tuple(argument_types), [])
        variadic = []
        # exact match case
        variadic.extend(self.variadic_function[tuple(argument_types)])
        for i in range(len(argument_types) - 1, 0, -1):
            if argument_types[i] != argument_types[i - 1]:
                break
            variadic.extend(self.variadic_function[tuple(argument_types[:i])])
        return non_variadic + variadic


if __name__ == '__main__':
    # Test cases
    func_library = FunctionLibrary()
    func_a = Function("func_a", ["String", "Integer", "Integer"], False)
    func_b = Function("func_b", ["String", "Integer"], True)
    func_c = Function("func_c", ["Integer"], True)
    func_d = Function("func_d", ["Integer", "Integer"], True)
    func_e = Function("func_e", ["Integer", "Integer", "Integer"], False)
    func_f = Function("func_f", ["String"], False)
    func_g = Function("func_g", ["Integer"], False)

    func_library.register({func_a, func_b, func_c, func_d, func_e, func_f, func_g})
    print(func_library.find_matches(["String"]))
    print(func_library.find_matches(["Integer"]))
    print(func_library.find_matches(["Integer", "Integer", "Integer", "Integer"]))
    print(func_library.find_matches(["Integer", "Integer", "Integer"]))
    print(func_library.find_matches(["String", "Integer", "Integer", "Integer"]))
    print(func_library.find_matches(["String", "Integer", "Integer"]))
