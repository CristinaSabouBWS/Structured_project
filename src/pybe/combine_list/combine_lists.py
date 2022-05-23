
#Given a file with 2 sorted lists of integers (each list on its row), 
#print a single list with all of the elements from the input lists, such that the single list is also sorted. 
#Hint: you should not use any sort function here, but rely on the property of the inputs.
def combine(sorted_list_1, sorted_list_2):
    combined_list = []
    i = j = 0
    while i < len(sorted_list_1) and j < len(sorted_list_2):
        if sorted_list_1[i] < sorted_list_2[j]:
            combined_list.append(sorted_list_1[i])
            i +=1
        else:
            combined_list.append(sorted_list_2[j])
            j +=1
    while i < len(sorted_list_1):
        combined_list.append(sorted_list_1[i])
        i += 1
    while j < len(sorted_list_2):
        combined_list.append(sorted_list_2[j])
        j += 1
    return combined_list

def combined_sorted_list(file_name):
    f = open(file_name, "r")
    sorted_string_1 = f.readline()
    sorted_string_2 = f.readline()
    sorted_string_1 = sorted_string_1.strip()
    sorted_string_1 = sorted_string_1.split(" ")
    sorted_string_2 = sorted_string_2.split(" ")
    sorted_list_1 = []
    sorted_list_2 = []
    for i in sorted_string_1:
        sorted_list_1.append(int(i))
    for i in sorted_string_2:
        sorted_list_2.append(int(i))

    combined_list = combine(sorted_list_1, sorted_list_2)
    print(f"Combined lists: of {sorted_string_1} + {sorted_string_2}:")
    print(combined_list)
    return combined_list

