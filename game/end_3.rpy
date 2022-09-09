init:
    image end_bg_3 = 'images/scenes/nespravedlivo.png'
label end_3:
    scene end_bg_3
    stop music
    play sound "audio/defeat.mp3"
    e "Полиция выяснила про деньги, которые нашёл главный герой. Главного героя арестовали."
    e "Конец"
    return