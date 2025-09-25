def g(n):
    if not(n==0):
        return 1 
    else:
        return 0
a=3 
b=2 
c=2
def col(n):
    r=n%b
    return (a**g(r))*(n-r)/b+c*g(r)
    
n=51
l=[n]

for i in range(25):
    n=col(n)
    l.append(n)
  
print(l)
