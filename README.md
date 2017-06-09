# codenames
simulates the popular "Codenames" board game

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


This script uses the default list of words at the location:

/usr/share/dict/words

However, if you put a text file named "codenames_words.txt" in the same directory as the script, it will use this instead.

The file in this repo ("codenames_words.txt") was taken from the github repo:

https://github.com/first20hours/google-10000-english/blob/master/20k.txt
