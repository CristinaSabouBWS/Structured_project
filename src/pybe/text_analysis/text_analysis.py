#Given a piece of text( article), extract the following: read from file
#How many words are there in total - oly words with 3+ char, split by space, remove all puctuation
#How many unique words are there - use dictionary
#What are the top 5 words that appear in the text ? What are their number of appearances?
#Print all phone numbers - ro mobile phone numbers

# Read about Regex. There's a nice cheatsheet interactive website https://pythrex.org where you can figure out how that works roughly.
# Implement the words analysis prblem from yesterday with regex too (this won't exclude the original non-regex assignment)


#Read a line, transform it and save it as a list of strings
def read_file():
    f = open("input.txt", "r")

    # Read all file in an list of lines
    lines = f.readlines()

    #Define characters that have a space after (asumption)
    char1 = [".", ",", ";", "?", "!"]                                                       #how to remove the \n from lines? mandatory to fix for word_occurance to work as expected
    #Define characters that should be replaced with a space                                 #will add a "" to the list when 2 spaces and not remove when <3 char
    char2 = ["-", "_", "+", "/", "*", "\"", "'"]

    line_counter = -1  #to count the lines read from file
    for line in lines: #for each line in array
        line_counter +=1
        for character in line:  #for each character in the line
            if character in char1:
                line = line.replace(character,"")
            elif character in char2:
                line = line.replace(character," ")

        line = line.split(" ") #line is now a list of words
        # remove words <3 char                                                              # do remove numbers?
        for word in line:
            if len(word) < 3:                                                               #see why 'a' is not removed - affects word_occurance
                line.remove(word)

        lines[line_counter] = line #replace curent lines with the updated lists of words
    print(lines)
    return lines


def number_of_words(arr):
    count = 0
    for line in arr:
        for word in line:
            if len(word) > 2:                                                               #keep for now, but remove when 'a' is dealt with (the index is skiped)
                count += 1
    print(f"How many words are there in total? {count}") 

def words_occurance(arr):                                                                   # counts the "a" error!
    word_counter= {}
    for line in arr:
        for word in line:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
    print(word_counter)
    return word_counter

def unique_words(dict):
    unique_words_counter = 0
    for i in dict:
        if dict[i] == 1:
            unique_words_counter +=1 
    print(f"unique words: {unique_words_counter}")

#assume the values don't matter. Re-do for categories print
def top_five_words(dict):
    print("top 5 words:")
    marklist = sorted(dict.items(), key=lambda x:x[1], reverse = True)                              #read more on use
    for i in range(0, 5):
        print(marklist[i])

    
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
        
#assume phone numbers are one word
def print_phone_numbers(arr):
    print("phone numbers in text:")
    count = 0
    for line in arr:
        for word in line:
            if all_10_numbers(word):
                print(word)
                count +=1
    if count == 0:
        print("no phone nb")




# if __name__ == "__main__" :

#     list_of_lines_of_words = read_file()
#     number_of_words(list_of_lines_of_words)
#     z = words_occurance(list_of_lines_of_words)
#     unique_words(z)
#     top_five_words(z)
#     print_phone_numbers(list_of_lines_of_words)