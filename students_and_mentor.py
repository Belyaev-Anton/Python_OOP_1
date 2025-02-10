class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if grade<0 or grade>10: print(f'    ОШИБКА: Оценка = {grade} / Значение отценки должно быть от 0 до 10'); return ("Переходим к концу")
        if course not in lector.courses_attached: print(f'    ОШИБКА: Лектор "{lector.name} {lector.surname}" НЕ преподает курс - "{course}"'); return ("Переходим к концу")
        if course not in self.courses_in_progress: print(f'    ОШИБКА: Студент "{self.name} {self.surname}" не учится на курсе - "{course}"'); return ("Переходим к концу")
        if not isinstance(lector, Lecturer): print('    ОШИБКА: Оцениваются только - Лекторы!!!'); return ("Переходим к концу")
        if course in lector.grades:
            lector.grades[course] += [grade]
        else:
            lector.grades[course] = [grade]

    def Average_value(self):
        # /* Расчет среднего значения =
            # так как у нас может быть что студент проходит несколько курсов и на каждом курсе преподаватель ставит отценки
            # то нужно посчитать Общей средний бал по всем отценкам каждого курса
        if not self.grades.keys(): return 0
        all_summ = 0
        all_count = 0

        for k in self.grades.keys():
            all_summ = all_summ + sum(self.grades[k])
            all_count = all_count + len(self.grades[k])

        average_value = round(all_summ / all_count, 1)
        return average_value

    # */ Расчет среднего значения
    def __str__(self):
        #if not self.grades:
            #return (f'ОШИБКА: У Студента "{self.name}" нет отценок по курсу "{self.courses_in_progress}"\n'
                    #f'---------------------------------------------')
        #else:
            #/* Список курсов в строке
        all_courses_in_progress=', '.join(self.courses_in_progress)
        all_courses_finished=', '.join(self.finished_courses)
            #*/ Список курсов в строке

        return (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.Average_value()}\n'
            f'Курсы в процессе изучения: {all_courses_in_progress}\n'
            f'Завершенные курсы: {all_courses_finished}\n'
            f'---------------------------------------------')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def Average_value(self):
        # /* Расчет среднего значения
        if not self.grades.keys():  return 0
        all_summ = 0
        all_count = 0
        for k in self.grades.keys():
            all_summ = all_summ + sum(self.grades[k])
            all_count = all_count + len(self.grades[k])
        average_value = round(all_summ / all_count, 1)
        return average_value

    def __str__(self):
        return  (f'Имя: {self.name}\n'
                 f'Фамилия: {self.surname}\n'
                 f'Средняя оценка за лекции: {self.Average_value()}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if not isinstance(student, Student): print('    ОШИБКА: Оцениваются только - Студенты!!!'); return ("Переходим к концу")
        if grade<0 or grade>10: print(f'    ОШИБКА: Оценка = {grade} / Значение отценки должно быть от 0 до 10'); return ("Переходим к концу")
        if course not in student.courses_in_progress: print(f'    ОШИБКА: Студент "{student.name} {student.surname}" НЕ учится на курсе - "{course}"'); return ("Переходим к концу")
        if course not in self.courses_attached: print(f'    ОШИБКА: Ревьюер "{self.name} {self.surname}" не переподает курс - "{course}"'); return ("Переходим к концу")
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return  (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')
#__Определяем СТУДЕНТОВ__________________________________________________________________________________

Student1=Student('Alex','Won','Male')
Student1.courses_in_progress.append('Python')
Student1.courses_in_progress.append('Git')
Student1.finished_courses.append('Введение в програмирование')
Student1.finished_courses.append('Git - ясельки')

Student2=Student('Kate','Honey','Female')
Student2.courses_in_progress.append('Python')
Student2.courses_in_progress.append('Java')
Student2.courses_in_progress.append('Алгебра')
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

Reviewer1.rate_student(Student1,'Python',11)
print(Lector1.grades)
print('*/')


Student1.rate_lector(Lector1,'Python',2)    #Студент учится на курсе а Лектор НЕ преподает курс
Student1.rate_lector(Lector1,'Git',9)      #Студент НЕ учится на курсе а Лектор преподает курс
Student2.rate_lector(Lector2,'Java',2)    #Студент учится на курсе а Лектор НЕ преподает курс
Student2.rate_lector(Lector2,'Java',7)    #Студент учится на курсе а Лектор НЕ преподает курс

#_/*Чистим словарь с отценками________________
Student1.grades.clear()
Student2.grades.clear()
Student3.grades.clear()
Lector1.grades.clear()
Lector2.grades.clear()
#_*/

#_/*Выставляем отценки Лекторам________________
Student1.rate_lector(Lector1,'Python',2)
Student1.rate_lector(Lector1,'Git',9)
Student2.rate_lector(Lector2,'Java',3)
Student2.rate_lector(Lector2,'Java',4)
#_*/________________
#_/*Выставляем отценки Студентам________________
Reviewer1.rate_student(Student1,'Python',5)
Reviewer1.rate_student(Student1,'Python',10)
Reviewer2.rate_student(Student2,'Java',3)
Reviewer2.rate_student(Student2,'Java',4)
#_*/________________

print(f'\n ______________STR_____________________ \n')
print('Reviewer1 ->')
print(Reviewer1)
print('Reviewer2 ->')
print(Reviewer2)
print('')
print('Lector1 ->')
print(Lector1)
print('')
print('Lector2 ->')
print(Lector2)
print('')
print('Student1 ->')
print(Student1)
print('')
print('Student2 ->')
print(Student2)
print(f'\n ______________Сравнение Лекторов по средней отценке_____________________ ')
print(f"Lector1 ({Lector1.Average_value()}) > Lector2 "
      f"({Lector2.Average_value()}) = ", Lector1.Average_value() > Lector2.Average_value())
print(f"Lector1 ({Lector1.Average_value()}) < Lector2 "
      f"({Lector2.Average_value()})= ", Lector1.Average_value() < Lector2.Average_value())

print(f'\n ______________Сравнение Студентов по средней отценке_____________________ ')
print(f"Student1 ({Student1.Average_value()}) > Student2 "
      f"({Student2.Average_value()}) = ", Student1.Average_value() > Student2.Average_value())
print(f"Student1 ({Student1.Average_value()}) < Student2 "
      f"({Student2.Average_value()}) = ", Student1.Average_value() < Student2.Average_value())

