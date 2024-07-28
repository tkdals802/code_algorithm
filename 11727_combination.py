n = int(input())

def combination(a,b):
    t=b
    r1, r2 = 1,1
    while t>0:
        r1*=a
        r2*=b
        a-=1
        b-=1
        t-=1
    return r1//r2


a = n//2
b = n%2
result=0
while a>=0:
    result+=(2**a * combination(a+b,b))
    a-=1
    b+=2
print(result%10007)
