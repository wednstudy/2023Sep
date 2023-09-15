def mygen():
    yield "a"
    yield "b"
    yield "c"

g=mygen()
print(next(g))
print(next(g))
print(next(g))

#generator
def mygen():
    for i in range(1,1000):
        result= i*i
        yield result

gen = mygen()
print(next(gen))
print(next(gen))

gen= (i*i for i in range(1,1000))


class MyIterator:
    def __init__(self):
        self.data=1

    def __iter__(self):
        return self

    def __next__(self):
        result= self.data*self.data
        self.data+=1
        if self.data >=1000:
            raise StopIteration
        return result

# generator2
import time

def longtime_job():
    print("job start")
    time.sleep(1) #1초 지연
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))

