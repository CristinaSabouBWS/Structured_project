from pybe.binary_search.index_search import find_index

# Read the number and the list and returns the index of the number in the list       
def get_index_from_file(file_name):
    # Open input.txt to read lines
    f = open(file_name, "r")

    # Read the first line to a number
    given_number = int((f.readline()))

    # Read second line to a list of strings by splitting the line
    second_line = (f.readline())
    ordered_list = second_line.split(" ")


    # Converting the list of strings to a list of integers
    for i in range(0, len(ordered_list)):
        ordered_list[i] = int(ordered_list[i])
    index_number = find_index(ordered_list, 0, len(ordered_list), given_number)
    print(f"{index_number}")
    return index_number
