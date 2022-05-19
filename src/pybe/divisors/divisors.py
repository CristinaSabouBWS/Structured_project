from pybe.fibonacci.fibo_number import read_number

#2. Find all the divisors of a number
def divisors(n):
    divisors =[1]
    for i in range(2, int(n/2) +1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def print_divisors():
    print("Divisors exercise")
    number = read_number()
    print(f"List o divisors for {number}: {divisors(number)}")