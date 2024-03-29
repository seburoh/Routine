define mc = DynamicCharacter("mcName")
define seb = Character("seburoh")

init python:
    import os
    mcName = os.environ.get("USERNAME") or "You"
    happiness = 50
    eveningEvents = [
    ["Play HeckDiving 2 with friends", "Those bugs never knew what hit them!", 20],
    ["Watch a lets play of Last of Them Part II", "The visuals look so much better than the narrative is. Kinda meh.", 3],
    ["Watch YoYo Hakusho", "Man his spirit gun is awesome!", "He's so lucky to be in an anime where anything can happen", 21],
    ["Watch One Piece", "Luffy stretch long", "Luffy stretch longer", "Luffy stretch longest", "Just how many episodes?", 798]
    ]
screen happy_overlay:
    text("Happiness: " + str(happiness))

# The game starts here.
label start:
    scene bg room
    show eileen happy

    seb "Hi."

    seb """
    My partner and I made this game over the course of three days.
    We wanted to submit to NaNoRenO, but only found the time at the very end of the month.
    """

    seb """
    We challenged ourselves to try and create something within the remaining days, finding time
    after work and the like. This is a short title, but we hope you enjoy!
    """

    seb """
    Before we put up the fourth wall, I have one question for you.
    """

    menu:
        "Are you at your destination in life?"

        "Yes":
            seb """
            That is so awesome to hear! I'm glad you've found a place you feel you belong.
            When playing this game though, you'll have to play a bit of pretend. Put yourself
            in the shoes of somebody who's not there yet. Be that a you of the past, or a friend
            you wish better for. This game is about that journey.
            """
        "No":
            seb """
            I may just be a faceless stranger on the internet, but I believe in you. You can accomplish
            great things if you put your mind to it. If you don't already believe that,
            maybe by the end of this little game you'll believe the same, even if just a little.
            """

    #Swap from here on.
    seb """
    I'm getting ahead of myself though, it's nice to meet you, what's your name?
    """

    $ playerName = renpy.input("Name go here", length=30).strip()
    if playerName != "":
        $ mcName = playerName

    seb """
    So your name is [mcName] huh? Nice to meet you.
    """

    seb """
    One more question, what's your dream job?
    """

    $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()
    while dreamJob == "":
        seb """
        Hey now, take this seriously. Or type in vtuber, whatever floats your boat.
        """
        $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()

    seb "Pokemon reference gooooo."
    show screen happy_overlay

    jump workDay

label workDay:

    scene skyrim
    "Rolof" "Hey you, you're finally awake."
    "Rolof" "You shorted me a WcNugget you asshole. I demand a refund."
    "Rolof" "WHERE IS YOUR MANAGER."

    $ happiness -= 20
    $ happiness = max(happiness, 0)

    jump eveningChoice

label eveningChoice:

    scene homelife
    $ choices = [renpy.random.randint(0, len(eveningEvents) - 1), 
                renpy.random.randint(0, len(eveningEvents) - 1), 
                renpy.random.randint(0, len(eveningEvents) - 1)]

    mc """
    Man I'm fried.
    """

    $ narrator("Choose your fate my dude", interact=False)
    $ result = renpy.display_menu([ (eveningEvents[choices[0]][0], choices[0]), 
        (eveningEvents[choices[1]][0], choices[1]), 
        (eveningEvents[choices[2]][0], choices[2]),
        ("winrar", -1)])

    if result == -1:
        seb """
            Just use 7zip what are you doing.
            """
        jump winrar
    else:
        python:
            theEvent = eveningEvents[choices[result]]
            for i in theEvent[1:-1]:
                renpy.say(mc, i)
            happiness += theEvent[-1]

    jump workDay

label winrar:
    seb """
    Now you're a hero. You've beat the whole damn game. We're happy you've made it, but
    how are you going to spend the rest of this day? Maybe watch a video, maybe press
    refresh and start again.
    """

# This ends the game.
return
