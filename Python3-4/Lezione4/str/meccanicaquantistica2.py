def word_count(s: str) -> dict[str,int]:
    """Questa funzione conta il numero di occorenze delle parole di una stringa

    e.s : se la stringa è un "ciao come stai. tutto bene. ciao io sto bene"
    il risultato deve essere 
    {"ciao":2, "come":2, "stai":1} """

    s: str =s.replace(".","").replace(",","").replace(";","")
    words: list[str] = s.split()
    d: dict[str,int]= dict()
    for word in words:
        if word not in d: 
            d[word ]= 1 
        else:
            d[word]=d[word]+1

    d_filtrer: dict [str, int] = dict()




    return d

    


stringa: str ="ciao come stai. tutto bene. ciao io sto bene bene"
print(word_count(stringa))