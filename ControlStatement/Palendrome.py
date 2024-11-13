# 121
# 123

num=123
temp=num
rev=0


# 123 > 0 --> true
while num>0:
    # 12>0
    # 1 > 0
    # 0 > 0 --> false

    remainder=num%10

    # remainder=3
    # remainder = 32
    # remainder = 1
    rev=rev*10+remainder

    # 0*10=0+3 = 3
    # 3*10+32 = 32
    # 32*10+1=321

    num=num//10
    #num=12
    #num = 1
    #num=0

print(rev)










