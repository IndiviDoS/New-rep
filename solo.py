import random
def guess(gu):
    guess = 0
    guessed = False
    print(f"Well,{gu},I am thinking of a number between 1 and 20.")
    num = random.randint(1,20)
    while(guessed == False):
        guess += 1
        gn = int(input("Take a guess.\n"))
        if gn == num:
            print(f"Good job,{gu}! You guessed my number in {guess} guesses!")
            guessed = True
        elif gn < num:
            print("Your guess is too low.")
        elif gn > num:
            print("Your guess is too high.")
guess(input("Hello! What is your name?\n"))