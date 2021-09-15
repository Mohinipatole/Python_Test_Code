### single except block that can handle multiple different exception



try:

        x=int(input('Enter 1st number:'))

        y=int(input('Enter 2nd numbeer:'))

        print('The Result of:', x/y)

except (ZeroDivisionError, ValueError) as msg:
   
            print('The Raised Exception:', msg.__class__.__name__)
            print('Description of Exception:',msg)
            print('Please provide valid input only.....')
        



### o/p:1
          Enter 1st number:10
          Enter 2nd numbeer:0
('The Raised Exception:', 'ZeroDivisionError')
('Description of Exception:', ZeroDivisionError('integer division or modulo by zero',))
Please provide valid input only.....'''




##o/p:2
            #Enter 1st number:10
           # Enter 2nd numbeer:'two'
('The Raised Exception:', 'ValueError')
('Description of Exception:', ValueError("invalid literal for int() with base 10: 'two'",))
Please provide valid input only.....
