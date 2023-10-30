def is_even(user_input):
    for number in user_input:
        if number % 2 == 0:
            print(f"{number}is even")
        else:
                print(f"{number}is odd")