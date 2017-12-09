# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
from ICourse import ICourse, Course

# Interface to description concrete OffsiteCourse implementation
class IOffsiteCourse(ICourse, metaclass=ABCMeta):
    @abstractproperty
    def town(self): raise NotImplementedError
    
    @town.setter
    def town(self): raise NotImplementedError

class OffsiteCourse(Course, IOffsiteCourse):
    # May to created full empty
    def __init__(self, name=None, teachers=None, topics=None,
                 town=None, *args, **kwargs):
       
        if town:
            if not isinstance(town, str):
                raise ValueError(VALUE_ERR.format(town, 'town', 'str'))
            else:
                self.__town = town
        else:
            self.__town = str()
        
        super().__init__(name, teachers, topics)
    
    # Getter and Setter to town atribute
    @property
    def town(self, *args, **kwargs):
        return self.__town
    
    @town.setter
    def town(self, town, *args, **kwargs):
        if not isinstance(town, str):
            raise ValueError(VALUE_ERR.format(town, 'town', 'str'))
        else:
            self.__town = town
