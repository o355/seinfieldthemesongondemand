# (c) 2017, o355 under the GNU GPL 3.0 license.
# version thereisnoversiontothisprogram

import pygame
from appJar import gui
import sys

def musicButtons(btnName):
    if btnName == "1 hour of Seinfield Theme Music":
        pygame.mixer.music.load("1hour.mp3")
        pygame.mixer.music.play()
    elif btnName == "10 hours of Seinfield Theme Music":
        pygame.mixer.music.load("10hours.mp3")
        pygame.mixer.music.play()
    elif btnName == "Stop Music":
        pygame.mixer.music.stop()
    elif btnName == "Close":
        pygame.mixer.music.stop()
        sys.exit()
app = gui()
pygame.mixer.init()
app.addButton("1 hour of Seinfield Theme Music", musicButtons)
app.addButton("10 hours of Seinfield Theme Music", musicButtons)
app.addButton("Stop Music", musicButtons)
app.addButton("Close", musicButtons)

app.go()
