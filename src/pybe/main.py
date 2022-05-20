from pybe.binary_search.get_index import get_index_from_file
from pybe.prime_numbers.prime_list import print_list
from pybe.prime_numbers.prime_to_file import write_prime_numbers
from pybe.fibonacci.fibo_number import print_fibo
from pybe.divisors.divisors import print_divisors
from pybe.combine_list.combine_lists import combined_sorted_list
from pybe.text_analysis.text_analysis import print_phone_numbers, read_file, number_of_words, top_five_words, words_occurance, unique_words
from pybe.copy_to_file.copy_file import copy_function, size_compare
# #Binary search
# x = get_index_from_file("/Users/bws/work/newproject/src/pybe/binary_search/input.txt")

# #Prime numbers < N
# primeList = print_list()

# #Print the Nth number in the Fibonacci sequence
# print_fibo()

# #Find all the divisors of a number
# print_divisors()

# #Given a file with 2 sorted lists of integers (each list on its row) 
# # Print a single list with all of the elements from the input lists, such that the single list is also sorted.
# combined_sorted_list("/Users/bws/work/newproject/src/pybe/combine_list/input_sorted_list.txt")

#Print all the prime numbers up to it in a file, one on each line
#write_prime_numbers("/Users/bws/work/newproject/src/pybe/prime_numbers/output.txt")

# ex 3 from https://docs.google.com/document/d/1UBtgp_JiR_EuUlas925mu7QAAJCG1YkxFN5waQ7fOII/edit#
# word_count = number_of_words(read_file("/Users/bws/work/newproject/src/pybe/text_analysis/text_article.txt"))
# occurace_dict= words_occurance(read_file("/Users/bws/work/newproject/src/pybe/text_analysis/text_article.txt"))
# unique_words = unique_words(occurace_dict)
# top_5 = top_five_words(occurace_dict)
# phone_count = print_phone_numbers(read_file("/Users/bws/work/newproject/src/pybe/text_analysis/text_article.txt"))

size = size_compare("/Users/bws/work/newproject/src/pybe/copy_to_file/text1.txt","/Users/bws/work/newproject/src/pybe/copy_to_file/text2.txt")

