class Angle:
    """
    Classe représentant un angle géométrique de mesure v, en degrés.
    La mesure doit être comprise entre 0 et 180 degrés.
    """

    def __init__(self, v):
        """
        Construit un angle de mesure v en degrés.

        Déclenche une erreur si v n'est pas comprise entre 0 et 180.
        """
        # Vérifier que v est comprise entre 0 et 180.
        pass

    def mesure_en_degres(self):
        """
        Renvoie la mesure en degrés de l'angle.
        """
        pass

    def est_aigu(self):
        """
        Renvoie True si l'angle est aigu, False sinon.

        Un angle est aigu si sa mesure est strictement inférieure
        à 90 degrés.
        """
        pass

    def mesure_en_radians(self):
        """
        Renvoie la mesure de l'angle en radians.
        """
        # Rappel :
        # 180 degrés correspondent à pi radians.
        #
        # La conversion peut être effectuée à l'aide du module math.
        pass

    def mesure_en_degres_minutes_secondes(self):
        """
        Renvoie la mesure de l'angle sous la forme
        (degrés, minutes, secondes).

        Une minute d'angle correspond à 1/60 degré.
        Une seconde d'angle correspond à 1/60 minute.
        """
        # La partie entière de la mesure correspond aux degrés.
        #
        # Convertir la partie décimale en minutes.
        #
        # La partie entière obtenue correspond aux minutes.
        #
        # Convertir le reste en secondes.
        pass

    def supplementaire(self):
        """
        Renvoie un objet Angle qui représente le supplémentaire
        de l'instance.

        Deux angles supplémentaires ont une somme égale à 180 degrés.
        """
        pass

    def __str__(self):
        """
        Renvoie une chaîne de caractères composée de la valeur
        de l'angle en degrés suivie du symbole °.
        """
        pass

    def __add__(self, autre):
        """
        Renvoie un objet Angle qui représente la somme de l'instance
        et de l'angle autre.
        """
        # Additionner les mesures des deux angles.
        #
        # Attention : le résultat doit lui-même être un angle
        # géométrique valide.
        pass

    def __sub__(self, autre):
        """
        Renvoie un objet Angle qui représente la différence entre
        l'instance et l'angle autre.
        """
        # Soustraire la mesure de autre à celle de l'instance.
        #
        # Attention : le résultat doit être compris entre 0 et 180.
        pass


# ============================================================
# Tests de la classe Angle
# ============================================================

# ------------------------------------------------------------
# 1. Construction et mesure en degrés
# ------------------------------------------------------------

assert Angle(0).mesure_en_degres() == 0
assert Angle(45).mesure_en_degres() == 45
assert Angle(90).mesure_en_degres() == 90
assert Angle(180).mesure_en_degres() == 180

# Les valeurs en dehors de [0, 180] doivent être refusées
for valeur in [-1, -10, 180.1, 200]:
    try:
        Angle(valeur)
        assert False, f"Valeur acceptée à tort : {valeur}"
    except AssertionError:
        pass

# ------------------------------------------------------------
# 2. Est-ce un angle aigu ?
# ------------------------------------------------------------

assert Angle(0).est_aigu() is True
assert Angle(45).est_aigu() is True
assert Angle(89.9).est_aigu() is True

assert Angle(90).est_aigu() is False
assert Angle(120).est_aigu() is False
assert Angle(180).est_aigu() is False

# ------------------------------------------------------------
# 3. Conversion en radians
# ------------------------------------------------------------

import math

assert math.isclose(Angle(0).mesure_en_radians(), 0)

assert math.isclose(Angle(90).mesure_en_radians(), math.pi / 2)

assert math.isclose(Angle(180).mesure_en_radians(), math.pi)

assert math.isclose(Angle(45).mesure_en_radians(), math.pi / 4)

# ------------------------------------------------------------
# 4. Conversion en degrés / minutes / secondes
# ------------------------------------------------------------

assert Angle(0).mesure_en_degres_minutes_secondes() == (0, 0, 0)

assert Angle(30).mesure_en_degres_minutes_secondes() == (30, 0, 0)

assert Angle(30.5).mesure_en_degres_minutes_secondes() == (30, 30, 0)

assert Angle(30.25).mesure_en_degres_minutes_secondes() == (30, 15, 0)

assert Angle(30 + 15 / 60 +
             20 / 3600).mesure_en_degres_minutes_secondes() == (30, 15, 20)

# ------------------------------------------------------------
# 5. Angle supplémentaire
# ------------------------------------------------------------

assert Angle(0).supplementaire().mesure_en_degres() == 180
assert Angle(30).supplementaire().mesure_en_degres() == 150
assert Angle(90).supplementaire().mesure_en_degres() == 90
assert Angle(180).supplementaire().mesure_en_degres() == 0

# ------------------------------------------------------------
# 6. Affichage
# ------------------------------------------------------------

assert str(Angle(0)) == "0°"
assert str(Angle(45)) == "45°"
assert str(Angle(90)) == "90°"
assert str(Angle(30.5)) == "30.5°"
assert str(Angle(180)) == "180°"

# ------------------------------------------------------------
# 7. Addition
# ------------------------------------------------------------

assert (Angle(10) + Angle(20)).mesure_en_degres() == 30
assert (Angle(45) + Angle(45)).mesure_en_degres() == 90
assert (Angle(90) + Angle(90)).mesure_en_degres() == 180

# Dépassement de 180° : le résultat doit être refusé
try:
    Angle(120) + Angle(61)
    assert False, "Une somme supérieure à 180° a été acceptée"
except AssertionError:
    pass

# ------------------------------------------------------------
# 8. Soustraction
# ------------------------------------------------------------

assert (Angle(30) - Angle(20)).mesure_en_degres() == 10
assert (Angle(90) - Angle(30)).mesure_en_degres() == 60
assert (Angle(30) - Angle(30)).mesure_en_degres() == 0
assert (Angle(180) - Angle(90)).mesure_en_degres() == 90

# Résultat négatif : il doit être refusé
try:
    Angle(20) - Angle(30)
    assert False, "Une différence négative a été acceptée"
except AssertionError:
    pass

print("Tous les tests sont réussis !")
