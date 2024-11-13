age=17
weight=60

def ifelse ():

     # 18 >18 --> false
    if age > 18:
        print('he is eligible')
    else:
        print('Not eligible')



# Selection
def nestedIf():


    # 17 >=18  --> false
    if age >=18:
        print('He is edligible to check weight')
        if weight>=60:
            print('Eligible for examination')
        else:
            print('under weigth not eligible')

    else:
        print('age less than 18 not eligible')

def elifCondition():
    mark = 86

    if mark>=95 and mark<=100:
        print('A+ grade')

    elif mark>=85 and mark<=90:
        print('A')

    else:
        print('fail')

elifCondition()