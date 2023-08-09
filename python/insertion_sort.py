

def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        hole_position = i
        value_to_insert = list_to_sort[i]

        while hole_position > 0 and list_to_sort[hole_position - 1] > value_to_insert:
            list_to_sort[hole_position] = list_to_sort[hole_position - 1]
            hole_position -= 1

        list_to_sort[hole_position] = value_to_insert

        print('Current list: ', list_to_sort)

    return list_to_sort
