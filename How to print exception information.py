## How to print exception information:



try:

            x=int(input('Enter 1st number:'))

            y=int(input('Enter 2nd number:'))

            print('The Result of :', x/y)

except (BaseException) as msg:

                print('The type of Exception:', msg.__class__)

                print('The Raised Exception :', msg.__class__.__name__)

                print('The Description of Exception:', msg)

                


### o/p:1

         Enter 1st number:10
        Enter 2nd number:0
    ('The type of Exception:', <type 'exceptions.ZeroDivisionError'>)
    ('The Raised Exception :', 'ZeroDivisionError')
    ('The Description of Exception:', ZeroDivisionError('integer division or modulo by zero',))






## o/p:2

    Enter 1st number:10
    Enter 2nd number:'five'
('The type of Exception:', <type 'exceptions.ValueError'>)
('The Raised Exception :', 'ValueError')
('The Description of Exception:', ValueError("invalid literal for int() with base 10: 'five'",))







