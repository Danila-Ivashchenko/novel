init:
    image end_bg_2 = 'images/scenes/terpila.png'
label end_2:
    stop music 
    scene end_bg_2
    play sound "audio/defeat.mp3"
    e "Главный герой во всём сознаётся своей маме. Мама покидает сына, присвоив себе все деньги."
    e "Конец"
    return