def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = "".join(reversed_words)
    return reversed-string
    input_string = "hello ,world!"
    reversed_string = reverse_words(input_string)
    print(reversed_string)