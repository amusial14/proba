import pygame as pg
from ustawienia import *



class silnik:
    def __init__(self,gra):
        self.gra=gra
        self.ekran= gra.ekran
        self.struktury=self.zaladuj_teksture()

    @staticmethod
    def pobierz_teksture(path, res=(ROZMIAR_TEKSTURY, ROZMIAR_TEKSTURY)):
        tekstura = pg.image.load(path).convert_alpha()
        return pg.transform.scale(tekstura, res)
    
    def zaladuj_teksture(self):
        return {}