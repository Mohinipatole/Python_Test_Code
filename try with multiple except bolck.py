### try with multiple except blocks



try:



        x=int(input('enter 1st number:'))
        y=int(input('enter 2nd number:'))
        print('the result of:', x/y)



except ZeroDivisionError:

        print('cannot divide with zero')

except ValueError:

        print('please provide int values only')





    # o/p:
            enter 1st number:20
            enter 2nd number:0

            cannot divide with zero



    ## o/p:

           enter 1st number:10
           enter 2nd number:'two'

            please provide int values only
