import time
def calculate_time(func):
    def wrapper():
        t = time.time()
        func()
        x = (time.time()-t)
        print('Total time', x )
    return wrapper
@calculate_time
def test():
    print('running test function')
    time.sleep(2)
    
