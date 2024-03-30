###POINTER###
define config.mouse = {
    "default" : [("gui/mouse_default.png", 16, 0)]
    }
init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('mouseup_3')
    import os
    config.debug_sound = False
    renpy.music.register_channel("blip", mixer= "voice")
    def everyonevoice(event, interact=True, **kwargs):
        if not interact:
                return
        if event == "show":
            renpy.music.play("blippies.ogg", channel="blip", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="blip", fadeout=.1)   
    mc = DynamicCharacter("mcName", what_prefix="\"", what_suffix="\"", callback=everyonevoice)
    seb = Character("seb", callback=everyonevoice)
    car = Character("carmints", callback=everyonevoice)

    preferences.text_cps = 50  
    # config.all_character_callbacks = everyonevoice
    mcName = os.environ.get("USERNAME") or "You"
    happiness = 50
    dayCount = 1
    eveningEvents = [
        ["play HeckDiving 2 with friends", "HD2"],
        ["watch a lets play of Last of Them part II", "LoU2"],
        ["watch YoYo Hakusho", "YuYu"],
        ["watch One Piece", "1P"],
        ["go 2 the gym and get ripped", "Gym"],
        ["date people", "Date"],
        ["browse the cool net", "Net"],
        ["play games", "Game"],
        ["sleep", "Sleep"],
        ["hang with the homies", "Friends"]
    ]
    eventCount = len(eveningEvents) - 1

    winEvents = [
        ["reflect and do something new", "Reflect"],
        ["schedule some time with a career advisor", "Advise"]
    ]
    winCount = len(winEvents) - 1

    dayEvents = [
        "Skyrim",
        "Raise",
        "Turkey",
        "Clopen",
        "Downsize",
        "Lunch",
        "Promotion"
    ]
    dayEventsLen = len(dayEvents) - 1


# The game starts here.
label start:
    play music "choices.ogg"
    scene black

    seb "Hi."

    seb """
    My partner and I made this game over the course of three days.
    We wanted to submit to NaNoRenO, but only found the time at the very end of the month.
    """
    
    car "uwu"

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

    stop music fadeout 1.5
        
    seb "A [dreamJob] huh? That sounds pretty cool. I bet you'd be pretty good at it too."

    $ dreamLower = dreamJob.lower()
    if dreamLower == "vtuber":
        seb "The next KSon maybe?"

    seb "Well that's enough talking out of me, maybe I'll see you again sometime."

    show wall:
        ypos 1200

    show wall with move:
        ypos 800

    seb "Sorry, one minute, need to put up the fourth wall."

    show wall with move:
        ypos 400

    $ renpy.pause(0.8, hard=True)

    show wall with move:
        ypos 0

    seb "Much better."

    show wallbroke
    hide wall

    seb "I know, I know, it's a pretty silly looking wall, but man I tried. What matters is I put in the effort."

    seb "Never be afraid to try something new! You never know what you may find!"

    seb "...oh, I need to fix this wall now, huh."

    window hide
    show wallfixing
    hide wallbroke

    $ renpy.pause(0.8, hard=True)

    show wallfixed
    hide wallfixing
    show wallfixed 
    # $ renpy.pause(3, hard=True)
    $ show_quick_menu = False
    scene black with Fade(3,0,0)
    $ show_quick_menu = False
    $ renpy.pause(2, hard=True)

    $ show_quick_menu = False
    show screen happy_overlay
    $ show_quick_menu = False
    jump daySkyrim

label workDay:
    scene black
    $ choice = renpy.random.randint(0, dayEventsLen)
    $ renpy.jump(("day" + dayEvents[choice]))

    #failsafe
    jump eveningChoice

