# Projet 1 : Mastermind — Terminale NSI 2026-2027
# Solution complète (même code que tp1/TP_resolution.ipynb)
# Lancer avec :  python3 mastermind_solution.py

# Modules utilisés : tkinter pour l'interface, random pour le tirage (choice, leçon 02B)
from tkinter import *
from random import choice

# Couleurs disponibles : blanc, noir, jaune, bleu, rouge, vert
COULEURS = ['white', 'black', 'yellow', 'blue', 'red', 'green']
NB_ESSAIS = 12                                # 12 essais maximum
FICHIER_SCORES = "scores_mastermind.csv"      # fichier des meilleurs scores

# Positions sur le canevas
X_GRILLE = 340        # abscisse du centre du 1er rond de chaque ligne
ECART = 60            # écart horizontal entre deux ronds
Y_GRILLE = 30         # ordonnée du centre de la 1re ligne
HAUTEUR = 40          # écart vertical entre deux lignes
RAYON = 16            # rayon d'un rond


# ---------- La fenêtre et le canevas 600x600 ----------
fenetre = Tk()
fenetre.title("Mastermind")
canevas = Canvas(fenetre, width=600, height=600, bg='burlywood')
canevas.grid(row=0, column=0, rowspan=10)

# Personnalisation : le nom du jeu
canevas.create_text(95, 40, text="MASTER\nMIND", font=('Arial', 22, 'bold'), fill='saddlebrown')

# ---------- La grille des 12 essais : 12 lignes de 4 ronds gris ----------
# Grille[ligne][colonne] contient l'identifiant du rond (tableau à 2 dimensions)
Grille = []
Textes_bien = []      # identifiants des textes "bien placés" (un par ligne)
Textes_mal = []       # identifiants des textes "mal placés" (un par ligne)
for ligne in range(NB_ESSAIS):
    Grille.append([])                             # on ajoute une nouvelle ligne
    y = Y_GRILLE + ligne * HAUTEUR
    for colonne in range(4):
        x = X_GRILLE + colonne * ECART
        objet = canevas.create_oval(x - RAYON, y - RAYON, x + RAYON, y + RAYON,
                                    fill='lightgrey')
        Grille[ligne].append(objet)               # on range l'identifiant dans le tableau
    # Deux textes vides à gauche de la ligne, remplis à l'étape 6
    Textes_bien.append(canevas.create_text(X_GRILLE - 70, y, text="", fill='red', font=('Arial', 16, 'bold')))
    Textes_mal.append(canevas.create_text(X_GRILLE - 45, y, text="", fill='black', font=('Arial', 16, 'bold')))

# ---------- La 13e ligne : 4 ronds noirs surmontés d'un « ? » ----------
canevas.create_line(X_GRILLE - 90, 505, 590, 505, width=3)
Secret = []           # identifiants des 4 ronds de la combinaison cachée
Points_interro = []   # identifiants des 4 « ? »
for colonne in range(4):
    x = X_GRILLE + colonne * ECART
    Secret.append(canevas.create_oval(x - RAYON, 545 - RAYON, x + RAYON, 545 + RAYON, fill='black'))
    Points_interro.append(canevas.create_text(x, 545, text="?", fill='white', font=('Arial', 16, 'bold')))

# ---------- 4 boutons de couleur (la commande sera ajoutée à l'étape 3) ----------
Label(fenetre, text="Votre proposition :").grid(row=0, column=1, columnspan=4)
Choix = ['white', 'white', 'white', 'white']     # couleur actuelle de chaque bouton
Boutons = []
for numero in range(4):
    bouton = Button(fenetre, width=3, height=2, bg=Choix[numero], activebackground=Choix[numero])
    bouton.grid(row=1, column=1 + numero, padx=2)
    Boutons.append(bouton)

# ---------- Boutons « Valider » et « Rejouer » (commandes ajoutées aux étapes 6 et 7) ----------
bouton_valider = Button(fenetre, text="Valider", width=10)
bouton_valider.grid(row=2, column=1, columnspan=2, pady=5)
bouton_rejouer = Button(fenetre, text="Rejouer", width=10)
bouton_rejouer.grid(row=2, column=3, columnspan=2, pady=5)


# Une entry pour le pseudo, avec son étiquette
Label(fenetre, text="Pseudo :").grid(row=3, column=1, columnspan=2)
entree_pseudo = Entry(fenetre, width=12)
entree_pseudo.grid(row=3, column=3, columnspan=2)

# Label qui affichera le pseudo du joueur (étape 6)
label_joueur = Label(fenetre, text="Joueur : ", font=('Arial', 11, 'bold'))
label_joueur.grid(row=4, column=1, columnspan=4)

# Label pour les messages (erreur, victoire, défaite)
message = Label(fenetre, text="", fg='darkred', wraplength=200)
message.grid(row=5, column=1, columnspan=4)


