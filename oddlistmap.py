lst=[1,2,3,4,5,6,7,8,9,10]
f1=list(filter(lambda n:n%2==0,lst))
m=list(map(lambda n:n*n,f1))
print(m)
