label day_4:

    scene room

    show gr normal

    e "[name] просыпается и собирается в школу в новых вещах"

    g "*вздох*"

    g "Снова а школу... Надеюсь, что хоть что-то изменится"

    scene school

    show gr normal
    
    e "[name] приходит в школу"

    scene school_corridor

    show first at posL

    show second at center

    show third at posR

    e "Одноклассницы без ума от нового образа [name]"

    girl_1 "Девочкиииии, [name] такой сегодня красивый... Уииииии..."

    girl_2 "Дааааа, когда он успел так изменится?!"

    $root = False
    menu:
        "Твои действия?"
        "*Пройти мимо*":
            $root = True
        "*Подмигнуть одноклассницам*":
            $bad_answers += 1
    
    scene school_corridor

    e "К [name] подходит гопник"

    show b_normal at posL

    show gr_normal at posR

    b "Э, анимешник, потеряйся. Ты меня, видимо, не понял в прошлый раз. Походу, придется напомнить твое место."

    hide gr_normal

    show gr_smile at posR

    menu:
        "Предложить сотрудничество.":
            $bad_answers += 1
            jump day_4_branch_1 
        "Ударить по лицу пачкой денег.":
            $bad_answers += 2   
            jump day_4_branch_2
            
    