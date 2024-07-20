#def is_palindrome (s: str) -> bool:
"""Restituisce True se s è palindroma; altrimenti restituisci False
    e.s "Amo Roma" è una stringa palindroma
    e.s "Ciao come stai?" non è una stringa palindorma 
    """

stringa:str = "Amo Roma"
frase2: str ='Ciao come stai?" non è una stringa palindorma'

stringa: str = stringa.lower().replace(' ','').replace('\n','').replace('.','').strip()


def is_palindroma(stringa: str):
    stringa: str = stringa.lower().replace(' ','').replace('\n','').replace('.','').strip()

    i:int = 0
    while i < len(stringa):
        j = len(stringa) - (i+1)
        if stringa[i]!= stringa[j]:

            return False
    else:
        i += 1

        return True 
    

def is_palindroma_new(s: str) -> bool:
    s: str = stringa.lower().replace(' ','').replace('\n','').replace('.','').strip()
    
    s1: str = ""
    for i in range(len(s)-1, 0, -1):
        s1 += s[i]

    for i in range (len(s)):
        if s[i] != s1[i]:
            return False
        else:
            return True



   
#is_palindroma(stringa)

print(is_palindroma_new(stringa))










