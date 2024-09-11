#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self): 
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["__created_at__"] = self.created_at.isoformat()
        inst_dict["__updated_at__"] = self.updated_at.isoformat()

        return inst_dict
    def __str__(self):
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My Firt Model" 
    my_model.my_number = 90  
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json) 
    print('JSON format of my_model:')
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
