#!/usr/bin/env python3
import os

class Console():
    def __init__(self):
        buffer_size = 40
        self.buffer = ['' for i in range(buffer_size)]
    
    def clear_screen(self):
        self.buffer = ['' for i in range(buffer_size)]

    def print(self,message):
        self.buffer.pop(0)
        self.buffer.append(message)
        self.refresh_display()

    def refresh_display(self):
        os.system("clear")
        for line in self.buffer:
            print(line)
        
    def getInteger(self,prompt=""):
        return int(input(prompt))
        #Todo: Make this actually validate input!
        invalid_input = False
        converted_input = False
        while invalid_input:
            user_input = input(prompt)
            try:
                converted_input = int(user_input)
            except ValueError:
                self.print("[Error] Please input a valid integer!")

class Game():
    def __init__(self,console,config={}):
        self.console = console
        pass
    
    def run(self):
        console = self.console
        number_of_bots = console.getInteger("Number of bots")

        bots = [ Bot() for i in range(number_of_bots)]

        game_round = 0
        alive = True 
        basket = []

        while alive:
            #Start a new round, the user always goes first

            #If the basket has items in, ask the player to recite the contents.
            if len(basket) > 0:
                print("Round {0} | What are the {1} items in the basket?".format(game_round,len(basket)))
                for item in basket:
                    user_input = input("")


def main():
    config = {} #Information about how the game should be played (AI Bots, timing waits etc)
    profile = {} #Information about the player
    
    console = Console()
    game = Game(console,config)
    
    console.print("In my grandmothers baskset | A Link-Method Pratice Game")
    console.print("------------------------------------------------------")
    results = game.run()

    #update profile with results

    pass
if __name__ == "__main__":
    main()
