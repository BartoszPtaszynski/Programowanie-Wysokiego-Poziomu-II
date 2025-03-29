from threading import Thread, RLock
from time import sleep
from random import random

counter = 0



def count(lock:RLock )-> None:
    global counter
    sleep(5*random())
    with lock: #samo zamyka i otwiera
        x = counter + 1
        sleep(random())
        if random()<0.1: raise Exception("Hello world!")
        counter = x
        print(x)
    # lock.acquire()#samo zamyka i otwiera
    # x = counter + 1
    # sleep(random())
    # counter = x
    # print(x)
    # lock.release()

#starac sie nie korzystać z blokad , pamieci dzielonej. a jesli potrzebujemy synchronizacji to preferowanym rozwiązanie jest stosowanie kolejek komunikatu. Obiekty powinny byc nie modyfikalne
lock = RLock()
threads = [Thread(target=count, args=(lock,)) for i in range(20)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(f'Threads finished, counter={counter}')

# lock.acquire() - nadaje blokade
# # code in critical section
# lock.release() - oddaje blokade