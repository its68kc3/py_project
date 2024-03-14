import process, time

class main:
    def __init__(self):
        pass
    
    @process.getExecTime
    def print(self, message):
        time.sleep(1.5)
        print(message)

obj = main()
obj.print('Can I have a cup of coffee now? :((')