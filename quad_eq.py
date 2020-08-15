import math

#   Example case: Correct answer
#   Equal roots: Correct answer
#   Distinct roots: Correct answer 
def find_roots(a, b, c):
    x1 = (-b + math.sqrt(math.pow(b,2) - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(math.pow(b,2) - 4*a*c)) / (2*a)
    roots = (x1,x2)
    return roots

print(find_roots(2, 10, 8));