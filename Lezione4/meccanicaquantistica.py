# e: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

# def counter(s : str) -> list[int ]:

#     s = s.lower
#     res: list[int]= []
#     #quanti caratteri ha la stringa 
#     res.append(len(s))
#     # quante parole ha la stringa 
#     res.append(len(s.split())) # s = "ciao bello "
#     #quante parole distinte ha la stringa
#     parole = s.split ()
#     parole_distinte = set(parole)
#     res.append(parole_distinte)
#     #quanti frasi ha la stringa 
#     res.append(len(s.split("."))-1)

#     return res 

# print(counter(e))


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
    return d


stringa: str ="ciao come stai. tutto bene. ciao io sto bene bene"
print(word_count(stringa))



