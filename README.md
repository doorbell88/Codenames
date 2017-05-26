# codenames
simulates the popular "Codenames" board game

    Usage:
        python codenames.py
        python codenames.py [size]

    Options:
        [size]  The length of each side (the board is a square)

this script uses the default list of words at the location:

/usr/share/dict/words

However, if you put a text file named "most_common_words.txt" in the same directory as where you run the script from, it will use this instead.

the file in this repo ("most_common_words.txt") was taken from the github repo:

https://github.com/first20hours/google-10000-english/blob/master/20k.txt
