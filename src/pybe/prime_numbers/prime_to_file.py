# Optional 3:
# Given N <=2000 000
# print all the prime numbers up to it in a file, one on each line
# Hint. Look up how to reuse the computations

from pybe.prime_numbers.prime_list import read_number, prime_list

def write_prime_numbers():
    prime_values = prime_list(read_number())
    f = open("src/pybe/prime_numbers/output.txt","w")
    for number in prime_values:
        f.write(f"{number}\n")
        
