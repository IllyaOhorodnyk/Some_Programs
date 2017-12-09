# -*- coding: utf-8 -*-
from abc import abstractmethod, abstractproperty, ABCMeta
import json

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
        out += 'Name={};'
        out += 'Teachers=[ '
        for teacher in self.teachers:
            out += teacher.name + ','
        out = out[:-1]
        out += ']; '
        out += 'Topics=[ '
        for topic in self.topics:
            out += topic + ','
        out = out[:-1]
        out += ']; '
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
            self.__lab = lab
        
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
            self.__town = town
        
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
            
# Template to create ValueError message
VALUE_ERR = "Not supported type {} to attribute {}, this need to {} type"

# Maintain menu
MAIN_MENU = "\
What you want to do?\n\
1 - Create new Teacher\n\
2 - Show all Teachers\n\
3 - Upgrade data on Teacher\n\
4 - Create new Course\n\
5 - Show all Courses\n\
6 - Upgrade date on Course\n\
7 - Read from the File\n\
8 - Write to the File\n\
9 - Close Progam"

# Teacher upgrading menu
TEACHER_MENU = "\
What you want to do?\n\
1 - Reset new name\n\
2 - Add a Course from list\n\
3 - Delete a Course from exist\n\
4 - Delete all Teacher instance\n\
5 - Leave this menu"

# Course upgrading menu
COURSE_MENU = "\
What you want to do?\n\
1 - Reset new name\n\
2 - Add a new topic\n\
3 - Delete a exist topic\n\
4 - Add a Teacher from list\n\
5 - Delete a Teacher from exits\n\
6 - Reset Lab/Town\n\
7 - Delete all Course instance\n\
8 - Leave this menu"

# Meun to select type of creating course
TYPE_MENU = "\
Which type of Course you want\n\
1 - LocalCourse\n\
2 - OffsiteCourse\n\
3 - Leave this menu\n"

# Text wrapper, representation text in mose readeble see
def box_wrapper(string):
    if not isinstance(string, str):
        return None
    else:
        out = ''
        lines = string.split('\n')
        width = max(map(lambda x: len(x), lines))
        out += '-' * width + '\n'
        for line in lines:
            out += '|' + line + ' ' * (width-len(line)) + '|' + '\n'
        out += '-' * width + '\n'
        
        return out

# Func for selecting from some iterable collection
def selector(iterable):
    out = ''
    for i in range(len(iterable)):
        out += str(i+1) + ' - ' + str(iterable[i])
    print(box_wrapper(out))
    
    while True:
        try:
            index = int(input("Select the number of item\n>>>"))
            item = iterable[index-1]
        except ValueError as e:
            print(e)
            continue
        except IndexError as e:
            print(e)
            continue
        else:
            
            return item

MAIN_MENU = box_wrapper(MAIN_MENU)
TEACHER_MENU = box_wrapper(TEACHER_MENU)
COURSE_MENU = box_wrapper(COURSE_MENU)
TYPE_MENU = box_wrapper(TYPE_MENU)

def main():
    teachers = list()
    courses = list()
    factory = CourseFactory()
    while True:
        choice = input(MAIN_MENU+">>>")
        if choice == '1': # Create new Teacher
            teachers.append(factory.get_Teacher())
            print("New empty teacher is created!")
        elif choice == '2': # Show all Teachers
            if  not teachers:
                print("No one teacher is create!")
            else:
                for teacher in teachers:
                    print(teacher)
        elif choice == '3': # Upgrade Teacher
            if not teachers:
                print("No one teacher is create!")
            else:
                teacher = selector(teachers)
                while True:
                    print(teacher)
                    sub_choice = input(TEACHER_MENU+"\n>>>")
                    if sub_choice == '1': # Reset name
                        name = input('Type the new name\n>>>')
                        teacher.name = name
                    elif sub_choice == '2': # Add course
                        if not courses:
                            print('No one course is created')
                        else:
                            course = selector(courses)
                            teacher.add_Course(course)
                    elif sub_choice == '3': # Remove course
                        if not teacher.courses:
                            print("Teacher has no one course")
                        else:
                            course = selector(teacher.courses)
                            teacher.del_Course(course)
                    elif sub_choice == '4': # Delete Teacher
                        teachers.remove(teacher)
                        break
                    elif sub_choice == '5': # Leave this menu
                        break
                    else:
                        print("Not exist variant")
        elif choice == '4': # Create new Course
            while True:
                sub_choice = input(TYPE_MENU+'\n>>>')
                if sub_choice == '1':
                    courses.append(factory.get_LocalCourse())
                    break
                elif sub_choice == '2':
                    courses.append(factory.get_OffsiteCourse())
                    break
                elif sub_choice == '3':
                    break
                else:
                    print("Not exist variant")
        elif choice == '5': # Show all Courses
            if not courses:
                print("No one course in created!")
            else:
                for course in courses:
                    print(course)
        elif choice == '6': # Upgrade Course
            if not courses:
                print('No one course is created!')
                continue
            else:
                course = selector(courses)
                while True:
                    print(course)
                    sub_choice = input(COURSE_MENU+'\n>>>')
                    if sub_choice == '1': # Reset name
                        name = input('Type the name of course\n>>>')
                        course.name = name
                    elif sub_choice == '2': # Add topic
                        topic = input('Type the name of topic\n>>>')
                        course.add_Topic(topic)
                    elif sub_choice == '3': # Remove topic
                        if not course.topics:
                            print("Course have no one topic")
                            continue
                        else:
                            topic = selector(course.topics)
                            course.del_Topic(topic)
                    elif sub_choice == '4': # Add Teacher
                        if not teachers:
                            print("No one teacher is created")
                            continue
                        else:
                            teacher = selector(teachers)
                            course.add_Teacher(teacher)
                    elif sub_choice == '5': # Remove Teacher
                        if not course.teachers:
                            print("Course have no one teacher")
                            continue
                        else:
                            teacher = selector(course.teachers)
                            course.del_Teacher(teacher)
                    elif sub_choice == '6': # Reset lab\town
                        if isinstance(course, LocalCourse):
                            lab = input('Type the Lab\n>>>')
                            course.lab = lab
                        elif isinstance(course, OffsiteCourse):
                            town = input("type the Town\n>>>")
                            course.town = town
                    elif sub_choice == '7': # Delete course
                        courses.remove(course)
                        break
                    elif sub_choice == '8': # Leave this menu
                        break
                    else:
                        print("Not exits variant")
        elif choice == '7': # Read to File
            file_name = input('Type the name of File\n>>>')
            try:
                file = open(file_name+'.json')
            except:
                print("File is not exist")
            else:
                teachers, courses = list(), list()
                teachers_info, courses_info = json.load(file)
                for teacher_info in teachers_info:
                    teachers.append(factory.dict2Techer(teacher_info))
                
                for course_info in courses_info:
                    courses.append(factory.dict2Course(course_info))
                file.close()
        elif choice == '8': # Write from File
            file_name = input("Type the name of File\n>>>")
            try:
                file = open(file_name+".json", 'x')
            except FileExistsError:
                file = open(file_name+".json", 'w')
            finally:
                out = (list(map(lambda x: x.to_dict(), teachers)), 
                       list(map(lambda x: x.to_dict(), courses)))
                json.dump(out, file, indent=4)
                file.close()
        elif choice == '9': # Close Program
            break
        else:
            print("Not exist variant")

if __name__ == "__main__":
    main()









