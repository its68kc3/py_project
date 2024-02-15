class testLainecakes:
    def classFunc(self):
        print(self)

def decoration(func1):
    print('Executed from outer function')
    def wrapper(*args, **kwargs):
                print('Executed from inner function')
                print('Pre execution of function')
                func1(*args, **kwargs)
                print('Post execution of function')
    return wrapper

@decoration
def printSomething(message):
    print(message)

printSomething(message='Hello Lainecakes Pwetcakes')