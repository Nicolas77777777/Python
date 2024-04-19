def median(l: list[float]) -> float:


l:int = [2,9,0,-1,25,2,4,3]
l = sorted(l)
mid = len(l) //2
mediana: float = 0
if len(l)% 2 == 1: #dispari
    print("La mia lista ha la lunghezza dispari")
    mediana= l[mid]

else: # pari
    print("La mia lunghezza è pari") 
    mediana = (l[mid]+ l[mid -1]) / 2

return mediana


ff




