firstlst: list[int] = [1, 5, 7, 8]
secondlst: list[int] = [2, 3, 7, 6]

firstlst.extend(secondlst)


thirdlst: list[int] = firstlst + secondlst

print(f'{firstlst}\n{secondlst}\n{thirdlst}')

########################

firstset: set[int] = {1, 5, 7, 8} 
secondset: set[int] = {2, 3, 7, 6}

firstset.update(secondset)

print(firstset)

mydict: dict[str, int] = {"a": 5, "b": 2}

for key,value in mydict.items():
    print(key,value)