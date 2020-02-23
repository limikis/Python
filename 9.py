def fun(x):
    digit=0
    while (x>0):
        digit+= int(x%10)
        x=int(x/10)
        print (digit)
    return digit



num=int(input())

while num>9:
    num=num*3+1
    print (num)
    num=fun(num)

print (num)
