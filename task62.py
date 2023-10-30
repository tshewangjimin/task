user_inputs =[]
for i in range(3):
    number = int(input("enter a number:"))
    user_inputs.append(number)
    print(user_inputs)
def is_even(user_input):
    for number in user_input:
        if number % 2!=0:
            return False
            return True