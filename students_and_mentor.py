class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if grade<0 or grade>10:
            result = print(f'Error:  Студент выставил отценку {grade} Ревьюеру/ Значение отценки должно быть от 0 до 10')
            return result
        if course not in lector.courses_attached:
            result = print(f'Error:  Лектор "{lector.name} {lector.surname}" НЕ преподает курс - "{course}"')
            return result
        if course not in self.courses_in_progress:
            result = print(f'Error: Студент "{self.name} {self.surname}" не учится на курсе - "{course}"')
            return result
        if not isinstance(lector, Lecturer):
            result = print('Error:   Оцениваются только - Лекторы!!!')
            return result
        if course in lector.grades:
            lector.grades[course] += [grade]
        else:
            lector.grades[course] = [grade]

    def average_value(self):
        # /* Расчет среднего значения =
            # так как у нас может быть что студент проходит несколько курсов и на каждом курсе преподаватель ставит отценки
            # то нужно посчитать Общей средний бал по всем отценкам каждого курса
        if not self.grades.keys():
            return 0
        all_summ = 0
        all_count = 0
        for k in self.grades.keys():
            all_summ = all_summ + sum(self.grades[k])
            all_count = all_count + len(self.grades[k])
        result = round(all_summ / all_count, 1)
        return result
    # */ Расчет среднего значения

    def __str__(self):
        all_courses_in_progress=', '.join(self.courses_in_progress)
        all_courses_finished=', '.join(self.finished_courses)
        result = (f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_value()}\n'
            f'Курсы в процессе изучения: {all_courses_in_progress}\n'
            f'Завершенные курсы: {all_courses_finished}\n')
        return result

    def __eq__(self, other):
        result = self.average_value() == other.average_value()
        return result
    def __gt__(self, other):
        result = self.average_value()>other.average_value()
        return result
    def __lt__(self, other):
        result = self.average_value()<other.average_value()
        return result
    def __le__(self, other):
        result = self.average_value() <= other.average_value()
        return result
    def __ge__(self, other):
        result = self.average_value() >= other.average_value()
        return result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_value(self):
        # /* Расчет среднего значения
        if not self.grades.keys():
            return 0
        all_summ = 0
        all_count = 0
        for k in self.grades.keys():
            all_summ = all_summ + sum(self.grades[k])
            all_count = all_count + len(self.grades[k])
        result = round(all_summ / all_count, 1)
        return result

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                 f'Фамилия: {self.surname}\n'
                 f'Средняя оценка за лекции: {self.average_value()}')
        return  result

    def __eq__(self, other):
        result = self.average_value() == other.average_value()
        return result
    def __gt__(self, other):
        result = self.average_value() > other.average_value()
        return result
    def __lt__(self, other):
        result = self.average_value() < other.average_value()
        return result
    def __le__(self, other):
        result = self.average_value() <= other.average_value()
        return result
    def __ge__(self, other):
        result = self.average_value() >= other.average_value()
        return result

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if not isinstance(student, Student):
            result = print(f'Error:   Оцениваются только - Студенты!!!')
            return result
        if grade<0 or grade>10:
            result = print(f'Error:   Ревьюер выставил {grade} Студенту  / Значение отценки должно быть от 0 до 10')
            return result
        if course not in student.courses_in_progress:
            result = print(f'Error:   Студент "{student.name} {student.surname}" НЕ учится на курсе - "{course}"')
            return result
        if course not in self.courses_attached:
            result = print(f'Error:   Ревьюер "{self.name} {self.surname}" не переподает курс - "{course}"')
            return result
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')
        return  result

def Mega_Average_value(people,course):
    all_sum = 0
    all_count = 0
    if type(people[0]) != type(people[1]):
        result = ('Error:   Сравнить можно только одинаковые личности (Лектор/Лектор или Студент/Студент) !!!')
        return result
    for element in people:
        if course in element.grades.keys():
            all_sum = all_sum + sum(element.grades[course])
            all_count = all_count  + len(element.grades[course])

    if all_sum==0:
        return 0
    else:
        result = round(all_sum / all_count,1)
        return result





