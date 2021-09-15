### control flow in try-except block

### case 3: if an exception raised at stmt-2 but corresponding except block not matched

print('stmt0')

try:
    print('stmt1')
    print(10/0)
    print('stmt2')
except ValueError:
        print('stmt3')
        print('stmt4')


## o/p:

        stmt0
        stmt1

Traceback (most recent call last):
  File "C:/Users/admin/Desktop/practices 1/except block not matched.py", line 9, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
