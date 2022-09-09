init:
    $ bad_answers = 0
    $ end = False
label start:
    stop music
    $ name = ""
    while name == "":
        $ name = renpy.input("Как вас зовут?")

    play music "audio/playground.wav"
    scene bg_pg
    show g normal

    g "О нет, мяч улетел в кусты...{w=3}\nПойду за ним"
    
    g "Что это лежит, похожу на какую-то сумку{w=3}\nХмм"

    hide g normal
    scene bg_b

    menu:
        "Что же делать?"
        "Взять сумку":
            $ bad_answers += 1
        "Сообщить в полицию":
            $ end = True
    if end:
        stop music
        g "Приехала полиция"
        jump end_1
    else:
        g "Что же тут, оооо, деньги, кайфффф"
        g "Пойду куплю покушать"
    jump day_2
    stop music
    return
