# -*- coding: utf-8 -*-
from abc import abstractmethod, abstractproperty, ABCMeta

# Abctract interface to description of concrete Teacher implementation
class ITeacher(metaclass=ABCMeta):    
    @abstractproperty
    def name(self): raise NotImplementedError
    
    @name.setter
    def name(self): raise NotImplementedError
    
    @abstractproperty
    def courses(self): raise NotImplementedError
    
    @courses.setter
    def courses(self): raise NotImplementedError
    
    @abstractmethod
    def add_Course(self, course): raise NotImplementedError
    
    @abstractmethod
    def del_Course(self, course): raise NotImplementedError

class Teacher(ITeacher):
    # May to created full empty
    def __init__(self, name=None, courses=None, *args, **kwargs):
        if name:
            if not isinstance(name, str):
                raise ValueError(VALUE_ERR.format(name, "name", 'str'))
            else:
                self.__name = name
        else:
            self.__name = str()
        
        if courses:
            if not isinstance(courses, list):
                raise ValueError(VALUE_ERR.format(courses, "courses", 'list'))
            else:
                self.__courses = list()
                for course in courses:
                    self.add_Course(course)
        else:
            self.__courses = list()
    
    # Add course to courses list
    def add_Course(self, course, *args, **kwargs):
        if not isinstance(course, Course):
            raise ValueError(course, 'courses', 'Course')
        else:
            if course not in self.courses:
                self.__courses.append(course)
                course.add_Teacher(self)
    
    # Remove course from course list
    def del_Course(self, course, *args, **kwargs):
        if course in self.courses:
            self.__courses.remove(course)
            course.del_Teacher(self)
    
    # Export interall repr to dictionary fomat
    def to_dict(self, *args, **kwargs):
        out = {}
        out['name'] = self.name
        out['courses'] = {}
        for course in self.courses:
            if course.name not in out['courses']:
                temp = {}
                temp['name'] = course.name
                temp['topics'] = course.topics
                temp['teacher'] = self.name
                temp['type'] = course.__class__.__name__
                if temp['type'] == 'LocalCourse':
                    temp['lab'] = course.lab
                
                elif temp['type'] == 'OffsiteCourse':
                    temp['town'] = course.town
                
                out['courses'][course.name] = temp
        
        return out
    
    # Humane view representation
    def __repr__(self, *args, **kwargs):
        out = ''
        out += 'Teacher: Name=({}); '.format(self.name)
        out += 'Courses =[ '
        for course in self.courses:           
            out += course.name + ','
        out = out[:-1]
        out += ']\n'
        
        return out
    
    # Getter and Setter to name attribute
    @property
    def name(self, *args, **kwargs):
        return self.__name
    
    @name.setter
    def name(self, value, *args, **kwargs):
        if not isinstance(value, str):
            raise ValueError(VALUE_ERR.format(value, "name", 'str'))
        else:
            self.__name = value
    
    # Getter and Setter to courses attribute
    @property
    def courses(self, *args, **kwargs):
        return self.__courses
    
    @courses.setter
    def courses(self, value, *args, **kwargs):
        if not isinstance(value, list):
            raise ValueError(VALUE_ERR.format(value, 'courses', 'list'))
        else:
            for course in value:
                self.add_Course(course)
