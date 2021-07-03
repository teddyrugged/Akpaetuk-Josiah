def simple_interest(i,p,r,t):
    i = (p * t * r)/100
    print(i)
i = int(0)
p = int(input("please enter the principal: "))
r = int(input("please enter the rate: "))
t = int(input("please enter the time: "))
simple_interest(i,p,r,t)