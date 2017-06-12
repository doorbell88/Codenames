#!/usr/bin/env python

"""
________________________________________________________________________________
Codenames
---------
A program to randomly generate a map for red/blue players for a codenames game.

Usage:
    python codenames.py
    python codenames.py [SIZE]
    python codenames.py [-r | --rules]
    python codenames.py [-h | --help]

Options:
    SIZE         The length of each side (the board is a square)
    -r, --rules  Show the rules
    -h, --help   Show usage

________________________________________________________________________________
Rules:
    - Players:       2-8
    - Time:          15 minutes
    - Default size:  (5x5) --> 8 words per team

    Gameplay:
        Players form two teams.  Each team has a single Spymaster, and the rest
        are Guessers.  The board is a square matrix of words that everyone can
        see.  Only the Spymasters can see the colored grid on the computer.
        Each Spymaster has several words they need their teammates to guess by
        giving one-word clues.

        There is also one Assassin word - if guessed by a team, that team loses
        immediately.

    Turn Summary:
        The Spymaster gives a one-word clue, and a number.
            (a) The number is how many codenames on the board relate to the one-
                word clue.  The teammates can guess that number of words that
                turn.  If they have guess all correct that turn, they may guess
                one additional word.
            (b) The turn is over if a neutral word or one of the other team's
                words is guessed.
            (c) If the Assassin word is guessed, the game is over and that team 
                loses the game.

    Endgame/Victory:
        The first team to guess all their words wins.
________________________________________________________________________________

"""
from time import sleep
from random import randint, choice
from termcolor import colored
import os
import sys
import signal

#----------------- SIGNAL HANDLER -------------------#
def signal_handler(signum, frame):
    os.system('tput sgr0')
    print "\n"
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)


#--------------------------------- VARIABLES -----------------------------------
# side length of board
board_size = 5

# for generating words from internal dictionary
script_location     = os.path.dirname(os.path.realpath(__file__))
codenames_words_txt = "codenames_words.txt"
codenames_wordfile  = '{}/{}'.format(script_location, codenames_words_txt)

# built-in dictionary
word_file = "/usr/share/dict/words"


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
            print '|'.join(row),
            print
            print "\t",
            print '-'*(self.size)*4 
        
        print

class Team():
    def __init__(self, color):
        global board_size
        self.color = color
        self.secretWords = ((board_size**2) - 1) / 3
    
    def randomPlacement(self, Game):
        n=0
        while n < self.secretWords:
            # choose random coordinates
            row = randint(0, board_size-1)
            col = randint(0, board_size-1)

            # if the spot is not yet chosen, place marker there
            if Game.board[row][col] == '   ':
                Game.board[row][col] = colored(' X ', self.color, 'on_'+self.color)
                n+=1            
    

#--------------------------------- FUNCTIONS -----------------------------------
def get_cmd_line_args():
    global board_size
    # get board size (if argument is given)
    if len(sys.argv) > 1:
        arg = sys.argv[1]

        #----------------------------------------------------#
        # specify board size (if arg is a number)
        try:
            board_size = abs(int(arg))
            return
        except:
            pass

        #----------------------------------------------------#
        #rules
            if arg in ['-r', '--rules']:
                display_rules()
                exit()
                
        #----------------------------------------------------#
        # usage
            if arg not in ['-r', '--rules']:
                display_usage()
                exit()

        #----------------------------------------------------#
        # usage (if argument is ill-formed or unknown)
        else:
            display_usage()
            exit()
    
def display_usage():
    os.system('clear')
    print "________________________________________________________________________________"
    print "Codenames"
    print "---------"
    print "A program to randomly generate a map for red/blue players for a codenames game."
    print ""
    print "Usage:"
    print "    python codenames.py"
    print "    python codenames.py [SIZE]"
    print "    python codenames.py [-r | --rules]"
    print "    python codenames.py [-h | --help]"
    print ""
    print "Options:"
    print "    SIZE         The length of each side (the board is a square)"
    print "    -r, --rules  Show the rules"
    print "    -h, --help   Show usage"
    print "________________________________________________________________________________"
    print

