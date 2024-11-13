productPrice=100
customer=int(input('Enter your amount'))
#   false
if customer==productPrice:
    print('Deliver a product')
#   200<100  --> false
elif customer<productPrice:
    pendingAmt=productPrice-customer
    print('Need to pay',pendingAmt)

# 200>100 --> true
elif customer>productPrice:
    balAmt=customer-productPrice
    print('Your balance is',balAmt)
    print('Thanks for coming your product delivered')



