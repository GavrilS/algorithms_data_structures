"""
Shell Sort:
Knuth's Formula: h = h*3 + 1, where h is interval with initial value 1
"""


def shell_sort(list_to_sort):
    interval = 1
    while interval < len(list_to_sort)/3:
        interval = interval*3 + 1

    while interval > 0:
        print('List: ', list_to_sort)
        print('Interval: ', interval)
        inner_pos = 0
        outer_pos = inner_pos + interval
        while outer_pos < len(list_to_sort):
            if list_to_sort[inner_pos] > list_to_sort[outer_pos]:
                value_inner = list_to_sort[inner_pos]
                list_to_sort[inner_pos] = list_to_sort[outer_pos]
                list_to_sort[outer_pos] = value_inner

            inner_pos = outer_pos
            outer_pos = inner_pos + interval

        # interval = int((interval - 1)/3)
        interval = round((interval - 1)/3)

    return list_to_sort
