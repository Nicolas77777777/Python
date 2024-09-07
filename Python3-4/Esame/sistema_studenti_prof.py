# Definizione della classe Student
class Student:
    def _init_(self, student_id: str):
        # Inizializzazione dell'oggetto Student con un ID studente e una lista di corsi vuota
        self.student_id: str = student_id
        self.courses: list[str] = []

    def enroll(self, course: str) -> None:
        # Iscrive lo studente al corso se non è già iscritto
        if course not in self.courses:
            self.courses.append(course)
        else:
            # Stampa un messaggio se lo studente è già iscritto al corso
            print(f"Lo studente è già iscritto al corso {course}.")

    def get_courses(self) -> list[str]:
        # Restituisce la lista dei corsi a cui lo studente è iscritto
        return self.courses

# Definizione della classe School
class School:
    def _init_(self):
        # Inizializzazione dell'oggetto School con un dizionario vuoto di studenti
        self.students: dict[str, Student] = {}

    def create_student(self, student_id: str) -> None:
        # Crea un nuovo studente se l'ID studente non esiste già
        if student_id not in self.students:
            self.students[student_id] = Student(student_id)
        else:
            # Stampa un messaggio se lo studente con l'ID dato esiste già
            print(f"Lo studente con ID {student_id} esiste già.")

    def enroll_student(self, student_id: str, course: str) -> None:
        # Iscrive uno studente esistente a un corso
        if student_id in self.students:
            student = self.students[student_id]
            student.enroll(course)
        else:
            # Stampa un messaggio se lo studente non è trovato
            print("Studente non trovato.")

    def get_student_courses(self, student_id: str):
        # Restituisce la lista dei corsi di uno studente o un messaggio se lo studente non è trovato
        if student_id in self.students:
            student = self.students[student_id]
            return student.get_courses()
        else:
            return "Studente non trovato."
        
    def get_student_list(self) -> list[str]:
        # Restituisce la lista degli ID degli studenti
        return list(self.students.keys())
        
    def search_by_course(self, course: str):
        # Cerca tutti gli studenti iscritti a un corso specifico
        enrolled_students: list[str] = []
        for student_id, student in self.students.items():
            if course in student.get_courses():
                enrolled_students.append(student_id)

        if not enrolled_students:
            # Restituisce un messaggio se nessuno studente è iscritto al corso
            return f"Nessuno studente è iscritto al corso {course}."
        
        return enrolled_students