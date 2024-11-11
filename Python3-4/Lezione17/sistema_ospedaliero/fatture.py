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
    
    def addPatient(self, newPatient:Paziente):
        if newPatient in self.patient:
            print(f'{newPatient.getidCode} è gia presente nella lista')
        else:
            newPatient is not self.patient
            self.patient.append(newPatient)
            self.setSalary()
            self.setFatture()
            print (f'Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}')


    def removePatient(self, idCode):
        i:Paziente
        for i in self.patient:
            if i.getidCode() == idCode:
                self.patient.remove(i)
        self.setSalary()
        self.setFatture()
        print(f'Alla lista del Dottor {self.doctor.getLastname()} è stato rimosso il paziente {idCode}')



p2:Paziente= Paziente("mimmi","me puzza il culo", "2222")
p1:Paziente = Paziente("Franco","Minkia","11233")
p3:Paziente = Paziente("Giovanni","More","1333")
p4:Paziente = Paziente("Giuseppe ","Scordamaglia","1553")


d1: Dottore = Dottore("Mario","Rossi","Ostretica",30.0)
d2:Dottore = Dottore("Sonia","Figliola","Immunologia",350.0)
d2.setAge(40)
lista1=[]

fattura1:Fattura = Fattura(lista1,d2)

fattura1.addPatient(p1)
fattura1.addPatient(p2)
print(fattura1.getFatture())
fattura1.addPatient(p3)
fattura1.addPatient(p2)

fattura1.removePatient("2222")

fattura1.addPatient(p4)

li= fattura1.patient
print(fattura1.patient)
print(li)

print(fattura1.getFatture())
print(str(fattura1.getSalary()))
fattura1.removePatient("1553")
print(fattura1.getSalary())






                   
                   
           
           






