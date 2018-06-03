'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

'''

# writing our beautiful song lyrics
lyrics = """this is my first verse, so beautiful oh yeah

and then comes the second verse, even better oh boy

and since my song is short, the third verse wraps it up. yup."""
chorus = "yeah yeah yeah, this is a chorus, yeah yeah yeah."

# and now the programming logic to weave a song
verses = lyrics.split("\n\n")  # split the lyrics on two newlines

for v in verses:
    print(v)
    print((chorus + "\n") * 3)  # so that everyone can sing along