from pybe.binary_search.get_index import get_index_from_file
from pybe.combine_list.combine_lists import combined_sorted_list
from pybe.copy_to_file.copy_file import size_compare
from pybe.fibonacci.fibo_number import fibonacci_iterative, fibonacci_recursive
from pybe.prime_numbers.prime_list import prime_list
from pybe.fibonacci.fibo_number import fibonacci_recursive, fibonacci_iterative
from pybe.divisors.divisors import divisors
from pybe.combine_list.combine_lists import combined_sorted_list
from pybe.text_analysis.text_analysis import number_of_words



def test_binary_search():
    x = get_index_from_file("/Users/bws/work/newproject/src/pybe/binary_search/input.txt")
    assert x == 4

def test_prime_numbers():
    n = 45
    assert prime_list(45) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

def test_fibo_iterative():
    n = 5
    assert fibonacci_iterative(n) == 5

def test_fibo_recursive():
    n = 5
    assert fibonacci_recursive(n) == 5

def test_divisors():
    n = 46
    assert divisors(n) == [1, 2, 23, 46]

def test_combine_list():
    assert combined_sorted_list("/Users/bws/work/newproject/src/pybe/combine_list/input_sorted_list.txt") == [1, 3, 4, 5, 11, 30, 34, 36, 38, 44, 67, 88, 99]

def test_number_of_words():
    words = ['tuna', 'and', 'sleeping', 'our', 'humans', 'they']
    assert number_of_words(words) == 6

def test_cp_emulation():
    x = size_compare("/Users/bws/work/newproject/src/pybe/copy_to_file/text1.txt","/Users/bws/work/newproject/src/pybe/copy_to_file/text2.txt")
    assert x == 1051