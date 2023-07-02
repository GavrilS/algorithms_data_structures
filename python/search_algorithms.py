

def binary_search(search_list, search_item):
    print(search_list)
    if len(search_list) == 1 and search_list[0]==search_item:
        print('The item was found in the list!')
        return
    elif len(search_list) == 0:
        print('The item was not found in the list!')
        return
    middle_index = round(len(search_list)/2) - 1
    if search_list[middle_index] == search_item:
        print('The item was found in the list!')
        return
    elif search_list[middle_index] > search_item:
        updated_list = search_list[:middle_index]
        print('Search item in the first half: ', search_list)
        binary_search(updated_list, search_item)
    else:
        updated_list = search_list[middle_index+1:]
        print('search item in the second half: ', search_list)
        binary_search(updated_list, search_item)



def interpolation_search(search_list, search_item):
    low = 0
    high = len(search_list) - 1
    mid = -1
    list_size = len(search_list)

    flag = False
    while not flag:
        print('Low: ', low)
        print('High: ', high)
        if low >= high or search_list[low] == search_list[high]:
            return -1
        
        mid = round(low + ((high - low) / (search_list[high] - search_list[low])) * (search_item - search_list[low]))
        print('Mid: ', mid)
        if mid > high or mid < low:
            return -1

        if search_list[mid] == search_item:
            return mid
        else:
            if search_list[mid] < search_item:
                low = mid + 1
            elif search_list[mid] > search_item:
                high = mid - 1
