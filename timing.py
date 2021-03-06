import time
def calculate_time(func): #wrapper function gets current time reads test function then gets time again, returns time2-time1
    def wrapper():
        t = time.time()
        func()
        x = (time.time()-t)
        print('Total time', x )
    return wrapper
@calculate_time
def test(): #sleeps for 2 seconds to test total time
    time.sleep(2)
    
