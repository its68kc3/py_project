class testLainecakes:
    def classFunc(self):
        print(self)

def outerFunction(func1):
    print('Executed from outer function')
    def innerFunction():
                print('Executed from inner function')
                print('Pre execution of function')
                func1()
                print('Post execution of function')
    return innerFunction

@outerFunction
def printHelloWorld():
    print('Hello, world! :)')

printHelloWorld()
x = testLainecakes()
x.classFunc()