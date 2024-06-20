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
            self.fatture = 0
        else:
            self.salary =  None
            self.fatture = None
            doctor = None
            patient = None 
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def setSalary(self): 
        self.salary = self.doctor.getParcel() * len(self.patient)
    
    def getSalary(self) -> int:
        return self.salary

    def setFatture(self):
        self.fatture = len(self.patient)

    def getFatture(self)-> int:
        return self.fatture
    
    def addPatient(self, newPatient:Paziente, doctor):
        i:Paziente
        for i in self.patient:
            if i.getidCode() != newPatient.getidCode():
                self.patient.append(newPatient)
                self.setSalary(self)
                self.setFatture(self)
                print (f'Alla lista del Dottor {doctor.getLastname} è stato aggiunto il paziente {newPatient.getidCode}')
            else: 
                print(f'{newPatient.getidCode} è gia presente nella lista')


    def removePatient(self, idCode:Paziente, doctor):
        i:Paziente
        for i in self.patient:
            if idCode.getidCode() == i.getidCode():
                self.patient.remove(idCode)
                self.setSalary(self)
                self.setFatture(self)
                print(f'Alla lista del Dottor {doctor.getLastname} è stato rimosso il paziente {idCode.getidCode}')



p1:Paziente = Paziente("Franco","Minkia","11233")
d1: Dottore = Dottore("Mario","Rossi","Ostretica",30.0)
d2:Dottore = Dottore("Sonia","Figliola","Immunologia",350.0)
d2.setAge(40)
lista1=[]

fattura1:Fattura = Fattura(lista1,d2)




fattura1.addPatient(p1,d2)




                   
                   
           
           






