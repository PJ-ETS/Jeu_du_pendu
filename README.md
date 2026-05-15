# Jeu du Pendu
Ce Jeu est un jeu que nous connaissons tous qui est le jeu du pendu réaliser sous forme de code et executable dans un terminal. Ce jeu est réalisé dans le cadre du cour MGA802-01 Introduction à la programmation avec Python à l'ÉTS.

## Description
Un jeu du pendu en mode texte dans un terminal. Le programme choisit un mot aléatoire dans un fichier texte et le joueur doit le deviner lettre par lettre en 6 chances. Lors de ça dernière tentative, le jeu donne un indice au joueur sur une lettre qui n'est pas dans le mot.

## Fichiers fourni dans github
- `pendu.py` : le script principal du jeu
- `mots_pendu.txt` : le fichier de mots utilisé par défaut
- `README.md` : fichier de description du contenu du code et de sont utilisation.

## Comment jouer au jeu
1. Télécharger sur sont ordinateur le fichier `.py` et `.txt` et les mettres dans un même dossier
2. Ouvrir un terminal dans le dossier du projet
3. Lancer le jeu avec la commande : `python pendu.py`
4. Choisir d'utiliser le fichier de mots par défaut ou un fichier personnel
5. Deviner le mot lettre par lettre
6. Rejouer avec la letre `o` pour oui ou décider d'arreter avec la lettre `n` pour non

## Fonctionnement du code
- Sélection aléatoire d'un mot depuis un fichier texte que le joeur a choisi (fichier de base fournit avec ou fichier personnel du joeur)
- Gestion des lettres accentuées (é, è, à, etc.) en les remplacant par leur équivalent sans accent (e, e, a, etc.)
- Evolution des lettres ca
- Indice donné à la dernière chance
- Option de rejouer après chaque partie
