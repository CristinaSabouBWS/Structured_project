def find_index(list, start, finish, number):
    if list[finish-1] < number or list[start] > number:
            return -1
    else:
        mid =  (start + finish) // 2
        if number == list[mid]:
            return(mid)
        elif number < list[mid]:
            find_index(list, start, mid, number)
        else:
            find_index(list, mid + 1, finish, number)