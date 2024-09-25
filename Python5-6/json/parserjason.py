import sys, json 

def Serialize(Mydict1, file_path)-> bool :

    try:
        str1 = json.dumps(Mydict1, indent=4)  

       
        with open(file_path, 'w') as json_file:
        
            json_file.write(str1)
        
        return True
    except Exception:

        return False
    

def Deserialize(file_path) -> dict:
    try:
        
        with open(file_path, "r") as json_file:
            
            dict_1 = json.load(json_file)
        
        return dict_1
    except Exception as errore:
     
        print(f" errore : {errore}")
        return None


dict1:dict = { "brand": "Ford",
            "electric": False,
            "year": 1964,
            "colors": ["red", "white", "blue"]}


bRet = Serialize(dict1,"diz.json") 
print(Deserialize("diz.json"),type(Deserialize("diz.json")))


Serialize(dict1,"dizejson") 
print(Deserialize("dize.json"),type(Deserialize("diz.json")))








