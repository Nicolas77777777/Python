class Animal:
    def __init__(self, name : str, species : str,
                age : float, height : float,
                width : float, preferred_habitat: str,
                ):

        self.name: str = name
        self.species: str = species
        self.age: float = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat = preferred_habitat
        self.health= round( 100 * (1 / age),3)
        self.animal_area : float = height * width #area animale 

    def animal_area():
        animal_area = Animal.height * Animal.height
        return animal_area

    
    def __str__(self) -> str:
        return (f'{self.name.capitalize()} (species = {self.species}, age = {self.age} height = {self.height}'
                + f'width ={self.width} preferred habitat = {self.preferred_habitat} health ={self.health}'
                +f' area animale {self.animal_area}')   
       
class Fence:
    def __init__(self, area : float, temperature : float, habitat : str):

        self.area : float = area
        self.temperature : float = temperature
        self.habitat : str = habitat
        self.lista_animali_recinto: list= []
        chek_area: float = chek_area



    def __str__(self) -> str:
        return f'area = {self.area} temperature = {self.temperature}, habitat = {self.habitat}'

class ZooKeeper:

    def __init__(self, nome : str, cognome : str, id: float):
         
        self.nome : float = nome
        self.cognome : float = cognome
        self.id : str = id
        self.area_recinto= None
        self.area_fence_animal_plus= 0
        self.area_fence_animal_minus= 0

    def add_animal(self, animal : Animal, fence: Fence) : 
        if animal.animal_area < fence.area and animal.preferred_habitat == fence.habitat:
            fence.lista_animali_recinto.append(animal.name)
            self.area_fence_animal_plus = animal.animal_area + fence.area
            print (f"{animal.name} è stato aggiunto alla gabbia")
        elif animal.animal_area > fence.area and animal.preferred_habitat == fence.habitat:
                 print (f"{animal.name} l'animale è troppo grande per questa gabbia")
        elif animal.animal_area < fence.area and animal.preferred_habitat != fence.habitat:
                  print(f"{animal.name} l'habitat del animale non è adeguato a questa gabbia")
        
    
    def remove_animal(self, animal: Animal, fence : Fence):
          if animal.name in fence.lista_animali_recinto:
              fence.lista_animali_recinto.remove(animal.name)
              self.area_fence_animal_minus= self.area_fence_animal_plus - animal.animal_area 
              print("L'animale è stato rimosso !")
          else:
              print("L'animale non è presente nel recinto.")

    def feed (self, animal : Animal):
            
                    animal.health += 1
                    animal.height *= 1.02
                    animal.width *= 1.02

    def clean(fence: Fence) :
        for i in Fence:
        
            pass
     
    def __str__(self) -> str:
        return f'nome = {self.nome} cognome = {self.cognome}, id ={self.id} '

# prove argomenti 
#animali
lupo = Animal("Lupo","lupus",7,30,20,"Foresta")
gatto_pallas = Animal("Gatto Pallas","Felide",4,15,10,"Steppa")
aquila = Animal("Aquila Reale","volatile",2,8,3,"Foresta")
cervo= Animal("cervo","cervide",4,30,11,"Foresta")
orso = Animal("orso","orside",4,300,3,"Foresta")

# fine animali

#fence
fence1 = Fence(300,25,"Steppa")
fence2 = Fence(1000,25,"Foresta")
# fine fence

#guardiani
franco = ZooKeeper("Franco","Minkia",333333)
# fine guardini 

print(f'{lupo.__str__()}\n{gatto_pallas.__str__()}\n{fence1}\n{franco.__str__()}')
# prove argomenti fine 

# prove funzioni 

franco.add_animal(lupo, fence1)
franco.add_animal(lupo,fence2)
franco.add_animal(aquila,fence2)
franco.add_animal(orso,fence2)

franco.add_animal(gatto_pallas, fence1)
franco.add_animal(gatto_pallas, fence2)

print(fence1.lista_animali_recinto)
print(fence2.lista_animali_recinto)

franco.add_animal(orso,fence2)

print(fence2.lista_animali_recinto)

franco.add_animal(aquila,fence2)
franco.add_animal(cervo,fence2)


print(fence2.lista_animali_recinto)







