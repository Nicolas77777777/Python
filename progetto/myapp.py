# ogni volta che si modifca il file in python va rifatta la build da terminale con:
# docker build -t myapp-container .

import time
import sys # questo comando è stato aggiunto per visualizzare il print
sys.stdout = open("./file_per_le_print.txt","w+")
ii=1
while 1:
    time.sleep(3)
    sys.stdout.flush() # puntatore ad aun file 
    #questo comando è stato aggiunto per visualizzare il print 
    ii+=1

    print ("Col cazzo")
sys.stdout.close()
    

