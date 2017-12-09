# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
from ILocalCourse import LocalCourse
from IOffsiteCourse import OffsiteCourse
from ITeacher import Teacher

# Interface to description concrete CourseFactory implementation
class ICourseFactory(metaclass=ABCMeta):
    @abstractmethod
    def get_Teacher(self, name=None): raise NotImplementedError
    
    @abstractmethod
    def get_LocalCourse(self, name=None, 
                        teacher=None, lab=None): raise NotImplementedError
    
    @abstractmethod
    def get_OffsiteCourse(self, name=None,
                          teacher=None, town=None): raise NotImplementedError

class CourseFactory(ICourseFactory):
    # Return Teacher instance
    def get_Teacher(self, name=None, *args, **kwargs):
        
        return Teacher(name)
    
    # Return LocalCourse instace
    def get_LocalCourse(self, name=None, teachers=None, 
                        topics=None, lab=None, *args, **kwargs):
        
        return LocalCourse(name, teachers, topics, lab)
    
    # Return OffsiteCourse instance
    def get_OffsiteCourse(self, name=None, teachers=None,
                          topics=None, town=None, *args, **kwargs):
        
        return OffsiteCourse(name, teachers, topics, town)
    
    # Convertation from dictionary to Teacher instance
    def dict2Techer(self, dictionary, *args, **kwargs):
        if not isinstance(dictionary, dict):
            raise ValueError(VALUE_ERR.format(dictionary, 'dict', 'dict'))
        else:   
            teacher = self.get_Teacher()
            if dictionary['name']:
                teacher.name = dictionary['name']
                
            if dictionary['courses']:
                for key in dictionary['courses']:
                    course_info = dictionary['courses'][key]
                    if course_info['type'] == 'LocalCourse':
                        course = self.get_LocalCourse()
                        
                        if course_info['lab']:
                            course.lab  = course_info['lab']
                        
                    elif course_info['type'] == 'OffsiteCourse':
                        course = self.get_OffsiteCourse()
                        
                        if course_info['town']:
                            course.town = course_info['town']
                    
                    if course_info['name']:
                        course.name = course_info['name']
                    
                    if course_info['topics']:
                        course.topics = course_info['topics']
                        
                    course.add_Teacher(teacher)
            
            return teacher
    
    # Convertation from dictionary to Course instance
    def dict2Course(self, dictionary, *args, **kwargs):
        if not isinstance(dictionary, dict):
            raise ValueError(VALUE_ERR.format(dictionary, 'dict', 'dict'))
        else:
            if dictionary['type'] == 'LocalCourse':
                course = self.get_LocalCourse()
                if dictionary['lab']:
                    course.lab = dictionary['lab']
            
            elif dictionary['type'] == 'OffsiteCourse':
                course = self.get_OffsiteCourse()
                if dictionary['town']:
                    course.town = dictionary['town']
            
            if dictionary['topics']:
                course.topics = dictionary['topics']
            
            if dictionary['name']:
                course.name = dictionary['name']
            
            if dictionary['teachers']:
                for key in dictionary['teachers']:
                    teacher_info = dictionary['teachers'][key]
                    teacher = self.get_Teacher()
                    
                    if teacher_info['name']:
                        teacher.name = teacher_info['name']
                    
                    teacher.add_Course(course)
            
            return course
