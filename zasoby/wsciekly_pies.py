import pygame as pg
from ustawienia import *
import os

class WscieklyPies:
    def __init__(self, gra, x, y, sciezka_ruch, predkosc=3):
        self.gra = gra
        self.x, self.y = x, y
        self.sciezka_ruch = sciezka_ruch
        self.aktualny_cel = 0
        self.predkosc = predkosc
        self.kierunek = 1
        
        # Atrybuty do kontroli obrażeń
        self.obrazenia = 5  # Mniej obrażeń
        self.aktywny_atak = False
        self.czas_ostatniego_ataku = 0
        self.cooldown_ataku = 1000  # 1 sekunda przerwy
        self.calkowite_obrazenia = 0
        self.max_obrazen_na_spotkanie = 15  # Maksymalne obrażenia na jedno spotkanie
        
        # Ładowanie grafiki
        sciezka_obrazu = os.path.join("spritey", "wscieklypies.png")
        if not os.path.exists(sciezka_obrazu):
            raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_obrazu}")
        
        self.obraz = pg.image.load(sciezka_obrazu).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (120, 120))
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))

    def aktualizuj(self):
        # Ruch psa (bez zmian)
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

        # Ulepszony system obrażeń
        teraz = pg.time.get_ticks()
        if self.sprawdz_kolizje_z_graczem():
            if not self.aktywny_atak and self.calkowite_obrazenia < self.max_obrazen_na_spotkanie:
                self.rozpocznij_atak(teraz)
            elif (self.aktywny_atak and 
                  teraz - self.czas_ostatniego_ataku > self.cooldown_ataku and
                  self.calkowite_obrazenia < self.max_obrazen_na_spotkanie):
                self.kontynuuj_atak(teraz)
        else:
            self.zakoncz_atak()

    def rozpocznij_atak(self, czas):
        self.aktywny_atak = True
        self.czas_ostatniego_ataku = czas
        self.zadaj_obrazenia()

    def kontynuuj_atak(self, czas):
        self.czas_ostatniego_ataku = czas
        self.zadaj_obrazenia()

    def zakoncz_atak(self):
        if self.aktywny_atak:
            self.aktywny_atak = False
            # Resetuj licznik po 2 sekundach od ostatniego kontaktu
            pg.time.set_timer(pg.USEREVENT, 2000, loops=1)

    
   def zadaj_obrazenia(self):
    # Stop any existing timers
    pg.time.set_timer(pg.USEREVENT+1, 0)
    pg.time.set_timer(pg.USEREVENT+2, 0)
    
    # Visual effect (100ms)
    if not hasattr(self.gra.gracz, 'normalny_wyglad'):
        self.gra.gracz.normalny_wyglad = pg.image.load("spritey/parszywek1.png").convert_alpha()
        self.gra.gracz.normalny_wyglad = pg.transform.scale(self.gra.gracz.normalny_wyglad, (70, 90))
    
    self.gra.gracz.obraz = self.gra.gracz.normalny_wyglad.copy()
    self.gra.gracz.obraz.fill((255, 0, 0, 100), special_flags=pg.BLEND_MULT)
    pg.time.set_timer(pg.USEREVENT+1, 100, loops=1)
    
    # Immunity (2000ms)
    pg.time.set_timer(pg.USEREVENT+2, 2000, loops=1)
    
    # Damage calculation
    self.gra.gracz.energia = max(0, self.gra.gracz.energia - self.obrazenia)
    self.calkowite_obrazenia += self.obrazenia
    # 0.1 sekundy
    def sprawdz_kolizje_z_graczem(self):
        gracz_rect = pg.Rect(self.gra.gracz.x, self.gra.gracz.y,
                           self.gra.gracz.obraz.get_width(),
                           self.gra.gracz.obraz.get_height())
        return self.rect.colliderect(gracz_rect)

    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
