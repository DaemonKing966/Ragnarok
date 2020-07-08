# Esta es nuestra clase de fabricas, ya que usamos el patron Abstract Factory
from Products import *

# Farica abstracta que tiene como metodos mover izq y mover der


class AbstractFactory():
    def moveLeft(self): pass
    def moveRight(self): pass
    def moveDown(self): pass
    def moveUp(self): pass
    def caida(self): pass


# Fabrica concreta que produce sprites de cada personaje

class GaticornioSprites(AbstractFactory):

    def moveLeft(self):
        left = leftGaticornio()
        return left.get_sprites()

    def moveRight(self):
        right = rightGaticornio()
        return right.get_sprites()

    def moveUp(self):
        up = upGaticornio()
        return up.get_sprites()

    def moveDown(self):
        down = downGaticornio()
        return down.get_sprites()
    def caida(self):
        caida= caidaGaticornio()
        return caida.get_sprites()



