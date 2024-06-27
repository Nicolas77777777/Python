def funzione(id: int):
    import time
    import random


    sleep_time: int = random.randint(1,10)
    print(f'{id=}time {time.time}')
    #print(f'{id=} time {time.time()}')
    time.sleep(sleep_time)
    print(f'{id=} time {time.time()}')


if __name__ == "__main__":

    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(10))

    # list_thread: list[threading.Thread]= []

    # for id in range(3):


    #      x: threading.Thread = threading.Thread (target=funzione, args=(1,))
    #      list_thread.append(x)
    #      print(f" Prima di runnare il thread {time.time()}")

    #      x.start()

    #      print(f'ho runnato il thread!{time.time()}')


    # for t in list_thread:
    #     t.join()
    #     print(f'terminato')

    
