from persona import Persona
from dottore import Dottore
from paziente import Paziente


class Fattura:

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        
        self.patient:list = patient
        self.doctor = doctor

        self.fatture: int = 0
        self.salary: int = 0

        if doctor.isAValidDoctor() == True:
            self.salary = 0
            self.fatture =0
        else:
            self.salary =  None
            self.fatture = None
            doctor = None
            patient = None 
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
