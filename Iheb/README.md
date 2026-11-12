# NSI Terminale — POO, « diviser pour régner » et files : cours et exercices résolus

Notebooks Jupyter : chaque question est résolue, testée et accompagnée d'une **explication pédagogique**, avec les erreurs fréquentes à éviter.

## Contenu

```
01_POO_Programmation_Orientee_Objet/
├── POO_Cours_et_Exercices_Heros_de_Troie.pdf      sujet
├── POO_Ex1_Heros_de_Troie_resolution.ipynb        classes, attributs, méthodes, composition
├── POO_Ex2_Angle_resolution.ipynb                 implémenter une API, méthodes spéciales
└── POO_Ex3_Instant_resolution.ipynb               méthodes statiques
02_Diviser_pour_regner_Photos_originales/          photos du polycopié
02_Diviser_pour_regner_Transcription_PDF/          transcription fidèle du polycopié
02_Diviser_pour_regner_Resolutions/
├── DPR_Ex1_Mots_mysterieux_dichotomie.ipynb       recherche dichotomique
├── DPR_Ex2_Tri_fusion.ipynb                       fusion, tri fusion récursif et itératif
├── DPR_Ex3_Exponentiation_rapide.ipynb            compter les multiplications
├── DPR_Ex4_Ex5_Logarithme_et_croissance.ipynb     log binaire, ordres de grandeur
├── DPR_Ex6_Pavage_triominos.ipynb                 pavage récursif d'une grille 2^k × 2^k
├── DPR_Ex7_Rotation_image.ipynb                   rotation d'image avec / sans tableau
└── DPR_Ex8_Plus_proche_paire_de_points.ipynb      plus courte distance en n log(n)
03_Files_Structure_de_donnees/
├── Files_Cours_et_Exercices.pdf                   sujet
├── file.py                                        la classe File (exercice 1), importée par les autres notebooks
├── FILES_Ex1_Classe_File.ipynb                    implémenter une file (FIFO)
├── FILES_Ex2_Passe_ton_tour_occurrences.ipynb     rotation, parcourir une file sans la modifier
├── FILES_Ex3_Permutations.ipynb                   modifier une file en place
├── FILES_Ex4_Recherche_et_doublons.ipynb          recherche, file auxiliaire
├── FILES_Ex5_VIN_first.ipynb                      répartir les éléments selon un critère
├── FILES_Ex6_Pile_avec_deux_files.ipynb           une pile (LIFO) avec deux files
└── FILES_Ex7_Nombres_de_Hamming.ipynb             force brute, trois files, optimisation
```

## Utilisation

- **Sur son ordinateur :** lancer `jupyter notebook` dans le dossier, ouvrir un notebook, puis *Cell → Run All*.
- Les notebooks n'utilisent **que Python standard** (aucune bibliothèque à installer).
- Exercice 1 de « diviser pour régner » : placer `dico.txt` et `mots.txt` à côté du notebook. Sans ces fichiers, des fichiers de démonstration sont générés automatiquement.
- Exercice 7 : le module `turnbuffon.py` (pygame) est simulé dans le notebook. La fin du notebook explique comment utiliser le vrai module.
- Files : garder `file.py` dans le même dossier que les notebooks (ils font `from file import File`).
