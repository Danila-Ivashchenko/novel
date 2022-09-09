label day_4_branch_1:
    scene school_corridor

    show gr_smile at posR

    show b_normal at posL

    g "Подожди, громила, не торопись. Я предложу тебе то, от чего ты не сможешь отказаться."

    g "Я дам тебе денег, а ты мне защиту от таких, как ты."

    b "Хах... ты мне деньги? За это мне просто не нужно бить тебя? Хорошо."

    scene school_corridor

    show gr_smile at posR

    show b_slave at posL

    e "[name] сидит на задней парте, вокруг него вьются девочки, сбоку стоит гопник и охраняет его."

    if bad_answers > 5:
        scene school_corridor

        show gr_smile

        g "Знаете, я ведь могу купить даже жену директора, хахах."

        e "Девочки смеются."

        play sound "womens_laugh.mp3"
    
    else:
        scene school_corridor

        show gr_smile

        g "Знаете, я ведь могу купить всё, о чем вы и мечтать не могли."

        e "*Девочки умиляются*"

        play sound "audio/womens_laugh.mp3"
    
    scene school_corridor

    show first

    girl_1 "Знаешь, ты мне... нравишься... Давай п-п-погуляем вечером после школы..."

    e "*закручивает волосы*"

    play sound "audio/uwu.mp3"

    menu:
        "Ваше действие?"
        "Отказаться от предложения":
            e "*Проходит 20 лет*"
            if bad_answers > 4:
                "[name] заметил перемены в себе, он решил, что неожиданные деньги только искушают его. Он отдал все деньги в благотворительность и стал жить как раньше."
            else:
                "[name] со временем научился разумно пользоваться деньгами. На них он смог прожить счастливую жизнь, ни в чем себе не отказывая."
        "Согласиться на её предложение":
            scene girl_room

            e "Девочка и [name] приходят к ней домой"

            show gr_normal at posL

            show first at posR

            e "Девочка кидает [name] на кровать и садится на него сверху."

            girl_1 "я т-тебя л-люблю..."

            scene knife

            girl_1 "Признавайся! Откуда у тебя на всё это?! Я тебя убью, если не скажешь, куда спрятал их!"

            play sound "audio/knife.mp3"

            menu:
                "Ваше действие?"
                "Я ничего тебе не скажу, д-д-дура!":
                    pass
                "Я во всём сознаюсь, только не убивай!!!":
                    pass
            
            scene girl_room

            show first at posL

            show gr_normal at posR

            girl_1 "Ты был мне полезен ровно до этого момента. Теперь попращайся со своей жизнью!"

            hide first

            hide gr_normal

            e "Девочка пронзает шею [name]"

            play sound "audio/roblox-death-sound-effect.mp3"

            "Главный герой был зарезан девушкой."


