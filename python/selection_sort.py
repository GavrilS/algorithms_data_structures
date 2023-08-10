

def selection_sort(sort_list):
    print('Sort List: ', sort_list)
    min_unsorted_position = 0

    while True:
        flag = False
        current_min_value = sort_list[min_unsorted_position]
        current_position = min_unsorted_position

        for i in range(min_unsorted_position, len(sort_list)):
            if current_min_value > sort_list[i]:
                current_min_value = sort_list[i]
                current_position = i
                flag = True

        if flag:
            sort_list[current_position] = sort_list[min_unsorted_position]
            sort_list[min_unsorted_position] = current_min_value

        print('Sort List: ', sort_list)
        min_unsorted_position += 1

        if min_unsorted_position == len(sort_list):
            print('Ending loop, list is sorted!')
            break

    return sort_list
