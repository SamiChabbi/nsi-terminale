class File:
    """File (queue) en mode FIFO : premier entré, premier sorti.

    Les éléments sont rangés dans une liste python : la tête de la file
    est au début de la liste (indice 0), la queue à la fin.
    """

    def __init__(self):
        """Construit une nouvelle file vide."""
        self.contenu = []

    def enfile(self, el):
        """Ajoute un élément à la fin de la file."""
        self.contenu.append(el)

    def defile(self):
        """Supprime et renvoie l'élément en tête de file.
        Déclenche une erreur si la file est vide."""
        if self.est_vide():
            raise IndexError("defile() sur une file vide")
        return self.contenu.pop(0)

    def taille(self):
        """Renvoie le nombre d'éléments de la file."""
        return len(self.contenu)

    def est_vide(self):
        """Renvoie True si la file est vide, False sinon."""
        return self.taille() == 0

    def __repr__(self):
        """Renvoie une description du contenu de la file."""
        if self.est_vide():
            return "File vide"
        texte = "tête"
        for el in self.contenu:
            texte = texte + " < " + str(el)
        return texte + " < queue"
