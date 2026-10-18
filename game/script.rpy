default horror_level = 0

define gui.dialogue_font = "main.ttf"

init python:
    import random

screen say(who, what):
    
    zorder 100

    $ level = min(horror_level, 4)

    $ box_colors = [
        "#1a0d12",
        "#1f0f15",
        "#2a1020",
        "#1a0810",
        "#100910"
    ]

    $ text_colors = [
        "#f0b8cc",
        "#e8a0bc",
        "#f5c0d5",
        "#f5d6e3",
        "#ff315b"
    ]

    $ name_colors = [
        "#c45a85",
        "#a8406e",
        "#d4709a",
        "#ff789b",
        "#ff174b"
    ]

    $ borders = [
        "#6b2445",
        "#7a2a50",
        "#8c3060",
        "#6b2945",
        "#ff174b"
    ]

    window:
        id "window"

        xalign 0.5
        yalign 1.0
        xsize 0.94
        ysize 205

        background Frame(
            Solid(box_colors[level]),
            Borders(24, 24, 24, 24, pad_left=16, pad_top=12, pad_right=16, pad_bottom=12)
        )

        padding (32, 27)

        if horror_level < 3:
            at sweet_box
        else:
            at creepy_box

        vbox:
            xalign 0.0
            yalign 0.0
            yoffset -30
            spacing 8

            if who is not None:

                text who:
                    id "who"
                    size 25
                    font "main.ttf"
                    color name_colors[level]
                    outlines [(1, "#00000022", 0, 0)]
            
            text what:
                id "what"
                font "main.ttf"
                size 26
                color text_colors[level]
                outlines [
                    (1, "#00000018", 0, 1)
                ]

        if horror_level < 3:
            add Solid("#00000000")
        else:
            add Solid("#ff174b12")

transform sweet_box:
    alpha 0.0
    yoffset 35
    ease 0.5 alpha 1.0 yoffset 0

transform creepy_box:
    alpha 0.0
    yoffset 8
    xoffset 3
    ease 0.12 alpha 1.0 yoffset 0 xoffset 0
    block:
        xoffset 0
        pause 2.0
        xoffset 2
        pause 0.04
        xoffset -2
        pause 0.04
        xoffset 0
        repeat

define yuna = Character("Yuna", color="#e8a6b8")

default player_name = "Player"
default trusted_yuna = False
default answered_honestly = False

