from silnik import *
import sys
from przedmioty import * 
from gracz import *
from mapy import *
from wsciekly_pies import *
from ekrany import *
from przeszkody import Przeszkoda

class Gra: 
    def __init__(self, silnik):
        pg.init()
        self.silnik = silnik
        self.ekran = self.silnik.ekran
        self.silnik.wczytaj_teksty()
        pg.display.set_caption("Parszywek we Wrocławiu")
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.gracz = self.silnik.gracz
        self.ekran_startowy = ekran_startowy(self)
        self.ekran_jakgrac = ekran_jakgrac(self)
        self.ekran_gameover = ekran_gameover(self)
        self.mapa_wro = mapa_wro(self) 
        self.stan_gry = "start"
        self.ui_obraz = self.silnik.ui_obraz
        self.aktualna_mapa = 0
        self.mapy = self.silnik.mapy
        self.tlo = self.mapy[self.aktualna_mapa].tekstura

    
    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_e:
                    for przedmiot in self.mapy[self.aktualna_mapa].przedmioty:
                        if przedmiot.sprawdz_kolizje_z_graczem() and not przedmiot.podniesiony:
                            przedmiot.podnies()
                            print("Przedmiot podniesiony!")
                elif zdarz.key == pg.K_m: 
                   self.stan_gry = "mapa"
            elif zdarz.type == pg.USEREVENT:
                for pies in self.mapy[self.aktualna_mapa].psy:
                    pies.calkowite_obrazenia = 0
                self.gracz.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
                self.gracz.obraz = pg.transform.scale(self.gracz.obraz, (70, 90))
        

    
    def rysuj(self):
        self.ekran.blit(self.tlo, (0, 0)) 
        for przedmiot in self.mapy[self.aktualna_mapa].przedmioty:
            przedmiot.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.rysuj()
        for przeszkoda in self.mapy[self.aktualna_mapa].przeszkody:
            przeszkoda.rysuj(self.ekran)
        self.gracz.rysuj()
        self.silnik.rysuj_interfejs(self.ekran, self.gracz) ##self.rysuj_interfejs() wczesniej                 
        pg.display.flip() 

    def aktualizuj(self):
        self.gracz.aktualizuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.aktualizuj()
        self.mapy[self.aktualna_mapa].sprawdz_krawedzie()
        for przeszkoda in self.mapy[self.aktualna_mapa].przeszkody:
            if przeszkoda.koliduje(self.gracz):
                if self.gracz.odblokowywacz == przeszkoda.wymagany_przedmiot:
                    przeszkoda.aktywna = False
                    self.gracz.odblokowywacz = None
                else:
                    self.gracz.cofnij_ruch()
        self.rysuj()
        self.zegar.tick(FPS) 

    def resetuj(self):
        self.stan_gry = "start"
        self.aktualna_mapa = 0
        self.tlo = self.mapy[self.aktualna_mapa].tekstura
        self.gracz.resetuj()
        for mapa in self.mapy:
            mapa.resetuj()
        
    def graj(self):
        while True:
            if self.stan_gry == "start":
                self.ekran_startowy.rysuj()
                self.ekran_startowy.sprawdz_zdarzenia()
            if self.stan_gry == "jakgrac":
                self.ekran_jakgrac.rysuj()
                self.ekran_jakgrac.sprawdz_zdarzenia()
            if self.stan_gry == "mapa":
                self.mapa_wro.rysuj()
                self.mapa_wro.sprawdz_zdarzenia() 
            if self.stan_gry == "gameover":
                self.ekran_gameover.rysuj()
                self.ekran_gameover.sprawdz_zdarzenia() 
            if self.stan_gry == "gra":
                self.sprawdz_zdarzenia()
                self.aktualizuj()
 
if __name__ == "__main__":
    silnik = Silnik()
    gra = Gra(silnik)
    silnik.daj_gre_mapom_i_graczowi(gra)
    gra.graj()

    
