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
        



