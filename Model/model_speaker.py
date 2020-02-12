from .connection import Connection
from Model.Entities.entity import *

class Speaker(Hydrate):

    def __init__(self):
        self.db = Connection()
        Hydrate.__init__(self)

    def create_speaker(self,prenom,nom,description,profession):
        sql="INSERT INTO speaker(prenom,nom,description,profession) VALUES (%s,%s,%s,%s);"
        argument = (prenom,nom,description,profession)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()

    def display_all(self):
        sql = "SELECT * FROM speaker WHERE statut = TRUE;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        speaker = self.db.cursor.fetchall()
        self.db.close_connection()
        print(speaker)


    def display(self,prenom,nom):
        sql = "SELECT * FROM speaker LEFT JOIN conference ON speaker.id = conference.speaker_id;"
        argument = (prenom, nom)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        speaker_conf = self.db.cursor.fetchall()
        self.db.close_connection()
        if speaker_conf:
            return Hydrate(speaker_conf)
        return False

    def update(self,column,prenom,nom,description,profession,statut,nouvelles):
        sql="UPDATE speaker SET "+ column +" =%s WHERE id=%s and nom = %s; "
        argument= (nouvelles,id,nom)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()


    def delete(self,id,speaker_id):
        sql="DELETE FROM speaker LEFT JOIN conference ON speaker.id = conference.speaker_id ;"
        argument = (id, speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql,argument)
        self.db.connection.commit()
        self.db.close_connection()
