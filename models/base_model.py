#!/usr/bin/python3
"""
base model for the entire project
"""

import uuid
import datetime
import models


class BaseModel:
    """A class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize instance attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                # we don't want to add the __class__ key
                if key == "__class__":
                    continue
                else:
                    # We are formating time here
                    if key in ('created_at', 'updated_at'):
                        kwargs[key] = datetime.datetime.strptime(
                                kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                        # setting the rest of the attributes
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Function that return the string representation of the module"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     str(self.__dict__))

    def save(self):
        """Function that updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Function that
            returns a dictionary containing all keys/values
            of __dict__ of the instance:
        """
        objs = {}
        for key in self.__dict__.keys():
            if key in ('created_at', 'updated_at'):
                objs[key] = datetime.datetime.isoformat(self.__dict__[key])
            else:
                objs[key] = self.__dict__[key]
        objs['__class__'] = self.__class__.__name__
        return (objs)
