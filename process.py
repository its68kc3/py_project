import time

class process:
    def classFunc(self):
        print(self)

def getExecTime(func1):
    def wrapper(*args, **kwargs):
                _timeExecuted = time.time()
                func1(*args, **kwargs)
                _executionTime = time.time() - _timeExecuted
                print(_executionTime)
    return wrapper