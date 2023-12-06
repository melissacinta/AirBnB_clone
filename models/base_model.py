#!/usr/bin/python3
'''base model module'''
import uuid
import datetime


class BaseModel:
  '''A class that defines all common attributes/methods for other classes'''
  def __init__(self):
    '''initialize instance attributes'''
    self.id = str(uuid.uuid4())
    self.created_at = datetime.datetime.now()
    self.updated_at = datetime.datetime.now()

  def __str__(self):
    '''Function that return the string representation of the module'''
    return "[{}] ({}) {}".format(self.__class__.__name__,self.id, \
                                 str(self.__dict__))

  def save(self):
    '''Function that updates the public instance
    attribute updated_at with the current datetime
    '''
    self.updated_at = datetime.datetime.now()

  def to_dict(self):
    '''Function that
     returns a dictionary containing all keys/values of __dict__ of the instance:
    '''
    objs = {}
    for key in self.__dict__.keys():
      if key in ('created_at', 'updated_at'):
        objs[key] = datetime.datetime.isoformat(self.__dict__[key])
      else:
        objs[key] = self.__dict__[key]
    objs['__class__'] = self.__class__.__name__
    return (objs)
