### Default except block


try:
        x=int(input('Enter the 1st number:'))
        y=int(input('Enter the 2nd number:'))
        print('The Result :', x/y)

except ZeroDivisionError:

        print('ZeroDivisionError: divide by zero')

except:

        print('Default Except block: provide int values')



##### o/p:1

        Enter the 1st number:10
        Enter the 2nd number:0
ZeroDivisionError: divide by zero



#### o/p:2

        Enter the 1st number:10
        Enter the 2nd number:'ten'
Default Except block: provide int values