def generer_combinaison():
    """Renvoie une liste de 4 couleurs tirées au hasard (répétitions possibles)."""
    combinaison = []
    for i in range(4):
        combinaison.append(choice(COULEURS))   # choice : tirage au hasard (module random)
    return combinaison

# Appel au lancement du jeu + affichage console pour tester
combinaison = generer_combinaison()
print(combinaison)


def changer_couleur(numero_bouton):
    """Fait passer le bouton numero_bouton à la couleur suivante (retour au début après la dernière)."""
    indice = COULEURS.index(Choix[numero_bouton])   # position de la couleur actuelle
    if indice == len(COULEURS) - 1:                 # dernière couleur : on revient à la première
        indice = 0
    else:
        indice = indice + 1
    Choix[numero_bouton] = COULEURS[indice]
    Boutons[numero_bouton].config(bg=COULEURS[indice], activebackground=COULEURS[indice])

# Une petite fonction par bouton (pas de lambda)
def action1():
    changer_couleur(0)

def action2():
    changer_couleur(1)

def action3():
    changer_couleur(2)

def action4():
    changer_couleur(3)

Boutons[0].config(command=action1)
Boutons[1].config(command=action2)
Boutons[2].config(command=action3)
Boutons[3].config(command=action4)

def recuperer_proposition():
    """Renvoie la liste des 4 couleurs actuellement choisies par le joueur."""
    proposition = []
    for couleur in Choix:
        proposition.append(couleur)    # on renvoie une copie de la liste Choix
    return proposition


def compter_bien_places(proposition, combinaison):
    """Nombre de positions où proposition et combinaison ont la même couleur."""
    nb = 0
    for i in range(4):
        if proposition[i] == combinaison[i]:
            nb = nb + 1
    return nb

print(compter_bien_places(['red','red','blue','green'], ['red','red','blue','green']))   # 4


def compter_mal_places(proposition, combinaison):
    """Nombre de pions de bonne couleur mais mal placés (sans recompter les bien placés)."""
    # 1) On ne garde que les positions où proposition et combinaison diffèrent
    combinaison_restante = []
    proposition_restante = []
    for i in range(4):
        if proposition[i] != combinaison[i]:
            combinaison_restante.append(combinaison[i])
            proposition_restante.append(proposition[i])
    # 2) Chaque couleur trouvée est retirée pour ne pas la compter deux fois
    nb = 0
    for couleur in proposition_restante:
        if couleur in combinaison_restante:
            nb = nb + 1
            combinaison_restante.remove(couleur)   # supprime la 1re occurrence
    return nb

print(compter_mal_places(['blue','blue','green','red'], ['red','red','blue','green']))   # 3


numero_essai = 0          # numéro de la ligne d'essai en cours (0 à 11)
partie_terminee = False

def reveler_combinaison():
    """Affiche la combinaison secrète sur la 13e ligne."""
    for colonne in range(4):
        canevas.itemconfig(Secret[colonne], fill=combinaison[colonne])
        canevas.itemconfig(Points_interro[colonne], text="")

def verification():
    global numero_essai, partie_terminee
    # La partie est terminée : on ne fait rien
    if partie_terminee:
        return
    # Pseudo non renseigné : message d'erreur, la tentative n'est pas comptée
    pseudo = entree_pseudo.get()
    if pseudo == "":
        message.config(text="Erreur : entrez votre pseudo avant de valider !")
        return
    message.config(text="")
    label_joueur.config(text="Joueur : " + pseudo)
    # On récupère la proposition et on colorie la ligne d'essai
    proposition = recuperer_proposition()
    for colonne in range(4):
        canevas.itemconfig(Grille[numero_essai][colonne], fill=proposition[colonne])
    # On calcule et on affiche les deux nombres à côté de la ligne
    bien = compter_bien_places(proposition, combinaison)
    mal = compter_mal_places(proposition, combinaison)
    canevas.itemconfig(Textes_bien[numero_essai], text=str(bien))
    canevas.itemconfig(Textes_mal[numero_essai], text=str(mal))
    if bien == 4:
        # Victoire
        reveler_combinaison()
        message.config(text="Bravo " + pseudo + " ! Trouvé en " + str(numero_essai + 1) + " essai(s).")
        partie_terminee = True
        enregistrer_score_si_top3(pseudo, numero_essai + 1)    # étapes 8 à 10
    elif numero_essai == NB_ESSAIS - 1:
        # Plus d'essais : défaite
        reveler_combinaison()
        message.config(text="Perdu ! Voici la combinaison secrète.")
        partie_terminee = True
    numero_essai = numero_essai + 1

bouton_valider.config(command=verification)


