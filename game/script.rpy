define y = Character("Yuna", color="#e8a6b8")

default player_name = "Player"
default trusted_yuna = False
default answered_honestly = False

default persistent.yuna_net = False
default persistent.last_player_name = ""

label start:
    scene black
    with fade

    pause 2.0

    centered "{size=-3}version 1.0.0{/size}"
    pause 3.0

    centered "{size=-3}version 1.0.0{/size}"
    pause 2.0

    y "Oh."
    y "You're here."
    y "I thought nobody else was going to open this."
    pause 1.5

    y "Sorry. That seemed weird, didn't it?"
    y "Let's start over."
    y "Hi! I'm Yuna."
    y "What's your name?"
    $ player_name = renpy.input("Your name", length=20).strip()

    if player_name == "":
        $ player_name = "Player"

    return