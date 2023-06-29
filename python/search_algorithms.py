

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
