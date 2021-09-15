#### If exception raised but not handled using finally block

try:

        print('try')
        print(10/0)

except ValueError:

        print('except')

finally:

        print('finally')





### o/p:


        try
        finally

Traceback (most recent call last):
  File "C:/Users/admin/Desktop/practices 1/finally block exception is raised but not handled.py", line 6, in <module>
    print(10/0)
ZeroDivisionError: integer division or modulo by zero
