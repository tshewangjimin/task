def find_longest_word(string):
    words = string.split()
    longest_word = max(words,key=len)
    return longest_word
    input_string = "i love programming"
    longest_word= find_longest_word(input_string)
    longest_word
