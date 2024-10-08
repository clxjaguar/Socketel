#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minitel.Minitel import Minitel
from Reseau import Reseau
from parametres import (lire_vitesse, lire_reseau)

from pages.accueil import accueil
from pages.menu_principal import menu_principal

# on définit l'objet utilisé pour les opérations avec le minitel
minitel = Minitel()

# on établit la liaison en cherchant la vitesse de communication
if minitel.deviner_vitesse() < 0:
    minitel.recuperation()

# on récupère les paramètres, et on définit la vitesse souhaitée
parametres_vitesse = lire_vitesse()
if parametres_vitesse['auto']:
    minitel.definir_vitesse(parametres_vitesse['vitesse'])

# on initialise le minitel
minitel.definir_mode('VIDEOTEX')
minitel.efface('vraimenttout')
minitel.curseur(False)

# on récupère les paramètres réseau et on affiche le message
# de connexion automatique le cas échéant
parametres_reseau = lire_reseau()
if parametres_reseau['auto']:
    accueil(minitel, attendre=False)
    minitel.position(1,0)
    minitel.envoyer('Connexion automatique... ')
else:
    accueil(minitel)

# on définit l'objet utilisé pour les opérations de réseau
reseau = Reseau(parametres_reseau)
if parametres_reseau['auto']:
    item = 16 if reseau.isconnected() else 9
else:
    item = 0

# on affiche le menu principal
while True:
    minitel.position(1,0)
    minitel.couleur(caractere='vert')
    minitel.envoyer('Menu                              ')
    item = menu_principal(minitel, reseau, select = item)
