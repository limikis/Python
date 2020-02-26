with open("1.txt","r") as f:
        data =f.read().split()
f.close()
print (data)
x=len(data)
for i in range(0,x):
    pos=i
    for j in range(pos+1,x):
        if (len(data[pos])<len(data[j])):
            pos=j
    data[i],data[pos]=data[pos],data[i]
a=0
print ("oi 5 megaluteres:",data[0:4])
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U','.')  
for q in data[0:5]:
    for i in q:
       if i in vowels: 
        q = q.replace(i, "")
    data[a]=q[::-1]
    a=a+1
        
print (data[0:4])
