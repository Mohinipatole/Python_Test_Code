
 ##ternary operator
## example 1.
a=10
b=30
min = 40 if a>b else 50
print("the minimum value is:",min)





## example 2

a=int(input('enter the first number:'))
b= int(input('enter the second number:'))
min= a if a<b else b
print('the minimum value:',min)




### example 3

a= int(input('enter the first  number:'))
b= int(input('enter the second number:'))
c= int(input('enter the third number:'))
min =a if a<b and a<c else b if b<c else c
print('the minimum value:',min)

