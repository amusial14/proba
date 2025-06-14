import pygame as pg
from przedmioty import *
from ustawienia import *


marg = 20 #margines uzywany pozniej przy krawedziach mapy zeby parszywek nie wyszedl caly za okienko
class Mapa:
    def __init__(self, indeks, tekstura, gra):
        self.indeks = indeks
        self.tekstura = tekstura
        self.gra = gra
        self.polaczenia = {}
        self.przedmioty = []
        self.psy = []
    
    def dodaj_polaczenie(self, kierunek, indeks_mapy_docelowej):
        self.polaczenia[kierunek] = indeks_mapy_docelowej

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def dodaj_psa(self, pies):
        self.psy.append(pies)
    
    def sprawdz_krawedzie(self):
        gracz = self.gra.gracz
        #wymiary obrazka parszywka ustalone w pliku gracz.py: 70x90
        if gracz.x < marg and "lewo" in self.polaczenia:
            self.zmien_mape(self.polaczenia["lewo"], "lewo")
        elif gracz.x > DLUGOSC - marg - 70 and "prawo" in self.polaczenia:
            self.zmien_mape(self.polaczenia["prawo"], "prawo")
        elif gracz.y < marg and "gora" in self.polaczenia:
            self.zmien_mape(self.polaczenia["gora"], "gora")
        elif gracz.y > WYSOKOSC - marg - 90 and "dol" in self.polaczenia:
            self.zmien_mape(self.polaczenia["dol"], "dol")
    
    def zmien_mape(self, nowy_indeks, kierunek):

        self.gra.aktualna_mapa = nowy_indeks
        self.gra.tlo = self.gra.mapy[nowy_indeks].tekstura
        
        gracz = self.gra.gracz
        if kierunek == "lewo":
            gracz.x = DLUGOSC - marg - 70
        elif kierunek == "prawo":
            gracz.x = marg
        elif kierunek == "gora":
            gracz.y = WYSOKOSC - marg - 90
        elif kierunek == "dol":
            gracz.y = marg
        
