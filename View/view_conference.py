from Model.model_conference import *
from Model.Entities.entity_conference import HydrateConference

class ConferenceView():
    model = Conference()


    def add_conference(self):
        print("Veuillez renseignez les champs suivants")
        data = {}
        data["titre"] = input(" titre:")
        data["resume"] = input(" resume:")
        data["date_heure"] = input("date_heure:")
        data["speaker_id"] = int(input("speaker_id"))
        conference = HydrateConference(data)
        if ConferenceView.model.create_conference(conference):
            print("la conference a ete enregistré")


    def show_conference(self):
        conference = self.model.display_conferences()
        if conference:
            for x in conference:
                print(x)
        else:
            print("Veuillez reessayer:-)")

    def delete_conference(self):
        model = Conference()
        print("la suppression des conferences supprime le speaker qui lui sont associees")
        id = int(input("tapez son id"))
        print ("vous voulez supprimer l'id {}".format(id))
        self.model.delete(id)


    def update_conference(self,id):
        """Allow user to change attribut's value for specific event
            Autoriser l'utilisateur à modifier la valeur de l'attribut pour un événement spécifique"""
        # Retrieve an event if it exists
        # Récupérer un événement s'il existe
        choice = ""
        while choice != "s":
            id = int(input("taper l (id) de la conference a modifiee : "))
            event = self.model.single_conference(id)
            if event :
                break
            print("Nous ne trouvons rien sur cette conference")
            choice = input("Tapez s pour arrêter, n'importe quelle touche pour continuer")
        # If we have found an event
        # Si nous avons trouvé un événement
        if event:
            print("Voici les informations enregistrées")
            # User can change attributs as long as he wants
            # L'utilisateur peut modifier les attributs aussi longtemps qu'il le souhaite
            while True:
                print(event)
                print("Tapez s pour arrêter")
                champs = input("taper champs à modifier : ")
                if champs  == 's' :
                    break
                value = input("Nouvelle valeur : ")
                # If he chooses to change the hour then we check the hour is free
                # S'il choisit de changer l'heure, nous vérifions que l'heure est gratuite
                if champs == "id":
                    while self.model.single_conference(event.id, value):
                        print("le nouveau champs est pris !")
                        value = input('Nouvelle valeur : ')
                # Set the new value and update the database
                # Définissez la nouvelle valeur et mettez à jour la base de données
                setattr(event, champs, value)
            self.model.update_event(event)
