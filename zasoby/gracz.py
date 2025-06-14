import pygame as pg
from ustawienia import *
import os

class gracz():
    def __init__(self, gra):
        self.gra = gra
        self.x, self.y = 700, 400
        self.szybkosc = 5
        #sciezka_do_obrazka = os.path.join("spritey/parszywek1.png")
        
        #if not os.path.exists(sciezka_do_obrazka):
            #raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
        sciezka_obrazka = os.path.join(os.path.dirname(__file__), "spritey", "parszywek1.png")
        self.obraz = pg.image.load(sciezka_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (70, 90)) 
        #sciezka_gracza = os.path.join(os.path.dirname(__file__), "spritey", "parszywek1.png")
        #self.obraz = pg.image.load(sciezka_gracza).convert_alpha()

        self.dozwolony_kolor = (219, 187, 104)

    def czy_moze_isc(self, x, y):
        try:
            kolor = self.gra.ekran.get_at((int(x), int(y)))[:3] 
            return kolor == self.dozwolony_kolor
        except:
            return False

    def ruch(self):
        klawisze = pg.key.get_pressed()

        dx, dy = 0, 0
        
        if klawisze[pg.K_w]:  
            dy = -self.szybkosc
        elif klawisze[pg.K_s]:  
            dy = self.szybkosc
        elif klawisze[pg.K_a]:  
            dx = -self.szybkosc
        elif klawisze[pg.K_d]:  
            dx = self.szybkosc

        nowy_x = self.x + dx
        nowy_y = self.y + dy

        self.x = max(0, min(self.x, 1200))  
        self.y = max(0, min(self.y, 800)) 

        srodek_x = nowy_x + self.obraz.get_width() // 2
        dol_y = nowy_y + self.obraz.get_height()

        if self.czy_moze_isc(srodek_x, dol_y):
            self.x, self.y = nowy_x, nowy_y
    
    def aktualizuj(self):
        self.ruch()

    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
