class HydrateConference():

    def __init__(self,data=False):
        self.id = None
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.date_de_creation = None
        self.speaker_id = None
        if data:
            self.hydrate_conference(data)

    def hydrate_conference(self,data):
        """function to set a value to each attribut based on a dictionnary"""
        for key, value in data.items():
            # Prevent he creation of unwanted attributs
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return """~~~~~~~~~~~~~~~~~~~~~~~~
{} : {} : {} : {} : {} """.format(self.titre, self.resume, self.date_heure,self.date_de_creation,self.speaker_id)
