import pygame as pg
from ustawienia import *
import os

class WscieklyPies:
    def __init__(self, gra, x, y, sciezka_ruch, predkosc=3):
        self.gra = gra
        self.startowe_x = x
        self.startowy_y = y
        self.x, self.y = x, y
        self.sciezka_ruch = sciezka_ruch
        self.aktualny_cel = 0
        self.predkosc = predkosc
        self.kierunek = 1 
        self.obrazenia = 5 
        self.aktywny_atak = False
        self.czas_ostatniego_ataku = 0
        self.cooldown_ataku = 1000  # 1 sekunda
        self.czas_czerwonego = 0
        self.czerwony_aktywny = False
        
        sciezka_do_obrazka = os.path.join("spritey", "wscieklypies.png")
        if not os.path.exists(sciezka_do_obrazka):
            raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load(sciezka_do_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (120, 120)) 
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))
        
        # Ładowanie obrazów gracza
        self.oryginalny_obraz_gracza = self.gra.gracz.obraz.copy()
        self.czerwony_obraz = self.oryginalny_obraz_gracza.copy()
        self.czerwony_obraz.fill((255, 0, 0, 100), special_flags=pg.BLEND_MULT)
        
    def aktualizuj(self):
        # Aktualizacja pozycji psa
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

        # Aktualizacja efektu czerwonego
        teraz = pg.time.get_ticks()
        if self.czerwony_aktywny:
            if not self.sprawdz_kolizje_z_graczem() or teraz - self.czas_czerwonego > 500:
                self.czerwony_aktywny = False
                self.gra.gracz.obraz = self.oryginalny_obraz_gracza

        # Logika ataku
        kolizja = self.sprawdz_kolizje_z_graczem()
        if kolizja:
            if not self.aktywny_atak:
                self.rozpocznij_atak(teraz)
            elif self.aktywny_atak and teraz - self.czas_ostatniego_ataku > self.cooldown_ataku:
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
            if not self.czerwony_aktywny:
                self.gra.gracz.obraz = self.oryginalny_obraz_gracza

    def zadaj_obrazenia(self):
        if not self.sprawdz_kolizje_z_graczem():
            return
            
        self.gra.gracz.energia = max(0, self.gra.gracz.energia - self.obrazenia)
        print(f"Pies ugryzł! -{self.obrazenia} energii")
        
        # Aktywuj czerwony efekt
        self.gra.gracz.obraz = self.czerwony_obraz
        self.czerwony_aktywny = True
        self.czas_czerwonego = pg.time.get_ticks()
    
    def sprawdz_kolizje_z_graczem(self):
        gracz_rect = pg.Rect(self.gra.gracz.x, self.gra.gracz.y, 
                            self.gra.gracz.obraz.get_width(), 
                            self.gra.gracz.obraz.get_height())
        return self.rect.colliderect(gracz_rect)
    
    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))

    def resetuj(self):
        self.x = self.startowe_x
        self.y = self.startowy_y
        self.czerwony_aktywny = False
        self.gra.gracz.obraz = self.oryginalny_obraz_gracza
