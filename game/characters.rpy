init:
    image bg_pg = "images/scenes/playground.jpg"
    image bg_b = "images/scenes/bushes.jpg"
    image bg_r = "images/scenes/room.jpg"
    image bg_sc = "images/scenes/school_corridor.jpg"
    image bg_s = "images/scenes/shop.jpg"
    image bg_gr = "images/scenes/girl_room.jpg"
    image bg_w = "images/scenes/wheelchair.jpg"
    image bg_k = "images/scenes/knife.jpg"

define g = Character("[name]", color="#c8ffc8")         # главный герой
define gr = Character("[name]", color="#c8ffc8")         # главный герой
define girl_1 = Character("Маша", color="#ffe9c8")        # девушка
define girl_2 = Character("Маша", color="#ffe9c8")        # девушка
define girl_3 = Character("Маша", color="#ffe9c8")        # девушка
define b = Character("Гопник", color="#ffe9c8")         # гопник
define bandit = Character("Бандит", color="#ffe9c8")         # гопник
define m = Character("Мама", color="#ffe9c8")           # мама
define d = Character("Директор", color="#ffe9c8")       # директор
define s = Character("Охранник", color="#ffe9c8")       # охранник
define p = Character("Полицейский", color="#ffe9c8")       # полицейский

# слова автора
define n = Character(None, kind=nvl)
define e = Character(None)

image g smile   = "images/characters/g_smile.png"
image g normal  = "images/characters/g_normal.png"
image g beaten  = "images/characters/g_beaten.png"
image g scared  = "images/characters/g_scared.png"

image gr smile   = "images/characters/gr_smile.png"
image gr normal  = "images/characters/gr_normal.png"
image gr mone  = "images/characters/gr_mone.png"

image m normal  = "images/characters/m_normal.png"
image d angry  = "images/characters/d_angry.png"

image g_1   = "images/characters/first.png"
image g_2  = "images/characters/second.png"
image g_3  = "images/characters/third.png"

image b normal = "images/characters/b_normal.png"
image b slave  = "images/characters/b_slave.png"

image s normal = "images/characters/security.png"
image p normal  = "images/characters/policman.png"

image bandit = "images/characters/bandit.png"


init:
    $ posR = Position(xalign=0.8, yalign=0.99)
    $ posL = Position(xalign=0.2, yalign=0.99)
    $ posRl = Position(xalign=0.9, yalign=0.99)
    $ posLl = Position(xalign=0.1, yalign=0.99)