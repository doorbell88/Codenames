#!/usr/bin/env python
# CODENAMES 
"""
A program to randomly generate a map for red/blue players for a codenames game.

Usage:
    python codenames.py
    python codenames.py [size]

Options:
    [size]  The length of each side (the board is a square)

"""

from time import sleep
from random import randint, choice
from termcolor import colored
import os
import sys


#--------------------------------- VARIABLES -----------------------------------
# side length of board
board_size = 5

# for generating words from internal dictionary
most_common_words = "most_common_words.txt"
if os.path.isfile(most_common_words):
    word_file = most_common_words
else:
    word_file = "/usr/share/dict/words"

word_list = open(word_file).read().splitlines()
words = []


#---------------------------------- CLASSES ------------------------------------
class Board:
    def __init__(self, size):
        self.size = size
        
        self.board = []
        for x in range(self.size):
            self.board.append(['   '] * self.size)


    def display(self):
        os.system('clear')
        print
        print "\t",
        print '-'*(self.size)*4 
        
        for row in self.board:
            print "\t",
            #print '|',
            print '|'.join(row),
            #print '|'
            
            print
            print "\t",
            print '-'*(self.size)*4 
        
        print


class Team():
    #secretWords = 8
    def __init__(self, color):
        global board_size
        self.color = color
        self.secretWords = ((board_size**2) - 1) / 3
    
    def randomPlacement(self):
        n=0
        while n < self.secretWords:
            # choose random coordinates
            row = randint(0, board_size-1)
            col = randint(0, board_size-1)

            # if the spot is not yet chosen, place marker there
            if Game.board[row][col] == '   ':
                Game.board[row][col] = colored(' X ', self.color, 'on_'+self.color)
                #Game.board[row][col] = ' X '
                n+=1            
    

#--------------------------------- FUNCTIONS -----------------------------------
def ask_to_generate():
    global word_file
    os.system('clear')
    print "Word file:  {}".format(word_file)
    gen_words = raw_input("Would you like to generate words (y/n?):  ")
    if gen_words.lower() == 'y':
        print
        print '    (Words to generate: {})'.format(board_size**2)
        generate_words()
        print_word_list()


def generate_words():
    global board_size
    global words
    print

    i=0
    while len(words) < (board_size ** 2):
        word_option = choice(word_list)
        while word_option in words:
            word_option = choice(word_list)
        number = len(words) + 1
        decision = raw_input("{:>2})  {:<20} --> (y/n?):  "
                             .format(number, word_option))
        if decision.lower() == 'y':
            print "{:>39}{}".format("", word_option)
            words.append(word_option)


def print_word_list():
    global words
    os.system('clear')
    print

    for i in range(len(words)):
        number = i+1
        word   = words[i]
        print "    {:>2})  {}".format(number, word)

    print
    play = ''
    while play.lower() != 'play':
        play = raw_input("Type 'play' to show board  -->  ")


#------------------------------------ MAIN -------------------------------------
# get board size (if argument is given)
if len(sys.argv) > 1:
    board_size = int(sys.argv[1])


# ask if user would like to generate words
ask_to_generate()


# Generate the game board 
Game = Board(board_size)


# Create teams (Red, Blue, and the Assassin card)
Red   = Team('red')
Blue  = Team('blue')
White = Team('white')
White.secretWords = 1


# Randomly place cards on board
White.randomPlacement()
Red.randomPlacement()
Blue.randomPlacement()


# Display the board
Game.display()
