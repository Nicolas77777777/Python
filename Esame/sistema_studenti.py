class Student:
    def __init__(self, student_id: str) -> None:

        self.student_id = student_id
        self.courses:list[str]= []

    def enroll(self,course:str) -> str:
        if course not in self.courses:
            self.courses.append(course)
        else:
            return f'Lo studente è gia iscritto al corso '


    def get_courses(self)-> list:
        return self.courses
    

class School:
    def __init__(self) -> None:

        self.students:dict[str,Student]= {}

    def create_student(self,student_id:str):
        if student_id not in self.students:
            self.students[student_id]=Student(student_id)
            return {student_id: []}
        else:
            return f'lo studente con ID {student_id} esiste già'
        
    def enroll_student(self,student_id:str, course: str ) -> str:
        if student_id in self.students:
            self.students[student_id]=[course]
        else: 
            return f'Studente non trovato '
    
    def get_student_courses(self, student_id:str) -> list:

        if student_id in self.students:
            return self.students[student_id]
        else:
            return f'Studente non trovato '
        
    def get_student_list (self) -> list:

        return list(self.students.keys())
    

    def search_by_courses(self, courses):
        for key, value in self.students.items():
            print(key,value)
            if courses in value:
                return True
            else:
                return False




        
        

scuola = School()

print (scuola.create_student("1001"))
print (scuola.create_student("1001"))
print (scuola.create_student("1002"))
print (scuola.create_student("1003"))



print (scuola.enroll_student("1001","Filosofia"))
print (scuola.enroll_student("1002","Filosofia"))
print (scuola.get_student_courses("1001"))

print (scuola.get_student_list())

print(scuola.search_by_courses('Filosofia'))















        



