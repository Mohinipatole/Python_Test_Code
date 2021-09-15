##### nested try except finally block



## exception raised at outer try block



try:

        print('outer try block')
        print(10/0)


        try:
                print('inner try block')

        except ValueError:

                print('inner except block')

        finally:

                print('inner finally block ')


except:

        print('outer except block')

finally:

        print('outer finally block')




##O/P:
        outer try block
        outer except block
        outer finally block
