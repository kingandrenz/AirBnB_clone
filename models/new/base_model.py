#!/usr/bin/python3

"""
This model is the model for class BaseModel

"""
import uuid
from datetime import datetime

class BaseModel:

    def __init__(self):

        """
        this class model defines all common attributes/methods for other classes

        """

        self.id = str(uuid.uuid4())

        self.created_at = datetime.now()

        self.updated_at = datetime.now()

    def __init__(self):

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        updated_at = datetime.now()

    def to_dict(self):

        dict_rep = self.__dict__.copy()

        dict_rep["__class__"] = self.__class__.__name__

        dict_rep["created_at"] = self.created_at.isoformat()

        dict_rep["updates_at"] = self.updated_at.isoformat()

        return dict_rep
