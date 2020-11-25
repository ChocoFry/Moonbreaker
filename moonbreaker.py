import pygame as pg
import time as t
import random as r
import sys
from threading import Timer
pg.init()
last = pg.time.get_ticks()
now = pg.time.get_ticks()

scr = pg.display.set_mode((1366, 768))
scr.fill((40, 50, 50))
pg.display.set_caption("Moonbreaker")
pg.display.set_icon(pg.image.load("logo_small.png"))
pg.display.flip()

play_ = False
play_button = False
text__ = False
tut = False
fivecannons = False
cannons = False
demo_ = False
cannon1shoot = False
cannon2shoot = False
cannon3shoot = False
cannon4shoot = False
cannon5shoot = False
planet_ = False

font = pg.font.Font("pixelfont.ttf", 32)
font1 = pg.font.Font("pixelfont.ttf", 64)
text1 = "Hello"
text2 = "Hello"
text3 = "Hello"
text4 = "Hello"
text5 = "Hello"
text1_ = font.render(str(text1), True, (255, 255, 255))
text2_ = font.render(str(text2), True, (255, 255, 255))
text3_ = font.render(str(text3), True, (255, 255, 255))
text4_ = font.render(str(text4), True, (255, 255, 255))
text5_ = font.render(str(text5), True, (255, 255, 255))

play = pg.image.load("button_play.png")
cannon1 = pg.image.load("red_cannon.png")
cannon2 = pg.image.load("red_cannon.png")
cannon3 = pg.image.load("red_cannon.png")
cannon4 = pg.image.load("red_cannon.png")
cannon5 = pg.image.load("red_cannon.png")
laser1 = pg.image.load("full_laser.png")
laser2 = pg.image.load("full_laser.png")
laser3 = pg.image.load("full_laser.png")
laser4 = pg.image.load("full_laser.png")
laser5 = pg.image.load("full_laser.png")
Earth = pg.image.load("Earth.png")
Lunalus = pg.image.load("Lunalus.png")
Mars = pg.image.load("Mars.png")
Phobos = pg.image.load("Phobos.png")
Deimos = pg.image.load("Deimos.png")
Neptune = pg.image.load("Neptune.png")
Triton = pg.image.load("Triton.png")
Proteus = pg.image.load("Proteus.png")
Uranus = pg.image.load("Uranus.png")
Ariel = pg.image.load("Ariel.png")
Titania = pg.image.load("Titania.png")

soundclick = pg.mixer.Sound("sound_click.wav")
soundshoot = pg.mixer.Sound("sound_shoot.wav")

play_button_click = pg.draw.rect(scr, (175, 175, 20), (555, 400, 256, 256))
cannon1_click = pg.draw.rect(scr, (175, 175, 20), (0, 0, 128, 128))
cannon2_click = pg.draw.rect(scr, (175, 175, 20), (0, 160, 128, 128))
cannon3_click = pg.draw.rect(scr, (175, 175, 20), (0, 320, 128, 128))
cannon4_click = pg.draw.rect(scr, (175, 175, 20), (0, 480, 128, 128))
cannon5_click = pg.draw.rect(scr, (175, 175, 20), (0, 640, 128, 128))

planet = r.choice((Neptune, Mars))
moon = Triton
moonstate = 1

score = 1
score_ = font.render(str(score), True, (255, 255, 255))

def main():
    global background, play_button
    play_button = True
    scr.blit(pg.image.load("background.png"), (0, 0))
    scr.blit(pg.image.load("logo.png"), (353, 100))
    scr.blit(play, (555, 400))
    pg.display.flip()
    menumusic = pg.mixer_music.load("moonbreaker_menumusic.wav")
    pg.mixer_music.play(-1)

def text_change(newtext1, newtext2, newtext3, newtext4, newtext5, sound):
    global text1, text2, text3, text4, text5, skiptut_
    text1 = newtext1
    text2 = newtext2
    text3 = newtext3
    text4 = newtext4
    text5 = newtext5
    pg.mixer.Sound(sound).play()

def lasercannons():
    global fivecannons
    fivecannons = True
    scr.blit(pg.image.load("5lasercannons.png"), (555, 200))
    pg.display.flip()

