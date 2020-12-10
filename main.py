# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:33:03 2020
Ce programme est la page principale pour jouer au pendu sans interface graphique
https://github.com/Teklaw7/pendu-console.git
@author: Timothée Teyssier
"""




from donnees import *
from fonctions import *





scores = recup_scores()


utilisateur = recup_nom_utilisateur()


if utilisateur not in scores.keys():
    scores[utilisateur] = 0 

continuer_partie = 'o'

while continuer_partie != 'n':
    print("Joueur {0}: {1} point(s)".format(utilisateur, scores[utilisateur]))
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = affichage(mot_a_trouver, lettres_trouvees)
    nb_chances = tentatives
    while mot_a_trouver!=mot_trouve and nb_chances>0:
        print("Mot mystère est :{0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Attention cette lettre a déja été proposée")
        elif lettre in mot_a_trouver: 
            lettres_trouvees.append(lettre)
            print("Bien joué. Continuez.")
        else:
            nb_chances -= 1
            print("Faux, cette lettre ne se trouve pas dans le mot (encore {1} chances)".format(mot_trouve, nb_chances))
        mot_trouve = affichage(mot_a_trouver, lettres_trouvees)

 
    if mot_a_trouver==mot_trouve:
        print("Félicitations ! Vous avez trouvé le mot mystère: {0}.".format(mot_a_trouver))
    else:
        print("PENDU !!! Vous avez perdu.")

    scores[utilisateur] += nb_chances

    continuer_partie = input("Souhaitez-vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()


enregistrer_scores(scores)


print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))




