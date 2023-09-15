a= "Life is too short" #인코딩
b= a.encode("utf-8")
print(b)
print(type(b))

a="한글"  
b=a.encode("euc-kr")
print(b)

# 디코딩
a="한글"
b= a.encode("euc-kr")
b.decode("euc-kr")