def lasercannonsstop():
    global fivecannons, cannons
    fivecannons = False
    cannons = True
    scr.blit(cannon1, (0, 0))
    scr.blit(cannon2, (0, 160))
    scr.blit(cannon3, (0, 320))
    scr.blit(cannon4, (0, 480))
    scr.blit(cannon5, (0, 640))

def demo():
    global demo_
    demo_ = True
    scr.blit(pg.image.load("demo.png"), (555, 200))
    pg.display.flip()

def demostop():
    global demo_
    demo_ = False

def preplay():
    global play_, tut, cannons, text__
    tut = False
    play_ = True
    cannons = True
    text__ = False
    scr.blit(cannon1, (0, 0))
    scr.blit(cannon2, (0, 160))
    scr.blit(cannon3, (0, 320))
    scr.blit(cannon4, (0, 480))
    scr.blit(cannon5, (0, 640))
    scr.blit(pg.image.load("background.png"), (0, 0))
    playgame()

def tutorial():
    global text__, tut, text1, text2, text3, text4, text5
    text__ = True
    tut = True
    scr.blit(pg.image.load("game_background.png"), (0, 0))
    scr.blit(pg.image.load("tutorial_guy.png"), (0, 448))
    pg.mixer.Sound("speech1.wav").play()
    text1 = "Welcome, traveller, to the"
    text2 = "year 2999!"
    text3 = ""
    text4 = ""
    text5 = ""
    Timer(4, text_change, ("Here, we send our spaceships", "to distant planets!", "", "", "", "speech2.wav")).start()
    Timer(8, text_change, ("But, recently, we have found", "some issues with our", "pursuits...", "", "", "speech3.wav")).start()
    Timer(13, text_change, ("We found that planets have", "these things called \"Moons\".", "", "", "", "speech4.wav")).start()
    Timer(18, text_change, ("They are very bad.", "", "", "", "", "speech5.wav")).start()
    Timer(21, text_change, ("I hate them.", "", "", "", "", "speech6.wav")).start()
    Timer(23, text_change, ("So, it's your job to", "DESTROY them!", "", "", "", "speech7.wav")).start()
    Timer(26, text_change, ("You will get these 5", "laser cannons...", "", "", "", "speech8.wav")).start()
    Timer(26, lasercannons).start()
    Timer(29, text_change, ("They look really cool.", "", "", "", "", "speech9.wav")).start()
    Timer(31, text_change, ("I wish I had one.", "", "", "", "", "speech10.wav")).start()
    Timer(34, lasercannonsstop).start()
    Timer(34, text_change, ("So, this is how they", "work...", "", "", "", "speech11.wav")).start()
    Timer(37, text_change, ("You click on them,", "they shoot lasers.", "", "", "", "speech12.wav")).start()
    Timer(40, text_change, ("You will need to shoot", "Moons orbiting around", "planets...", "", "", "speech13.wav")).start()
    Timer(44, text_change, ("Moons are like a blockade", "for our spaceships.", "As shown in this high", "detail demonstration.", "", "speech14.wav")).start()
    Timer(44, demo).start()
    Timer(50, text_change, ("You have to DESTROY the", "Moons with the 5 laser", "cannons, but be careful, you", "may accidently destroy", "the planets...", "speech15.wav")).start()
    Timer(50, demostop).start()
    Timer(57, preplay).start()

def play_button_click_check():
    global play_button
    if play_button:
        pos = pg.mouse.get_pos()
        if play_button_click.collidepoint(pos):
            play = pg.image.load("button_play_hover.png")
            scr.blit(play, (555, 400))
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                play_button = False
                soundclick.play()
                pg.mixer.music.stop()
                tutorial()
        else:
            play = pg.image.load("button_play.png")
            scr.blit(play, (555, 400))
            pg.display.flip()

