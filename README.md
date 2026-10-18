# NSI Terminale — Supports de cours

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SamiChabbi/nsi-terminale/main)

Supports de cours de NSI (Terminale) sous forme de notebooks Jupyter : transcriptions de cours, exercices résolus avec explications pédagogiques, TP et devoirs corrigés.

## Contenu

```
cours/
├── Transcription/       leçons 01, 02A à 02F (texte du cours + exemples exécutables)
└── Exercices_resolus/   exercices de chaque leçon, corrigés et expliqués
tp1/
├── TP_transcription     énoncé du Projet 1 : Mastermind
└── TP_explication       explications étape par étape, erreurs courantes
dm1/
└── DM1_Files_Piles_resolution   DM Files et Piles : énoncé, résolution et explications
Iheb/
├── 01_POO_Programmation_Orientee_Objet   POO : cours et exercices résolus
└── 02_Diviser_pour_regner_*              diviser pour régner : sujet et exercices résolus
```

| Leçon | Thème |
|:---|:---|
| 01 | POO — Les classes |
| 02A | Structures linéaires — TDA / TDC |
| 02B | Les listes |
| 02C | Les dictionnaires |
| 02D | Les piles |
| 02E | Les files |
| 02F | Les listes chaînées |

## Utilisation

- **En ligne :** cliquer sur le badge *Binder* ci-dessus (premier lancement : quelques minutes).
- **Sur son ordinateur :** `jupyter notebook` dans le dossier du dépôt.

Exécuter les cellules **dans l'ordre** (*Cell → Run All*).

> ⚠️ Le TP Mastermind utilise Tkinter (fenêtre graphique) : le jeu doit être exécuté **sur son ordinateur**. La fenêtre ne peut pas s'ouvrir sur Binder ou Colab.
