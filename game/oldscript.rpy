# The game starts here.
label originalStart:
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

    jump workDayOriginal

label workDayOriginal:
    scene skyrim
    "Rolof" "Hey you, you're finally awake."
    "Rolof" "You shorted me a WcNugget you asshole. I demand a refund."
    "Rolof" "WHERE IS YOUR MANAGER."

    $ happiness -= 20
    $ happiness = max(happiness, 0)

    jump eveningChoiceOriginal

label eveningChoiceOriginal:
    scene homelife

    mc """
    Man I'm fried.
    """

    menu:
        "Choose your fate my dude"

        "It is wednesday":
            seb """
            Don't lie to me.
            """
            $ happiness += 10
        "My dude":
            seb """
            My duuuuude.
            """
            $ happiness += 15
        "winrar":
            seb """
            Just use 7zip what are you doing.
            """
            jump winrarOriginal

    jump workDayOriginal

label winrarOriginal:
    seb """
    Now you're a hero. You've beat the whole damn game. We're happy you've made it, but
    how are you going to spend the rest of this day? Maybe watch a video, maybe press
    refresh and start again.
    """
    jump gameEnd