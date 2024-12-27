n=int(input("Enter no:"))
s=n**2
st=str(s)
l=len(st)
h=l//2
lp=st[0:h]
rp=st[h:l+1]
lp1=int(lp)
rp1=int(rp) 

print("Given no:",n)
print("Square of",n,":",s)
print("Original number:",lp1+rp1)
if(lp1+rp1)==n:
    print("Given num is kaprekat")
else:
    print("oops its not kaprekat")
