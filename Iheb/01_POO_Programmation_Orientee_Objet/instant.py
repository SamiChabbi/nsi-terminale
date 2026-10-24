class Instant:
    """
    Représente un instant au format jj/mm/aaaa:hh:mm:ss

    Exemple :
        d = Instant(2, 10, 2026, 14, 30, 45)
        print(d)          # 02/10/2026:14:30:45
    """

    def __init__(self, jour, mois, annee, heure, minute, seconde):
        self.jour = jour
        self.mois = mois
        self.annee = annee
        self.heure = heure
        self.minute = minute
        self.seconde = seconde

        assert self.est_valide(), "Date ou heure invalide"

    def __str__(self):
        """
        Renvoie une représentation de l'objet sous la forme : jj/mm/aaaa:hh:mm:ss
        """
        return (f"{self.jour:02d}/"
                f"{self.mois:02d}/"
                f"{self.annee:04d}:"
                f"{self.heure:02d}:"
                f"{self.minute:02d}:"
                f"{self.seconde:02d}")

    @staticmethod
    def est_bissextile(annee):
        """
        Renvoie True si l'année est bissextile, False sinon.

        Règle :
        - une année divisible par 4 est bissextile ;
        - sauf si elle est divisible par 100 ;
        - mais elle reste bissextile si elle est divisible par 400.
        """
        pass

    @staticmethod
    def jours_dans_annee(annee):
        """
        Renvoie le nombre de jours dans une année.

        Une année bissextile comporte 366 jours,
        une année normale en comporte 365.
        """
        # Utiliser la méthode est_bissextile()
        pass

    @staticmethod
    def jours_dans_mois(mois, annee):
        """
        Renvoie le nombre de jours du mois indiqué.
        """
        pass

    def est_valide(self):
        """
        Vérifie que la date et l'heure sont valides.

        Une date valide doit respecter les contraintes suivantes :
        - année >= 1
        - mois compris entre 1 et 12
        - jour adapté au mois et à l'année
        - heure comprise entre 0 et 23
        - minute comprise entre 0 et 59
        - seconde comprise entre 0 et 59
        """
        # Vérifier chaque contrainte.
        #
        # Pour vérifier le nombre maximal de jours du mois,
        # utiliser Instant.jours_dans_mois().
        pass

    def en_secondes(self):
        """
        Renvoie le nombre de secondes écoulées depuis
        le 01/01/1970 à 00:00:00.

        Le résultat peut être négatif pour une date antérieure à 1970.
        """
        # On commence par calculer le nombre de jours écoulés
        # entre le 01/01/1970 et le début de l'année de self.
        #
        # Si l'année est >= 1970 :
        #   additionner les jours des années de 1970 à self.annee - 1.
        #
        # Si l'année est < 1970 :
        #   soustraire les jours des années de self.annee à 1969.
        #
        # Ajouter ensuite les jours des mois précédents
        # dans l'année de self.
        #
        # Ajouter self.jour - 1.
        #
        # Convertir ensuite les jours en secondes :
        #   1 jour = 24 * 3600 secondes
        #
        # Ajouter les secondes correspondant aux heures,
        # aux minutes et aux secondes.
        pass

    def jour_de_la_semaine(self):
        """
        Renvoie le nom du jour de la semaine.

        Le résultat doit être l'une des chaînes :
        lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche
        """
        # Le 01/01/1970 était un jeudi.
        #
        # Calculer le nombre de jours entiers écoulés depuis
        # le 01/01/1970 à partir du timestamp.
        #
        # Utiliser le modulo 7 pour déterminer le jour de la semaine.
        pass

    @staticmethod
    def depuis_timestamp(timestamp):
        """
        Construit et renvoie un Instant à partir d'un timestamp Unix.

        Le timestamp représente le nombre de secondes écoulées depuis
        le 01/01/1970 à 00:00:00.

        Le timestamp peut être négatif.
        """
        # Séparer le timestamp en :
        #   - nombre de jours écoulés depuis le 01/01/1970
        #   - nombre de secondes restantes dans la journée
        #
        # Attention : utiliser // et % permet également de gérer
        # correctement les timestamps négatifs.
        #
        # Partir de l'année 1970.
        #
        # Si le nombre de jours est positif :
        #   retirer successivement le nombre de jours de chaque année
        #   jusqu'à trouver l'année recherchée.
        #
        # Si le nombre de jours est négatif :
        #   reculer année par année en ajoutant le nombre de jours
        #   de chaque année traversée.
        #
        # Une fois l'année trouvée :
        #   rechercher le mois en retirant successivement
        #   le nombre de jours de chaque mois.
        #
        # Le nombre de jours restant permet d'obtenir le jour du mois.
        #
        # Convertir enfin les secondes restantes en :
        #   heure
        #   minute
        #   seconde
        #
        # Construire et retourner le Instant correspondant.
        pass


# ============================================================
# Tests de la classe Instant
# ============================================================

# ------------------------------------------------------------
# 1. Années bissextiles
# ------------------------------------------------------------

assert Instant.est_bissextile(2024) is True
assert Instant.est_bissextile(2025) is False
assert Instant.est_bissextile(1900) is False
assert Instant.est_bissextile(2000) is True

# ------------------------------------------------------------
# 2. Nombre de jours dans une année
# ------------------------------------------------------------

assert Instant.jours_dans_annee(2024) == 366
assert Instant.jours_dans_annee(2025) == 365
assert Instant.jours_dans_annee(1900) == 365
assert Instant.jours_dans_annee(2000) == 366

