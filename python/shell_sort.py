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
        outer_pos = interval

        while outer_pos < len(list_to_sort):
            value_to_insert = list_to_sort[outer_pos]
            inner_pos = outer_pos

            while inner_pos > interval - 1 and list_to_sort[inner_pos - interval] >= value_to_insert:
                list_to_sort[inner_pos] = list_to_sort[inner_pos - interval]
                inner_pos = inner_pos - interval

            list_to_sort[inner_pos] = value_to_insert
            outer_pos += 1

        interval = round((interval - 1)/3)

    return list_to_sort
