class Mul:
    def __init__(self, m):
        self.m=m

    def mul(self, n):
        return self. m*n

    def __call__(self, n):
        return self.m*n

if __name__ =="__main__":
    mul3 =Mul(3)
    mul5 =Mul(5)

    print(mul3(10))
    print(mul5(10))

#wrapper
def mul(m):
    def wrapper(n):
        return m*n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))
    print(mul5(10))
    

#decorator
import time

def elapsed(original_func):
    def wrapper():
        start=time.time()
        result=original_func()
        end=time.time()
        print("함수 수행시간: %f 초" %(end-start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

"""decorated_myfunc = elapsed(myfunc)
decorated_myfunc()
"""
myfunc()

#decorater2


