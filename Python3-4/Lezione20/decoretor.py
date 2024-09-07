def say_hello():
    print(f'Hello Flavio')

def say_ciao () :

    print(f'Mimmo')

# def saluta(func):

#     func('Flavio')

# saluta(say_hello)



# def parent():
#     print(f'sono in parent')

#     def first_child():

#         print(f'sono il figlio')

#     def second_child():

#         print(f'Sono in scendo child')

#     return second_child # ritorna il valore in memoriua

# out_function = parent()
# print(out_function)

# out_function()

import time

def get_time(func):
    def wrapper(*args):
        start = time.time()

        func(*args)

        end = time.time()
        elapsed_time = end - start
        print(f'{elapsed_time=}')

    return wrapper 


@get_time
def say_hello(name: str) -> None:
    print (f'Hello, {name}')


@get_time 
def random_list():
    import random
    import time

    sleep_time: int = random. randint(0,5)
    time.sleep(sleep_time)





