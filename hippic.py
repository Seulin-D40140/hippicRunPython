#!/usr/bin/env python
# -*- coding: utf-8 -*
import random
from itertools import islice
from pylint.checkers.utils import returns_bool


def hippic(response , horses):

    answer = response.lower()
    cheveaux = (n for n in range(1, horses+1))
    race = list(islice(cheveaux, 20))
    random.shuffle(race)
    horsesRace = print(f"courses avec {horses} de chevaux : {race}")
    # quinter = list(islice(cheveaux , 20))
    # tierce = list(islice(quinter, 18))
    # quarter = list(islice(quinter, 16))

    if answer == "quinte".lower():
        # random.shuffle(quinter) return quinter[:6]
        horsesRace
        return race[:6]
    elif answer == "tierce".lower():
        # random.shuffle(tierce) return tierce[:3]
        horsesRace
        return race[:3]
    elif answer == "quarte".lower():
        # random.shuffle(quarter) return quarter[:4]
        horsesRace
        return race[:4]
    else:
        return "pas de course a ce nom reessayez"

#..............................................................................................

def runRace ():

    continu = True
    nbHorses = 1

    while continu:
        question = (input("a quoi voulez vous jouer ? tierce , quinte , quarte ? : "))

        while nbHorses == 1:
            try:
                horses = int((input("combien de chevaux ? entre 12 et 20 : ")))
                if horses < 12 and horses > 20:
                    nbHorses = 1
                elif horses > 11 and horses < 21:
                    nbHorses = 0
            except ValueError:
                print("-> uniquement des nombres compri entre 12 et 20 !!")

        print(f"gagnant du {question} : {hippic(question, horses)}")

        nb = (input("voulez vous continuer ? y = yes , All-Other = no : "))
        if nb.lower() == "Y".lower():
            continu = True
            nbHorses = 1
        else:
            continu = False
            print("a bientot")

#..............................................................................................

if __name__ == '__main__':

    runRace()