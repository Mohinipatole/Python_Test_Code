#### Nested try-Except-finally


## 1. No exception is raised


try:
        print('outer try block')

        try:
                print('inner try block')

        except ZeroDivisionError:

                print('inner except block')

        finally:

                print('inner finally block')
except:

                print('outer except block')

finally:
                print('outer finally block')
            



#### O/P:

                outer try block
                inner try block
                inner finally block
                outer finally block
