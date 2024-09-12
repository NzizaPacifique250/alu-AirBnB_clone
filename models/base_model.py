#!/usr/bin/python3
import uuid
import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel with unique ID and creation time.
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, timeformat))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)
    def __str__(self):
        """String representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self): 
        """Returns a dictionary containing all keys/values of the instance."""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
