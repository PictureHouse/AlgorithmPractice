#최소공배수 

import math
a, b = map(int, input().split())

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = lcm(a, b)
print(result)

