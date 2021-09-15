#### customized exception handling by using try-except block

###example 1. without using try -except block

print('stmt1')
print(10/0)
print('stmt2')



##o/p:

stmt1

Traceback (most recent call last):
  File "C:/Users/admin/Desktop/practices 1/without try-except block.py", line 6, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
