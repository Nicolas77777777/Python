import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print (f"Elapsed time: {elapsed_time} second")




with timer():
    for i in range (0,100,2):
        print (i)