#__Определяем СТУДЕНТОВ__________________________________________________________________________________
Student1=Student('Alex','Won','Male')
Student1.courses_in_progress.append('Python')
Student1.courses_in_progress.append('Git')
Student1.finished_courses.append('Введение в програмирование')
Student1.finished_courses.append('Git - ясельки')
Student2=Student('Kate','Honey','Female')
Student2.courses_in_progress.append('Python')
Student2.courses_in_progress.append('Java')
Student2.finished_courses.append('Введение в програмирование')
Student2.finished_courses.append('Общие понятия синтаксиса')
#==Определяем ЛЕКТОРОВ============================================================================
Lector1=Lecturer('Martin','Hook')
Lector1.courses_attached.append('Python')
Lector1.courses_attached.append('Git')
Lector2=Lecturer('Zak','Chan')
Lector2.courses_attached.append('Java')
Lector2.courses_attached.append('Python')
#==Определяем РЕВЬЮЕРОВ============================================================================
Reviewer1=Reviewer('Bob','Good')
Reviewer1.courses_attached.append('Python')
Reviewer1.courses_attached.append('Git')
Reviewer2=Reviewer('Ron','Hool')
Reviewer2.courses_attached.append('Java')
#==============================================================================

#_/*Выставляем отценки Лекторам________________
Student1.rate_lector(Lector1,'Python',2)
Student1.rate_lector(Lector1,'Git',9)
Student1.rate_lector(Lector2,'Python',9)
Student2.rate_lector(Lector2,'Java',3)
Student2.rate_lector(Lector2,'Java',4)
#_*/________________
#_/*Выставляем отценки Студентам________________
Reviewer1.rate_student(Student1,'Python',-1)
Reviewer1.rate_student(Student1,'Python',10)
Reviewer1.rate_student(Student2,'Python',7)
Reviewer1.rate_student(Student2,'Python',8)
Reviewer2.rate_student(Student2,'Java',3)
Reviewer2.rate_student(Student2,'Java',4)
#_*/________________

print(f'\n ______________STR_____________________ ')
print('Reviewer1 ->')
print(Reviewer1)
print('Reviewer2 ->')
print(Reviewer2)
print('Lector1 ->')
print(Lector1)
print('')
print('Lector2 ->')
print(Lector2)
print('')
print('Student1 ->')
print(Student1)
print('Student2 ->')
print(Student2)
print(f'\n ______________Сравнение Лекторов по средней отценке_____________________ ')
print(f"Lector1 ({Lector1.average_value()}) > Lector2 ({Lector2.average_value()}) = {Lector1 > Lector2}")
print(f"Lector1 ({Lector1.average_value()}) < Lector2 ({Lector2.average_value()}) = {Lector1 < Lector2}")
print(f"Lector1 ({Lector1.average_value()}) == Lector2 ({Lector2.average_value()}) = {Lector1 == Lector2}")

print(f'\n ______________Сравнение Студентов по средней отценке_____________________ ')
print(f"Student1 ({Student1.average_value()}) > Student2 ({Student2.average_value()}) = {Student1 > Student2}")
print(f"Student1 ({Student1.average_value()}) < Student2 ({Student2.average_value()}) = {Student1 < Student2}")
print(f"Student1 ({Student1.average_value()}) == Student2 ({Student2.average_value()}) = {Student1 == Student2}")


print(f'\nПодсчет средней оценки за домашние задания по всем СТУДЕНТам в рамках конкретного курса:')
print(Mega_Average_value([Student1,Student2],'Python'))

print(f'\nПодсчет средней оценки за лекции всех ЛЕКТОРов в рамках конкретного курса:')
print(Mega_Average_value([Lector1,Lector2],'Python'))
