from Model.model_speaker import *
from Model.Entities.entity import Hydrate

class SpeakerView():

    def add_speaker(self,prenom,nom,description,profession):
        model = Speaker()
        self.prenom = None
        self.nom = None
        self.description = None
        self.profession = None
        model.create_speaker(prenom,nom,description,profession)

    def show_speaker(self):
        print("voici les conferenciers")
        model = Speaker()
        model.display_all()