label eveningChoice:
    scene black with dissolve
    play music "choices.ogg" fadein 2.0
    "After a long day at work, you return home, wherever that may be."
    scene bg bed with dissolve
    $ happiness = max(happiness, 0)

    mc """
    Man I'm fried, time to kick back and relax.
    """

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

        ran = renpy.random.randint(0, eventCount)
        while ran == choices[0] or ran == choices[1] or ran == choices[2]:
            ran = renpy.random.randint(0, eventCount)
        choices.append(ran)

        menuChoices = [
            (eveningEvents[choices[0]][0], eveningEvents[choices[0]][1]),
            (eveningEvents[choices[1]][0], eveningEvents[choices[1]][1]),
            (eveningEvents[choices[2]][0], eveningEvents[choices[2]][1]),
            (eveningEvents[choices[3]][0], eveningEvents[choices[3]][1])
        ]

        if dayCount > 4:
            ran = renpy.random.randint(0, winCount)
            menuChoices[renpy.random.randint(0, 3)] = (winEvents[ran][0], winEvents[ran][1])

        narrator("Choose your fate my dude", interact=False)
        result = renpy.display_menu(menuChoices)

        renpy.jump(("eve" + result))

    #failsafe
    jump night

label night:
    "You gained some happy points!"
    window hide
    # scene black
    # $ renpy.pause(0.1, hard=True)
    stop music
    play sound "pillowhit1.ogg"
    scene bg bed
    $ renpy.pause(0.8, hard=True)
    # scene black
    # $ renpy.pause(0.05, hard=True)
    #cut to bed, jump cut to workday
    $ dayCount += 1
    jump workDay

# Day activities

label dayPromotion:
    "Manager" "Hey [mcName] I just want to say you're doing great, so we'd like to put some extra responsibility on you and see how you handle it!"
    mc "Oh uh, thanks. What did you have in mind?"
    "Manager" "We want you to open the store, track some employees, that kind of thing."
    mc "Isn't that manager work? Am I getting a promotion?"
    "Manager" "No, we're not going to promote anybody right now, but think about how this could impact your chances of promotions later!"
    mc "So you want me to do a manager's workload, for normal pay?"
    "Manager" "Yeah, for now, but think of the possibilities!"
    $ happiness -= 25
    jump eveningChoice

label dayLunch:
    "NewGuy" "Hey [mcName] question, when do we take lunch breaks?"
    mc "Oh, uh, I don't know I don't really take them."
    "NewGuy" "Aren't they like, state mandated or something?"
    mc "Yeah, but the scheduling system this company uses doesn't attribute time for it, so there's never really a chance."
    "NewGuy" "Isn't that like, illegal?"
    mc """
    Yeah probably, but I guess I've just gotten used to it. Sometimes I can eat a candy bar, but normally
    if I try, I get interrupted halfway through by some new customer walking in I need to take care of.
    """
    $ happiness -= 30
    jump eveningChoice

label dayDownsize:
    "Manager" "Hey [mcName] just wanted to say it's been a pleasure working with you."
    mc "Huh, what happened?"
    "Manager" "I'm being let go, the company is restructuring."
    mc "They say that, but every 'restructure' is just them trying to make each employee juggle even more."
    "Manager" "Yeah I don't really envy you, good luck man."
    "At a meeting later that day..."
    "BigManager" "Today, we'll all find a way to learn from challenge and change."
    "...challenge and change, right, that's a way to put letting go of some of our workforce for the bottom line."
    $ happiness -= 25
    jump eveningChoice

label dayClopen:
    "Manager" "Hey [mcName] we need you to open the shop tomorrow."
    mc "But, I close tonight, that's only like eight hours total between shifts."
    "Manager" "I know, but we don't have a choice."
    "You spent the night toiling away, getting home and immediately going to bed."
    $ happiness -= 15
    $ happiness = max(happiness, 0)
    window hide
    scene bg bed
    $ renpy.pause(0.8, hard=True)
    $ dayCount += 1
    jump workDay

label daySkyrim:
    $ show_quick_menu = False
    scene bg wcdonalds 
    $ show_quick_menu = False
    show skyrim:
        zoom 0.4 xalign 0.8 yalign 0.5
    with Fade(0,0,2)
    window show
    $ show_quick_menu = True
    "Rolof" "Hey you, you're finally awake.{fast}"
    hide skyrim 
    show skyrim
    "Rolof" "You shorted me a WcNugget you asshole. I demand a refund."
    hide skyrim
    show skyrim:
        zoom 2.0 xalign 0.5 yalign 0.5
    "Rolof" "WHERE IS YOUR MANAGER." with vpunch
    $ happiness -= 20
    jump eveningChoice

