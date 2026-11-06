#---------------------- DECORATOR FUNCTION ------------------------
'''def instagram(func):
    def wrapper(*args,**kwargs):
        print('go to website')
        print('login')
        func(*args,**kwargs)
        print('logout')
    return wrapper

@instagram
def Amulya(name):
    print('Text with:',name)

@instagram
def Ammu(name):
    print('Reels with:',name)

@instagram
def Anish(name):
    print('Text with:',name)

@instagram
def Arya():
    print('Text with preethi')


(Amulya('joo'))
print()
(Ammu('junnu'))
print()
(Anish('jeevan'))
print()
(Arya())'''


#total time calculation using st time and ed time 
'''import time
def distance(func):
    def wrapper(*args,**kwargs):
        st=time.time()
        func(*args,*kwargs)
        et=time.time()
        print(' The total distance is :',et-st)
    return wrapper

@distance
def person():
    for i in range(1,200):
       print('Steps count')

person()'''

#wap to give the delay time of 5 sec before exceute the main task
'''import time
def movie(func):
    def wrapper(*args,**kwargs):
        time.sleep(5)
        func(*args,**kwargs)
        print('let us enjoy the movie time ')
    return wrapper
    
@movie
def start():
    print('Movie start ')
start() '''

#count the function call
'''def callfunction(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        print('function call count start')
        func(*args,**kwargs)
        count+=1
        print(f'function call :{count}')
    return wrapper

@callfunction
def counter():
        print('hello')
   
counter()
counter()
counter()
counter()
counter()
counter()'''

        
    
