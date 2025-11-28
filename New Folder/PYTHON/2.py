from numpy import *

"""
roll = array([101, 102, 103, 104, 105])
for element in roll:
    print(element)
print(len(roll))"""


""" # linspace() Function
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
a = linspace(1, 8)
a = linspace(1, 8, num=5)
a = linspace(1, 8, 5)
for i in a:
    print(i, end=" ")
print()
a = linspace(1, 8, 5, endpoint=False)
for i in a:
    print(i, end=" ")
print() """


""" # logspace() function
# numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
a = logspace(1, 3)
a = logspace(1, 3, 5)
print(a) """


""" # arange() function
# numpy.arange(start, stop, stepsize, dtype=None)
a = arange(5)
print(a)
a = arange(1, 6.0)
print(a)
a = arange(1, 10, 2)
print(a) """


""" # zeros() function
# numpy.zeros(shape, dtype=float, order="C")
a = zeros(5)
print(a)
a = zeros(5, dtype=int)
print(a) """


""" # ones() function
# numpy.ones(shape, dtype=float, order="C")
a = ones(5)
print(a)
a = ones(5, dtype=int)
print(a) """


""" # mathematical operations on array using numpy
# a = array([100, 200, 300, 400, 500])
# b = array([1, 2, 3, 0, 1000])
# a = a + 5
# a = a - 5
# a = a * 5
# a = a / 5
# print(a)

# c = a + b
# c = a == b
# c = a < b
# c = a > b
# print(c)

# all(), any() function
# c = a > b
# c = a < b
# print(any(c), all(c))

# where() function
# result = where(a > b, a, b)
# print(result)

# nonzero() function
# c = nonzero(b)
# print(c)

# aliasing array
# x = array([1, 2, 3, 4, 5])
# y = array([1, 2, 3, 4, 5])
# print("a", id(a))
# print("b", id(b))

# view() method --> memory share
# x = array([1, 2, 3, 4, 5])
# y = x.view()
# x[1] = 20
# y[2] = 30
# print("x", x, id(x))
# print("y", y, id(y))

# copy() method --> memory not share
# x = array([1, 2, 3, 4, 5])
# y = copy(x)
# x[1] = 20
# y[2] = 30
# print("x", x, id(x))
# print("y", y, id(y))

# getting input from user in numpy
# n = int(input("Enter number of elements :: "))
# a = zeros(n, dtype=int)
# for i in range(n):
#     x = int(input())
#     a[i] = x
# print(a) """


# multi dimensional array
