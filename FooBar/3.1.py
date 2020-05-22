def solution(x, y):
    generation = 0
    tuple_to_find = (x, y)
    current_list = [['1', '1']]
    while generation < int(x) and generation < int(y):
        generation += 1
        new_list = get_next_list(current_list)
        if compare_list(new_list, tuple_to_find):
            return str(generation)
        else:
            current_list = new_list
            new_list = list()
    else:
        return 'impossible'


def compare_list(_list, tuple_to_compare):
    return True if tuple_to_compare in _list or tuple_to_compare[::-1] in _list else False


def get_next_list(current_list):
    new_list = list()
    for _list in current_list:
        position = 1
        for digit in _list:
            new_list.append((str(int(digit) + int(_list[position])), str(int(_list[position]))))
            position = position - 1
    return new_list


print(solution('2', '4'))
