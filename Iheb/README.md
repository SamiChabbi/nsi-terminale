# NSI Terminale — POO et « diviser pour régner » : cours et exercices résolus

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
```

## Utilisation

- **Sur son ordinateur :** lancer `jupyter notebook` dans le dossier, ouvrir un notebook, puis *Cell → Run All*.
- Les notebooks n'utilisent **que Python standard** (aucune bibliothèque à installer).
- Exercice 1 de « diviser pour régner » : placer `dico.txt` et `mots.txt` à côté du notebook. Sans ces fichiers, des fichiers de démonstration sont générés automatiquement.
- Exercice 7 : le module `turnbuffon.py` (pygame) est simulé dans le notebook. La fin du notebook explique comment utiliser le vrai module.
