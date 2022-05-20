#Given a piece of text( article), extract the following: read from file
#How many words are there in total - oly words with 3+ char, split by space, remove all puctuation
#How many unique words are there - use dictionary
#What are the top 5 words that appear in the text ? What are their number of appearances?
#Print all phone numbers - ro mobile phone numbers

# Read about Regex. There's a nice cheatsheet interactive website https://pythrex.org where you can figure out how that works roughly.
# Implement the words analysis prblem from yesterday with regex too (this won't exclude the original non-regex assignment)


#Read a line, transform it and save it as a list of strings
def read_file(file_name):
    f = open(file_name, "r")

    # Read all file in an list of lines
    read_text = f.read()
    
    #Define characters that have a space after (asumption)
    char_to_remove = [".", ",", ";", "?", "!"]                                                      
    #Define characters that should be replaced with a space                                
    char_to_replace = ["-", "_", "+", "/", "*", "\"", "'"]

    #read_text = read_text.rstrip()
    
    for character in read_text:
        if character in char_to_remove:
            read_text = read_text.replace(character,"")
        elif character in char_to_replace:
            read_text = read_text.replace(character," ")
    
    read_text = read_text.split(" ") #line is now a list of words
    
    # remove words <3 char   
    final_word_list = []                                                           
    for word in read_text:
        if len(word) >= 3:                                                               
            final_word_list.append(word)
    
    return final_word_list


def number_of_words(arr):
    words_count = len(arr)
    print(f"How many words are there in total? {words_count}") 
    return words_count

def words_occurance(arr):                                                                   # counts the "a" error!
    word_counter= {}
    for word in arr:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter

def unique_words(dict):
    unique_words_counter = 0
    for i in dict:
        if dict[i] == 1:
            unique_words_counter +=1 
    print(f"unique words: {unique_words_counter}")
    return unique_words_counter

# assume the values don't matter. Re-do for categories print
def top_five_words(dict):
    print("top 5 words:")
    marklist = sorted(dict.items(), key=lambda x:x[1], reverse = True)                              #read more on use
    for i in range(0, 5):
        print(marklist[i])
    return marklist

    
def all_10_numbers(word):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    count = 0
    for i in word:
        if i in numbers:
            count += 1
    if count == 10:
        return True
    else: 
        return False
        
# #assume phone numbers are one word
def print_phone_numbers(arr):
    print("phone numbers in text:")
    count = 0

    for word in arr:
        if all_10_numbers(word):
            print(word)
            count +=1
    if count == 0:
        print("no phone nb")
    return count
