class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if grade<0 or grade>10: print(f'ОШИБКА: Оценка = {grade} / Значение отценки должно быть от 0 до 10'); return ("Переходим к концу")
        if course not in lector.courses_attached: print(f'ОШИБКА: Лектор "{lector.name} {lector.surname}" НЕ преподает курс - "{course}"'); return ("Переходим к концу")
        if course not in self.courses_in_progress: print(f'ОШИБКА: Студент "{self.name} {self.surname}" не учится на курсе - "{course}"'); return ("Переходим к концу")
        if not isinstance(lector, Lecturer): print('ОШИБКА: Оцениваются только - Лекторы!!!'); return ("Переходим к концу")
        if course in lector.grades:
            lector.grades[course] += [grade]
        else:
            lector.grades[course] = [grade]

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if not isinstance(student, Student): print('ОШИБКА: Оцениваются только - Студенты!!!'); return ("Переходим к концу")
        if grade<0 or grade>10: print(f'ОШИБКА: Оценка = {grade} / Значение отценки должно быть от 0 до 10'); return ("Переходим к концу")
        if course not in student.courses_in_progress: print(f'ОШИБКА: Студент "{student.name} {student.surname}" НЕ учится на курсе - "{course}"'); return ("Переходим к концу")
        if course not in self.courses_attached: print(f'ОШИБКА: Ревьюер "{self.name} {self.surname}" не переподает курс - "{course}"'); return ("Переходим к концу")
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
#__Определяем СТУДЕНТОВ__________________________________________________________________________________

Student1=Student('Alex','Won','Male')
Student1.courses_in_progress.append('Python')
Student1.courses_in_progress.append('Git')
Student1.finished_courses.append('Введение в програмирование')
Student1.finished_courses.append('Git - ясельки')

Student2=Student('Kate','Honey','Female')
Student2.courses_in_progress.append('Python')
Student2.courses_in_progress.append('Java')
#Student2.courses_in_progress.append('Алгебра')
Student2.finished_courses.append('Введение в програмирование')
Student2.finished_courses.append('Общие понятия синтаксиса')

Student3=Student('1','2','3')
Student3.courses_in_progress.append('Java')
Student3.courses_in_progress.append('Git')
Student3.finished_courses.append('Введение в програмирование')
Student3.finished_courses.append('Общие понятия синтаксиса')

#==Определяем ЛЕКТОРОВ============================================================================
Lector1=Lecturer('Martin','Hook')
Lector1.courses_attached.append('Python')
Lector1.courses_attached.append('Git')

Lector2=Lecturer('Zak','Chan')
Lector2.courses_attached.append('Java')
#==Определяем РЕВЬЮЕРОВ============================================================================
Reviewer1=Reviewer('Bob','Good')
Reviewer1.courses_attached.append('Python')
Reviewer1.courses_attached.append('Git')

Reviewer2=Reviewer('Ron','Hool')
Reviewer2.courses_attached.append('Java')
#==============================================================================

print('#/*Ревьюер выставляет отценку  - Студенту / Проверка')

Reviewer1.rate_student(Student1,'Python',-1)          #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',0)     #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',1)     #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',5)     #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',10)    #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',11)    #Проверка - Значение отценки от 0 до 10
Reviewer1.rate_student(Student1,'Python',1)     #Студент учится на курсе Ревьер преподает курс
Reviewer1.rate_student(Student1,'Java',2)     #Студент НЕ учится на курсе Ревьер преподает курс
Reviewer2.rate_student(Student1,'Python',3)     #Студент учится на курсе Ревьер преподает курс
Reviewer2.rate_student(Lector1,'Python',4)     #Ревьюер пытается установить отценку Лектору!!!

print(Student1.grades)
print('*/')

print('#/*Студент выставляет отценку  - Летору / Проверка')
Student1.rate_lector(Lector1,'Python',-1)   #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',0)    #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',1)    #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',5)    #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',10)   #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',11)   #Проверка - Значение отценки от 0 до 10
Student1.rate_lector(Lector1,'Python',1)    #Студент учится на курсе а Лектор преподает курс
Student1.rate_lector(Lector2,'Python',2)    #Студент учится на курсе а Лектор НЕ преподает курс
Student1.rate_lector(Lector2,'Java',3)      #Студент НЕ учится на курсе а Лектор преподает курс
Student1.rate_lector(Reviewer1,'Git',4)    #Студент выставляет отценку Ревьеру!!!

#Reviewer1.rate_student(Student2,'Python',5)
#Reviewer2.rate_student(Student2,'Java',10)

Reviewer1.rate_student(Student1,'Python',11)
#Reviewer1.rate_student(Student1,'Python',7)
#Reviewer1.rate_student(Student1,'Git',10)
#Reviewer1.rate_student(Student1,'Git',9)

#Reviewer2.rate_student(Student3,'Java',0)
#Reviewer2.rate_student(Student3,'Python',0)
print('*/')
print(Lector1.grades)
