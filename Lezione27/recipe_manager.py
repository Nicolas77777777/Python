
class RecipeManager:
    def __init__(self) -> None:
        "Gestisce tutte le operazioni legate alle ricette."

        self.recipes: dict = {}

    def create_recipe(self,name: str, ingredients:list[str]) -> dict: 
        
        """Crea una nuova ricetta con il nome specificato
          e una lista di ingredienti. Restituisce un nuovo 
          dizionario con la sola ricetta appena creata 
          o un messaggio di errore se la ricetta esiste già."""
        
        if name not in self.recipes:
            self.recipes[name]=ingredients
            return self.recipes
        else :
            raise ValueError("la ricetta esiste già")
            
    def add_ingredient(self,recipe_name: str, ingredient: str):

        """ Aggiunge un ingrediente alla ricettaå specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore 
        se l'ingrediente esiste già o la ricetta non esiste."""

        if recipe_name in self.recipes:
            if ingredient not in self.recipes[recipe_name]:
                self.recipes[recipe_name].append(ingredient)
                return self.recipes
            else:
                raise ValueError("l'ingrediente esiste già")

    def remove_ingredient(self,recipe_name, ingredient):
        """ Rimuove un ingrediente dalla ricetta specificata. 
        Restituisce la ricetta aggiornata o un messaggio di errore 
        se l'ingrediente non è presente o la ricetta non esiste."""

        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return self.recipes
            else:
                raise ValueError("l'ingrediente  non esiste")

    def update_ingredient(self,recipe_name, old_ingredient, new_ingredient):

        """Sostituisce un ingrediente con un altro nella ricetta
            specificata. Restituisce la ricetta aggiornata 
            o un messaggio di errore se l'ingrediente 
            non è presente o la ricetta non esiste."""
        
        if recipe_name in self.recipes:
            self.remove_ingredient(recipe_name,old_ingredient)
            self.add_ingredient(recipe_name,new_ingredient)
            return self.recipes
        else:
            raise ValueError("la ricetta non esiste")
    pass

    def list_recipes(self,): #Elenca tutte le ricette esistenti.
        return list(self.recipes.keys())

    def list_ingredients(self,recipe_name): 
        
        """Mostra gli ingredienti di una specifica 
        ricetta. Restituisce un elenco di ingredienti
        o un messaggio di errore se la ricetta non esiste."""
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            raise ValueError(f"La ricetta '{recipe_name}' non esiste")


    def search_recipe_by_ingredient(self,ingredient):
        
        """ Trova e restituisce tutte le ricette 
        che contengono un determinato ingrediente. 
        Restituisce un elenco di ricette o un messaggio 
        di errore se nessuna ricetta contiene l'ingrediente."""
        found_recipes = [name for name, ingredients in self.recipes.items() if ingredient in ingredients]
        if found_recipes:
            return found_recipes
        else:
            raise ValueError(f"Nessuna ricetta contiene l'ingrediente '{ingredient}'")




manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))

print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))