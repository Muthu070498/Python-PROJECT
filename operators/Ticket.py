userAge=int(input('Enter your age: '))
Economy=100
Premium=150

if userAge>=18:
    print('Eligible to watch a movie')
    customerPrice=int(input('Enter your Amt: '))
    if customerPrice==Economy:
        print('Economy')
    if customerPrice==Premium:
        print('Premium')
    else:
        print('not equal to premium amt')

    if customerPrice>Premium:
        returnAmt= customerPrice-Premium
        print('Your bal Amt: ',returnAmt)
        print(' you are eligible to 100,150  tickets ')

    else:
        print('Invalid Amt')
else:
    print('Below 18')