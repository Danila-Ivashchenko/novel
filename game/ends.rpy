init:
    image end_bg_1 = "images/scenes/Frame_2.png"
    image end_bg_2 = 'images/scenes/terpila.png'
    image end_bg_3 = 'images/scenes/nespravedlivo.png'
    image end_bg_4 = 'images/scenes/Frame_2_2.png'
    image end_bg_5 = 'images/scenes/Frame_2_1.png'
    image end_bg_6 = 'images/scenes/Frame_2_3.png'
    image end_bg_7 = 'images/scenes/Frame_2_4.png'
    image end_bg_8 = "images/scenes/Frame_2_3.png"
    image end_bg_9 = 'images/scenes/Frame_2_4.png'
    image end_bg_10 = "images/scenes/wheelchair.jpg"
    image authors = "images/scenes/authors.png"

label end_1:
    stop music
    stop sound
    play sound "audio/win-police.mp3"
    scene end_bg_1
    e "Полиция приехала и забрала деньги, в дальнейшем они выяснили, что их обранили преступники во время ограбления банка."
    e "Интересно, какие непроиятности могли произойти с нашем героем, если бы он забрал эти деньги себе....?"

    scene authors
    e " "
    return

label end_2:
    stop music
    stop sound
    scene end_bg_2
    play sound "audio/defeat.mp3"
    e "Главный герой во всём сознаётся своей маме. Мама покидает сына, присвоив себе все деньги."
    e "Конец"

    scene authors
    e " "
    return

label end_3:
    scene end_bg_3
    stop music
    stop sound
    play sound "audio/defeat.mp3"
    e "Полиция выяснила про деньги, которые нашёл главный герой. Главного героя арестовали."
    e "Конец"

    scene authors
    e " "
    return

label end_4:
    stop music
    stop sound
    scene end_bg_4
    play music "audio/win.mp3"
    "[name] заметил перемены в себе, он решил, что неожиданные деньги только искушают его. Он отдал все деньги в благотворительность и стал жить как раньше."
    
    scene authors
    e " "
    return

label end_5:
    stop music
    stop sound
    scene end_bg_5
    play music "audio/win.mp3"
    e "[name] со временем научился разумно пользоваться деньгами. На них он смог прожить счастливую жизнь, ни в чем себе не отказывая."
    
    scene authors
    e " "
    return

label end_6:
    stop music
    stop sound
    scene end_bg_6
    play sound "audio/defeat.mp3"
    e "Главный герой был зарезан девушкой."
    
    scene authors
    e " "
    return

label end_7:
    stop music
    stop sound
    play sound "audio/win.mp3"
    scene end_bg_7
    e "Главный герой сознаётся во всём своей маме. Мама со своим сыном купили дом в другом городе. Главный герой начал ходить в другую школу. Всю школу он проучился без буллинга"
    
    scene authors
    e " "
    return

label end_8:
    stop music
    stop sound
    play sound "audio/defeat.mp3"
    scene end_bg_8
    e "Смерть, она такая, внезапная"
    
    scene authors
    e " "
    return

label end_9:
    stop music
    stop sound
    play sound "audio/win.mp3"
    scene end_bg_9
    e "Главного героя начали уважать в школе."
    
    scene authors
    e " "
    return

label end_10:
    stop music
    stop sound
    play sound "audio/defeat.mp3"
    scene end_bg_8
    e "Главного героя избили до полусмерти. Он остался инвалидом на всю жизнь."
    
    scene authors
    e " "
    return
