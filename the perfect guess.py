import random

n = random.randint(1,100)
a = -1

guesses = 0

while(a != n):
    guesses +=1
    a = int(input("Guess the number : "))

    if(a > n):
        print("Lower number please")
  
    else:
        print("higher number please")


print(f"you have guessed the number {n} correctly in {guesses} attempts")