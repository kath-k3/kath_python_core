# the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
#Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print (letter + "u" + suffix)
    else:
        print (letter + suffix)


