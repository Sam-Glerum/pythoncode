import os

<<<<<<< HEAD
# import pygame

=======
>>>>>>> 9bfc5edbe9e11a6f06f1ed5acdd38c07979c7f11

class Player(object):
    """Player Class."""

    player_stats = {'name': '',
                    'hp': 10, 'attack': 4}

    def __init__(self):
        os.system('clear')
        pass

    def first_time(self):
<<<<<<< HEAD
        name_input = raw_input("What is your name? ")
        if len(name_input) > 0:
            Player.player_stats['name'] = name_input
        else:
            os.system('clear')
            print "Please enter your name"
            self.first_time()
=======
        self.name_input = raw_input("What is your name? ")
        for x in self.name_input:
            x.upper()
        Player.player_stats['name'] = self.name_input
>>>>>>> 9bfc5edbe9e11a6f06f1ed5acdd38c07979c7f11

    def show_stats(self):
        print "-" * \
            (len("What is your name? ") + len(self.player_stats['name']))
        print "Name: " + self.player_stats['name']
        print "Health Points: " + str(self.player_stats['hp'])
        print "Attack Damage: " + str(self.player_stats['attack'])
        print "-" * \
            (len("What is your name? ") + len(self.player_stats['name']))


class Game(Player):
    """Game actions and stuff."""

    def get_event(self):
        pass

    def input_action(self):
        action_list = {'curse': self.curse()}
        for action in action_list:
            player_input = raw_input()
            if player_input == action:
                print action

    def curse(self):
        print "fuck jou en je moeder!"

running = True
testobj = Player()
<<<<<<< HEAD
testobj.first_time()
os.system('clear')
testobj.show_stats()
=======
while running:
    testobj.first_time()
    testobj.show_stats()
>>>>>>> 9bfc5edbe9e11a6f06f1ed5acdd38c07979c7f11
