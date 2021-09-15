#### exception handling


# syntax error

x=10
if x==10      ## missing :
print('x value 10')

#o/p:
    invalid program syntax error


#### run time error

x=int(input('enter first number:'))
y=int(input('enter second number:'))
print('the result:',x/y)

#o/p: 1
enter first number:10
enter second number:2
('the result:', 5)

## o/p:2
enter first number:10
enter second number:0
Traceback (most recent call last):
 File "C:/Python27/exception handling.py", line 13, in <module>
    print('the result:',x/y)
ZeroDivisionError: integer division or modulo by zero
