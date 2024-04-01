init python:
    import os
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('mouseup_3')
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
    npc = DynamicCharacter("npcName", what_prefix="\"", what_suffix="\"", callback=everyonevoice)
    npc2 = DynamicCharacter("npcName2", what_prefix="\"", what_suffix="\"", callback=everyonevoice)
    seb = Character("seb", callback=everyonevoice)
    car = Character("carmints", callback=everyonevoice)

    preferences.text_cps = 50  
    mcName = os.environ.get("USERNAME") or "You"
    happiness = 50
    dayCount = 1
    eveningEvents = [
        ["play HeckDiving 2 with friends", "HD2"],
        ["watch a lets play of Last of Them part II", "LoU2"],
        ["watch YoYo Hakusho", "YuYu"],
        ["watch One Peace", "1P"],
        ["go 2 the gym and get ripped", "Gym"],
        ["date people", "Date"],
        ["browse the cool net", "Net"],
        ["play games", "Game"],
        ["sleep", "Sleep"],
        ["hang with the homies", "Friends"],
        ["play Last Fantasy 14", "FF14"],
        ["scroll through xwitter", "Scroll"],
        ["watch some Utube", "YT"],
        ["buy a new game", "NG"]
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
        "Promotion",
        "Rent",
        "Plans",
        "Raid",
        "Appointment",
        "Hours",
        "Quit",
        "Security",
        "Turnover",
        "Bonus"
    ]
    dayEventsLen = len(dayEvents) - 1


# The game starts here.
label start:
    play music "audio/choices.ogg"
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
            Put yourself in the shoes of somebody who's not there yet, be that a you of the past, 
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

    $ nameCheck = playerName.lower()
    if nameCheck == "totaka":
        stop music fadeout 1.5
        play music "audio/totakasong.flac" fadein 1.5
        jump originalStart

    seb """
    One more question, what's your dream job?
    """

    $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()
    while dreamJob == "":
        seb """
        Hey now, take this seriously. Or type in vtuber, whatever floats your boat.
        """
        $ dreamJob = renpy.input("Don't let your dreams be memes", length=30).strip()
        
    seb "A [dreamJob] huh? That sounds pretty cool. I bet you'd be pretty good at it too."

    $ dreamLower = dreamJob.lower()
    if dreamLower == "vtuber":
        seb "The next KSon maybe?"

    seb "Well that's enough talking out of me, maybe I'll see you again sometime."

    stop music fadeout 1.5

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

    seb ". . . oh, I need to fix this wall now, huh."

    window hide
    show wallfixing
    hide wallbroke

    $ renpy.pause(0.8, hard=True)

    show wallfixed
    hide wallfixing 
    $ quick_menu = False
    scene black with Fade(3,0,0)
    $ renpy.pause(2, hard=True)
    show screen happy_overlay
    jump daySkyrim

label workDay:
    scene black
    window show
    $ choice = renpy.random.randint(0, dayEventsLen)
    $ renpy.jump(("day" + dayEvents[choice]))
    window show
    #failsafe
    jump eveningChoice

label eveningChoice:
    $ happiness = max(happiness, 0)
    scene black with dissolve
    play music "audio/choices.ogg" fadein 2.0
    "After a long day at work, you return home, wherever that may be."
    scene bg bed with dissolve

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
    stop music
    play sound "pillowhit1.ogg"
    scene bg bed
    $ renpy.pause(0.8, hard=True)
    $ dayCount += 1
    jump workDay

# Day activities

label dayBonus:
    $ npcName = "Manager"
    npc "Hey guys, I have some bad news."
    npc "We were on excellent track to get a holiday bonus, the metrics we were giving corporate were above and beyond."
    npc "But unfortunately corporate decided against giving us any bonus, they moved the numbers needed at the last minute."
    mc "How is that even allowed?"
    npc "Well, they're in charge. I know it's not much, but I have some pizza in the back. We'll try again next year!"
    $ happiness -= 20
    jump eveningChoice

