def subtract_all(x:list[float], y: float) -> list[float]:
    res: list[float]=[]
    for elem in x:
        diff: float = elem -y

        res.append(diff)
    return res


l: list[float]=[1,2,3,4,5]
y= 5

print(subtract_all(l,5))


