define mc = DynamicCharacter("mcName")
define seb = Character("seburoh")

init python:
    import os
    mcName = os.environ.get("USERNAME") or "You"
    happiness = 50
    eveningEvents = [
        ["play HeckDiving 2 with friends", "HD2"],
        ["watch a lets play of Last of Them part II", "LoU2"],
        ["watch YoYo Hakusho", "YuYu"],
        ["watch One Piece", "1P"],
        ["reflect on your actions and do something new", "Reflect"],
        ["go 2 the gym and get ripped", "Gym"],
        ["date people", "Date"],
        ["browse the cool net", "Net"],
        ["play games", "Game"],
        ["sleep", "Sleep"],
        ["hang with the homies", "Friends"]
    ]
    eventCount = len(eveningEvents) - 1


# The game starts here.
label start:
    # scene bg room
    # show eileen happy
    scene black

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
    # scene homelife
    python:
        choices = [renpy.random.randint(0, eventCount)]
        
        ran = renpy.random.randint(0, eventCount)
        while ran == choices[0]:
            ran = renpy.random.randint(0, eventCount)
        choices.append(ran)

        ran = renpy.random.randint(0, eventCount)
        while ran == choices[0] or ran == choices[1]:
            ran = renpy.random.randint(0, eventCount)
        choices.append(ran)

    mc """
    Man I'm fried.
    """

    $ narrator("Choose your fate my dude", interact=False)
    $ result = renpy.display_menu([
        (eveningEvents[choices[0]][0], choices[0]),
        (eveningEvents[choices[1]][0], choices[1]),
        (eveningEvents[choices[2]][0], choices[2]),
        ("winrar", -1)
    ])

    if result == -1:
        seb """
            Just use 7zip what are you doing.
            """
        jump winrar
    else:
        $ renpy.jump(("eve" + eveningEvents[result][1]))

    #failsafe
    jump workDay

label night:
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

label eveYuYu:
    mc "Man his spirit gun is awesome!"
    mc "He's so lucky to be in an anime where anything can happen"
    $ happiness += 21
    jump night

label eveHD2:
    mc "Those bugs never knew what hit them!"
    $ happiness += 20
    jump night

label eveLoU2:
    mc "The visuals look so much better than the narrative is."
    mc "Kinda meh."
    $ happiness += 3
    jump night

label eve1P:
    mc "Luffy stretch long"
    mc "Luffy stretch longer"
    mc "Luffy stretch longest"
    mc "HOW LONG IS THIS"
    $ happiness += 798
    jump night

label eveFriends:
    scene bg friends
    mc "yeahhh buddy"
    mc "yum yum beer fun fun times"
    $ happiness += 10
    jump night

label eveSleep:
    scene bg bed
    mc "zzz good nap"
    $ happiness += 10
    jump night

label eveGame:
    scene bg game
    mc "you went up 100 levels."
    mc "sick gains!!!"
    $ happiness += 15
    jump night

label eveDate:
    scene bg date
    mc "so, drop-dead gorgeous mommy daddy,"
    mc "what do u do for a living"
    "they don't wait for a response and smoochies smooch you"
    $ happiness += 15
    jump night

label eveGym:
    scene bg gym
    mc "your ligaments tore."
    mc "sick gains!!!"
    $ happiness += 15
    jump night

label eveNet:
    scene bg net
    mc "what a cool net."
    $ happiness += 15
    jump night

label eveReflect:
    scene bg grad
    $ happiness += 100
    mc "Just use 7zip what are you doing."
    jump winrar
    jump night
    








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
