import pygame
import pygame_gui

#vektorid
vektor = pygame.math.Vector2

pygame.init()

# akna moodud - 800 x 640 ehk 25 x 20 tile'i
akna_laius = 800
akna_korgus = 640

aken = pygame.display.set_mode((akna_laius, akna_korgus))
vamp_img_r = pygame.transform.scale(pygame.image.load('img/vampiir_0.png'), (40, 54))
vamp_img_l = pygame.transform.flip(vamp_img_r, True, False)


class Ruut(pygame.sprite.Sprite):
    
    def __init__(self, x, y, pildi_nr, grupp, alamgrupp = ""):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(f'ruudud/ruut_{pildi_nr}.png'), (32, 32))
        if pildi_nr in [2, 14, 15, 16]:
            alamgrupp.add(self)
            self.mask = pygame.mask.from_surface(self.image)

        grupp.add(self)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

ruudud = pygame.sprite.Group()
platvormid = pygame.sprite.Group()

class Vampiir(pygame.sprite.Sprite):

    def __init__(self, x, y, platvormid):
        super().__init__()
        self.image = vamp_img_r
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        self.platvormid = platvormid

        self.asukoht = vektor(x, y)
        self.kiirus = vektor(0, 0)
        self.kiirendus = vektor(0, 0)

        self.kiirus_x = 0
        self.kiirus_y = 20
        self.kiirendus_x = 3
        self.inerts = 0.15
        self.gravitatsioon = 1.5

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.liikumine()
        self.kontrolli_porkeid()

    def liikumine(self):

        #kui klahvivajutusi pole, siis kiirendus.x = 0, kiirendus.y = gravitatsioon)
        self.kiirendus = vektor(0, self.gravitatsioon)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.kiirendus.x = -1*self.kiirendus_x
            self.image = vamp_img_l

        elif keys[pygame.K_RIGHT]:
            self.kiirendus.x = self.kiirendus_x
            self.image = vamp_img_r

        self.kiirendus.x -= self.kiirus.x*self.inerts
        self.kiirus += self.kiirendus
        self.asukoht += self.kiirus + 0.5*self.kiirendus

        if self.asukoht.x < 0:
            self.asukoht.x = akna_laius
        elif self.asukoht.x > akna_laius:
            self.asukoht.x = 0


        self.rect.bottomleft = self.asukoht
    
    def hype(self):
        if pygame.sprite.spritecollide(self, self.platvormid, False):
            self.kiirus.y = -1*self.kiirus_y

    def kontrolli_porkeid(self):
        porked_platvormidega = pygame.sprite.spritecollide(self, self.platvormid, False, pygame.sprite.collide_mask)
        if porked_platvormidega:
            if self.kiirus.y > 1:
                self.asukoht.y = porked_platvormidega[0].rect.top
                self.kiirus.y = 0

vampiirid = pygame.sprite.Group()

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
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        if ruudustik[rida][veerg] == 5:
            Ruut(veerg*32, rida*32, 5, ruudud)
        elif ruudustik[rida][veerg] == 2:
            Ruut(veerg*32, rida*32, 2, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 14:
            Ruut(veerg*32, rida*32, 14, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 15:
            Ruut(veerg*32, rida*32, 15, ruudud, platvormid)
        elif ruudustik[rida][veerg]  == 16:
            Ruut(veerg*32, rida*32, 16, ruudud, platvormid)
        elif ruudustik[rida][veerg] == 100:
            vampiir = Vampiir(veerg*32, rida*32+32, platvormid)
            vampiirid.add(vampiir)


#main muusika
#muusikapala ise
pygame.mixer.music.load("Sounds/mystery.mp3")
#et l??putult m??ngiks
pygame.mixer.music.play(-1)

#muusika algne valjusus
valjusus = 0.5
pygame.mixer.music.set_volume(valjusus)

#liugur et m??ngija saaks valjusust muuta
manager = pygame_gui.UIManager([akna_laius, akna_korgus])
liugur_music = pygame_gui.elements.UIHorizontalSlider(pygame.Rect((690, 615), (100, 20)),
                                                      50, (0,100), manager)

taust_pilt = pygame.transform.scale(pygame.image.load(f'img/taust.png'), (800, 640))
taust_rect = taust_pilt.get_rect()
taust_rect.topleft = (0, 0)

# fps ja kell
fps = 30
kell = pygame.time.Clock()

mang_kaib = True

while mang_kaib:

    dt = kell.tick(fps) / 1000

    aken.blit(taust_pilt, taust_rect)

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
                vampiir.hype()

    ruudud.draw(aken)

    vampiirid.update()
    vampiirid.draw(aken)
   
    #muusika slideri jaoks vajalikud read
    manager.update(dt)
    manager.draw_ui(aken)

    pygame.display.update()

pygame.quit()