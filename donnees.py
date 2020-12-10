# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:24:43 2020
cette page contient l'ensemble des données utiles au jeu 
@author: Timothée Teyssier
"""

mon_fichier=open("mot.txt","r")
liste_mot_desorganise=mon_fichier.read()
mon_fichier.close()
liste=liste_mot_desorganise.split(" ")
liste.sort(key=lambda l : len(l))
tentatives= 8
nom_fichier_scores = "scores"

