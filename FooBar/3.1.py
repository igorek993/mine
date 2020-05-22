def solution(x, y):
    generation = 0
    x = int(x)
    y = int(y)
    while x > 1 or y > 1:
        if x > y:
            x = x - y
            generation += 1
        elif y > x:
            y = y - x
            generation += 1
        elif x == 1 and y == 1:
            return str(generation)
        elif x == y:
            return 'impossible'



print(solution(1, 2))
