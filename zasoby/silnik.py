import pygame as pg
from ustawienia import *
from gracz import *
from mapy import *
from wsciekly_pies import *
from przedmioty import *
from przeszkody import *

import pygame as pg

class Silnik:
    def __init__(self):
        self.ekran = pg.display.set_mode(RES)
        ##self.wczytaj_teksty()
        self.wczytaj_ui()
        self.gracz = gracz(self)

    def daj_gre_mapom_i_graczowi(self, gra):
        self.gra = gra
        self.gracz.gra = gra
        for mapa in self.mapy:
            mapa.gra = gra
    
    def wczytaj_teksty(self):
        self.mapki = [
            pg.transform.scale(pg.image.load("tekstury/staremiasto.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/dworzec.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/krzyki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/mapa.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/Nadodrze.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/placgrunwaldzki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/pustystarter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/zoo.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/niepolda.png").convert(), RES)
        ]
        
        #self.mapki = [
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/staremiasto.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/dworzec.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/jakgrac.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/krzyki.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/mapa.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/Nadodrze.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/placgrunwaldzki.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/pustystarter.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/starter.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/zoo.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/niepolda.png").convert(), RES)
        #]

        self.mapy = [Mapa(i, mapa, self) for i, mapa in enumerate(self.mapki)]


        self.mapy[0].dodaj_polaczenie("gora", 5)
        self.mapy[0].dodaj_polaczenie("dol", 1)
        self.mapy[1].dodaj_polaczenie("dol", 3)
        self.mapy[3].dodaj_polaczenie("gora", 1)
        self.mapy[1].dodaj_polaczenie("gora", 0)
        self.mapy[5].dodaj_polaczenie("dol", 0)
        self.mapy[0].dodaj_polaczenie("prawo", 6)
        self.mapy[6].dodaj_polaczenie("lewo", 0)
        self.mapy[6].dodaj_polaczenie("gora", 9)
        self.mapy[9].dodaj_polaczenie("dol", 6)
        self.mapy[0].dodaj_polaczenie("lewo", 10)
        self.mapy[10].dodaj_polaczenie("prawo", 0)
        sciezka_ruch_niepolda = [
            (505, 420),  
            (950, 420), 
            (505, 420)   
        ]

        pies_niepolda = WscieklyPies(self, 375, 420, sciezka_ruch_niepolda)
        self.mapy[10].dodaj_psa(pies_niepolda)
        
        sciezka_grunwald = [
            (290, 230),  
            (840, 230),  
            (290, 230)   
        ]
        pies_grunwald = WscieklyPies(self, 290, 230, sciezka_grunwald, predkosc=2)
        self.mapy[6].dodaj_psa(pies_grunwald)
        
        sciezka_dworzec = [
            (445, 350),  
            (920, 350),  
            (920, 545),
            (920, 350),
            (445, 350)   
        ]
        pies_dworzec = WscieklyPies(self, 445, 350, sciezka_dworzec, predkosc=1.5)  # Wolniejszy
        self.mapy[1].dodaj_psa(pies_dworzec)

        self.przedmioty = [
        ]

        hulajnoga = Przedmiot(self, 685, 685, "hulajnoga.png")
        self.mapy[10].dodaj_przedmiot(hulajnoga)

        ser = Przedmiot( self, 260, 380, "ser.png")
        self.mapy[1].dodaj_przedmiot(ser)

        ksiazka = Przedmiot(self, 460, 300, "ksiazka.png")
        self.mapy[5].dodaj_przedmiot(ksiazka)

        puzzle = Przedmiot(self, 330, 120, "puzzle.png")
        self.mapy[6].dodaj_przedmiot(puzzle)

        tort = Przedmiot(self, 850, 120, "tort.png")
        self.mapy[6].dodaj_przedmiot(tort)

        autobus = Przeszkoda(self, 670, 585, "autobus.png", wymagany_przedmiot = "bilet")
        self.mapy[5].dodaj_przeszkode(autobus)

        bilet = Przedmiot(self, 370, 445, "bilet.png")
        self.mapy[10].dodaj_przedmiot(bilet)

        chmurka_bilet = Przeszkoda(self, 670 - 100, 585 - 50, "chmurka_bilet.png", wymagany_przedmiot = "bilet")
        self.mapy[5].dodaj_przeszkode(chmurka_bilet)
        chmurka_bilet.obraz = pg.transform.scale(
            pg.image.load("spritey/chmurka_bilet.png").convert_alpha(), 
            (300, 300)
        )# Nowy rozmia
        
        paniszczurek = Przeszkoda(self, 940, 600, "paniszczurek.png", wymagany_przedmiot = "roza")
        self.mapy[1].dodaj_przeszkode(paniszczurek)

        roza = Przedmiot(self, 405, 180, "roza.png")
        self.mapy[0].dodaj_przedmiot(roza)

        nauczyciel = Przeszkoda(self, 570, 365, "nauczyciel.png", wymagany_przedmiot = "dokument")
        self.mapy[6].dodaj_przeszkode(nauczyciel)

        dokument = Przedmiot(self, 350, 185, "dokument.png")
        self.mapy[3].dodaj_przedmiot(dokument)

        # siwek1= Przedmiot( self, 610, 280, "siwek1.png" )
        # siwek1.obraz = pg.transform.scale(siwek1.obraz, (100, 90)) 
        # self.mapy[9].dodaj_przedmiot(siwek1)
        #zostawiam bo moze sie przyda ale grafika sie tu rozwala


     

        #tu można dodać więcej połączeń, przedmioty i psów
        
    def wczytaj_ui(self):
        self.ui_obraz = pg.image.load("spritey/energia.png").convert_alpha()
        #self.ui_obraz = pg.image.load("zasoby/spritey/energia.png").convert_alpha()
        self.ui_obraz = pg.transform.scale(self.ui_obraz, (300, 150))
    def rysuj_interfejs(self, ekran, gracz):
        ui_x, ui_y = 0, WYSOKOSC - self.ui_obraz.get_height()
        self.ekran.blit(self.ui_obraz, (ui_x, ui_y))
        pasek_x = ui_x + 142
        pasek_y = ui_y + 13
        maks_szerokosc = 137
        wysokosc_paska = 30
        energia = max(0, min(100, self.gracz.energia))
        aktualna_szerokosc = int(maks_szerokosc * energia / 100)
        if energia > 60:
            kolor_paska = (0, 255, 0) #zielony
        elif energia > 30:
            kolor_paska = (255, 165, 0) #pomarańczowy
        else:
            kolor_paska = (255, 0, 0) #czerwony

        pg.draw.rect(self.ekran, (50, 50, 50), (pasek_x, pasek_y, maks_szerokosc, wysokosc_paska))
        pg.draw.rect(self.ekran, kolor_paska, (pasek_x, pasek_y, aktualna_szerokosc, wysokosc_paska))

        start_x = ui_x + 160
        start_y = ui_y + 100
        
        for i, obraz in enumerate(self.gracz.przedmioty_zebrane):
            miniatura = pg.transform.scale(obraz, (30, 30))

            if i < 3:
                x = start_x + i * 35
                y = start_y

            else:
                x = start_x + (i - 3) * 35
                y = start_y - 35  #górny rząd
            
            self.ekran.blit(miniatura, (x, y))

        if gracz.odblokowywacz:
            nazwa_pliku = f"{gracz.odblokowywacz}.png"
            sciezka = os.path.join("spritey", nazwa_pliku)
            if os.path.exists(sciezka):
                obrazek = pg.image.load(sciezka).convert_alpha()
                obrazek = pg.transform.scale(obrazek, (40, 40))
                fiolet_x = ui_x + 40  
                fiolet_y = ui_y + 85
                self.ekran.blit(obrazek, (fiolet_x, fiolet_y))
        
    
    

    

            
