class Hydrate:

    def __init__(self,data=False):
        self.id = None
        self.prenom = None
        self.nom = None
        self.description = None
        self.profession = None
        self.statut = None
        if data:
            data.Hydrate()

    def hydrate(self):
        """function to set a value to each attribut based on a dictionnary"""
        for key, value in data.items():
            # Prevent he creation of unwanted attributs
            if hasattr(self, key):
                setattr(self, key, value)
