from random import randint


class Heros:

    def __init__(self, nom, pv, res, dmax):
        print("Création du héros " + nom)
        self.nom = nom
        self.points_de_vie = pv
        self.resistance = res
        self.degats_max = dmax

    def est_en_vie(self):
        return self.points_de_vie > 0

    def attaque(self, autre):
        if self.est_en_vie():
            degats = randint(1, self.degats_max)
            autre.subit_attaque(self, degats)

    def subit_attaque(self, autre, degats):
        if degats > self.resistance:
            self.points_de_vie -= degats
            print(self.nom + " perd " + str(degats) + " points de vie")
        else:
            print(autre.nom + " a raté son attaque contre " + self.nom)

        if not self.est_en_vie():
            print(autre.nom + " a tué " + self.nom)


achille = Heros("Achille", 100, 10, 30)
hector = Heros("Hector", 100, 15, 25)
paris = Heros("Pâris", 80, 8, 20)

while achille.est_en_vie() and hector.est_en_vie():
    achille.attaque(hector)
    hector.attaque(achille)
