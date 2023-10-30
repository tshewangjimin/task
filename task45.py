user_name= input("please enter your name:")
vowels=['a','e','i','o','u']
vowels_count = 0
for char in user_name:
    if char.lower() in vowels:
        vowels_count += 1
        print("vowels_count")