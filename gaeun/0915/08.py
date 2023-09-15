import re
p = re.compile("[a-z]+")

m= p.match("python")
print(m)

#search 
m= p.search("python")
print(m)

#findall 정규식과 매치되는 문자열을 리스트로 리턴
result= p.findall("life is too short")
print(result)


#finditer 정규식과 매치되는 문자열을 반복 가능한 객체로 리턴
result= p.finditer("life is too short")
print(result)
for r in result: print(r)

#match
m= p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

m = re.match("[a-z]+","python")
