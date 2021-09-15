## OS.-exit(0) vs finally block

import os

try:

         print('try')

         os._exit(100)

except ValueError:

         print('except')


finally:

        print('finally')



##: O/P
          try
