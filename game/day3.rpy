init:
    $ first_root_day_3 = False
    $ second_root_day_3 = False
    $ third_root_day_3 = False

label day_3:
    scene room
    g "Зевок...."
    
    show g_normal
    g "Интересно, чем же мне заняться, может схожу в магазин, как раз деньги есть, может быть прикуплю себе что-нибудь?"

    scene bg_s

    n "[name] приходит в магазин и осматривает витрины магазина."

    g "Что же мне выбрать?"

    menu:
        "Что мне следует прикупить?"
        "Я куплю себе парочку вещей":
            $ answers += 1
            $ firslt_root_day_3 = True
        "Я не буду себе ничего покупать.":
            $ second_root_day_3 = True
        "Я куплю всё, что подаётся мне на глаза.":
            $ third_root_day_3 = True

    if first_root_day_3:
        g "Хм, возьму себе парочку вещей и пойду домой."
        n "[name] прикупил себе парочку вещей и вернулся домой."

        scene room
        m "Привет солнце. Как то ты сегодня поздновато."
        g "Да, мама, есть такое. {w=2}Ладно мама, я спать пойду."

        jump day_4
    if second_root_day_3:
        n "[name] ничего себе не взял и вернулся домой."


        scene room
        m "Привет солнце. Как то ты странно выглядишь. Рассказывай всё, что произошло."
        g "Вообщем... {w=1}мам... {w=1}я нашёл сумку с деньгами и спрятал её под кроватью."

        jump end_2
    
    if third_root_day_3:
        g "Чтож мелочиться, скуплю себе всё, что тут найдёт"
        n "Глупый [name] носился по магазинам и скупал всё, что только видел. {w=3}\nОн совсем не следил за временем и магазин начал закрываться.{w=3}Охранник подашёл к мальчику."
        show s normal at posL
        s "Мальчик, что ты тут делаешь в столь поздний час совсем один и с таким количеством вещей?"
        show gr mone at posR
        g "Делаю вдох, так пахнет диор, я искал тебя вечность, вот идиотю..."
        s "Давай я вызову полицию, они отвезут тебя домой"
        hide s normal
        hide gr mone
        n "Полиция приехала за мальчиком, чтобы отвезти его домой. Полицейский был смущён таким большим количеством покупок у мальчика и тем, что он совсем один."
        show p normal at posL
        show gr mone at posR
        p "Мальчик откуда у тебя столько денег?"
        gr "Дело в том, что я поднялся на ставках и прошёл курс Гусейна Гасанова, поэтому я стал таким богатым в столь юном возрасте.{w=3}\nСделал кеш...."
        p "Что-то я тебе не верю"
        hide p normal
        hide gr mone
        n "Вот нашего мальца и повзали("

        jump end_3

return
    