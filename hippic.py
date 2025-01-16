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


if __name__ == '__main__':

    continu = True
    question = (input("a quoi voulez vous jouer ? tierce , quinte , quarte ? : "))
    horses = int((input("combien de chevaux ? : ")))
    testNumber = isinstance(horses, (int))
    while continu:

        while (horses < 12 or horses > 20) or testNumber == False:
            try:
                horses = int(input("Seulement des nombres compris entre 12 et 20 : "))
            except ValueError:
                horses = int(input("Veuillez entrer un nombre entier valide : "))

        print(f"gagnant du {question} : {hippic(question, horses)}")

        try:
            nb = (input("voulez vous continuer ? y = yes , All-Other = no : "))
            if nb.lower() == "Y".lower():
                continu = True
                question = (input("a quoi voulez vous rejouer ? tierce , quinte , quarte ? : "))
                horses = int((input("combien de chevaux ? entre 12 et 20 : ")))
            else:
                continu = False
                print("a bientot")

            #print(f"le resultat total est : {fact_nb} , {nb} etant le nombre de depart")
        except ValueError:
            print("ceci n'est pas correcte ressayer ! ")