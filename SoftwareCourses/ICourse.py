# -*- coding: utf-8 -*-
from abc import abstractmethod, abstractproperty, ABCMeta
from ITeacher import Teacher

# Interface to describe 
class ICourse(metaclass=ABCMeta):
    @abstractproperty
    def name(self): raise NotImplementedError
    
    @name.setter
    def name(self): raise NotImplementedError
    
    @abstractproperty
    def teachers(self): raise NotImplementedError
    
    @teachers.setter
    def teachers(self): raise NotImplementedError
    
    @abstractmethod
    def add_Teacher(self, teacher): raise NotImplementedError
    
    @abstractmethod
    def del_Teacher(self, teacher): raise NotImplementedError

    @abstractproperty
    def topics(self): raise NotImplementedError
    
    @topics.setter
    def topics(self): raise NotImplementedError
    
    @abstractmethod
    def add_Topic(self, topic): raise NotImplementedError
    
    @abstractmethod
    def del_Topic(self, topic): raise NotImplementedError

class Course(ICourse):
    # May to created full empty
    def __init__(self, name=None, teachers=None, topics=None,
                 *args, **kwargs):
        if name:
            if not isinstance(name, str):
                raise ValueError(VALUE_ERR.format(name, 'name', 'str'))
            else:
                self.__name = name
        else:
            self.__name = str() 
        
        if teachers:
            if not isinstance(teachers, list):
                raise ValueError(VALUE_ERR.format(teachers, 'teachers', 'list'))
            else:
                self.__teachers = list()
                for teacher in teachers:
                    self.add_Teacher(teacher)
        else:
            self.__teachers = list()
        
        if topics:
            if not isinstance(topics, list):
                raise ValueError(VALUE_ERR.format(topics, 'topics', 'list'))
            else:
                self.__topics = list()
                for topic in topics:
                    self.add_Topic(topic)
        else:
            self.__topics = list()
    
    # Add to teachers list
    def add_Teacher(self, teacher, *args, **kwargs):
        if not isinstance(teacher, Teacher):
            raise ValueError(VALUE_ERR.format(teacher, 'teachers', 'Teacher'))
        else:
            if teacher not in self.teachers:
                self.__teachers.append(teacher)
                teacher.add_Course(self)
    
    # Remove from teachers list
    def del_Teacher(self, teacher, *args, **kwargs):
        if teacher in self.teachers:
            self.__teachers.remove(teacher)
            teacher.del_Course(self)
    
    # Add to topic list
    def add_Topic(self, topic, *args, **kwargs):
        if not isinstance(topic, str):
            raise ValueError(topic, 'topics', 'str')
        else:
            if topic not in self.__topics:
                self.__topics.append(topic)
    
    # Remove from topics list
    def del_Topic(self, topic, *args, **kwargs):
        if topic in self.topics:
            self.__topics.remove(topic)
    
    # Export current status to dictiatary form
    def to_dict(self, *args, **kwargs):
        out = {}
        out['name'] = self.name
        out['topics'] = self.topics
        out['type'] = self.__class__.__name__
        if out['type'] == 'LocalCourse':
            out['lab'] = self.lab
            
        elif out['type'] == 'OffsiteCourse':
            out['town'] = self.town
        out['teachers'] = {}
        for teacher in self.teachers:
            if teacher.name not in out['teachers']:
                temp = {}
                temp['name'] = teacher.name
                temp['courses'] = list(map(lambda x: x.name, teacher.courses))
                
                out['teachers'][teacher.name] = temp
        
        return out
    
    # Humanyty representation
    def __repr__(self, *args, **kwargs):
        out = ''
        out += self.__class__.__name__ + ': '
        out += 'Name=[{}]; '.format(self.name)
        if self.teachers:
            teachers = list(map(lambda x: x.name, self.teachers))
        else:
            teachers = list()

        out += 'Teachers={}; '.format(teachers)
        out += 'Topics={}; '.format(self.topics)
        if self.__class__.__name__ == "LocalCourse":
            out += 'Lab=[{}]\n'.format(self.lab)
           
        elif self.__class__.__name__ == "OffsiteCourse":
            out += 'Town=[{}]\n'.format(self.town)
        
        return out
    
    # Getter and Setter to name attribute
    @property
    def name(self, *args, **kwargs):
        return self.__name
    
    @name.setter
    def name(self, value, *args, **kwargs):
        if not isinstance(value, str):
            raise ValueError(VALUE_ERR.format(value, 'name', 'str'))
        else:
            self.__name = value
    
    # Getter and Setter to teachers attribute
    @property
    def teachers(self, *args, **kwargs):
        return self.__teachers

    
    @teachers.setter
    def teachers(self, value, *args, **kwargs):
        if not isinstance(value, list):
            raise ValueError(VALUE_ERR.format(value, 'teachers', 'list'))
        else:
            for teacher in value:
                self.add_Teacher(teacher)
    
    # Getter and Setter to topics attribute
    @property
    def topics(self, *args, **kwargs):
        return self.__topics
    
    @topics.setter
    def topics(self, value, *args, **kwargs):
        if not isinstance(value, list):
            raise ValueError(VALUE_ERR.format(value, 'topics', 'list'))
        else:
            for topic in value:
                self.add_Topic(topic)
