# NOTE: filter(functionName, iterable) কিছু মান বাছাই করে (True/False দিয়ে)
# a = [10, 20, 30, 40, 50, 60]

# def highMarks(n):
#     if n >= 60:
#         return True

# print(filter(highMarks, a))
# result = list(filter(highMarks, a))
# result = list(filter(lambda n: (n >= 30), a))
# print(result)


# NOTE: map(functionName, iterable) প্রতিটি মান পরিবর্তন করে
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]


# def add(n):
#     return n + 2


# result = map(add, a)
# print(result)

# result = list(map(add, a))
# print(result)

# result = list(map(lambda n: (n + 2), a))
# print(result)

# result = list(map(lambda i, j: (i + j), a, b))
# print(result)


# NOTE: reduce(functionName, sequence)  সব মান মিলিয়ে একটাই ফলাফল বানায়
from functools import reduce

a = [1, 2, 3, 4, 5]
result = reduce(lambda i, j: i + j, a)
print(result)
