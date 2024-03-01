# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define b = Character("Brian")
define l = Character("Lee")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

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


    label bear:
        b "Okay then."
    # This ends the game.

    return
