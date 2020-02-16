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

    def single_conference(self,id):
        sql = "SELECT * FROM conference WHERE id = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(id,))
        conference = self.db.cursor.fetchone()
        self.db.close_connection()
        if conference:
            return HydrateConference(conference)
        return False


    def create_conference(self, event):
        """add new entry in table conference"""
        sql = "INSERT INTO conference(titre, resume, date_heure,date_de_creation,speaker_id) VALUES(%s, %s, %s, now(),%s);"
        argument= (event.titre, event.resume, event.date_heure, event.speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, argument)
        self.db.connection.commit()
        self.db.close_connection()
        return True

    def update_event(self, conference):
        """Update and event object in the database
            Mise à jour d'une conference dans la base de données"""
        sql = """UPDATE conference
                 SET titre=%s, resume=%s, date_heure=%s, speaker_id=%s
                 WHERE id=%s"""
        arguments = (conference.titre, conference.resume, conference.date_heure, conference.speaker_id,conference.id)
        self.db.initialize_connection()
        self.db.cursor.execute(sql, arguments)
        self.db.connection.commit()
        self.db.close_connection()

    def delete(self,id):
        """delete data in table conference"""
        sql = "DELETE FROM conference WHERE id = %s;"
        self.db.initialize_connection()
        self.db.cursor.execute(sql,(id,))
        self.db.connection.commit()
        self.db.close_connection()
