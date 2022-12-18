import pygame
import pygame_gui

pygame.init()

# akna moodud - 800 x 640 ehk 25 x 20 tile'i
akna_laius = 800
akna_korgus = 640

aken = pygame.display.set_mode((akna_laius, akna_korgus))

class Ruut(pygame.sprite.Sprite):
    
    def __init__(self, x, y, pildi_nr, grupp, alamgrupp = ""):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'ruudud/ruut_{pildi_nr}.png'), (32, 32))
        if pildi_nr in [5, 14, 15, 16]:
            alamgrupp.add(self)

        grupp.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

ruudud = pygame.sprite.Group()
platvormid = pygame.sprite.Group()



ruudustik = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 14, 15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 0, 14, 15, 15, 15, 15],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 14, 15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 14, 15, 15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 14, 15, 15, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 0, 0, 14, 15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 14, 15, 15, 15, 15, 15, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
]

# ruudustik platvormideks
for rida in range(len(ruudustik)):
    for veerg in range(len(ruudustik[rida])):
        if ruudustik[rida][veerg] == 2:
            Ruut(veerg*32, rida*32, 2, ruudud)
        elif ruudustik[rida][veerg] == 5:
            Ruut(veerg*32, rida*32, 5, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 14:
            Ruut(veerg*32, rida*32, 14, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 15:
            Ruut(veerg*32, rida*32, 15, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 16:
            Ruut(veerg*32, rida*32, 16, ruudud, platvormid)


#main muusika
#muusikapala ise
pygame.mixer.music.load("Sounds/mystery.mp3")
#et lõputult mängiks
pygame.mixer.music.play(-1)

#muusika algne valjusus
valjusus = 0.5
pygame.mixer.music.set_volume(valjusus)

#liugur et mängija saaks valjusust muuta
manager = pygame_gui.UIManager([akna_laius, akna_korgus])
liugur_music = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((690, 615), (100, 20)),
                                                      50, (0,100), manager)

taust_pilt = pygame.transform.scale(pygame.image.load(f'img/taust.png'), (800, 640))
taust_rect = taust_pilt.get_rect()
taust_rect.topleft = (0, 0)


vamp_img_r = pygame.transform.scale(pygame.image.load('img/vampiir_0.png'), (60, 83))
vamp_img_l = pygame.transform.flip(vamp_img_r, True, False)

# fps ja kell
fps = 30
kell = pygame.time.Clock()

mario_x = 200
mario_y = 200
kiirus_x = 0
kiirus_y = 5
kiirendus_x = 20
inerts = 0.9
gravitatsioon = 15
hype = 100


class Vampiir(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = vamp_img_r
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.kiirus = 5

    def update(self):
        self.liikumine()
        self.kontrolli_porkeid()

    def liikumine(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.kiirus
            self.image = vamp_img_l

        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.kiirus
            self.image = vamp_img_r

    def kontrolli_porkeid(self):
        pass

vampiirid = pygame.sprite.Group()
vampiir = Vampiir(akna_laius/2, akna_korgus/2)
vampiirid.add(vampiir)



mang_kaib = True

while mang_kaib:

    dt = kell.tick(fps) / 1000

    aken.blit(taust_pilt, taust_rect)

    vampiirid.update()
    vampiirid.draw(aken)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            mang_kaib = False
            
        elif e.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if e.ui_element == liugur_music:
                pygame.mixer.music.set_volume(e.value/100)
        
        manager.process_events(e)
            
        if e.type == pygame.KEYDOWN:
            # hyppamine
            if e.key == pygame.K_SPACE:
                if mario_y > 2 * hype:
                    mario_y -= hype
    ruudud.draw(aken)



    mario_x += dt * kiirus_x

    # # kui nupuvajutust ei ole, siis x kiirus vaheneb
    # kiirus_x *= inerts

    # asukoht = mario.get_rect(center=(mario_x, mario_y))

    # aknast_valjas = False
 
    # # kontrollime, kas mario on ekraanist valja lennanud

    # if asukoht[0] < 0:
    #     asukoht.move_ip(akna_laius, 0)
    #     aknast_valjas = True

    # if asukoht[0] + mario.get_width() > akna_laius:
    #     asukoht.move_ip(-akna_laius, 0)
    #     aknast_valjas = True

    # # gravitatsioon
    # if asukoht[1] + mario.get_height() + 5 < akna_korgus and asukoht[1] + mario.get_height() > hype:
    #     kiirus_y += gravitatsioon
    #     mario_y += dt * kiirus_y
    # else:
    #     kiirus_y = 0

    # # kui valjas ekraanist vasakult/paremalt siis joonistame mario siia...
    # if aknast_valjas:
    #     aken.blit(mario, asukoht)

    # asukoht[0] = asukoht[0] % akna_laius
    # mario_x = mario_x % akna_laius

    # # ... aga igal juhul ka siia
    # aken.blit(mario, asukoht)
    
    #muusika slideri jaoks vajalikud read
    manager.update(dt)
    manager.draw_ui(aken)

    pygame.display.update()

pygame.quit()