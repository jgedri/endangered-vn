# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bearrator = Character(None, what_color="#0099ff")
define b = Character("Brian", what_color="#0099ff")
define l = Character("Lee", what_color="#009900")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    

    # These display lines of dialogue.

    b "..."

    b "Hello there. I'm Brian."

    l "And I'm Lee, the panther."

    menu:
        "Which story would you like to follow?"

        "Lee's":
            jump panther

        "Brian's":
            jump bear

    label panther:
        l "I'm honored that you would choose little ol' me."
        l "Let's see. It all started when I came out to my mom."

        jump coming_out

    label bear:
        b "Okay then."

        jump day_1
    # This ends the game.

    return
