# try:
#     print(10/0)
# except:
#     print(10/0)
# finally:
#     print('muthu')


# recursion
lst=[]
def fac(num1):
    if num1==10:
        lst.append(num1)
        print(num1)
    else:
        print(num1)
        lst.append(num1)
        fac(1 + num1)


# fac(1)
# print(lst)
# set
veg=['carrot',12,'tomato','onion']
frozen=frozenset(veg)
print(frozen)

print(id(veg))
print(id(frozen))











# value=add(10,10)
# if value==20:
#     print('its true')

# add=lambda  a,b : a+b
#
# result=add(50,50)
# print(result)

