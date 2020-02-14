from .connection import Connection
from Model.Entities.entity_conference import HydrateConference

class Conference():
    """class to perform all queries in table conference"""
    def __init__(self):

        self.db = Connection()

    def display_conferences(self):
        """select all conference from conference and add last name and first name from speaker """
        sql = "SELECT c.*, s.prenom,s.nom FROM conference AS c JOIN speaker AS s ON s.id = c.speaker_id;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql)
        conference = self.db.cursor.fetchall()
        self.db.close_connection()
        for key, value in enumerate(conference):
            conference[key] = HydrateConference(value)
        return conference

    def create_conference(self, event):
        """add new entry in table conference"""
        sql = "INSERT INTO conference(titre, resume, date_heure,date_de_creation,speaker_id) VALUES(%s, %s, %s, now(),%s);"
        argument= (event.titre, event.resume, event.date_heure, event.speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, argument)
        self.db.connection.commit()
        self.db.close_connection()
        return True

    def update_conference(self, titre, resume, date_heure, conference_id,speaker_id):
        """update data in table conference"""
        self.sql = "UPDATE conference SET titre = %s, resume = %s, date_heure = %s speaker_id = %s WHERE conference_id =%s;"
        self.values = (titre, resume, date_heure, conference_id, speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()

    def delete(self,id):
        """delete data in table conference"""
        sql = "DELETE FROM conference WHERE id = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(id,))
        self.db.connection.commit()
        self.db.close_connection()
