class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_hw(self):
        self.amount_grades = []
        for grades in self.grades.values():
            for grade in grades:
                self.amount_grades.append(grade)
        self.average = round(sum(self.amount_grades) / len(self.amount_grades), 2)        
        return self.average

    def __str__ (self):
            return(f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self.average_grade_hw()}
Курсы в процессе изучения: {",".join(self.courses_in_progress)} 
Завершенные курсы: {",".join(self.finished_courses)}''')

    def __lt__(self, other):
        if not isinstance (other, Student):
            print('Такого студента нет.')
        return self.average_grade_hw() < other.average_grade_hw()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []        
     
class Lecturer(Mentor):
    def __init__(self, name, surname):  
        super().__init__(name, surname)
        self.grades = {}
        
    def average_grade(self):
        self.amount_grades = []
        for grades in self.grades.values():
            for grade in grades:
                self.amount_grades.append(grade)
        self.average = round(sum(self.amount_grades) / len(self.amount_grades), 2)        
        return self.average
   
    def __lt__(self, other):
        if not isinstance (other, Lecturer):
            print('Такого преподавателя нет.')
        return self.average_grade() < other.average_grade()

    def __str__ (self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_grade()} ''')

class Reviewer(Mentor):
    def __init__(self, name, surname):  
        super().__init__(name, surname)

    def __str__ (self):
        return(f'''Имя: {self.name}
Фамилия: {self.surname}''')
        

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
def average_all_grade(students_list,course):
    all_grades = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades += student.grades.get(course)
    average = round(sum(all_grades) / len(all_grades),2)
    print(f'Средняя оценка всех студентов за домашние задания по курсу {course}: {average}')

def average_all_grade_lecturer(lecturer_list, course):
    all_grades = []
    for lecturer in lecturer_list:
        if lecturer.grades.get(course) is not None:
            all_grades += lecturer.grades.get(course)
    average = round(sum(all_grades) / len(all_grades),2)
    print(f'Средняя оценка всех лекторов за лекции курса {course}: {average}')

#Полевые испытания
#Создаём по 2 экземпляра каждого класса
student_first = Student('Petr', 'Petrov', 'men')
student_first.courses_in_progress += ['Python']
student_first.courses_in_progress += ['Git']
student_first.finished_courses += ['Введение в программирование']

student_second = Student('Elena', 'Pavlova', 'woman')
student_second.courses_in_progress += ['Python']
student_second.courses_in_progress += ['Git']
 
reviewer_first = Reviewer('Oleg', 'Bykin')
reviewer_first.courses_attached += ['Python']
reviewer_first.courses_attached += ['Git']

reviewer_second = Reviewer('Alla', 'Pushkina')
reviewer_second.courses_attached += ['Python']
reviewer_second.courses_attached += ['Git']

lecturer_first = Lecturer ('Robert','Ivanov')
lecturer_first.courses_attached += ['Python']
lecturer_first.courses_attached += ['Git']

lecturer_second = Lecturer ('Maria','Belkina')
lecturer_second.courses_attached += ['Python']
lecturer_second.courses_attached += ['Git']

#Проверяем методы
student_first.rate_lecturer(lecturer_first, 'Python', 10)
student_first.rate_lecturer(lecturer_first, 'Git', 8)
student_first.rate_lecturer(lecturer_first, 'Python', 7)

student_first.rate_lecturer(lecturer_second, 'Python', 8)
student_first.rate_lecturer(lecturer_second, 'Git', 10)
student_first.rate_lecturer(lecturer_second, 'Python', 9)

student_second.rate_lecturer(lecturer_first, 'Python', 9)
student_second.rate_lecturer(lecturer_first, 'Git', 9)
student_second.rate_lecturer(lecturer_first, 'Python', 9)

student_second.rate_lecturer(lecturer_second, 'Python', 9)
student_second.rate_lecturer(lecturer_second, 'Git', 8)
student_second.rate_lecturer(lecturer_second, 'Python', 9)

reviewer_first.rate_hw(student_first, 'Python', 10)
reviewer_first.rate_hw(student_second, 'Python', 8)
reviewer_first.rate_hw(student_first, 'Git', 9)
reviewer_first.rate_hw(student_second, 'Git', 9)

reviewer_second.rate_hw(student_first, 'Python', 9)
reviewer_second.rate_hw(student_second, 'Python', 9)
reviewer_second.rate_hw(student_first, 'Git', 10)
reviewer_second.rate_hw(student_second, 'Git', 9)

print(student_first)
print('---------')
print(student_second)
print('---------')
print(reviewer_first)
print('---------')
print(reviewer_second)
print('---------')
print(lecturer_first)
print('---------')
print(lecturer_second)
print('---------')
print(student_first < student_second)
print('---------')
print(lecturer_first > lecturer_second)

#Проверяем функции подсчёта средних оценок по всем студентам и лекторам
average_all_grade([student_first,student_second], 'Python')
average_all_grade([student_first,student_second], 'Git')
average_all_grade_lecturer([lecturer_first,lecturer_second],'Python')
average_all_grade_lecturer([lecturer_first,lecturer_second],'Git')
