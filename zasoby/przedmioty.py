import pygame as pg
import os
from gracz import *

class Przedmiot:
    def __init__(self, gra, x, y, nazwa_pliku):
        self.gra = gra
        self.x = x
        self.y = y
        sciezka_do_obrazka = os.path.join("spritey", nazwa_pliku)
        
        if not os.path.exists(sciezka_do_obrazka):
            raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load(sciezka_do_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (40, 40))  
        
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))
        self.podniesiony = False  

    def rysuj(self):
        if not self.podniesiony:
            self.gra.ekran.blit(self.obraz, (self.x, self.y))
    
    def sprawdz_kolizje_z_graczem(self):
        gracz_rect = pg.Rect(self.gra.gracz.x, self.gra.gracz.y, 50, 50)  
        return self.rect.colliderect(gracz_rect)

    def podnies(self):
        self.podniesiony = True
        self.gra.gracz.przedmioty_zebrane.append(self.obraz)
        self.gra.gracz.energia = min(100, self.gra.gracz.energia + 10)
       
