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


    def update_statut(self):
        """Allow user to change attribut's value for specific event
            Autoriser l'utilisateur à modifier la valeur de l'attribut pour un événement spécifique"""
        # Retrieve an speaker if it exists
        # Récupérer un speaker s'il existe
        #id = int(input("taper l (id) du speaker a modifier : "))
        prenom = input("prenom :")
        nom = input("nom")
        choice = ""
        while choice != "s":

            speaker = self.model.single_speaker(prenom,nom)
            if speaker :
                break
            print("Nous ne trouvons rien sur ce speaker")
            choice = input("Tapez s pour arrêter, n'importe quelle touche pour continuer")
        # If we have found an event
        # Si nous avons trouvé un événement
        if speaker:
            print("Voici les informations enregistrées")
            # User can change attributs as long as he wants
            # L'utilisateur peut modifier les attributs aussi longtemps qu'il le souhaite
            while True:
                print(speaker)
                print("Tapez s pour arrêter")
                champs = input("taper champs à modifier :  ")
                if champs  == 's' :
                    break
                value = input("Nouvelle valeur du champs à modifier : ")
                if champs == "statut" or champs == "description" or champs == "profession":
                    while self.model.single_speaker(speaker.nom, value):
                        print("le nouveau champs est pris !")
                        value = input('Nouvelle valeur : ')

                # Set the new value and update the database
                # Définissez la nouvelle valeur et mettez à jour la base de données
                setattr(speaker, champs, value)
            if self.model.update(speaker):
                print("les informations ont été enregistrées")

            else:
                raise ValueError("un probleme est survenu")


    def delete_speaker(self,id):
        model = Speaker()
        print("Vous voulez supprimer un speaker")
        id = int(input("tapez son id"))
        model.delete(id)
        print ("vous voulez supprimer l'id {}".format(id))
