import pygame as pg
import os

class Przeszkoda:
    def __init__(self, gra, x, y, obrazek, wymagany_przedmiot=None, kontrolowana_przeszkoda=None):
        self.gra = gra
        self.x = x
        self.y = y
        self.nazwa = obrazek
        self.wymagany_przedmiot = wymagany_przedmiot
        self.aktywna = True
        self.kontrolowana_przeszkoda = kontrolowana_przeszkoda  

        sciezka_obrazka = os.path.join("spritey", obrazek)
        self.obraz = pg.image.load(sciezka_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (90,90))
        self.rect = self.obraz.get_rect(topleft=(x, y))  

    def rysuj(self, ekran):
        if self.aktywna:
            ekran.blit(self.obraz, (self.x, self.y)) 

    def dezaktywuj(self):
        print(f"Dezaktywuję: {self.nazwa}")
        self.aktywna = False
        if self.kontrolowana_przeszkoda:
            print(f"Również dezaktywuję: {self.kontrolowana_przeszkoda.nazwa}")
            self.kontrolowana_przeszkoda.aktywna = False


    def koliduje(self, gracz):
        if not self.aktywna:
            return False

        gracz_rect = pg.Rect(gracz.x, gracz.y, gracz.obraz.get_width(), gracz.obraz.get_height())
        
        if self.rect.colliderect(gracz_rect):
            if self.wymagany_przedmiot and gracz.odblokowywacz == self.wymagany_przedmiot:
                print(f"Używam {self.wymagany_przedmiot} na {self.nazwa}")
                self.dezaktywuj()
                gracz.odblokowywacz = None
                return False
            return True
        return False
