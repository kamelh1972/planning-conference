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
