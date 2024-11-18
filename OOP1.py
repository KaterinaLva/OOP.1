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

def average_hw_grade(students, course):
    """Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса."""
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


def average_lectures_grade(lectors, course):
    """Подсчет средней оценки за лекции всех лекторов в рамках курса."""
    total_grades = []
    for lector in lectors:
        if course in lector.grades:
            total_grades.extend(lector.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0
 
# Создаем студентов
student1 = Student('Степан', 'Леднёв', 'Мужской')
student1.add_courses('Python')
student1.add_courses('ООП')

student2 = Student('Анна', 'Петрова', 'Женский')
student2.add_courses('C++')
student2.finished_courses.append('Введение в программирование')

# Создаем лекторов и закрепляем их за курсом
lecturer1 = Lecturer('Нестор', 'Северов')
lecturer1.courses_attached.append('Python')

lecturer2 = Lecturer('Ираида', 'Васильева')
lecturer2.courses_attached.append('С++')

# Создаем экспертов
reviewer1 = Reviewer('Иван', 'Сидорова')
reviewer1.courses_attached.append('Python')

reviewer2 = Reviewer('Ольга', 'Иванова')
reviewer2.courses_attached.append('С++')

# Выставление оценок студентам
lecturer1.rate_student(student1, 'Python', 9)
lecturer1.rate_student(student1, 'Python', 8)
lecturer1.rate_student(student1, 'Python', 7)

lecturer2.rate_student(student2, 'С++', 6)
lecturer2.rate_student(student2, 'С++', 7)
lecturer2.rate_student(student2, 'С++', 8)

# Проверка домашних заданий студентов
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)

reviewer2.rate_hw(student2, 'С++', 9)
reviewer2.rate_hw(student2, 'С++', 8)
reviewer2.rate_hw(student2, 'С++', 7)

# Выставление оценок лекторам
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 7)

student2.rate_lecturer(lecturer2, 'С++', 6)
student2.rate_lecturer(lecturer2, 'С++', 7)
student2.rate_lecturer(lecturer2, 'С++', 8)

# Вывод информации об объектах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравнение студентов и лекторов
print("Сравниваем студентов:")
print(student1 > student2)
print()

print("\nСравниваем лекторов:")
print(lecturer1 > lecturer2)
print()

# Подсчет средней оценки за домашние задания по всем студентам в рамках курса
students_list = [student1, student2]
course = 'Python'
avg_hw_grade = average_hw_grade(students_list, course)
print(f"\nСредняя оценка за домашние задания по курсу '{course}': {avg_hw_grade:.1f}")
print()

# Подсчет средней оценки за лекции всех лекторов в рамках курса
lectors_list = [lecturer1, lecturer2]
course_lecturers = 'С++'
avg_lectures_grade = average_lectures_grade(lectors_list, course_lecturers)
print(f"Средняя оценка за лекции по курсу '{course_lecturers}': {avg_lectures_grade:.1f}")
print()