num1=[20,50,40]
num2=[20,50,40,5]
country=['india','japan','usa','da']

for i in country:
    if len(i)%2==1:
        print(i)

print('--Reverse list---')
for i in range(len(country)-1,-1,-1):
    print(country[i])


print(type(num1))
print(type(num2))

# mutable vs immutable
# Mutable didn't share the memory for dup vals
print(id(num1))
print(id(num2))

num3=20,50,40
num4=20,50,40
print(type(num3))
print(type(num4))

# im-mutable will share the memory for dup vals

print(id(num3))
print(id(num4))

fname='Muthu'
sname='Kumar'

# swap using without third variable change the values

print(id(fname))
print(id(sname))

fname,sname=sname,fname
print(fname)
print(sname)


# 10 methods
# covert the start

str= 'cap tailize'
da=str.split(' ')
print(da)
for i in da:
    print(i.capitalize(),end=" ")