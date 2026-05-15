import random

# ------------------------------------------------------------
# Jeu du Pendu - MGA802-01
# Etudiant : Pierre-Jean Tulasne (TULP86260301)
# ------------------------------------------------------------


def supprimer_accents(mot):
    # On remplace les lettres avec les accents par leurs équivalents sans accents (ici le code ce base sur la position de l'indice de chaque lettre avec accent pou prendre son équivalent a la même position)
    accents = "àâäéèêëîïôùûüç"
    sans_accents = "aaaeeeeiiouuuc"
    mot_sans_accent = ""
    for lettre in mot:
        if lettre in accents:
            mot_sans_accent = mot_sans_accent + sans_accents[accents.index(lettre)]
        else:
            mot_sans_accent = mot_sans_accent + lettre
    return mot_sans_accent


def charger_mots(nom_fichier):
    # On ouvre le fichier et on charge tous les mots dans une liste
    fichier = open(nom_fichier, "r", encoding="utf-8")
    mots = []
    for ligne in fichier:
        mot = ligne.strip()
        if mot != "":
            mots.append(supprimer_accents(mot.lower()))
    fichier.close()
    return mots


def choisir_fichier():
    # On demande a l'utilisateur s'il veut utiliser son propre fichier qu'il a réaliser ou le fichier par défaut qui est fournie
    print("Voulez-vous utiliser votre propre fichier de mots ?")
    print("1. Oui")
    print("2. Non, utiliser le fichier par défaut")
    choix = input("Quel est votre choix (1 ou 2) : ")
    if choix == "1":
        nom_fichier = input("Entrez le nom de votre fichier et vérifiez qu'il est bien dans le bon emplacement (ex: mon_fichier.txt) : ")
        return nom_fichier
    else:
        return "mots_pendu.txt"


def choisir_mot(mots):
    # On choisit un mot aléatoire dans la liste que l'utilisateur a choisi.
    return random.choice(mots)


def afficher_etat(mot, lettres_devinees):
    # On affiche le mot avec des _ pour les lettres qui non pas encore était trouver
    etat = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            etat = etat + lettre + " "
        else:
            etat = etat + "_ "
    print("Mot : " + etat)


def verifier_victoire(mot, lettres_devinees):
    # On vérifie si toutes les lettres du mot ont été devinées par le joueur.
    for lettre in mot:
        if lettre not in lettres_devinees:
            return False
    return True


def donner_indice(mot, lettres_devinees):
    # BONUS : On donne une lettre qui n'est pas dans le mot
    lettres_alphabet = "abcdefghijklmnopqrstuvwxyz"
    lettres_pas_dans_mot = []
    for lettre in lettres_alphabet:
        if lettre not in mot and lettre not in lettres_devinees:
            lettres_pas_dans_mot.append(lettre)
    if len(lettres_pas_dans_mot) > 0:
        indice = random.choice(lettres_pas_dans_mot)
        print("Indice : la lettre '" + indice + "' ne fait pas partie du mot !")


def jouer(mot):
    # Fonction principale du jeu qui gère la boucle de jeu
    chances = 6
    lettres_devinees = []
    print("\n" + "=" * 40)
    print("Le mot a " + str(len(mot)) + " lettres.")

    while chances > 0:
        print("\n" + "-" * 40)
        print("Chances restantes : " + str(chances))
        afficher_etat(mot, lettres_devinees)

        # BONUS : Si il reste une chance, on donne un indice
        if chances == 1:
            print("Dernière chance ! Voici un indice :")
            donner_indice(mot, lettres_devinees)

        # On demande une lettre à l'utilisateur
        lettre = input("Entrez une lettre : ").lower()
        lettre = supprimer_accents(lettre)

        # On vérifie que c'est bien une seule lettre et si elle est bien dans les 26 lettres de l'alphabet.
        if len(lettre) != 1 or lettre not in "abcdefghijklmnopqrstuvwxyz":
            print("Veuillez entrer une seule lettre valide.")
            continue

        # On vérifie si la lettre a déjà été proposée
        if lettre in lettres_devinees:
            print("Vous avez déjà proposé la lettre '" + lettre + "' !")
            continue

        # On ajoute la lettre aux lettres devinées
        lettres_devinees.append(lettre)

        # On vérifie si la lettre est dans le mot a deviner
        if lettre in mot:
            print("Bonne réponse ! La lettre '" + lettre + "' est dans le mot !")
        else:
            chances = chances - 1
            print("Mauvaise réponse ! La lettre '" + lettre + "' n'est pas dans le mot.")

        # On vérifie si le joueur a gagné
        if verifier_victoire(mot, lettres_devinees):
            afficher_etat(mot, lettres_devinees)
            print("\nFélicitations ! Vous avez trouvé le mot : " + mot + " !")
            return

    # Si on sort de la boucle sans avoir gagné, le joueur a perdu
    print("\nVous avez perdu ! Le mot était : " + mot)


def lancer_jeu():
    # Fonction qui lance le jeu et propose de rejouer
    print("=" * 40)
    print("     Bienvenue dans le Jeu du Pendu !")
    print("=" * 40)

    # On choisit le fichier de mots, entre celui de base et si il préfère un perso.
    nom_fichier = choisir_fichier()
    mots = charger_mots(nom_fichier)

    # Boucle principale qui permet de rejouer
    continuer = "o"
    while continuer == "o":
        mot = choisir_mot(mots)
        jouer(mot)

        # On propose de rejouer
        print("\nVoulez-vous rejouer ?")
        continuer = input("Entrez 'o' pour rejouer ou 'n' pour quitter : ").lower()

    print("\nMerci d'avoir joué ! À bientôt !")


# Point d'entrée du programme
lancer_jeu()