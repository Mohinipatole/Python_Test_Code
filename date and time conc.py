Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #### date and time concept in python
>>> 
>>> ### example.1 simple program to print ticks
>>> 
>>> import time;
>>> ticks=time.time()
>>> print("number of ticks since 12:00am, sep18, 1999:",ticks)
('number of ticks since 12:00am, sep18, 1999:', 1630728158.154)
>>> 

>>> 
>>> #### getting current time
>>> 
>>> ## example
>>> import time;
>>> localtime=time.localtime(time.time())
>>> print("local current time:",localtime)
('local current time:', time.struct_time(tm_year=2021, tm_mon=9, tm_mday=4, tm_hour=9, tm_min=37, tm_sec=30, tm_wday=5, tm_yday=247, tm_isdst=0))
>>> 
>>> 
>>> 
>>> 
>>> #### getting formated time
>>> 
>>> ## example
>>> import time;
>>> localtime=time.asctime(time.localtime(time.time()))
>>> print("local current time:",localtime)
('local current time:', 'Sat Sep 04 09:54:02 2021')
>>> 
>>> 
>>> #### getting calendar for the month
>>> 
>>> ## example: print a calendar for a givent month(sep2021)
>>> 
>>> import calendar
>>> cal=calendar.month(2021,9)
>>> print("here is the calendar:",cal)
('here is the calendar:', '   September 2021\nMo Tu We Th Fr Sa Su\n       1  2  3  4  5\n 6  7  8  9 10 11 12\n13 14 15 16 17 18 19\n20 21 22 23 24 25 26\n27 28 29 30\n')
>>> 
>>> ## OR
>>>  import calendar
>>> cal=calendar.month(2021,9)
  File "<pyshell#37>", line 2
    import calendar
    ^
IndentationError: unexpected indent
>>> import calendar
>>> cal=calendar.month(2021,9)

>>> print(cal)
   September 2021
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

>>> 
