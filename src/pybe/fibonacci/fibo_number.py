import pdb
#Print the Nth number in the Fibonacci sequence (google for rule). 0 <= N <=1 000 000
def fibonacci_recursive(number):
    if number == 0:
        return(0)
    elif number == 1:
        return(1)
    else:
        return(fibonacci_recursive(number-1) + fibonacci_recursive(number -2))

def fibonacci_iterative(number):
    fib_list = [0] * (number+1) 
    fib_list[1] = 1
    for i in range(2, number+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[number]

def read_number():
    number = int(input("Give a number greater than 0 and smaller than 1 000 000: "))
    if number < 0 or number > 1000000:
        number = int(input("You gave a number out of range. Give a number greater than 0 and smaller than 1 000 000: "))
    return(number)

def print_fibo():
    print("Fibonacci exercise")
    number = read_number()
    print(f"Recursive is simpler: {fibonacci_recursive(number)}")
    print(f"iterative is more efficient: {fibonacci_iterative(number)}")

