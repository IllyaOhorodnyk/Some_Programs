# -*- coding: utf-8 -*-
from abc import abstractmethod, abstractproperty, ABCMeta
from ITeacher import Teacher
from ICourse import ICourse
from ILocalCourse import LocalCourse
from IOffsiteCourse import OffsiteCourse
from ICourseFactory import CourseFactory

constants = open('constants.txt')
exec(constants.read())
constants.close()
del constants

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
