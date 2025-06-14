from silnik import *
import sys
from przedmioty import Przedmiot 
from gracz import *
from mapy import *
from wsciekly_pies import *

class Gra: 
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode(RES)
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.gracz = gracz(self)
        #sciezka_tla = os.path.join(os.path.dirname(__file__), "tekstury", "staremiasto.png")
        #self.tlo = pg.image.load(sciezka_tla).convert()
        self.tlo = pg.image.load("tekstury/staremiasto.png").convert()
        # self.tlo = pg.image.load("zasoby/tekstury/staremiasto.png").convert()
        self.tlo = pg.transform.scale(self.tlo, RES) 
        self.przedmioty = [
           # Przedmiot(self,300,300, "tort.png")
        ] 
        # self.mapki = [
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/staremiasto.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/dworzec.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/jakgrac.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/krzyki.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/mapa.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/Nadodrze.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/placgrunwaldzki.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/pustystarter.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/starter.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/zoo.png").convert(), RES),
        # ]
        self.mapki = [
            pg.transform.scale(pg.image.load("tekstury/staremiasto.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/dworzec.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/krzyki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/mapa.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/Nadodrze.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/placgrunwaldzki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/pustystarter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/zoo.png").convert(), RES),
        ]
        
        self.mapy = [
            Mapa(0, self.mapki[0], self),
            Mapa(1, self.mapki[1], self),
            Mapa(2, self.mapki[2], self),
            Mapa(3, self.mapki[3], self),
            Mapa(4, self.mapki[4], self),
            Mapa(5, self.mapki[5], self),
            Mapa(6, self.mapki[6], self)
        ]

        sciezka_stare_miasto = [
            (200, 500),  # Punkt startowy
            (400, 500),  # W prawo
            (400, 600),  # W dół
            (200, 600),  # W lewo
            (200, 500)   # W górę (powrót)
        ]
        pies_stare_miasto = WscieklyPies(
            self, 
            x=200, 
            y=500,
            sciezka_ruch=sciezka_stare_miasto,
            predkosc=2  # Wolniejszy niż domyślny
        )
        self.mapy[0].dodaj_psa(pies_stare_miasto)

        self.aktualna_mapa = 0
        self.tlo = self.mapy[self.aktualna_mapa].tekstura 




    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_e:
                    for przedmiot in self.przedmioty:
                        if przedmiot.sprawdz_kolizje_z_graczem() and not przedmiot.podniesiony:
                            przedmiot.podnies()
                            print("Przedmiot podniesiony!")


    def rysuj(self):
        self.ekran.blit(self.tlo, (0, 0)) 
        for przedmiot in self.przedmioty:
            przedmiot.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.rysuj()
        self.gracz.rysuj()                 
        pg.display.flip() 

    def aktualizuj(self):
        self.gracz.aktualizuj()
        self.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.aktualizuj()
        self.mapy[self.aktualna_mapa].sprawdz_krawedzie()
        self.zegar.tick(FPS) 

    def graj(self):
        while True:
            self.sprawdz_zdarzenia()
            self.aktualizuj()
            

if __name__=="__main__":
    gra=Gra()
    gra.graj()
    