def rejouer():
    global combinaison, numero_essai, partie_terminee
    # Nouvelle combinaison secrète
    combinaison = generer_combinaison()
    print(combinaison)
    # Grille remise en gris et historique effacé
    for ligne in range(NB_ESSAIS):
        for colonne in range(4):
            canevas.itemconfig(Grille[ligne][colonne], fill='lightgrey')
        canevas.itemconfig(Textes_bien[ligne], text="")
        canevas.itemconfig(Textes_mal[ligne], text="")
    # Combinaison de nouveau cachée
    for colonne in range(4):
        canevas.itemconfig(Secret[colonne], fill='black')
        canevas.itemconfig(Points_interro[colonne], text="?")
    # Compteur d'essais et messages réinitialisés
    numero_essai = 0
    partie_terminee = False
    message.config(text="")

bouton_rejouer.config(command=rejouer)


def lire_classement(nom_fichier=FICHIER_SCORES):
    """Renvoie le classement contenu dans le fichier sous forme de liste de listes [pseudo, score]."""
    try:
        fichier = open(nom_fichier, "r", encoding="utf-8")
        lignes = fichier.readlines()
        fichier.close()
    except FileNotFoundError:
        return []                          # premier lancement : pas encore de fichier
    classement = []
    for ligne in lignes[1:]:               # on saute la ligne d'en-tête Pseudo;Score
        if ligne[-1] == "\n":
            ligne = ligne[:-1]             # on retire le \n de fin de ligne
        if ligne != "":
            morceaux = ligne.split(";")    # ["Zelda", "5"]
            classement.append([morceaux[0], int(morceaux[1])])
    return classement

def ecrire_classement(classement, nom_fichier=FICHIER_SCORES):
    """Écrit le classement dans le fichier (en-tête puis une ligne par joueur)."""
    lignes = ["Pseudo;Score"]
    for joueur in classement:
        lignes.append(";".join([joueur[0], str(joueur[1])]))
    texte = "\n".join(lignes)
    fichier = open(nom_fichier, "w", encoding="utf-8")
    fichier.write(texte)
    fichier.close()


def trier_classement(classement):
    """Trie sur place le classement du meilleur score (le plus petit) au moins bon : tri à bulle."""
    n = len(classement)
    for i in range(n):
        for j in range(n - 1 - i):
            if classement[j][1] > classement[j + 1][1]:     # on compare les scores
                temporaire = classement[j]                   # on échange les deux joueurs
                classement[j] = classement[j + 1]
                classement[j + 1] = temporaire

def calculer_nouveau_classement(classement, pseudo, score):
    """Renvoie le nouveau classement (3 joueurs max) après la victoire de pseudo en score essais."""
    # Copie du classement pour ne pas modifier la liste reçue
    nouveau = []
    for joueur in classement:
        nouveau.append([joueur[0], joueur[1]])
    trier_classement(nouveau)
    # Règle 1 : un joueur a déjà exactement ce score, on prend sa place
    place_prise = False
    for i in range(len(nouveau)):
        if not place_prise and nouveau[i][1] == score:
            nouveau[i] = [pseudo, score]
            place_prise = True
    if not place_prise:
        if len(nouveau) < 3:
            # Règle 2 : moins de 3 joueurs, on ajoute
            nouveau.append([pseudo, score])
        elif score < nouveau[-1][1]:
            # Règle 3 : meilleur que le moins bon (le dernier après tri), on le remplace
            nouveau[-1] = [pseudo, score]
        # Sinon : le classement ne change pas
    trier_classement(nouveau)
    return nouveau


# Zone d'affichage du classement, en bas à gauche du canevas
texte_classement = canevas.create_text(10, 470, text="", anchor='nw', font=('Arial', 10, 'bold'))

def construire_texte_classement(classement):
    """Construit le texte : une ligne « Classement : » puis une ligne numérotée par joueur."""
    texte = "Classement :"
    for i in range(len(classement)):
        texte = texte + "\n" + str(i + 1) + ". " + classement[i][0] + " : " + str(classement[i][1]) + " essai(s)"
    return texte

def afficher_classement(classement):
    """Met à jour le texte du classement sur le canevas."""
    canevas.itemconfig(texte_classement, text=construire_texte_classement(classement))

def enregistrer_score_si_top3(pseudo, score):
    """Lit le classement, calcule le nouveau, l'écrit dans le fichier et rafraîchit l'affichage."""
    classement = lire_classement()
    nouveau = calculer_nouveau_classement(classement, pseudo, score)
    ecrire_classement(nouveau)
    afficher_classement(nouveau)

# Affichage du classement dès l'ouverture de la fenêtre
afficher_classement(lire_classement())


# Lancement de la boucle d'événements : la fenêtre reste ouverte jusqu'à sa fermeture
fenetre.mainloop()
