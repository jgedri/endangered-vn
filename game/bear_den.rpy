image bg bedroom day = "personal room day.png"
image bg bedroom evening = "personal room evening.png"

label bear_den:
    menu:
        "Living Room":
            jump bear_den.livingroom

        "Bedroom":
            jump bear_den.bedroom

label bear_den.livingroom:
    menu:
        "Talk to Brian":
            b "How're you, Lee?"

        # "Sit on the couch":

label bear_den.bedroom:
    show bg bedroom day
label sex_scene:
    show bg bedroom evening

    "This is it: my first time. Am I nervous? You bet."
    "Then Brian's pants drop, along with my mouth."

    l "Man, you're big."

    b "I mean, I {i}am{/i} a bear."

    l "A bear who's totally blushing."