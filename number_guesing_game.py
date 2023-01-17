import random

def get_number():
    while True:
        try:
            user_choice = int(input('Guess the number: '))
            break
        except ValueError:
            print ("It's not a number")
    return user_choice

def guess_number():
    number = random.randint(1, 100)
    user_number = get_number()

    while user_number != number:
        if user_number < number:
            print ("too small!")
        else:
            print ("too big!")
        user_number = get_number()
    else:
        print ("You win!")

if __name__ == '__main__':
    guess_number()

