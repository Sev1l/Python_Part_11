## List comprehensions
# Task 1 (Square roots)

import math
def square_roots(numbers: list):
    new_list = [math.sqrt(number)for number in numbers]
    return new_list

lines = square_roots([1,2,3,4])
for line in lines:
    print(line)
