from Model.model_speaker import *
from Model.Entities.entity import HydrateSpeaker

class SpeakerView():
    model = Speaker()


    def add_speaker(self):
        print("Veuillez renseignez les champs suivants")
        data = {}
        data["prenom"]= input(" prenom:")
        data["nom"] = input(" nom:")
        data["description"] = input("description:")
        data["profession"] = input("profession:")
        speaker = HydrateSpeaker(data)
        if SpeakerView.model.create_speaker(speaker):
            print("le speaker a ete enregistré")

    def show_speaker(self):
        speaker = self.model.display_all()

        if speaker:
            for x in speaker:
                print(x)
        else:
            print("Veuillez reessayer:-)")


    def update_speaker(self,column,prenom,nom,description,profession,statut,nouvelles):
        model = Speaker()
        column = input("Quel speaker voulez vous apporter des changemant(prenon,nom,description,profession) : ")
        prenom = input(" prenon  :")
        nom = input(" nom :")
        nouvelles = input("nouveau changement")
        event.update(column,prenom,nom,nouvelles)

    def delete_speaker(self,id):
        model = Speaker()
        print("Vous voulez supprimer un speaker")
        id = int(input("tapez son id"))
        model.delete(id)
        print ("vous voulez supprimer l'id {}".format(id))
