# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
from ICourse import ICourse, Course

# Interface to description concrete LocalCourse implementation
class ILocalCourse(ICourse, metaclass=ABCMeta):
    @abstractproperty
    def lab(self): raise NotImplementedError
    
    @lab.setter
    def lab(self): raise NotImplementedError

class LocalCourse(Course, ILocalCourse):
    # May to created full empty
    def __init__(self, name=None, teachers=None, 
                 topics=None, lab=None, *args, **kwargs):
        if lab:
            if not isinstance(lab, str):
                raise ValueError(VALUE_ERR.format(lab, 'lab', 'str'))
            else:
                self.__lab = lab
        else:
            self.__lab = str()
        
        super().__init__(name, teachers, topics)
    
    # Getter and Setter block to lab attribute
    @property
    def lab(self, *args, **kwargs):
        return self.__lab
    
    @lab.setter
    def lab(self, lab, *args, **kwargs):
        if not isinstance(lab, str):
            raise ValueError(VALUE_ERR.format(lab, 'lab', str))
        else:
            self.__lab = lab
