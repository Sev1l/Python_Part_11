##Recursion
# Task 2 (Recursive sum)

def recursive_sum(number: int):
    if number <= 1:
        return number
    summ = number
    summ += recursive_sum(number-1)
    return summ


result = recursive_sum(3)
print(result)

print(recursive_sum(5))
print(recursive_sum(10))