label dayRaise:
    "Manager" "Thank you all for attending this meeting, we are so excited to share all the new benefits with you!"
    "The meeting goes on for what feels like an age, with promises from the corporation you've heard many times before."
    "Each time, none of the benefits come through, all that comes through is more work."
    $ happiness -= 15
    jump eveningChoice

label dayTurkey:
    "You get to work Thanksgiving again, Black Friday is always such a pain."
    "Customer" "Wow, you have to work on Thanksgiving? That sucks! Why do you even need to work today?"
    mc "It's busy."
    "Customer" "Wow true! Hey, do you have the doorbuster TV still in stock?"
    "Screams internally."
    $ happiness -= 25
    jump eveningChoice

#Evening activities

label eveYuYu:
    mc "Man Yoyoske is so cool."
    mc "He's so lucky to be in an anime where anything can happen, how am I supposed to ever compete with that?"
    $ happiness += 21
    jump night

label eveHD2:
    mc "Those bugs never knew what hit them! For Super Earth!"
    "Bowfinger" "FOR SUPER EARTH"
    mc "Heck yeah man! You down for another game?"
    "Bowfinger" "Nah I gotta jet, gotta prep for a meeting tomorrow."
    mc "Alright man, you have a good one."
    "You continued to play for another few hours, many bugs died."
    $ happiness += 10
    jump night

label eveLoU2:
    mc "This game looks so amazing, but I don't get this plot at all. Didn't Ell-E learn the lesson already that revenge is bad?"
    mc "Why can't she learn from her past mistakes and just take a step forward in the right direction?"
    $ happiness += 3
    jump night

label eve1P:
    mc "Luffy stretch long"
    mc "Luffy stretch longer"
    mc "Luffy stretch longest"
    mc "HOW LONG IS THIS"
    "You finish the entirety of One Piece's >1000 episode series and movies."
    mc "... It wasn't long enough. What am I supposed to do now?"
    $ happiness += 18
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
    "You go to the gym."
    "Your ligaments tear."
    mc "Sick gains!!!"
    $ happiness += 15
    jump night

label eveNet:
    scene bg net
    mc "what a cool net."
    $ happiness += 15
    jump night

label eveReflect:
    $ happiness -= 10
    mc "I've been in this same crap job for way too long. I need out. This is just ridiculous."
    $ happiness += 20
    mc "Time to buckle down and actually figure out how to be a [dreamJob]!"
    scene bg grad
    $ happiness = 9001
    mc "...Wow."
    jump winrar
    
label eveAdvise:
    scene black
    "You schedule time to see an expert about how you can achieve your goals."
    $ happiness += 20
    "Working together, you come up with a plan that actually even seems doable."
    scene bg grad
    $ happiness = 9001
    mc "I did it! I'm a [dreamJob] now!"
    jump winrar

#End

label winrar:
    scene black
    seb """
    Oh, hello again [mcName]!
    """
    seb """
    How'd it go? Did you have a little fun? How many days did it take you to reach this point?
    """
    if dayCount == 1:
        seb """
        Wow first day? You are full of agency, nice! Maybe you're a person who's already reached
        their goals? Or just good at having their dream in mind? 
        """
        seb """
        You didn't get stuck in the routine at all, I wonder if I should feel bad about spending so much time on writing
        so many silly little diversions now.
        """
    else:
        seb """
        Day [dayCount]? Interesting. I didn't program in a way to react to that number much,
        but I'm sure it's impressive in some way.
        """
    seb """
    This game is for anybody who's stuck in a loop, a routine they feel trapped in. Stuck at some job
    they hate each day, spending each evening just trying to recharge those batteries to deal with
    the job another day.
    """
    seb """
    I've been there, as have many. And the only thing I want to say, is you're better than you
    think you are. If you truly want it, you can land a job you actually appreciate it.
    """
    seb """
    Never let yourself get stuck a routine you can't escape.
    """
    seb """
    Take it one step at a time, keep moving towards your dreams.
    You can be a great [dreamJob] if you put your mind to it.
    """
    seb """
    So, now that this game was perhaps even shorter than you expected it to be, what are you going
    to do with all that free time?

    Go, be awesome.
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
