define mc = DynamicCharacter("mcName")
define seb = Character("seburoh")

init python:
    import os
    mcName = os.environ.get("USERNAME") or "You"
    happiness = 50

screen happy_overlay:
    text("Happiness: " + str(happiness))
    # text("{=date_s}Happiness: " + str(happiness)) + "{/=date_s}"

# style date_s is text:
    # color "#657CD5"
    # size 108
style text:
    outlines [ (3, "#000", 0, 0) ] # a shadow

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
            When playing this game though, you'll have to play a bit of pretend.
            """
            seb """
            Put yourself in the shoes of somebody who's not there yet. Be that a you of the past, 
            or a friend you wish better for. This game is about that journey.
            """
        "No":
            seb """
            I may just be a faceless stranger on the internet, but I believe in you. You can accomplish
            great things if you put your mind to it. 
            """
            seb """
            If you don't already believe that, maybe by the end of this little game you'll believe the 
            same, even if just a little.
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
    window show
    scene bg wcdonalds
    show skyrim:
        zoom 0.4 xalign 0.8 yalign 0.5
    "Rolof" "Hey you, you're finally awake."
    hide skyrim 
    show skyrim
    "Rolof" "You shorted me a WcNugget you asshole. I demand a refund."
    hide skyrim
    show skyrim:
        zoom 2.0 xalign 0.5 yalign 0.5
    "Rolof" "WHERE IS YOUR MANAGER." with vpunch

    $ happiness -= 20
    $ happiness = max(happiness, 0)

    jump eveningChoice

label eveningChoice:

    scene bg bed with None

    mc """
    Man I'm fried.
    """

    menu:
        "Choose your fate my dude"

        "hang with the homies":
            scene bg friends
            seb "yeahhh buddy"
            seb "yum yum beer fun fun times"
            $ happiness += 10
        "sleep":
            scene bg bed
            seb "zzz good nap"
            $ happiness += 10
        "play games":
            scene bg game
            seb "you went up 100 levels."
            seb "sick gains!!!"
            $ happiness += 15
        "browse the cool net":
            scene bg net
            seb "what a cool net."
            $ happiness += 15
        "go 2 the gym and get ripped":
            scene bg gym
            seb "your ligaments tore."
            seb "sick gains!!!"
            $ happiness += 15
        "date people":
            scene bg date
            seb "so, drop-dead gorgeous mommy daddy,"
            seb "what do u do for a living"
            "they don't wait for a response and smoochies smooch you"
            $ happiness += 15
        "reflect on your actions and do something new":
            scene bg grad
            $ happiness += 100
            seb "Just use 7zip what are you doing."
            jump winrar
    "You gained some happy points!"
    window hide
    # scene black
    # $ renpy.pause(0.1, hard=True)
    scene bg bed
    $ renpy.pause(0.8, hard=True)
    # scene black
    # $ renpy.pause(0.05, hard=True)
    #cut to bed, jump cut to workday
    jump workDay

label winrar:
    seb """
    Now you're a hero. You've beat the whole damn game.
    """
    seb """
    We're happy you've made it, but how are you going to spend the rest of this day? 
    Maybe watch a video, maybe press refresh and start again.
    """


# # The game starts here.
# label start:
#     scene bg room
#     show eileen happy

#     seb "Hi."

#     seb """
#     My partner and I made this game over the course of three days.
#     We wanted to submit to NaNoRenO, but only found the time at the very end of the month.
#     """

#     seb """
#     We challenged ourselves to try and create something within the remaining days, finding time
#     after work and the like. This is a short title, but we hope you enjoy!
#     """

#     seb """
#     Before we put up the fourth wall, I have one question for you.
#     """

#     menu:
#         "Are you at your destination in life?"

#         "Yes":
#             seb """
#             That is so awesome to hear! I'm glad you've found a place you feel you belong.
#             When playing this game though, you'll have to play a bit of pretend. Put yourself
#             in the shoes of somebody who's not there yet. Be that a you of the past, or a friend
#             you wish better for. This game is about that journey.
#             """
#         "No":
#             seb """
#             I may just be a faceless stranger on the internet, but I believe in you. You can accomplish
#             great things if you put your mind to it. If you don't already believe that,
#             maybe by the end of this little game you'll believe the same, even if just a little.
#             """

#     #Swap from here on.
#     seb """
#     I'm getting ahead of myself though, it's nice to meet you, what's your name?
#     """

#     $ playerName = renpy.input("Name go here", length=30).strip()
#     if playerName != "":
#         $ mcName = playerName

#     seb """
#     So your name is [mcName] huh? Nice to meet you.
#     """

#     seb """
#     One more question, what's your dream job?
#     """

#     $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()
#     while dreamJob == "":
#         seb """
#         Hey now, take this seriously. Or type in vtuber, whatever floats your boat.
#         """
#         $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()

#     seb "Pokemon reference gooooo."
#     show screen happy_overlay

#     jump workDay

# label workDay:

#     scene skyrim
#     "Rolof" "Hey you, you're finally awake."
#     "Rolof" "You shorted me a WcNugget you asshole. I demand a refund."
#     "Rolof" "WHERE IS YOUR MANAGER."

#     $ happiness -= 20
#     $ happiness = max(happiness, 0)

#     jump eveningChoice

# label eveningChoice:

#     scene homelife

#     mc """
#     Man I'm fried.
#     """

#     menu:
#         "Choose your fate my dude"

#         "It is wednesday":
#             seb """
#             Don't lie to me.
#             """
#             $ happiness += 10
#         "My dude":
#             seb """
#             My duuuuude.
#             """
#             $ happiness += 15
#         "winrar":
#             seb """
#             Just use 7zip what are you doing.
#             """
#             jump winrar

#     jump workDay

# label winrar:
#     seb """
#     Now you're a hero. You've beat the whole damn game. We're happy you've made it, but
#     how are you going to spend the rest of this day? Maybe watch a video, maybe press
#     refresh and start again.
#     """

# This ends the game.
return
