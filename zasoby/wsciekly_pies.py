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
        self.ostatnie_ugryzienie = 0 
        self.cooldown = 2000
        self.obrazenia = 10
        self.aktywny_atak = False  # Czy pies aktualnie atakuje
        self.czas_ataku = 0
        
        sciezka_do_obrazka = os.path.join("spritey", "wscieklypies.png")
        if not os.path.exists(sciezka_do_obrazka):
            raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load(sciezka_do_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (120, 120)) 
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))
        
    def aktualizuj(self):
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
        
        
        if self.sprawdz_kolizje_z_graczem():
            self.gra.gracz.energia = max(0, self.gra.gracz.energia - 5)
            print("Pies ugryzł gracza! -5 energii")

        teraz = pg.time.get_ticks()
        if self.sprawdz_kolizje_z_graczem() and self.gra.gracz.obrazenia_aktywne:
            if not self.aktywny_atak:
                # Rozpocznij atak
                self.aktywny_atak = True
                self.czas_ataku = teraz
                self.zadaj_obrazenia()
            elif teraz - self.czas_ataku > 1000:  # Nowy atak co sekundę
                self.czas_ataku = teraz
                self.zadaj_obrazenia()
        else:
            self.aktywny_atak = False

    def zadaj_obrazenia(self):
        self.gra.gracz.energia = max(0, self.gra.gracz.energia - self.obrazenia)
        self.gra.gracz.obrazenia_aktywne = False
        self.gra.gracz.czas_immunitetu = pg.time.get_ticks()
        print(f"Pies ugryzł! -{self.obrazenia} energii")
        
        # Wizualna informacja o ugryzieniu
        self.gra.gracz.obraz.fill((255, 0, 0, 100), special_flags=pg.BLEND_MULT)
        
        # Timer do przywrócenia normalnego stanu
        pg.time.set_timer(pg.USEREVENT, self.gra.gracz.dlugosc_immunitetu)

    
    def sprawdz_kolizje_z_graczem(self):
        gracz_rect = pg.Rect(self.gra.gracz.x, self.gra.gracz.y, 
                            self.gra.gracz.obraz.get_width(), 
                            self.gra.gracz.obraz.get_height())
        return self.rect.colliderect(gracz_rect)
    
    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
