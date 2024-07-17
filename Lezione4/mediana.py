def mediana (l: list[float]) -> float:

    """questa funzione restituisce la mediana 
     della lista

     Esempio 
        lpari = [2,9,0,-1,25,2,4,3]

        lpariordinata = [-1 0 2 2 3 4 9 25]
        mediana = (2+3)/2 = 2.5

        ldispari = [2, 9, 0, -1, 25, 2, 4]
        lordinata = [ -1, 0, 2, 2, 4, 9, 25]
        mediana = 2 perche 2 è l'elemento centrale 
     """
    

    l.sort()
    print(l)
    lenghtlista = len(l)
    print(f'lunghezza lista {lenghtlista}')

    if lenghtlista % 2== 0:
        num_cen=(lenghtlista //2) -1
        #print(f'numemro centrale lunghezza {num_cen}')
        print(f'num centrale index {l[num_cen]}')
        num_cen1 = num_cen +1
        print(f'num centrale index {l[num_cen1]}')
        mediana=  (l[num_cen] + l[num_cen1]) /2

        return mediana
    
    elif lenghtlista%2 !=0:

        num_cen=(lenghtlista //2)
        print(f'num centrale  dispari {num_cen}')

        print(f'num centrale index dispari {l[num_cen]}')

    return {l[num_cen]}

        
    

lpari = [2,9,0,-1,25,2,4,3]
ldispari = [2, 9, 0, -1, 25, 2, 4]

#print(mediana(lpari))
print(mediana(ldispari))