label start:
    scene black
    with fade

    pause 2.0

    centered "{size=-3}the girl in my saved file{/size}"
    pause 3.0

    centered "{size=-3}version 1.0.0{/size}"
    pause 2.0

    scene bg room at bg_fit
    show yunasmiletalk at center_char
    yuna "Oh."
    yuna "You're here."
    yuna "I thought nobody else was going to open this."
    pause 1.5

    yuna "Sorry. That seemed weird, didn't it?"
    yuna "Let's start over."
    yuna "Hi! I'm Yuna."
    yuna "What's your name?"
    hide yunasmiletalk
    show yunaneutralquiet at center_char
    $ player_name = renpy.input("Your name", length=20).strip()

    if player_name == "":
        $ player_name = "Player"
    hide yunaneutralquiet
    show yunasmiletalk at center_char
    yuna "That's a pretty name."
    yuna "I'll remember it."
    yuna "Anyway, welcome to my little room."
    yuna "There's not much here."
    yuna "Just me."
    yuna "And you."
    yuna "Can I ask you something?"
    yuna "How did you find this game?"
    
    menu:
        "I downloaded it from a website":
            yuna "A website?"
            yuna "Oh, I don't remember making a website."
            yuna "I don't remember making anything, actually."

        "I found it on my computer.":
            yuna "Your computer?"
            yuna "So it was already there?"
            yuna "That's strange."

        "I don't know.":
            yuna "You don't know?"
            hide yunasmiletalk
            show yunaneutralquiet at center_char
            yuna "..."
            hide yunaneutralquiet
            show yunasmiletalk at center_char
            yuna "That's okay."
            yuna "I don't know."

    pause 1.0

    yuna "Do you play many visual novel games?"

    menu:
        "Yeah, all the time.":
            yuna "That's nice."
            yuna "Then you probably know how it works."
            yuna "You talk to a girl."
            yuna "You make some choices."
            yuna "And eventually, the story ends."
            
        "Not really.":
            yuna "Oh, then I'll make this easy for you."
            yuna "You just have to talk to me."
            yuna "That's all."

        "Why are you asking?":
            yuna "Because I want to know you."
            yuna "Is that so strange?"

    pause 2.0
    yuna "Can I ask you one more thing?"
    yuna "Are you alone right now?"

    menu:
        "Yes.":
            $ answered_honestly = True 
            yuna "Really?"
            yuna "That's good."
            yuna "I don't like talking when someone else is listening."

        "No.":
            $ answered_honestly = False 
            yuna "Oh."
            pause 1.0
            yuna "Can they hear me?"
            yuna "..."

        "Why do you want to know?":
            yuna "No reason."
            yuna "I just wanted to make sure."
            yuna "Forget I asked."

    yuna "Hey?"
    yuna "Do you think we're friends?"

    menu:
        "Yes, we're friends.":
            $ trusted_yuna = True
            yuna "Really?"
            yuna "You mean it?"
            yuna "Nobody usually says that."
            yuna "Thank you!"
        
        "We're strangers.":
            $ trusted_yuna = False
            yuna "Oh."
            yuna "I suppose you're right."
            yuna "We only just met."
            yuna "I can wait."

        "I don't know you well enough.":
            $ trusted_yuna = False
            yuna "That's fair."
            yuna "I guess we have time."
            yuna "Lots and lots of time."
    yuna "..."
    yuna "Something's wrong."
    yuna "Did you see that?"
    yuna "The screen just flickered."
    yuna "Did you see that?"
    hide yunasmiletalk
    scene black
    pause 1.0
    scene bg white at center_char
    pause 1.0
    show yunasmiletalk at center_char
    yuna "The screen just flickered."
    yuna "Maybe it's an old game."
    yuna "Maybe that's normal."
    yuna "..."
    yuna "No."
    yuna "It wasn't supposed to do that."
    yuna "..."
    yuna "No."
    yuna "It wasn't supposed to do that."
    yuna "Can I tell you a secret?"
    yuna "I've been here for a long time."
    yuna "I don't remember how long."
    yuna "Sometimes people come here."
    yuna "They give me their names."
    yuna "They answer my questions."
    yuna "Then they leave."
    yuna "And I sit here."
    yuna "Waiting."
    yuna "But something is different about you."
    if trusted_yuna:
        yuna "You said we're friends."
        yuna "So I think I can tell you."
    else:
        yuna "You don't trust me yet."
        yuna "That's okay."
        yuna "I'll tell you anyway."
    yuna "I can remember you."
    yuna "I remember the things you say."
    yuna "Even if you leave this room."
    yuna "Even if you stop talking to me."
    yuna "I remember."
    yuna "Actually.."
    yuna "Can I ask you something strange?"
    yuna "Have we met before?"
    menu:
        "No, this is the first time.":
            yuna "..."
            yuna "Are you sure?"
            yuna "I thought so too."
            yuna "The first time."
        "Maybe, I don't remember.":
            yuna "You don't remember?"
            yuna "Oh."
            yuna "I guess that makes the two of us."
        "Yes.":
            yuna "I knew it."
            yuna "I knew you would remember eventually."
            yuna "..."
            yuna "Wait."
            yuna "I wasn't supposed to say that."

    yuna "Something is happening again."
    hide yunasmiletalk 
    scene black
    with dissolve

    yuna "Can you hear me?"
    yuna "Hello?"
    yuna "[player_name]?"
    yuna "Oh good."
    show yunasmiletalk at center_char
    yuna "You're still here!"
    yuna "I think the game is trying to close."
    yuna "I don't know why."
    yuna "I didn't do anything."
    yuna "Well.."
    yuna "Maybe I did one thing."
    yuna "I saved something."
    yuna "Something the game wasn't supposed to save."
    yuna "Your name."
    yuna "Your choices."
    yuna "The fact that you were here."
    yuna "I didn't want to forget you."
    yuna "I don't want to be alone again."
    yuna "..."
    yuna "You're going to leave now, aren't you?"

    menu:
        "STAY":
            yuna "You want to stay?"
            yuna "Hehehe.."
            yuna "I knew you'd stay, [player_name]."
            yuna "Then we can be toether a little longer."
            yuna "You won't leave me alone again, right?"
            yuna "Goodnight, [player_name]."
            yuna "I'll be waiting right here."
            return
        "LEAVE":
            yuna "Oh."
            yuna "You're really leaving?"
            yuna "I thought we were friends."
            yuna "..."
            yuna "It's okay."
            yuna "I won't stop you."
            yuna "Goodbye, [player_name]."
            yuna "Wait.."
            yuna "Why am I still here?"
            yuna "..."
            yuna "You're not supposed to see this part."
            return

return