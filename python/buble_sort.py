

def buble_sort(list_to_sort):
    while True:
        swapped = False

        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                swap(list_to_sort, i, i+1)
                swapped = True

        print(list_to_sort)
        if not swapped:
            break

    return list_to_sort


def swap(list_to_sort, low_index, high_index):
    low_index_elem = list_to_sort[low_index]
    list_to_sort[low_index] = list_to_sort[high_index]
    list_to_sort[high_index] = low_index_elem
