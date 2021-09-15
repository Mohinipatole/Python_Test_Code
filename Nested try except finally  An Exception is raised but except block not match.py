##### Nested try-except finally block


## An exception is raised but except block not matched





try:

        print('outer try block')

        try:
                print('inner try block')

                print(10/0)

        except ValueError:

                print('inner except block')

        finally:

                print('inner finally block')

except:

        print('outer except block')

finally:

        print('outer finally block')
        


########### o/p:


        outer try block
        inner try block
        inner finally block
        outer except block
        outer finally block
