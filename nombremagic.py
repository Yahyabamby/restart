import random


def nombre_magic(nb_min, nb_max, ):
    nb_int = 0

    while nb_int == 0:
        nb_str = input(f"Please enter the number between {nb_min} , {nb_max}: ")
        try:
            nb_int = int(nb_str)
        except:
            print("ERROR: You should enter an integer number")
        else:
            if nb_int < nb_min or nb_int > nb_max:
                print(f"Error: The number should be between {nb_min} & {nb_max} ")
                nb_int = 0
    return nb_int


def recommencer():
    while True:
        rest = input("Would you like to restart the game? (1 for Yes, 2 for No): ")
        if rest == '1':
            return True
        elif rest == '2':
            print("Thank you for playing! See you later ")
            return False
        else:
            print("Please: You should enter 1 or 2.")


def jouer():
    nb_min = 1
    nb_max = 100
    nb_magic = random.randint(nb_min, nb_max)
    nb_lifes = 3
    nbre = 0
    lifes = nb_lifes
    while not nbre == nb_magic and lifes > 0:
        print(f"You have  {lifes} lifes")
        nbre = nombre_magic(nb_min, nb_max)
        if nbre > nb_magic:
            print("The magic number is more smaller")
            lifes -= 1
        elif nbre < nb_magic:
            print("The magic number is more larger")
            lifes -= 1
        else:
            print("Congrat !! You win  !")
    if lifes == 0:
        print(f"You lost ; The magic number was {nb_magic}")


while True:
    jouer()
    if not recommencer():
        break
