""" This file houses the main code of the program that will primarily call from other files. """
from playsound import playsound
import pygame as pg
import random

pg.init()

game_display = pg.display.set_mode((800,600))
pg.display.set_caption('The Dead King')
clock = pg.time.Clock()



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
        race = input("What's your race? ").lower()

    def Dominant():
        global dom
        dom = input("Are you left handed or right? ")

    def Inventory():
        global inv, head, left_arm, right_arm, torso, legs, feet
        
        inv = {
          "head": "None",
          "left_arm": "None",
          "right_arm": "None",
          "torso": "None",
          "legs": "None",
          "feet": "None"
        }

    def Location():
        global local, main, level
        local = []
        main = local[0]
        level = local[1]

class game:
    def input():
        user = input("")
    
    def start():
        print("Welcome to the game. It's a work in progress so don't be surprised if it's bad.")
        character.Name()
        character.Race()
        character.Dominant()

    def home():
        if race == 'human':
            print("You are awoken by the sounds of war drums, pounding away.")
        else:
            print("You awake in the woods.")

    def first_comflict():
        if race == 'human':
            print("You get up and quickly throw on some basic armor. You reach for sword and march to the main living area.")
            character.Inventory()
            inv["torso"] = "Basic Armor"
            inv["legs"] = "Basic Armor"
            inv["feet"] = "Boots"
            if dom == 'right':
                inv["right_arm"] = "Basic Sword"
            elif dom == 'left':
                inv["left_arm"] = "Basic Sword"
            print("Inventory updated...")
            print(inv)
        else:
            print("test")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
    clock.tick(30)

pg.quit()
    
game.start()
game.home()
game.first_comflict()