# ------------------------------------------------------------
# 3. Nombre de jours dans un mois
# ------------------------------------------------------------

assert Instant.jours_dans_mois(1, 2025) == 31
assert Instant.jours_dans_mois(2, 2025) == 28
assert Instant.jours_dans_mois(2, 2024) == 29
assert Instant.jours_dans_mois(4, 2025) == 30
assert Instant.jours_dans_mois(12, 2025) == 31

# ------------------------------------------------------------
# 4. Validation des dates
# ------------------------------------------------------------

# Dates valides
assert Instant(1, 1, 2025, 0, 0, 0).est_valide()
assert Instant(31, 1, 2025, 23, 59, 59).est_valide()
assert Instant(29, 2, 2024, 12, 0, 0).est_valide()
assert Instant(31, 12, 2025, 23, 59, 59).est_valide()

# Dates invalides
for date in [
    (29, 2, 2025, 12, 0, 0),
    (31, 4, 2025, 12, 0, 0),
    (31, 6, 2025, 12, 0, 0),
    (32, 1, 2025, 12, 0, 0),
    (1, 0, 2025, 12, 0, 0),
    (1, 13, 2025, 12, 0, 0),
    (1, 1, 0, 12, 0, 0),
    (1, 1, 2025, 24, 0, 0),
    (1, 1, 2025, 12, 60, 0),
    (1, 1, 2025, 12, 0, 60),
]:
    try:
        Instant(*date)
        assert False, f"Date acceptée à tort : {date}"
    except AssertionError:
        pass

# ------------------------------------------------------------
# 5. Affichage
# ------------------------------------------------------------

assert str(Instant(2, 10, 2026, 14, 30, 45)) == \
       "02/10/2026:14:30:45"

assert str(Instant(1, 1, 2025, 0, 0, 0)) == \
       "01/01/2025:00:00:00"

assert str(Instant(9, 3, 2025, 7, 5, 4)) == \
       "09/03/2025:07:05:04"

# ------------------------------------------------------------
# 6. Timestamp
# ------------------------------------------------------------

# Origine Unix
assert Instant(1, 1, 1970, 0, 0, 0).en_secondes() == 0

# Quelques secondes après l'origine
assert Instant(1, 1, 1970, 0, 0, 1).en_secondes() == 1
assert Instant(1, 1, 1970, 0, 1, 0).en_secondes() == 60
assert Instant(1, 1, 1970, 1, 0, 0).en_secondes() == 3600

# Un jour après l'origine
assert Instant(2, 1, 1970, 0, 0, 0).en_secondes() == 86400

# Juste avant l'origine
assert Instant(31, 12, 1969, 23, 59, 59).en_secondes() == -1

# Une année complète
assert Instant(1, 1, 1971, 0, 0, 0).en_secondes() == 365 * 86400

# Passage par une année bissextile
assert Instant(1, 1, 1973, 0, 0, 0).en_secondes() == \
       (365 + 366 +365) * 86400

# ------------------------------------------------------------
# 7. Jour de la semaine
# ------------------------------------------------------------

assert Instant(1, 1, 1970, 0, 0, 0).jour_de_la_semaine() == "jeudi"
assert Instant(2, 1, 1970, 0, 0, 0).jour_de_la_semaine() == "vendredi"
assert Instant(4, 1, 1970, 0, 0, 0).jour_de_la_semaine() == "dimanche"
assert Instant(5, 1, 1970, 0, 0, 0).jour_de_la_semaine() == "lundi"

# Quelques dates connues
assert Instant(1, 1, 2000, 0, 0, 0).jour_de_la_semaine() == "samedi"
assert Instant(29, 2, 2024, 0, 0, 0).jour_de_la_semaine() == "jeudi"
assert Instant(2, 10, 2026, 0, 0, 0).jour_de_la_semaine() == "vendredi"

# ------------------------------------------------------------
# 8. Timestamp -> Instant
# ------------------------------------------------------------

assert str(Instant.depuis_timestamp(0)) == \
       "01/01/1970:00:00:00"

assert str(Instant.depuis_timestamp(1)) == \
       "01/01/1970:00:00:01"

assert str(Instant.depuis_timestamp(60)) == \
       "01/01/1970:00:01:00"

assert str(Instant.depuis_timestamp(3600)) == \
       "01/01/1970:01:00:00"

assert str(Instant.depuis_timestamp(86400)) == \
       "02/01/1970:00:00:00"

assert str(Instant.depuis_timestamp(-1)) == \
       "31/12/1969:23:59:59"

# ------------------------------------------------------------
# 9. Vérification aller-retour
# ------------------------------------------------------------

dates = [
    Instant(1, 1, 1970, 0, 0, 0),
    Instant(31, 12, 1969, 23, 59, 59),
    Instant(29, 2, 2024, 12, 30, 45),
    Instant(31, 12, 2024, 23, 59, 59),
    Instant(1, 1, 2000, 0, 0, 0),
    Instant(2, 10, 2026, 14, 30, 45),
    Instant(31, 12, 2026, 23, 59, 59),
]

for date in dates:
    timestamp = date.en_secondes()
    nouvelle_date = Instant.depuis_timestamp(timestamp)

    assert nouvelle_date == date, \
        f"Échec pour {date} (timestamp = {timestamp})"

print("Tous les tests sont réussis !")
