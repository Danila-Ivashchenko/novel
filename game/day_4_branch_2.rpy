init:
    $ day_4_left_school = False
    
label day_4_branch_2:

    stop music
    stop sound
    play music "audio/fight.mp3"
    
    scene bg_sc

    show gr mone at posR
    show b normal at posL

    b "Ах ты мелкий......."

    menu:
        "Что же делать дальше?"
        "Остаться на месте":
            pass
        "Убежать из школы":
            $ day_4_left_school = True
        
    if day_4_left_school:
        if bad_answers >= 6:
            hide gr mone
            hide b normal
            play music "audio/main_motiv.mp3"
            scene bg_pg
            e "*Главный герой несколько часов гуляет по улице, обдумывая правильно ли он поступил, что убежал*\n*Из-за поворота выходит подозрительный мужчина*
    Бандит: *Кричит имя главного героя* и ускоряет шаг"
            show gr normal at posL
            show bandit at posR

            e "*Бандит хватает мальчика*"

            bandit "*Бандит хватает мальчика*
    бандит: хаха, слухи в школе разошлись очень быстро. Мы с моим кентом как раз потеряли сумку денег.
    Да ты не бойся, мы уже вычислили где ты живёшь и забрали свои деньги и замочили твою мамку...ха-аха... Осталось устранить последнего свидетеля..."
            stop music
            play sound "audio/pistol.mp3"
            e "*[name] не успел закричать о помощи, и умер от пули в лоб(*"
            jump end_8
        else:
            play music "audio/main_motiv.mp3"
            scene bg_pg
            hide gr mone
            hide b normal
            e "*Главный герой несколько часов гуляет по улице, обдумывая правильно ли он поступил, что убежал*"
            e "*Главный герой слышит  как кричат его имя группа людей*\n*Оказывается это был B со своими друзьями*"
            show b normal at posR
            show gr normal at posL
            b "B:Ты думал, что я всё это так оставлю. {w=1}Да ты...{w=1} да я...\nты обоснуй свои действия, чтобы потом о здоровье не пожалеть"
            if bad_answers >= 4:
                gr "Ты шутишь про меня, но настоящую шутку сыграла с тобой жизнь."

                e "друзья В:*Начали смеяться над B и показывать в него пальцами* -Вот ты выдал, малой B:Расплакался и убежал в слезах подальше от этого"
                b "((((плак плак"
                jump end_9
                return
            else:
                b "Моли о пощаде, ботан."
                gr "Оставь меня в покое, п..п...прошу!"
                
                jump end_10
                return
    else:
        b "B: *В недоумении* Ты оборзел! В себя поверил?? *Замахивается рукой*"
        e "*В драку вмешивается директор*"
        hide gr mone
        hide b normal
        show d angry
        show gr mone at posRl
        show b normal at posLl
        d "Юноши, что вы себе позволяете, срочно в мой кабинет! Я вызываю в школу ваших родителей"
        hide gr mone
        hide b normal
        hide d angry
        stop music
        stop sound
        play music "audio/main_motiv.mp3"
        e "[name] ждёт свою мать в кабинете директора."
        show m normal at posL
        show gr normal at posR
        m "Сынок, что это такое?! И что за одежда на тебе?!Я тебе её не покупала!"
        e "[name] сознаётся во всём."
        gr "Мама, я нашёл деньги и купил себе вещи."
        hide m normal
        hide gr normal

        jump end_7
        

        