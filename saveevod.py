from functools import reduce
lst = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda n:n%2==0,lst))
print(even)
square = list(map(lambda n:n**2,even))
print(square)
sum = reduce(lambda a,b:a+b,square)
print(sum)
