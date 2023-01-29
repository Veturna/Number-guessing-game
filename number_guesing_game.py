import random

def get_number():
    """
    Get number from user.
    Try until get correct number.
    :rtype: int
    :return: number as int
    """
    while True:
        try:
            user_choice = int(input('Guess the number: '))
            break
        except ValueError:
            print ("It's not a number")
    return user_choice

def guess_number():
    """Main code of the program"""
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

