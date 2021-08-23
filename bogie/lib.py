#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def try_me():
    possibilite = ['pierre', 'feuille', 'ciseaux']
    Users = input("Quel est votre nom ?")
    print(f'Bonjour {Users}, bienvenue dans pierre / feuille / ciseaux \n \
          Vous allez vous confronter au maitre du jeu'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )
    input("")
    print('Etes vous prêt ?')
    input("")
    bot, User, manche = 0, 0, 0
    while User != 3 or bot !=3:
        print(f'Manche N°{manche} \n quel est votre choix ? \n \
            1 = pierre \n    2 = feuille \n 3 = ciseaux'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )
        forma = False
        while forma == False:
            answer = input()
            if answer in ['1','2','3']:
                forma = True
        game = np.random.randint(1,3)
        if game == 1:
            if answer == 1:
                print('égalité')
            elif answer == 3:
                bot += 1
                print('YOU ARE A LOSER !!!!')
            else :
                User += 1
                print('vous avez gagné mais à mon avis vous devez avoir triché')
        elif game == 2:
            if answer == 2:
                print('égalité')
            elif answer == 1:
                bot += 1
                print('YOU ARE A LOSER !!!!')
            else:
                User += 1
                print('vous avez gagné mais à mon avis vous devez avoir triché')
        elif game == 3:
            if answer == 3:
                print('égalité')
            elif answer == 2:
                bot += 1
                print('YOU ARE A LOSER !!!!')
            else:
                User += 1
                print('vous avez gagné mais à mon avis vous devez avoir triché')
    if bot == 3:
        print('YOU ARE SUCH A HUGE LOOOOooooOOOOSER !!!!')
    else:
        print('You should not win, that is a fake news!!')
