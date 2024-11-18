class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course):
        self.courses_in_progress.append(course)

    "Позволяет студенту выставлять оценки лектору"
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        "Возвращает строку с именем, фамилией, средней оценкой за ДЗ, текущими и завершенными курсами"
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade():.1f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    "Используются методы __lt__ и __eq__ для сравнения студентов по средней оценке за ДЗ"
    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        return self.average_grade() == other.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    "Подсчёт среднего балла на основе полученных оценок от студентов"
    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        "Возвращает строку с именем, фамилией и средней оценкой за лекции"
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade():.1f}'

    "Используются методы __lt__ и __eq__ для сравнения лекторов по средней оценке за лекции"
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    "Выставление оценки студенту за выполнение ДЗ"
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        "Возвращает строку с именем и фамилией"
        return f'Имя: {self.name}\nФамилия: {self.surname}'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)