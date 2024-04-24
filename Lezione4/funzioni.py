# def const (area: float):
#     l: int = area/2
#     w: int = area/2
#     li,wi=int(l),int(w)
#     list_w_l:list= [li,wi]
   
#     return list_w_l


#print(const(4))


# def somma_elementi(x: list[int], y: list[int]) -> list[int]:
#     res: list = []
#     for i in range(len(y)):
#         r:list=x[i]+y[i]
#         res.append(r)
#     return res


#print(somma_elementi([1,1,1],[1,1,1]))
	
# def somma_elementi1(x: list[int], y: list[int]) -> list[int]:
#     res: list = []
#     if len(x)  == len(y):
#         for i in range(len(y)):
#             r:list=x[i]+y[i]
#             res.append(r)
#         return res
#     elif len(x) != len(y):
#         z: list = x[0]+y[0]
#         res.append(z)
#     return res

# print(somma_elementi1([1,],[1,2]))
# print(somma_elementi1([1,1,1],[1,1,1]))


# def even_odd_pattern(nums: list[int]) -> list[int]:
#     pari =[x for x in nums if x % 2 ==0]
#     dispari = [x for x in nums if x % 2 != 0]

#     return dispari, pari 


# print(even_odd_pattern([3, 6, 1, 8, 4, 7]))



def even_odd_pattern1(nums: list[int]) -> list[int]:
    pari=[]
    dispari=[]
    for i in nums:
        if i % 2==0:
            pari.append(i)
        elif i % 2 !=0:
            dispari.append(i)
        
    return pari + dispari

print(even_odd_pattern1([3, 6, 1, 8, 4, 7]))
    
