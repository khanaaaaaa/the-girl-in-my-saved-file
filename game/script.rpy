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
    yuna "That's a pretty name."
    yuna "I'll remember it."
    pause 1.0
    yuna "Anyway, welcome to my little room."
    yuna "There's not much here."
    yuna "Just me."
    yuna "And you."

    pause 2.0

    yuna "Can I ask you something?"
    hide yunasmiletalk
    show yunaneutralquiet at center_char
    yuna "How did you find this game?"
    
    menu:
        "I downloaded it from a website":
            hide yunaneutralquiet
            show yunasmiletalk at center_char
            yuna "A website?"
            yuna "Oh, I don't remember making a website."
            yuna "I don't remember making anything, actually."

        "I found it on my computer.":
            hide yunaneutralquiet
            show yunamsmiletalk at center_char
            yuna "Your computer?"
            yuna "So it was already there?"
            yuna "That's strange."

        "I don't know.":
            hide yunaneutralquiet
            show yunasmiletalk at center_char
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

return