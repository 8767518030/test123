# simple entrest calculator
def simple_intrest(p,n,r):
    i=(p*n*r)/100
    amt=p+i
    return{"intrest":i,"amount":amt}


# take inpute user in consol
p=float(input("pleas enter yoar principl in INR:"))
n=int(input("ples enter number of yrars:"))
r=float(input("pleas enter a rante of intrest in %p.a:"))

# calculate intrest and amount
results=simple_intrest(p,n,r)
print(results)



