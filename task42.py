user_name = input("please enter your name:")
vowels = ['a','e','i','o','u']
has_vowel = False
counter = 0
while counter < len(user_name):
    if user_name[counter].lower() in vowels:
        has_vowel = True
        break
    counter += 1
    print("has_vowel")