label dayTurnover:
    $ npcName = "Coworker"
    npc "Hey [mcName] why do you never remember people's names?"
    mc "Too many coworkers come and go, I tend to only remember the ones who stick around."
    npc "Wow, just how long have you been here to have seen that much turnover?"
    mc ". . . too long, I guess."
    $ happiness -= 5
    jump eveningChoice

label daySecurity:
    $ npcName = "Manager"
    npc "Per new rules from corporate, front door security can no longer confront shoplifters."
    npc "There have been incidents where angry shoplifters have pulled guns on security, or threatened legal action."
    mc "So now, the stuff in the store is all free?"
    npc "Now now, we all just need to be more vigilant!"
    $ happiness -= 10
    jump eveningChoice

label dayQuit:
    $ npcName = "Manager"
    $ npcName2 = "Coworker"
    "Walking in to work, there's an argument at the doors."
    npc2 "You know what? Screw this, I'm out."
    "The coworker walks out of the building."
    mc "Wait, what just happened?"
    npc "He didn't agree with the new policies we're putting in place. Speaking of, do you have time to talk?"
    mc "What is it this time?"
    npc "Nothing you haven't heard before, you're one of our veterans here after all!"
    "Why do I even put up with this?"
    $ happiness -= 15
    jump eveningChoice

label dayHours:
    $ npcName = "Manager"
    "You notice your hours for the next week look lower."
    mc "Hey boss, I was wondering if I could pick up extra hours next week to meet rent."
    npc "Sorry, we only had so many hours to give, and I just didn't think you wanted to be here."
    mc "But what about my rent?"
    npc "Could try taking on a second job?"
    $ happiness -= 20
    jump eveningChoice

label dayAppointment:
    $ npcName = "Irate Customer"
    $ npcName2 = "Chill Customer"
    npc "Hey I need you to fix my phone."
    mc "Sure, do you have an appointment with us today?"
    npc "No, I have a broken phone, fix it."
    mc "Sorry, but the custmers you see behind you are my appointments for the next hour or so."
    mc """
    I'll have to take care of them first, since they scheduled appointments.
    """
    mc """
    If you'd like to wait I can try to fix your phone as soon as there's some available time,
    but I don't know when an appointment will no show.
    """
    npc "What about the time you're spending talking to me now? Huh?"
    "You gesture behind you."
    mc "The customer behind me here is patiently waiting for me to continue working with them."
    npc "Fine, then I'll just leave my phone on the counter, and you can fix it when you're free!"
    mc "We have a process we have to follow for legal reasons, if you leave your phone here I can't work on it."
    npc "So? What will you do with it then?"
    mc "Report it to lost and found, and they discard those items when the shop closes for the night."
    npc "I'm going to find your manager!"
    "They storm off."
    npc2 "Man he was a dick, sorry you have to deal with people like them."
    mc "Thanks. It's all part of the job, now let me finish helping you out."
    $ happiness -= 5
    jump eveningChoice

label dayRent:
    $ npcName = "Coworker"
    "There's a stack of papers in the breakroom at work. 'How to Manage Your Finances'."
    mc "Huh, I mean managing money is important."
    npc "Oh [mcName], did you notice the best part though?"
    mc "Huh?"
    npc "Look closer at the first section, where you calculate the money you earn."
    mc "Oh I guess they have a little explanation here . . . wait, are you serious??"
    npc "Yeah, it's kind of great."
    "The form clearly stated at the beginning, that the company knew they were not paying a livable wage."
    "It then listed options for how to deal with it, by working two jobs or acquiring extra roommates."
    $ happiness -= 25
    jump eveningChoice

label dayPlans:
    $ npcName = "Friendo"
    npc "Hey man you down to go to a concert in a couple weeks?"
    mc "Sorry I can't, dunno if I'll have work."
    npc "What do you mean?"
    mc "I get my work hours for the week on like, the Friday before. So I never really know in advance when I work."
    npc "Wow man that kinda sucks."
    mc "You get used to it I guess."
    $ happiness -= 10
    jump eveningChoice

