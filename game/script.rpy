﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bearrator = Character(None, kind=nvl, what_color="#0099ff")
define b = Character("Brian", kind=nvl, what_color="#0099ff")
define l = Character("Lee", kind=nvl, what_color="#009900", who_color="#009900")

# Define images

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg beach day

    

    # These display lines of dialogue.

    b "..."

    b "Hello there. I'm Brian."

    l "And I'm Lee, the panther."
    nvl clear

    menu (nvl=True):
        "Which story would you like to follow?"

        "Lee's":
            jump panther

        "Brian's":
            jump bear_den
    nvl clear
    
    label panther:
        l "I'm honored that you would choose little ol' me."
        l "Let's see. It all started when I came out to my mom."

        jump coming_out

    label bear:
        b "Okay then."
        nvl clear

        jump day_1
    # This ends the game.

    return
