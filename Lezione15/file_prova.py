

# reader = open('prova.txt') # apre file

# try:
#     # fut

# finally: 

#     reader.close()


# with contesto di esecuzione 


class ContentManager():
    
    def __enter__(self):

        print("risorsa acquisita")

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is not None:
            pass
        print("Risorsa RIlasciata")

        return False
    
with ContentManager() as manager:

    print("Sono dentro with")

    

    