label dayRaid:
    "Looking at the work schedule for next week, it looks like your hours have changed, there's more closing shifts."
    mc "Man, I guess I won't be raiding in World of Wowcraft for a while unless I join a group that runs at like 3am."
    $ happiness -= 25
    jump eveningChoice

label dayPromotion:
    $ npcName = "Manager"
    npc "Hey [mcName] I just want to say you're doing great, so we'd like to put some extra responsibility on you and see how you handle it!"
    mc "Oh uh, thanks. What did you have in mind?"
    npc "We want you to open the store, track some employees, that kind of thing."
    mc "Isn't that manager work? Am I getting a promotion?"
    npc "No, we're not going to promote anybody right now, but think about how this could impact your chances of promotions later!"
    mc "So you want me to do a manager's workload, for normal pay?"
    npc "Yeah, for now, but think of the possibilities!"
    $ happiness -= 25
    jump eveningChoice

label dayLunch:
    $ npcName = "New Guy"
    npc "Hey [mcName] question, when do we take lunch breaks?"
    mc "Oh, uh, I don't know I don't really take them."
    npc "Aren't they like, state mandated or something?"
    mc "Yeah, but the scheduling system this company uses doesn't attribute time for it, so there's never really a chance."
    npc "Isn't that like, illegal?"
    mc """
    Yeah probably, but I guess I've just gotten used to it. Sometimes I can eat a candy bar, but normally
    if I try, I get interrupted halfway through by some new customer walking in I need to take care of.
    """
    $ happiness -= 30
    jump eveningChoice

label dayDownsize:
    $ npcName = "Manager"
    $ npcName2 = "Upper Manager"
    npc "Hey [mcName] just wanted to say it's been a pleasure working with you."
    mc "Huh, what happened?"
    npc "I'm being let go, the company is restructuring."
    mc "They say that, but every 'restructure' is just them trying to make each employee juggle even more."
    npc "Yeah I don't really envy you, good luck man."
    "At a meeting later that day . . ."
    npc2 "Today, we'll all find a way to learn from challenge and change."
    ". . . challenge and change, right, that's a way to put letting go of some of our workforce for the bottom line."
    $ happiness -= 25
    jump eveningChoice

label dayClopen:
    $ npcName = "Manager"
    npc "Hey [mcName] we need you to open the shop tomorrow."
    mc "But, I close tonight, that's only like eight hours total between shifts."
    npc "I know, but we don't have a choice."
    "You spent the night toiling away, getting home and immediately going to bed."
    $ happiness -= 15
    $ happiness = max(happiness, 0)
    play sound "pillowhit2.ogg"
    window hide
    scene bg bed
    $ renpy.pause(0.8, hard=True)
    $ dayCount += 1
    jump workDay

label daySkyrim:
    scene bg wcdonalds 
    show skyrim:
        zoom 0.45 xalign 0.85 yalign 0.5
    with Fade(0,0,2)
    window show
    $ quick_menu = True
    $ npcName = "Rolof"
    npc "Hey you, you're finally awake."
    hide skyrim 
    show skyrim
    npc "You shorted me a WcNugget you asshole. I demand a refund."
    hide skyrim
    show skyrim:
        zoom 2.0 xalign 0.5 yalign 0.5
    npc "WHERE IS YOUR MANAGER." with vpunch
    $ happiness -= 20
    jump eveningChoice

label dayRaise:
    $ npcName = "Manager"
    npc "Thank you all for attending this meeting, we are so excited to share all the new benefits with you!"
    "The meeting goes on for what feels like an age, with promises from the corporation you've heard many times before."
    "Each time, none of the benefits come through, all that comes through is more work."
    $ happiness -= 15
    jump eveningChoice

