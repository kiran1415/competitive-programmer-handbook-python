# Input -> 10 20 monkey
#a, b, c = raw_input().split(' ')
#print(a, b, c)
#
## Input with map -> 10 20
#a, b = map(int, raw_input().split(' '))
#print(a, b)
#
## Input with map -> 10, 20
#a, b = map(int, raw_input().split(','))
#print(a, b)

# Python has dynamic data type so integers, float are same as variables

# Mathematics
## Sum Formulas -> 1 + 2 + 3 ... n = n(n+1)/2
## Sum Formulas -> 1^k + 2^k + 3^k ... n^k = n(n+1)(2n+1)/6	
## AP -> a + .. + b = n(a+b)/2
## GP -> a + ak + ak^2 + .. + b = (bk -a) / (k - 1)
ap = [3, 7, 11, 15]
print(4*(3+15)/2)

gp = [3, 6, 12, 24] # k is 2 here
print((24*2 - 3)/(2-1))

# Set
x = set([2, 4, 7])
a = set([1, 2, 5])
b = set([2, 4])
print(x)
print(a.intersection(b))
print(a.union(b))