def cannon_click_check():
    global cannons, cannon1, cannon2, cannon3, cannon4, cannon5, cannon1shoot, cannon2shoot, cannon3shoot, cannon4shoot, cannon5shoot, laser, laser2, laser3, laser4, laser5
    if cannons:
        pos = pg.mouse.get_pos()
        if cannon1_click.collidepoint(pos):
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                soundshoot.play()
                cannon1 = pg.image.load("red_cannon_shooting.png")
                cannon1shoot = True
                scr.blit(laser1, (128, 0))
                Timer(0.5, cannon1stop).start()

        if cannon2_click.collidepoint(pos):
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                soundshoot.play()
                cannon2 = pg.image.load("red_cannon_shooting.png")
                cannon2shoot = True
                scr.blit(laser2, (128, 160))
                Timer(0.5, cannon2stop).start()

        if cannon3_click.collidepoint(pos):
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                soundshoot.play()
                cannon3 = pg.image.load("red_cannon_shooting.png")
                cannon3shoot = True
                scr.blit(laser3, (128, 320))
                Timer(0.5, cannon3stop).start()

        if cannon4_click.collidepoint(pos):
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                soundshoot.play()
                cannon4 = pg.image.load("red_cannon_shooting.png")
                cannon4shoot = True
                scr.blit(laser4, (128, 480))
                Timer(0.5, cannon4stop).start()

        if cannon5_click.collidepoint(pos):
            pg.display.flip()
            if event.type == pg.MOUSEBUTTONDOWN:
                soundshoot.play()
                cannon5 = pg.image.load("red_cannon_shooting.png")
                cannon5shoot = True
                scr.blit(laser5, (128, 640))
                Timer(0.5, cannon5stop).start()

def screenmove(screen, loc):
    scr.blit(pg.image.load("game_background.png"), (0, 0))
    scr.blit(pg.image.load(screen), loc)

def loose():
    global play_, text__, tut, cannons, planet_
    play_ = False
    text__ = False
    tut = False
    cannons = False
    planet_ = False
    pg.mixer_music.stop()
    pg.mixer.Sound("sound_loose.wav").play()
    scr.blit(pg.image.load("loose.png"), (0, 768))
    Timer(0.3, screenmove, ("loose.png", (0, 668))).start()
    Timer(0.6, screenmove, ("loose.png", (0, 568))).start()
    Timer(0.9, screenmove, ("loose.png", (0, 468))).start()
    Timer(1.2, screenmove, ("loose.png", (0, 368))).start()
    Timer(1.5, screenmove, ("loose.png", (0, 268))).start()
    Timer(1.8, screenmove, ("loose.png", (0, 168))).start()
    Timer(2.1, screenmove, ("loose.png", (0, 68))).start()
    Timer(2.4, screenmove, ("loose.png", (0, 0))).start()

def loosecheck():
    global score
    if score <= 0:
        loose()
        score = 1

def win():
    global play_, text__, tut, cannons, planet_
    play_ = False
    text__ = False
    tut = False
    cannons = False
    planet_ = False
    pg.mixer_music.stop()
    pg.mixer.Sound("sound_win.wav").play()
    scr.blit(pg.image.load("win.png"), (0, 768))
    Timer(0.3, screenmove, ("win.png", (0, 668))).start()
    Timer(0.6, screenmove, ("win.png", (0, 568))).start()
    Timer(0.9, screenmove, ("win.png", (0, 468))).start()
    Timer(1.2, screenmove, ("win.png", (0, 368))).start()
    Timer(1.5, screenmove, ("win.png", (0, 268))).start()
    Timer(1.8, screenmove, ("win.png", (0, 168))).start()
    Timer(2.1, screenmove, ("win.png", (0, 68))).start()
    Timer(2.4, screenmove, ("win.png", (0, 0))).start()

def cannon1stop():
    global cannon1shoot, cannon1
    cannon1shoot = False
    cannon1 = pg.image.load("red_cannon.png")

def cannon2stop():
    global cannon2shoot, cannon2
    cannon2shoot = False
    cannon2 = pg.image.load("red_cannon.png")

def cannon3stop():
    global cannon3shoot, cannon3
    cannon3shoot = False
    cannon3 = pg.image.load("red_cannon.png")

def cannon4stop():
    global cannon4shoot, cannon4
    cannon4shoot = False
    cannon4 = pg.image.load("red_cannon.png")

def cannon5stop():
    global cannon5shoot, cannon5
    cannon5shoot = False
    cannon5 = pg.image.load("red_cannon.png")

def playgame():
    scr.blit(pg.image.load("background.png"), (0, 0))
    gamemusic = pg.mixer_music.load("moonbreaker_gamemusic.wav")
    pg.mixer_music.play(-1)
    planetsummon()

