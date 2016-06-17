class Player(object):

    player_stats = {'name': '',
    'hp': 10, 'attack': 4}

    def __init__(self):
        pass

    def first_time(self):
        name_input = raw_input("What is your name? ")
        Player.player_stats['name'] = name_input

    def show_stats(self):
        print "-" * \
            (len("What is your name? ") + len(self.player_stats['name']))
        print "Name: " + self.player_stats['name']
        print "Health Points: " + str(self.player_stats['hp'])
        print "Attack Damage: " + str(self.player_stats['attack'])


class Game(Player):

    def input_action(self):
        action_list = ["push"]
        for action in action_list:
            player_input = raw_input(action)

test = Player()
test.first_time()
test.show_stats()
main_game = Game()
main_game.input_action()
