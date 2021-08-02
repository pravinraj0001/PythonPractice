import threading #after python3 version _thread used in older version
import time

def func():
    print('1')
    time.sleep(0.1)
    print('2')
    time.sleep(0.1)
    print('3')

x = threading.Thread(target=func)
x.start()
#print(threading.activeCount())
print("4")
time.sleep(0.1)
print("5")
