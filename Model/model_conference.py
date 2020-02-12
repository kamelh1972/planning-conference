class ConferenceModel:
    """class to perform all queries in table conference"""
    def __init__(self):
        self.values = ()
        self.sql = ""
        self.db = Connection()

    def display_conferences(self):
        """select all conference from conference and add last name and first name from speaker """
        self.sql = "SELECT c.*, s.last_name, s.first_name FROM conference AS c LEFT JOIN speaker AS s ON c.speaker_id =s.speaker_id; "
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql)
        conference = self.db.cursor.fetchall()
        self.db.close_connection()
        """for key, values in enumerate(conference):
            conference[key] = Conference(values)"""
        print(conference)

    def add_conference(self, titre, resume, date_heure, speaker_id):
        """add new entry in table conference"""
        self.sql = "INSERT INTO conference(titre, resume, date_heure, creation_date, speaker_id) VALUES(%s, %s, %s, %s, now(),%s);"
        self.values = (titre, resume, date_heure, speaker_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()

    def update_conference(self, titre, resume, date_heure, conference_id):
        """update data in table conference"""
        self.sql = "UPDATE conference SET title = %s, summary = %s, date = %s, hour = %s WHERE conference_id =%s;"
        self.values = (title, summary, date, hour, conference_id)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, self.values)
        self.db.connection.commit()
        self.db.close_connection()

    def delete_conference(self, conference_id):
        """delete data in table conference"""
        self.sql = "DELETE FROM conference WHERE conference_id = %s;"
        self.values = (conference_id,)
        self.db.initialize_connection()
        self.db.cursor.execute(self.sql, (self.values,))
        self.db.connection.commit()
        self.db.close_connection()
