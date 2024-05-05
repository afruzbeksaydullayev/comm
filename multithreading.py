import threading
import time


def call():
    for n in range(10):
        print(n)
        time.sleep(1)

calling = threading.Thread(target=call())
calling.start()