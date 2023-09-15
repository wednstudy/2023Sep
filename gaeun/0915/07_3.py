a=[1,2,3]
ia = iter(a)
print(next(ia))
print(next(ia))
print(next(ia))

a=[1,2,3]
ia=iter(a)
for i in ia:
    print(i)

#class iterator
class MyItertor:
    def __init__(self, data):
        self.data=data
        self.position=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >=len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position+=1
        return result

if __name__ =="__main__":
    i =MyItertor([1,2,3])
    for item in i:
        print(item)


