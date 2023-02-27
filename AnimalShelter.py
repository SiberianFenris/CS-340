from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    # CRUD operation for Animal collection in MongoDB

    def __init__(self, username = "aacuser", password = "aacuser"):
        # Initializing the MongoClient.
        # This helps to access MongodDB db & collections
        self.client = MongoClient('mongodb://%s:%s@localhost:55579/AAC' % (username, password))
        self.database = self.client['AAC']

        #Create step of our CRUD operation
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data is the dict
            return True
        else:
            raise Exception("Nothing to save, because parameter is empty!")
            return False

        #Read step of our CRUD operation
    def read(self, data):
        if data is not None:
            animal_data = self.database.animals.find(data)
            return animal_data
        else:
            raise Exception("No data located. Try again!")
            return False
        
        #Update step of our CRUD operation
    def update(self, document, update):
        if update is not None:
            update_animal = self.database.animals.update(document, update)
            return update_animal
        else:
            raise Exception("Nothing to update, because parameter is empty!")
            return False
        
        #Delete step of our CRUD operation
    def delete(self, data):
        if data is not None:
            delete_animal = self.database.animals.delete(data)
            return delete_animal
        else:
            raise Exception("Nothing to delete, because parameter is empty!")
            return False