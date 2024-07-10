
from multiprocessing import Process
import time




def bubble_sort2(x: list[int]):
    ho_fatto_swap : int = 0
    for i in range(len(x)):
        for j in range(len(x)-i -1):
            if x[j] > x[j+1]:
               # swap (x[j], x[j+1])
               ho_fatto_swap = 1
               temp: int = x[j]
               x[j] = x[j+1]
               x[j+1] = temp

        if not ho_fatto_swap :
               break


def sleep():

    print(f'Sono nella funzione')
    time.sleep(60)
    #time.sleep(30)
    print(f'Sto uscendo dalla funzione ')

if __name__== "__main__":

    tic: float = time.time()
    t1 = Process(target=bubble_sort2)
    t2 = Process (target=bubble_sort2)
    t1.start()
    t2.start()

    toc: float = time.time()
    time_elapsed: float = toc -tic



    print (f'{time_elapsed}')


print(sleep())

