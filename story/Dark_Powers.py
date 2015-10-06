# -*- coding: utf-8 -*-

running = True

class Game(object):
    
    def __init__(self):
        pass
    
    def prologue(self):
        prologue_text = open('prologue.txt', 'r')
        print prologue_text.read()
        prologue_text.close()
        
        

while running:
    Game().prologue()
    
    running = False
