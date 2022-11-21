from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas2').query_db(query)
        dojos = []

        for d in results:
            dojos.append( cls(d) )
        return dojos

    @classmethod
    def save(cls, data):
        query= "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas2').query_db(query,data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT first_name, last_name, age FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas2').query_db(query,data)
        print(results)
        dojo = []
        for row in results:
            dojo.append( row )
        return dojo