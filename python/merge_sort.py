

def mergesort(sort_list):
    print("sort list: ", sort_list)
    if len(sort_list) == 1:
        return sort_list

    middle_pos = int(len(sort_list)/2)
    end_position = len(sort_list)
    l1 = sort_list[0:middle_pos]
    l2 = sort_list[middle_pos:end_position]

    if len(l1) > 0:
        print("l1")
        l1 = mergesort(l1)
    if len(l2) > 0:
        print('l2')
        l2 = mergesort(l2)

    l3 = merge(l1, l2)
    print('L3: ', l3)
    return l3


def merge(l1, l2):
    l3 = []

    while len(l1) > 0 and len(l2) > 0:
        if l1[0] > l2[0]:
            l3.append(l2[0])
            l2.pop(0)
        else:
            l3.append(l1[0])
            l1.pop(0)

    while len(l1) > 0:
        l3.append(l1[0])
        l1.pop(0)

    while len(l2) > 0:
        l3.append(l2[0])
        l2.pop(0)

    return l3
