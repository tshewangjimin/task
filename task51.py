num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1

sum_of_the_numbers= 0

for current_num in range(num1, num2 +1):
    sum_of_the_numbers += current_num

print("the sum of the numbers between",num1, "and", num2, "is", sum_of_the_numbers)