import random
secret_number = random.randint(1,100)
for _ in range(3):
    guess= int(input("take a guess:"))
if guess< secret_number:
    print("too low!")
elif guess> secret_number:
    print("too high!")
else:
    print("congratulations! your guessed the secret number correctly!")