def earthsummon():
    global planet_, planet, moon, planetloc, moonloc
    planet_ = True
    planet = Earth
    moon = Lunalus
    planetloc = (1302, 256)
    moonloc = (planetloc[0] - 172, planetloc[1] + 64)
    scr.blit(planet, planetloc)
    scr.blit(moon, moonloc)
    moonstate = 2
    Timer(0.1, planetmove).start()

def bosstext():
    global text__, text1, text2, text3, text4, text5
    pg.mixer_music.stop()
    text__ = True
    pg.mixer.Sound("speech16.wav").play()
    text1 = "Wow, look, it's Earth. That's"
    text2 = "where you are right now."
    text3 = ""
    text4 = ""
    text5 = ""
    Timer(3, text_change, ("It would be a real shame", "if you missed, 'cause", "that's your home and", "stuff.", "", "speech17.wav")).start()
    Timer(8, earthsummon).start()

def planetsummon():
    global planet_, planet, moon, planetloc, moonloc
    if score < 50:
        planet_ = True
        planet = r.choice((Neptune, Mars, Uranus))
        if planet == Neptune:
            moon = r.choice((Triton, Proteus))
        if planet == Mars:
            moon = r.choice((Phobos, Deimos))
        if planet == Uranus:
            moon = r.choice((Ariel, Titania))
        planetloc = r.choice(((1302, -64), (1302, 96), (1302, 256), (1302, 416), (1302, 576)))
        moonloc = (planetloc[0] - 172, planetloc[1] + 64)
        scr.blit(planet, planetloc)
        scr.blit(moon, moonloc)
        moonstate = 2
        Timer(0.3, planetmove).start()
    else:
        bosstext()

def planetmove():
    global moonstate, planetloc, moonloc
    if planet_:
        planetloc = (planetloc[0] - 64, planetloc[1])
        if moonstate == 1:
            moonloc = (planetloc[0] - 192, planetloc[1] + 64)
            scr.blit(moon, moonloc)
            moonstate = 2
        elif moonstate == 2:
            moonloc = (planetloc[0] - 192, planetloc[1] + 320)
            scr.blit(moon, moonloc)
            moonstate = 3
        elif moonstate == 3:
            moonloc = (planetloc[0] + 64, planetloc[1] + 320)
            scr.blit(moon, moonloc)
            moonstate = 4
        elif moonstate == 4:
            moonloc = (planetloc[0] + 320, planetloc[1] + 320)
            scr.blit(moon, moonloc)
            moonstate = 5
        elif moonstate == 5:
            moonloc = (planetloc[0] + 320, planetloc[1] + 64)
            scr.blit(moon, moonloc)
            moonstate = 6
        elif moonstate == 6:
            moonloc = (planetloc[0] + 320, planetloc[1] - 192)
            scr.blit(moon, moonloc)
            moonstate = 7
        elif moonstate == 7:
            moonloc = (planetloc[0] + 64, planetloc[1] - 192)
            scr.blit(moon, moonloc)
            moonstate = 8
        elif moonstate == 8:
            moonloc = (planetloc[0] - 192, planetloc[1] - 192)
            scr.blit(moon, moonloc)
            moonstate = 1
        if planet == Earth:
            Timer(0.1, planetmove).start()
        if planet is not Earth:
            Timer(0.3, planetmove).start()

def planetdone():
    global planet_, play, score, planetloc, moonloc, planet, Earth
    if play_:
        if planet_:
            if planetloc[0] <= 0 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1
            if cannon1shoot and 0 < moonloc[1] + 64 < 160 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score += 1
            elif cannon1shoot and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1
            if cannon2shoot and 160 < moonloc[1] + 64 < 320 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score += 1
            elif cannon2shoot and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1
            if cannon3shoot and 320 < moonloc[1] + 64 < 480 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score += 1
            elif cannon3shoot and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1
            if cannon4shoot and 480 < moonloc[1] + 64 < 640 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score += 1
            elif cannon4shoot and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1
            if cannon5shoot and 640 < moonloc[1] + 64 < 768 and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score += 1
            elif cannon5shoot and planet is not Earth:
                planet_ = False
                Timer(2, planetsummon).start()
                score -= 1

            if planet == Earth:
                if planetloc[0] <= 0:
                    planet_ = False
                    score -= 100
                if cannon1shoot and 0 < moonloc[1] + 64 < 160:
                    planet_ = False
                    score = 1
                    Timer(1, win).start()
                elif cannon1shoot:
                    planet_ = False
                    score -= 100
                if cannon2shoot and 160 < moonloc[1] + 64 < 320:
                    planet_ = False
                    score = 1
                    Timer(1, win).start()
                elif cannon2shoot:
                    planet_ = False
                    score -= 100
                if cannon3shoot and 320 < moonloc[1] + 64 < 480:
                    planet_ = False
                    score = 1
                    Timer(1, win).start()
                elif cannon3shoot:
                    planet_ = False
                    score -= 100
                if cannon4shoot and 480 < moonloc[1] + 64 < 640:
                    planet_ = False
                    score = 1
                    Timer(1, win).start()
                elif cannon4shoot:
                    planet_ = False
                    score -= 100
                if cannon5shoot and 640 < moonloc[1] + 64 < 768:
                    planet_ = False
                    score = 1
                    Timer(1, win).start()
                elif cannon5shoot:
                    planet_ = False
                    score -= 100

