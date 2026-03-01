from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):

    def __init__(self, _username='aacuser', _password='abc123'):

        HOST = 'localhost'#connection variables
        PORT = 27017
        DB = 'aac'

        userName = urllib.parse.quote_plus(_username)
        password = urllib.parse.quote_plus(_password)

        self.client = MongoClient(#auth string
            f'mongodb://{userName}:{password}@{HOST}:{PORT}/{DB}?authSource=aac'
        )

        self.dataBase = self.client[DB]

    def create(self, data):#method to create an animal for the collection
        if data is not None:
            insertValid = self.dataBase.animals.insert_one(data) #inserts the entry
            return True if insertValid.acknowledged else False
	
        else:
            raise Exception("Empty")#exception for an empty parameter
    
    def read(self, postId):#method to read the animal data
        _data = self.dataBase.animals.find_one({'_id': ObjectId(postId)})#finds the entry
                                  
        return _data
    
    def criteria(self, criteria = None):#criteria for finding stuff
        if criteria is not None:
            _data = self.dataBase.animals.find(criteria, {'_id' : 0})
                                 
        else:
            _data = self.dataBase.animals.find({}, {'_id' : 0})
                                  
        return _data
    
    def update(self, data, updateKey, updateValue):#method to update an existing animal entry
        if data is not None:
            result = self.dataBase.animals.update_many(data, {'$set': {updateKey:updateValue}})#with the key and value, it updates the entry
            return result.raw_result
        else:
            raise Exception("Parameter Empty")#exception for an empty parameter
    
    
    def delete(self, data):#method to delete an entry
        if data is not None:
            result = self.dataBase.animals.delete_many(data)#deletes the entry
            return result.raw_result
        else:
            raise Exception("Parameter empty")#exception for an empty parameter