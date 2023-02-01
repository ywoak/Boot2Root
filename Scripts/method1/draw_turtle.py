from turtle import *

raw = open("turtle").read().split("\n")
begin_fill()
for command in raw:
    words = command.split(" ")
    if words[0] == "Tourne":
        if words[1] == "gauche":
            left(int(words[3]))
        elif words[1] == "droite":
            right(int(words[3]))
        else:
            print("Tourne ailleurs que gauche ou droite ?")

    elif words[0] == "Avance":
        forward(int(words[1]))
    elif words[0] == "Recule":
        backward(int(words[1]))

    elif words[0] == "":
        pass
    elif words[0] == "Can":
        pass

done()