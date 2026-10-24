# NSI Terminale — POO et « diviser pour régner » : cours et exercices résolus

Notebooks Jupyter : chaque question est résolue, testée et accompagnée d'une **explication pédagogique**, avec les erreurs fréquentes à éviter.

Pour chaque question, trois blocs toujours séparés : **📝 ÉNONCÉ** (recopié du sujet), **✅ RÉSOLUTION** (la réponse attendue) et **💡 EXPLICATION PÉDAGOGIQUE** (à ne pas recopier).

## Contenu

```
01_POO_Programmation_Orientee_Objet/
├── POO_Cours_et_Exercices_Heros_de_Troie.pdf      sujet
├── heros.py, angle.py, instant.py                 fichiers distribués avec le cours
├── POO_Ex1_Heros_de_Troie_resolution.ipynb        classes, attributs, méthodes, composition
├── POO_Ex2_Angle_resolution.ipynb                 implémenter une API, méthodes spéciales
└── POO_Ex3_Instant_resolution.ipynb               méthodes statiques
02_Diviser_pour_regner_Transcription_PDF/          transcription fidèle du polycopié
02_Diviser_pour_regner_Resolutions/
├── DPR_Ex1_Mots_mysterieux_dichotomie.ipynb       recherche dichotomique
├── DPR_Ex2_Tri_fusion.ipynb                       fusion, tri fusion récursif et itératif
├── DPR_Ex3_Exponentiation_rapide.ipynb            compter les multiplications
├── DPR_Ex4_Ex5_Logarithme_et_croissance.ipynb     log binaire, ordres de grandeur
├── DPR_Ex6_Pavage_triominos.ipynb                 pavage récursif d'une grille 2^k × 2^k
├── DPR_Ex7_Rotation_image.ipynb                   rotation d'image avec / sans tableau
├── DPR_Ex8_Plus_proche_paire_de_points.ipynb      plus courte distance en n log(n)
└── dico.txt, mots.txt, turnbuffon.png             fichiers distribués avec le cours
```

## Utilisation

- **Sur son ordinateur :** lancer `jupyter notebook` dans le dossier, ouvrir un notebook, puis *Cell → Run All*.
- Les notebooks n'utilisent **que Python standard** (aucune bibliothèque à installer).
- Les fichiers distribués avec le cours sont placés à côté des notebooks : `heros.py`, `angle.py` et `instant.py` pour la POO (les corrections des exercices 2 et 3 passent les tests contenus dans `angle.py` et `instant.py`), `dico.txt` et `mots.txt` pour l'exercice 1 de « diviser pour régner », `turnbuffon.png` pour l'exercice 7.
- Exercice 7 : le module `turnbuffon.py` (pygame) est simulé dans le notebook. La fin du notebook explique comment utiliser le vrai module. Les deux méthodes de rotation ont été vérifiées sur la vraie image `turnbuffon.png`.
