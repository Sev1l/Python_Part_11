## List comprehensions
# Task 4 (Lengths)
def lengths(lists: list):
    return [len(sublist) for sublist in lists]


lists = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
print(lengths(lists))

