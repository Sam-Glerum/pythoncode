import os

import pygame


class Player(object):
    """Player Class."""

    player_stats = {'name': '',
                    'hp': 10, 'attack': 4}

    def __init__(self):
        os.system('clear')
        pass

    def first_time(self):
        name_input = raw_input("What is your name? ")
        Player.player_stats['name']  # = name_input
        return name_input

    def show_stats(self):
        print "-" * \
            (len("What is your name? ") + len(self.player_stats['name']))
        print "Name: " + self.player_stats['name']
        print "Health Points: " + str(self.player_stats['hp'])
        print "Attack Damage: " + str(self.player_stats['attack'])


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
while running:
    testobj.first_time()
