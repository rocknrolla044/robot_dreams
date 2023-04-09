def sum_func(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(sum_func(1, 2, 3, 4, 5, 6, 7, 8, 9))