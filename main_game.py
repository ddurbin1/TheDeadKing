""" This file houses the main code of the program that will primarily call from other files. """

class character:
    def Name():
        global name
        name = input("What's your name? ")
        print("Hello {}".format(name))

    def Race():
        print("Race Types:")
        print("Human")
        print("Reptilian")
        print("Barbarian")
        print("Blob")
        global race
        race = input("What's your race? ")

class game:
    def start():
        print("Welcome to the game. It's a work in progress so don't be surprised if it's bad.")
        character.Name()
        character.Race()

    def home():
        if race.lower() == 'human':
            print("You are awoken by the sounds of war drums, pounding away.")
        else:
            print("You awake in the woods.")

game.start()
game.home()
