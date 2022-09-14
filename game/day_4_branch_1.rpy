label day_4_branch_1:
    scene school_corridor

    show gr smile at posR

    show b normal at posL

    g "Подожди, громила, не торопись. Я предложу тебе то, от чего ты не сможешь отказаться."

    g "Я дам тебе денег, а ты мне защиту от таких, как ты."

    b "Хах... ты мне деньги? За это мне просто не нужно бить тебя? Хорошо."

    scene bg_sc

    show gr smile at posR

    show b slave at posL

    e "[name] сидит на задней парте, вокруг него вьются девочки, сбоку стоит гопник и охраняет его."

    if bad_answers > 5:

        show gr smile

        girl_1 "Знаете, я ведь могу купить даже жену директора, хахах."

        e "Девочки смеются."

        play sound "womens_laugh.mp3"
    
    else:

        show gr smile

        g "Знаете, я ведь могу купить всё, о чем вы и мечтать не могли."

        e "*Девочки умиляются*"

        play sound "audio/womens_laugh.mp3"
    
    scene bg_sc

    show g_1

    g "Знаешь, ты мне... нравишься... Давай п-п-погуляем вечером после школы..."

    e "*закручивает волосы*"

    play sound "audio/uwu.mp3"

    menu:
        "Ваше действие?"
        "Отказаться от предложения":
            e "*Проходит 20 лет*"
            if bad_answers > 4:
                jump end_4
            else:
                jump end_5


        "Согласиться на её предложение":

            scene bg_gr
            stop music
            stop sound
            play music "audio/Love.mp3"
            e "Девочка и [name] приходят к ней домой"

            show gr normal at posL

            show g_1 at posR

            e "Девочка кидает [name] на кровать и садится на него сверху."

            girl_1 "я т-тебя л-люблю..."

            scene bg_k

            stop music
            play sound "audio/knife.mp3"
            girl_1 "Признавайся! Откуда у тебя деньги на всё это?! Я тебя убью, если не скажешь, куда спрятал их!"



            menu:
                "Ваше действие?"
                "Я ничего тебе не скажу, д-д-дура!":
                    pass
                "Я во всём сознаюсь, только не убивай!!!":
                    pass
        

            girl_1 "Ты был мне полезен ровно до этого момента. Теперь попращайся со своей жизнью!"


            e "Девочка пронзает шею [name]"

            stop sound
            stop music
            play sound "audio/roblox-death-sound-effect.mp3"

            jump end_6



