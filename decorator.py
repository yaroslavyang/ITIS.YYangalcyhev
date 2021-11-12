import time 

f = open('text.txt', 'r')

def function_time(func):
    def wrap():
        start = time.time()
        f.write(start) 
        result = func()
        end = time.time()
        f.write(end)
        f.write(end-start)
    return wrap

@function_time
def example():
    f.write('Middle')
    return 123

print(example())