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
        self.w_kontakcie_z_psem = False
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

    def pokaz_wspolrzedne(self):
        """Wyświetla aktualne współrzędne szczurka w terminalu"""
        print(f"Pozycja szczurka: X={int(self.x)} Y={int(self.y)}")

    def debug_pozycja(self):
        """Wyświetla aktualną pozycję i kolor podłoża"""
        srodek_x = int(self.x + self.obraz.get_width()/2)
        dół_y = int(self.y + self.obraz.get_height())
    
        print("\n--- DEBUG POZYCJI ---")
        print(f"Lewy górny róg: X={self.x:.1f}, Y={self.y:.1f}")
        print(f"Środek podstawy: X={srodek_x}, Y={dół_y}")
    
        try:
            kolor = self.gra.ekran.get_at((srodek_x, dół_y))[:3]
            print(f"Kolor podłoża: {kolor}")
            print("Czy może iść?:", "TAK" if self.czy_moze_isc(self.x, self.y) else "NIE")
        except:
            print("Poza ekranem!")
        print("---------------------")

    
    def aktualizuj(self):
        self.ruch()

    def rysuj(self):
        self.gra.ekran.blit(self.obraz, (self.x, self.y))
