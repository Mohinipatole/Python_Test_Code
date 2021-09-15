##### with using try- except block

print('stmt1')
try:
        print(10/0)
except ZeroDivisionError:
        print(10/2)
        print('stmt2')


##o/p:
          stmt1
           5
          stmt2      
