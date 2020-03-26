# Rezolvarea problemei bazată pe 
# Threaduri, Problema PRODUCER-CONSUMER
# Am ales limbajul Python deoarece este
# Limbajul meu preferat, îl folosesc aproape 24/7
# Atât la crearea de scripturi cât și la testarea 
# Vulnerabilităților și crearea de GUIs + BackEnd 
# 
#
# CONTACT:
#   email: ufcolonel@gmail.com
#   linkedin: www.linked.com/in/olariu-alexandru
#   github: www.github.com/Razvan-Olariu
#
#
# Python 3.7 Stable Release
# x64 bit arhitectură


from threading import Thread, Condition
import time
import random

# Facem import a doua module din standard library
# Time pentru a putea folosi functia sleep
# Random pentru a alege random un intreg.


# Am ales sa rezolv problema folosind modulul threading
# deoarece concurrent.futures.ThreadPoolExecutor este valabil numai cu python 3 respectiv 3.8.2



queue = []
MAX_NUM = 10
condition = Condition()

# PAS 1: Cream o clasă PRODUCATOR ce produce
class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM: # Conditionala ; lista = plină
                print("Listă plină, producătorul așteaptă.")
                condition.wait()
                print("Spațiu în listă, consumatorul a notificat producătorul.")
            num = random.choice(nums)
            queue.append(num)
            # Un print ce afiseaza cate produse s-au creat.
            print("Am produs ", num, " produs", '' if num==1 else 'e',sep='')
            condition.notify()
            condition.release()
            time.sleep(random.random())

# PAS 2: Cream o clasă CONSUMATOR ce consumă
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nimic în listă, consumatorul așteaptă.")
                condition.wait()
                print("Producătorul a adăugat în listă și a notificat consumatorul.")
            num = queue.pop(0)
            # Un print ce afiseaza cate produse s-au consumat.
            print("Am consumat ", num, " produs", '' if num==1 else 'e',sep='')
            condition.notify()
            condition.release()
            time.sleep(random.random())


# Mai avem doar sa dam drumul la aceste threaduri (clase):
ProducerThread().start()
ConsumerThread().start()

# TODO: 
# -> Problema se putea rezolva si cu polimorfism si inheritance, dar nu s-a cerut.
