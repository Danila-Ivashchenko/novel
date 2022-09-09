label day_4:

    scene room

    show g_normal

    e "[name] просыпается и собирается в школу в новых вещах"

    g "*вздох*"

    g "Снова а школу... Надеюсь, что хоть что-то изменится"

    scene school

    show g_normal
    
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
            $answer += 1
    
    scene school_corridor

    e "К [name] подходит гопник"

    show b_normal at posL

    show g_normal at posR

    b "Э, анимешник, потеряйся. Ты меня, видимо, не понял в прошлый раз. Походу, придется напомнить твое место."

    show g_scared at posR

    menu:
        "Предложить сотрудничество.":
            $answer += 1
            jump day_4_branch_1 
        "Ударить по лицу пачкой денег.":
            $answer += 2   
            jump day_4_branch_2
            
    