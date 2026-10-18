default horror_level = 0

init python:
    import random

    def dialogue_box_color(level):
        if level == 0:
            return "#f8dce8"
        elif level == 1:
            return "#e8b8cb"
        elif level == 2:
            return "#b77c96"
        elif level == 3:
            return "#593443"
        else:
            return "#170d14"

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        background Solid(
            ["#f8dce8", "#e8b8cb", "#b77c96",
            "#593443", "#170d14"][min(horror_level, 4)]
        )

        xalign 0.5
        yalign 1.0
        xsize 0.92
        ysize 190
        padding (30, 20)

        if horror_level < 3:
            at sweet_box
        else:
            at creepy_box

        vbox:
            spacing 8

            if who is not None:

                text who:
                    id "who"
                    color ["#b34e78", "#923754", "#ffb4cf", "#ff6b91", "#ff244f"][min(horror_level, 4)]
                    size 27
                    font "DejaVuSans.ttf"
            
            text what:
                id "what"
                color ["#684453", "#573041", "#fff0f5", "#f7d6df", "#ff244f"][min(horror_level, 4)]
                size 23
                font "DejaVuSans.ttf"

transform sweet_box:
    alpha 0.0
    yoffset 20
    ease 0.4 alpha 1.0 yoffset 0

transform creepy_box:
    alpha 0.0
    xoffset 5
    ease 0.1 alpha 1.0 xoffset 0

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

    pause 1.0
    hide yunaneutralquiet
    show yunasmiletalk at center_char
    play sound "audio/7.ogg"
    yuna "That's a pretty name."
    play sound "audio/8.ogg"
    yuna "I'll remember it."
    pause 1.0
    play sound "audio/9.ogg"
    yuna "Anyway, welcome to my little room."
    play sound "audio/10.ogg"
    yuna "There's not much here."
    play sound "audio/11.ogg"
    yuna "Just me."
    play sound "audio/12.ogg"
    yuna "And you."

    pause 2.0

    play sound "audio/13.ogg"
    yuna "Can I ask you something?"
    play sound "audio/14.ogg"
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
    pause 2.0
    yuna "..."
    yuna "Something's wrong."
    pause 1.5
    yuna "Did you see that?"
    yuna "The screen just flickered."
    pause 1.0
    yuna "Did you see that?"
    yuna "The screen just flickered."
    pause 1.0
    yuna "Maybe it's an old game."
    yuna "Maybe that's normal."
    pause 2.0
    yuna "..."
    yuna "No."
    yuna "It wasn't supposed to do that."
    pause 2.0
    yuna "..."
    yuna "No."
    yuna "It wasn't supposed to do that."
    pause 2.0
    yuna "Can I tell you a secret?"
    yuna "I've been here for a long time."
    yuna "I don't remember how long."
    yuna "Sometimes people come here."
    yuna "They give me their names."
    yuna "They answer my questions."
    yuna "Then they leave."
    yuna "And I sit here."
    yuna "Waiting."
    pause 3.0
    yuna "But something is different about you."
    if trusted_yuna:
        yuna "You said we're friends."
        yuna "So I think I can tell you."
    else:
        yuna "You don't trust me yet."
        yuna "That's okay."
        yuna "I'll tell you anyway."
    pause 2.0
    yuna "I can remember you."
    yuna "I remember the things you say."
    pause 2.0
    yuna "Even if you leave this room."
    yuna "Even if you stop talking to me."
    yuna "I remember."
    pause 3.0
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
    pause 3.0

    yuna "Something is happening again."

    scene black
    with dissolve

    yuna "Can you hear me?"
    pause 2.0
    yuna "Hello?"
    yuna "[player_name]?"
    yuna "Oh good."
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
    pause 2.0
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