num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

sum_of_numbers= 0
current_number = num1
while current_number <= num2:
    sum_of_numbers += current_number
    current_number += 1
    print("the sum of all numbers between", num1, "and", num2, "is:",sum_of_numbers)