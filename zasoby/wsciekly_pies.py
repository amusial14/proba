import pygame as pg
from ustawienia import *
import os

class WscieklyPies:
    def __init__(self, gra, x, y, sciezka_ruch, predkosc=3):
        self.gra = gra
        self.x = x
        self.y = y
        self.sciezka_ruch = sciezka_ruch
        self.aktualny_cel = 0
        self.predkosc = predkosc
        self.kierunek = 1
        self.obrazenia = 5
        self.calkowite_obrazenia = 0
        self.max_obrazen_na_spotkanie = 15
        
        # Load image
        sciezka_obrazu = os.path.join("spritey", "wscieklypies.png")
        self.obraz = pg.image.load(sciezka_obrazu).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (120, 120))
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))

    def aktualizuj(self):
        # Movement logic (unchanged)
        cel_x, cel_y = self.sciezka_ruch[self.aktualny_cel]
        dx, dy = cel_x - self.x, cel_y - self.y
        odleglosc = (dx**2 + dy**2)**0.5
        
        if odleglosc < self.predkosc:
            self.x, self.y = cel_x, cel_y
            self.aktualny_cel += self.kierunek
            
            if self.aktualny_cel >= len(self.sciezka_ruch) or self.aktualny_cel < 0:
                self.kierunek *= -1
                self.aktualny_cel += self.kierunek * 2
        else:
            self.x += (dx / odleglosc) * self.predkosc
            self.y += (dy / odleglosc) * self.predkosc
        
        self.rect.topleft = (self.x, self.y)

    def zadaj_obrazenia(self):
        # Stop any existing timers
        pg.time.set_timer(pg.USEREVENT+1, 0)
        pg.time.set_timer(pg.USEREVENT+2, 0)
        
        # Apply damage
        self.gra.gracz.energia = max(0, self.gra.gracz.energia - self.obrazenia)
        self.calkowite_obrazenia += self.obrazenia
        
        # Visual effect
        if not hasattr(self.gra.gracz, 'normalny_wyglad'):
            self.gra.gracz.normalny_wyglad = pg.image.load("spritey/parszywek1.png").convert_alpha()
            self.gra.gracz.normalny_wyglad = pg.transform.scale(self.gra.gracz.normalny_wyglad, (70, 90))
        
        self.gra.gracz.obraz = self.gra.gracz.normalny_wyglad.copy()
        self.gra.gracz.obraz.fill((255, 0, 0, 100), special_flags=pg.BLEND_MULT)
        pg.time.set_timer(pg.USEREVENT+1, 100, loops=1)  # Visual effect timer
        
        # Immunity timer
        pg.time.set_timer(pg.USEREVENT+2, 2000, loops=1)

    def sprawdz_kolizje_z_graczem(self):
        gracz_rect = pg.Rect(self.gra.gracz.x, self.gra.gracz.y,
                           self.gra.gracz.obraz.get_width(),
                           self.gra.gracz.obraz.get_height())
        return self.rect.colliderect(gracz_rect)

    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
