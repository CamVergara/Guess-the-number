import random 


def run():
    random_number = random.randint(1, 50)
    choosen_number = int(input('Choose a number from 1 to 50: '))
    attempts = 5
    while choosen_number != random_number:
        if attempts == 1:
            print('Game over :c')
            break
        if choosen_number < random_number:
            print('Choose a larger number')
            attempts -=1
        else:
            print('Choose a smaller number')
            attempts -=1
        print ("You habe " + str(attempts) + " attempts")
        choosen_number = int(input('Choose another number: '))
        if random_number == choosen_number:
            print('!Hey, you won!')
        

if __name__ == "__main__":
    run()

    