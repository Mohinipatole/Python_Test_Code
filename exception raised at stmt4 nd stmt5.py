#### case 4: if an exceptin raised at stmt-4 and stmt-5

print('stmt-0')
try:
        print('stmt-1')
        print('stmt-2')
        print('stmt-3')
except xxx:
        print('stmt-4')
    print('stmt-5')

## o/p: Abnormal Termination



## Note:: here stmt-4 not in try block its inside the try block alwyas abnormal termination also this conditions is applicable for stmt-5 because stmt-5 is inside the try block
