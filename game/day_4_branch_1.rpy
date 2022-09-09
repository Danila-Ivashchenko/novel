label day_4_branch_1:
    scene school_corridor

    show g_smile at posL

    show b_normal at posR

    g "Подожди, громила, не торопись. Я предложу тебе то, от чего ты не сможешь отказаться."

    g "Я дам тебе денег, а ты мне защиту от таких, как ты."

    b "Хах... ты мне деньги? За это мне просто не нужно бить тебя? Хорошо."

    scene school_corridor

    show g_smile at posL

    show b_slave at posR

    e "[name] сидит на задней парте, вокруг него вьются девочки, сбоку стоит гопник и охраняет его."

    if bad_answers > 5:
        scene school_corridor

        show g_smile

        g "Знаете, я ведь могу купить даже жену директора, хахах."

        e "Девочки смеются."

        play sound "womens_laugh.mp3"
    
    else:
        scene school_corridor

        show g_smile

        g "Знаете, я ведь могу купить всё, о чем вы и мечтать не могли."

        e "*Девочки умиляются*"

        play sound "womens_laugh.mp3"
    
    scene school_corridor

    show g_1

    girl_1 "Знаешь, ты мне... нравишься... Давай п-п-погуляем вечером после школы..."

    e "*закручивает волосы*"

    play sound "uwu.mp3"

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

            show g_normal at posL

            show g_1 at posR

            scene girl_room

            e "Девочка кидает [name] на кровать и садится на него сверху."

            show g_1 at posR

            show g_normal at posL

            girl_1 "я т-тебя л-люблю..."

            scene knife

            girl_1 "Признавайся! Откуда у тебя на всё это?! Я тебя убью, если не скажешь, куда спрятал их!"

            play sound "knife.mp3"

            menu:
                "Ваше действие?"
                "Я ничего тебе не скажу, д-д-дура!":
                    pass
                "Я во всём сознаюсь, только не убивай!!!":
                    pass
            
            scene girl_room

            show g_1 at posL

            show g_scared at posR

            girl_1 "Ты был мне полезен ровно до этого момента. Теперь попращайся со своей жизнью!"

            hide g_1

            hide g_scared

            e "Девочка пронзает шею [name]"

            play sound "roblox-death-sound-effect.mp3"

            "Главный герой был зарезан девушкой."


