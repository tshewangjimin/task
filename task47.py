user_name = int(input("please enter a number:"))
factorial = 1
for i in range(1,user_name +1):
    factorial *= i
    print("the factorial of", user_name, "is:", factorial)
    