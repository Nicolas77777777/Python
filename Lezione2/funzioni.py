def area_rettangolo(x: float,y: float) -> float:
    print(f"x={x} e y= {y}")
    area= x*y
    return area 

def calc_mattoni (x : float) -> int:
    num_mattoni: int 

x,y = 2,3
out: float = area_rettangolo(2,3)

print(f"L'area dellrettangolo con x={x} + e y ={y} è {out}")