label dayTurkey:
    $ npcName = "Customer"
    "You get to work Thanksgiving again, Black Friday is always such a pain."
    npc "Wow, you have to work on Thanksgiving? That sucks! Why do you even need to work today?"
    mc "It's busy."
    npc "Wow true! Hey, do you have the doorbuster TV still in stock?"
    "Screams internally."
    $ happiness -= 25
    jump eveningChoice

#Evening activities

label eveScroll:
    scene bg net
    "You scroll through Xwitter, rexweeting uplifting posts about changing the world."
    mc "Wow it's 2am already, where did all the time go?"
    $ happiness += 1
    jump night

label eveYT:
    scene bg net
    "You spend some time watching Utube."
    mc "This guy keeps saying to not worry about the details and just start making games, maybe I should try?"
    mc "Eh, it's late, I'm tired, maybe tomorrow."
    $ happiness += 5
    jump night

label eveNG:
    scene bg net
    "Scrolling through Steamy, it feels like no game really jumps out at you."
    mc "No, no that one. Not that one either."
    mc "I want a game where I can feel a real sense of achievement, feels like there's a hole I need to fill you know?"
    "You end up going to bed having not bought any new game, nothing seemed to fit."
    $ happiness += 5
    jump night

label eveFF14:
    scene bg game
    mc "Time to do dailies in the critically acclaimed MMO Last Fantasy 14."
    "You spend some time doing daily quests."
    mc "Feels like I'm making good progress. Always feels nice to make headway towards a goal."
    $ happiness += 22
    jump night

label eveYuYu:
    scene bg watch
    mc "Man Yoyoske is so cool."
    mc "He's so lucky to be in an anime where anything can happen, how am I supposed to ever compete with that?"
    $ happiness += 21
    jump night

label eveHD2:
    $ npcName = "Space Cowboy"
    scene bg game
    mc "Those bugs never knew what hit them! For Super Earth!"
    npc "FOR SUPER EARTH"
    mc "Heck yeah man! You down for another game?"
    npc "Nah I gotta jet, gotta prep for a meeting tomorrow."
    mc "Alright man, you have a good one."
    "You continued to play for another few hours, many bugs died."
    $ happiness += 10
    jump night

label eveLoU2:
    scene bg watch
    mc "This game looks so amazing, but I don't get this plot at all. Didn't Ell-E learn the lesson already that revenge is bad?"
    mc "Why can't she learn from her past mistakes and just take a step forward in the right direction?"
    $ happiness += 3
    jump night

label eve1P:
    scene bg watch
    mc "Loffy stretch long"
    mc "Loffy stretch longer"
    mc "Loffy stretch longest"
    mc "HOW LONG IS THIS"
    "You finish the entirety of One Piece's >1000 episode series and movies."
    mc ". . . It wasn't long enough. What am I supposed to do now?"
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
    mc "Zzzz . . ."
    "You feel slightly rested after a hard day."
    mc "Good nap."
    mc ". . . Maybe too long of a nap."
    mc ". . ."
    mc "That nap took up most of my day."
    mc "I napped way too long."
    mc "It's bedtime now."
    mc ". . ."
    mc "Dang it, that was a long nap--"
    $ happiness += 10
    jump night

label eveGame:
    scene bg game
    "You went up 100 levels."
    mc "Sick gains!!!"
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
    mc "What a cool invention."
    $ happiness += 15
    jump night

label eveReflect:
    $ happiness -= 10
    mc "I've been in this same crap job for way too long. I need out. This is just ridiculous."
    $ happiness += 20
    mc "Time to buckle down and actually figure out how to be a [dreamJob]!"
    scene bg grad
    $ happiness = 9001
    mc ". . . Wow."
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
    This game is for anybody who's stuck in a loop, a routine they feel trapped in.
    """
    seb """
    Stuck at some job they hate each day, spending each evening just trying to recharge those batteries to deal with
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
    """
    seb """
    Go, be awesome.
    """
    jump gameEnd

label gameEnd:
    "Fin."
    return
