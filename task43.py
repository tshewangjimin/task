user_name = input("please enter your name:")
vowels = ['a','e','i','o','u']
has_vowel = False
for char in user_name:
    if char.lower() in vowels:
        has_vowel= True
        break
    print("has_vowel")