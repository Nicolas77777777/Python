
from multiprocessing import Process
import time


def sleep():

    print(f'Sono nella funzione')
    time.sleep(60)
    #time.sleep(30)
    print(f'Sto uscendo dalla funzione ')

if __name__== "__main__":

    tic: float = time.time()
    t1 = Process(target=sleep)
    t2 = Process (target=sleep)
    t1.start()
    t2.start()

    toc: float = time.time()
    time_elapsed: float = toc -tic



    print (f'{time_elapsed}')


print(sleep())