def reblit():
    if tut:
        scr.blit(pg.image.load("game_background.png"), (0, 0))
        text1_ = font.render(str(text1), True, (255, 255, 255))
        text2_ = font.render(str(text2), True, (255, 255, 255))
        text3_ = font.render(str(text3), True, (255, 255, 255))
        text4_ = font.render(str(text4), True, (255, 255, 255))
        text5_ = font.render(str(text5), True, (255, 255, 255))

        if fivecannons:
            scr.blit(pg.image.load("5lasercannons.png"), (555, 200))

        if demo_:
            scr.blit(pg.image.load("demo.png"), (555, 200))

        if cannons:
            scr.blit(cannon1, (0, 0))
            scr.blit(cannon2, (0, 160))
            scr.blit(cannon3, (0, 320))
            scr.blit(cannon4, (0, 480))
            scr.blit(cannon5, (0, 640))
            if cannon1shoot:
                scr.blit(laser1, (128, 0))
            if cannon2shoot:
                scr.blit(laser2, (128, 160))
            if cannon3shoot:
                scr.blit(laser3, (128, 320))
            if cannon4shoot:
                scr.blit(laser4, (128, 480))
            if cannon5shoot:
                scr.blit(laser5, (128, 640))

        scr.blit(pg.image.load("tutorial_guy.png"), (0, 448))

        if text__:
            scr.blit(text1_, (175, 500))
            scr.blit(text2_, (175, 525))
            scr.blit(text3_, (175, 550))
            scr.blit(text4_, (175, 575))
            scr.blit(text5_, (175, 600))

    if play_:
        scr.blit(pg.image.load("game_background.png"), (0, 0))

        if cannons:
            scr.blit(cannon1, (0, 0))
            scr.blit(cannon2, (0, 160))
            scr.blit(cannon3, (0, 320))
            scr.blit(cannon4, (0, 480))
            scr.blit(cannon5, (0, 640))

            if planet_:
                scr.blit(planet, planetloc)
                scr.blit(moon, moonloc)

            if cannon1shoot:
                scr.blit(laser1, (128, 0))
            if cannon2shoot:
                scr.blit(laser2, (128, 160))
            if cannon3shoot:
                scr.blit(laser3, (128, 320))
            if cannon4shoot:
                scr.blit(laser4, (128, 480))
            if cannon5shoot:
                scr.blit(laser5, (128, 640))

        score_ = font1.render(str(score), True, (255, 255, 255))
        scr.blit(score_, (1166, 64))


        if text__:
            scr.blit(pg.image.load("tutorial_guy.png"), (0, 448))

            text1_ = font.render(str(text1), True, (255, 255, 255))
            text2_ = font.render(str(text2), True, (255, 255, 255))
            text3_ = font.render(str(text3), True, (255, 255, 255))
            text4_ = font.render(str(text4), True, (255, 255, 255))
            text5_ = font.render(str(text5), True, (255, 255, 255))

            scr.blit(text1_, (175, 500))
            scr.blit(text2_, (175, 525))
            scr.blit(text3_, (175, 550))
            scr.blit(text4_, (175, 575))
            scr.blit(text5_, (175, 600))
main()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit

    play_button_click_check()
    loosecheck()
    cannon_click_check()
    planetdone()
    reblit()

    pg.display.flip()