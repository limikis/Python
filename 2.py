with open("2.txt","r") as f:
    data = f.read().split()
f.close()


good = list("bdghjlmnpqstvexz")
bad = list ("fckr")
print(data)

for word in data:
    for g in good:
        goodw=word.count(g)
    for b in bad:
        badw=word.count(b)
    if ( badw > goodw):
        print ("Kakh leksh:",word)
    else:
        print ("Kalh leksh:",word)

