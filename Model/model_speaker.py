from .connection import Connection
from Model.Entities.entity import HydrateSpeaker

class Speaker():

    def __init__(self):
        self.db = Connection()


    def create_speaker(self,speaker):
        sql="INSERT INTO speaker(prenom,nom,description,profession) VALUES (%s,%s,%s,%s);"
        argument = (speaker.prenom,speaker.nom,speaker.description,speaker.profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()
        return True

    def display_all(self):
        sql = "SELECT * FROM speaker WHERE statut = TRUE;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        speaker_conf = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(speaker_conf):
            speaker_conf[key] = HydrateSpeaker(value)
        return speaker_conf

    def single_speaker(self,prenom,nom):
        sql = "SELECT * FROM speaker WHERE prenom = %s AND nom = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(prenom,nom))
        speaker = self.db.cursor.fetchone()
        self.db.close_connection()
        if speaker:
            return HydrateSpeaker(speaker)
        return False



    def update(self,speaker):
        sql="UPDATE speaker SET  description = %s, profession = %s, statut = %s WHERE id = %s; "
        argument= (speaker.description, speaker.profession,speaker.statut,speaker.id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()


    def delete(self,id):
        sql="DELETE FROM speaker WHERE id = %s ;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(id,))
        self.db.connection.commit()
        self.db.close_connection()
