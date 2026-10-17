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

    yuna "Oh."
    yuna "You're here."
    yuna "I thought nobody else was going to open this."
    pause 1.5

    yuna "Sorry. That seemed weird, didn't it?"
    yuna "Let's start over."
    yuna "Hi! I'm Yuna."
    yuna "What's your name?"
    $ player_name = renpy.input("Your name", length=20).strip()

    if player_name == "":
        $ player_name = "Player"

    pause 1.0

    yuna "That's a pretty name."
    yuna "I'll remember it."
    pause 1.0
    yuna "Anyway, welcome to my little room."
    yuna "There's not much here."
    yuna "Just me."
    yuna "And you."

    pause 2.0

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
            yuna "..."
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
            yuna "Are you alone right now?"


return