def display_rules():
    os.system('clear')
    print "________________________________________________________________________________"
    print "Rules:"
    print "    - Players:       2-8"
    print "    - Time:          15 minutes"
    print "    - Default size:  (5x5) --> 8 words per team"
    print ""
    print "    Gameplay:"
    print "        Players form two teams.  Each team has a single Spymaster, and the rest"
    print "        are Guessers.  The board is a square matrix of words that everyone can"
    print "        see.  Only the Spymasters can see the colored grid on the computer."
    print "        Each Spymaster has several words they need their teammates to guess by"
    print "        giving one-word clues."
    print ""
    print "        There is also one Assassin word - if guessed by a team, that team loses"
    print "        immediately."
    print ""
    print "    Turn Summary:"
    print "        The Spymaster gives a one-word clue, and a number."
    print "            (a) The number is how many codenames on the board relate to the one-"
    print "                word clue.  The teammates can guess that number of words that"
    print "                turn.  If they have guess all correct that turn, they may guess"
    print "                one additional word."
    print "            (b) The turn is over if a neutral word or one of the other team's"
    print "                words is guessed."
    print "            (c) If the Assassin word is guessed, the game is over and that team "
    print "                loses the game."
    print ""
    print "    Endgame/Victory:"
    print "        The first team to guess all their words wins."
    print "________________________________________________________________________________"
    print

def get_word_file():
    global codenames_wordfile
    global word_file
    # check if codenames_words.txt exists in script directory
    if os.path.isfile(codenames_wordfile):
        word_file = codenames_wordfile

def ask_to_generate():
    global word_file
    global word_list
    global words

    # clear the screen
    os.system('clear')

    # prepare to read word_file
    get_word_file()
    word_list = open(word_file).read().splitlines()
    words = []

    # ask user if they want to generate words
    print "Word file:  {}".format(word_file)
    print
    gen_words = raw_input("    --> Would you like to generate words (y?):  ")

    # if user wants to generate words, do so
    if gen_words.lower() in ['y', 'yes']:
        generate_words()
        print_word_list()

def generate_words():
    global board_size
    global words
    i=0
    while len(words) < (board_size ** 2):
        # clear the screen to refresh the list
        os.system('clear')
        print "    (Words to generate: {})".format(board_size**2)
        print "    Type 'play' to show board\n"

        # print list for words so far
        for i in range(len(words)):
            print "{:>2})  {}".format((i+1), words[i])

        # get random word that's not on list so far
        word_option = choice(word_list)
        while word_option in words:
            word_option = choice(word_list)

        # ask user if they want to use this word
        os.system('tput bold')
        number = len(words) + 1
        decision = raw_input("{:>2})  {:<20} --> (y?):  "
                             .format(number, word_option))
        os.system('tput sgr0')

        # add to word list if so
        if decision.lower() in  ['y', 'yes']:
            words.append(word_option)
        elif decision.lower() == 'play':
            show_board()

def print_word_list():
    global words
    os.system('clear')
    print "\n\n"

    for i in range(len(words)):
        number = i+1
        word   = words[i]
        print "    {:>2})  {}".format(number, word)

    print
    play = ''
    while play.lower() != 'play':
        play = raw_input("Type 'play' to show board  -->  ")

def show_board():
    # Generate the game board 
    Game = Board(board_size)

    # Create teams (Red, Blue, and the Assassin card)
    Red   = Team('red')
    Blue  = Team('blue')
    White = Team('white')
    White.secretWords = 1

    # Randomly place cards on board
    White.randomPlacement(Game)
    Blue.randomPlacement(Game)
    Red.randomPlacement(Game)

    # Display the board
    Game.display()
    exit()


#------------------------------------ MAIN -------------------------------------
#process command line arguments
get_cmd_line_args()

# ask if user would like to generate words
ask_to_generate()

# display the board and exit
show_board()
