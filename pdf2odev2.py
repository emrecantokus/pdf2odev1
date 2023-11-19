x0=0
x1=2
x2=4
j=0


while j < 4:
    xc=(x1+x2)/2
    x=xc
    fonk=x*x*x-2*x*x-5
    if(fonk<0):
        x1=xc
    else:
        x2=xc
    j += 1

print("4 iterasyon sonucunda bulunan kok degeri",xc)
print("4 iterasyon sonucunda buluanan deger",fonk)
