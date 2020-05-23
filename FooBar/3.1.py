# import math
#
#
# def solution(x, y):
#     generation = 0
#     x = int(x)
#     y = int(y)
#     if (x < 1 or y < 1) or (x == y):
#         return 'impossible'
#     while x > 1 or y > 1:
#         if x > y:
#             generation += math.floor(x / y)
#             x = x - y * math.floor(x / y)
#         elif y > x:
#             generation += math.floor(y / x)
#             y = y - x * math.floor(y / x)
#         elif x == 1 and y == 1:
#             return str(generation)
#     return 'impossible'

# print(solution('4', '77')) # 22
# print(solution('4', '78')) # impossible
# print(solution('80', '598453')) # 7508
# print(solution('70', '5984153')) # impossible

# def solution(x, y):
#     generation = 0
#     x = int(x)
#     y = int(y)
#     if x < 1 or y < 1:
#         return 'impossible'
#     while x > 0 or y > 0:
#         if x > y:
#             x = x - y
#             generation += 1
#         elif y > x:
#             y = y - x
#             generation += 1
#         elif x == 1 and y == 1:
#             return str(generation)
#         elif x == y:
#             return 'impossible'
#     return 'impossible'
#
#
# print(solution('70', '5984153'))


import math


# def solution(x, y):
#     generation = 0
#     x = int(x)
#     y = int(y)
#     if (x < 1 or y < 1) or (x == y):
#         return 'impossible'
#     while x >= 1 and y >= 1:
#         if x > y:
#             generation += math.floor(x / y)
#             x = x - y * math.floor(x / y)
#         elif y > x:
#             generation += math.floor(y / x)
#             y = y - x * math.floor(y / x)
#     if x == 1 or y == 1:
#         return str(generation - 1)
#     else:
#         return 'impossible'


def solution(x, y):
    if x == y:
        return 'impossible'
    generation = 0
    x, y = int(x), int(y)
    while x >= 1 and y >= 1:
        if x > y:
            generation += int(x / y)
            x = x - y * int(x / y)
        elif y > x:
            generation += int(y / x)
            y = y - x * int(y / x)
    if x == 1 or y == 1:
        return str(generation - 1)
    else:
        return 'impossible'


print(solution('5', '5'))
print(solution('2', '1'))  # 1
print(solution('4', '77'))  # 22
print(solution('4', '78'))  # impossible
print(solution('80', '598453'))  # 7508
print(solution('70', '5984153'))  # impossible
