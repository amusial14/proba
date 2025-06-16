import pygame as pg
from ustawienia import *
import os

class gracz():
    def __init__(self, gra):
        self.gra = gra
        self.x, self.y = 700, 400
        self.szybkosc = 5
        self.energia = 100
        self.przedmioty_zebrane = []
        self.ostatnie_obrazenia = 0
        self.immunitet = 2000
        self.obrazenia_aktywne = True  # Czy można otrzymywać obrażenia
        self.czas_immunitetu = 0
        self.dlugosc_immunitetu = 2000
        # sciezka_do_obrazka = os.path.join("zasoby/spritey/parszywek1.png")
        
        # if not os.path.exists(sciezka_do_obrazka):
            # raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (70, 90)) 

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
        
        if klawisze[pg.K_UP]:  
            dy = -self.szybkosc
        elif klawisze[pg.K_DOWN]:  
            dy = self.szybkosc
        elif klawisze[pg.K_LEFT]:  
            dx = -self.szybkosc
        elif klawisze[pg.K_RIGHT]:  
            dx = self.szybkosc

        nowy_x = self.x + dx
        nowy_y = self.y + dy

        self.x = max(0, min(self.x, 1200))  
        self.y = max(0, min(self.y, 800)) 

        srodek_x = nowy_x + self.obraz.get_width() // 2
        dol_y = nowy_y + self.obraz.get_height()

        if self.czy_moze_isc(srodek_x, dol_y):
            self.x, self.y = nowy_x, nowy_y

        if self.x != nowy_x or self.y != nowy_y:
            self.energia = max(0, self.energia - 0.05)  

    
    def aktualizuj(self):
        self.ruch()

    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
