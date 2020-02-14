import os
import time
import calendar
import locale
from datetime import datetime
from Model.Entities.entity import HydrateSpeaker
from Model.Entities.entity_conference import HydrateConference
from View.view_speaker import *
from View.view_conference import *


if __name__ == '__main__':
    speaker = HydrateSpeaker()
    speaker_conf = HydrateConference()
    print("Bienvenue sur votre gestionnaire de conference personnel")
    time.sleep(1)
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    currentYear = datetime.now().year
    currentMonth = datetime.now().month
    action = ""
    while action != 'q':
        model = SpeakerView()
        model_conference = ConferenceView()
        print("Nous sommes le : {}".format(datetime.today().strftime('%d %B %Y')))
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print (calendar.month(currentYear, currentMonth, 2, 1))
        print("Que souhaitez vous gérer ? (c: conference, s: speaker, q: quitter)")
        action = input(": ")
        if action == "s":
            print("vous voulez gerer les speaker")
            user_choice = input("que voulez-vous faire:\n a : voir speaker\n b : supprimer speaker \n c : ajouter speaker \n q : quit \n")
            if user_choice == "a":
                print("voici la liste des speaker actifs")
                model.show_speaker()

            if user_choice == "b":
                model.delete_speaker(id)

            if user_choice == "c":
                model.add_speaker()

            if user_choice == "q":
                print("Au revoir à bientot")

        if action == "c":
            print("vous voulez gerer les conference")
            user_choice = input("que voulez-vous faire:\n a : voir conference\n b : supprimer conference \n d : ajouter conference \n m : modifier conference \n q : quit \n")

            if user_choice == "d":
                model_conference.add_conference()

            if user_choice == "a":
                print("Voici le listing des conférences")
                model_conference.show_conference()

            if user_choice == "b":
                model_conference.delete_conference()

            if user_choice == "m":
                model_conference.update_conference(id)

            if user_choice == "q":
                print("Au revoir")
