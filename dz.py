class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in self.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка' 
    def mid_rate(self):
        self.courses = []
        self.rate = []
        for k,v in self.grades.items():
            self.courses.append(k)
            self.rate.append(v)
        return sum(self.rate)/len(self.courses)      
    
    def __str__(self):
        text = f'Имя:{self.name}\nФамилия:{self.surname}\nCредняя оценка за домашние задания:{self.mid_rate()}'
        text_2 = f'Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return f'{text}\n{text_2}' 
    
    def __lt__(self,other):
        if not isinstance(other,Student):
            return
        return self.mid_rate() < other.mid_rate()   

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
class Lecturer:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses = []
        self.rate = []
        self.grades = {}
        self.courses_attached = []
    
    def mid_rate(self):
        for k,v in self.grades.items():
            self.courses.append(k)
            self.rate.append(v)
        return sum(self.rate)/len(self.courses)
    def __str__(self):
        text = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.mid_rate()}'
        return text
    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            return
        return self.mid_rate() < other.mid_rate()   
       
class Rewiver(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'
    def __str__(self):
        text = f'Имя:{self.name}\nФамилия:{self.surname}'
        return text

rewiver_1 = Rewiver('Ольга','Петрова')
rewiver_1.courses_attached = ['Git','Python','Метрика']
rewiver_2 = Rewiver('Диана','Семенова')
rewiver_2.courses_attached = ['Git','Метрика','Devops']
lecturer_1 = Lecturer('Денис','Иванов')
lecturer_1.courses_attached  = ['Git','Python','Java']
lecturer_2 = Lecturer('Евгений','Петров')
lecturer_2.courses_attached  = ['C++','Python','Git']
student_1 = Student('Иван','Семенов','Мужской')
student_1.finished_courses = ['Java','C++','Маркетинг']
student_1.courses_in_progress = ['Метрика','Общество','Git']
student_2 = Student('Петр','Скворцов','Мужской')
student_2.finished_courses = ['С++','Java','Финансы']
student_2.courses_in_progress = ['Devops','Метрика','Git']
rewiver_1.rate_hw(student_1,'Метрика',10)
rewiver_2.rate_hw(student_2,'Метрика',7)
student_1.rate_hw(lecturer_1,'Git',9)
student_1.mid_rate()
student_2.rate_hw(lecturer_2,'Git',7)
student_2.mid_rate()

student_list = [student_1,student_2]
lectors_list = [lecturer_1,lecturer_2]
def all_student_dz(spiski,cours):
    student_cout = 0
    sum_student_rate = 0
    for i in spiski:
      for k,v in i.grades.items():
          if k == cours:
              student_cout += 1
              sum_student_rate += v
    return print(sum_student_rate/student_cout)

def all_lectors_dz(spiski,course):
    lectors_count = 0
    sum_lectors_rate = 0
    for i in spiski:
        for k,v in i.grades.items():
            if k == course:
                lectors_count += 1
                sum_lectors_rate += v
    return print(sum_lectors_rate/lectors_count)
    
all_student_dz(student_list,'Метрика')
all_lectors_dz(lectors_list,'Git')