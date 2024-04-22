# print("ciao")
# print("Hello")

# def subtract_all (x : list[float], y: float) -> list[float]:
#     res: list=[float]= []
#     for elem in x:
#         diff: float = elem-y
#         res.append(diff)

#     return res

# list=[1.4,2.4,3.5,4.6,5.7]
# y= 5.3
# out= subtract_all(x,y)

# print(out)

def subtract_list(x: list [float], y:list = [float]) -> list[float]:
    for i in range(len(x)):
        
        newlist: list  =x[i]-y[i]
    
    return newlist



mylist: list[float]= [1,2,3,4,5]
y:list [float]= [2,3,4,5,6]
subtract_list(mylist,y)
print(f"il risulato dopo la sottrazione è{subtract_list}")