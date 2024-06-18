import math_ops

num1 = 5
num2 = 6

result_add = math_ops.add(num1, num2)

print(result_add)

result_subtract = math_ops.subtract(num1, num2)

print(result_subtract)

#  Another way to import
print("--------")
from math_ops import add, subtract
result_add = add(num1, num2)
print(result_add)


# Python's predefined moduless
print("------")
import math, random

num1 = math.pow(3,4)
print(num1)

num2 = math.sqrt(64)
print(num2)

randValue = random.randrange(1, 10)
print(randValue)