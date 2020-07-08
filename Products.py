import loadImages


class left():
    def get_sprites(self): pass


class leftGaticornio(left):
    def get_sprites(self):
        return[loadImages.load("gaticornio/MI1.png"),
               loadImages.load("gaticornio/MI2.png"),
               loadImages.load("gaticornio/MI3.png"),
               loadImages.load("gaticornio/MI4.png"),
               loadImages.load("gaticornio/MI5.png")]



# Producto Abstracto right


class right():
    def get_sprites(self): pass


class rightGaticornio(right):
    def get_sprites(self):
        return [loadImages.load("gaticornio/MR1.png"),
                loadImages.load("gaticornio/MR2.png"),
                loadImages.load("gaticornio/MR3.png"),
                loadImages.load("gaticornio/MR4.png"),
                loadImages.load("gaticornio/MR5.png")]






class up():
    def get_sprites(self): pass


class upGaticornio(up):
    def get_sprites(self):
        return[loadImages.load("gaticornio/MR1.png")]





class down():
    def get_sprites(self): pass


class downGaticornio():
    def get_sprites(self):
        return[
               loadImages.load("gaticornio/MR1.png")]
class caidaGaticornio():
    def get_sprites(self):
        return [
            loadImages.load("Meteoros/Met.png")]




