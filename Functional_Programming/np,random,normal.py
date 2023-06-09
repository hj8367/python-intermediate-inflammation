from functools import reduce
from multiprocessing import Pool


def sum_of_squares(sequence):
    integers = (int(x) for x in sequence if x[0] != "#")
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)


# print(sum_of_squares([0]))
# print(sum_of_squares([1]))
# print(sum_of_squares([1, 2, 3]))
# print(sum_of_squares([-1]))
# print(sum_of_squares([-1, -2, -3]))

# print(sum_of_squares(['1', '2', '3']))
# print(sum_of_squares(['-1', '-2', '-3']))
# print(sum_of_squares(['1', '2', '#100', '3']))

with Pool(5) as p:
    print(p.map(sum_of_squares, (['1', '2', '3'],
                                 ['-1', '-2', '-3'],
                                 ['1', '2', '#100', '3'],
                                 ) ))


