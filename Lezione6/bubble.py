def bubble_sort(x: list[int]):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
               temp: int = x[j]
               x[j] = x[j+1]
               x[j+1] = temp

               return x
 

listq : int = [4,7,6,7,8,2,67,8,2,4,5,6,]
ris= bubble_sort(listq)


print(ris)
