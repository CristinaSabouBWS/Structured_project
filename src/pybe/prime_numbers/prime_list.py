import math
def read_number():
    number = int(input("Give a number greater than 2 and smaller than 2 000 000: "))
    return(number)

def is_prime(value):
    square_root=round(math.sqrt(value))
    for i in range(2, square_root + 1):
        if (value % i == 0):
           return(False)
    return(True)

def prime_list(n):
    list = [2]
    for i in range(3,n):
        if is_prime(i):
            list.append(i)
    return(list)

def print_list():

    arr = prime_list(read_number())
    print(f"{arr}")
    return arr
    
