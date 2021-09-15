Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ######## Dictonary in python
>>> # dictionary is also known as a group of key value pairs
>>> 
>>> ## syntax: d={k1:v1, k2:v2,k3:v3}
>>> 
>>> ## example 1: write simple dic program to check which type of function used
>>> 
>>> 
>>> d ={100:'mohini', 200:'ovii', 300:'jui'}
>>> print(type(d))
<type 'dict'>
>>> 

>>> ### example 2.: how  to crate dictionary in empty dictionary or insert keys and values in dictionary
>>> 
>>> d{} ### empty dictionary
SyntaxError: invalid syntax
>>> d={} ## empty dict
>>> d[100]='ovii'
>>> d[200]='ravi'
>>> print(d)
{200: 'ravi', 100: 'ovii'}
>>> 

>>> d={}
>>> d[100]='apple'
>>> d[300]='dog'
>>> print(d)
{300: 'dog', 100: 'apple'}
>>> 

>>> 
>>> ### duplicate value in dic
>>> 
>>> ###example. 1.
>>> d={}
>>> d[100]='durga'
>>> d[200]='ravi'
>>> d=[100]='mohini'
SyntaxError: can't assign to literal
>>>  d={}
>>> d[100]='durga'
>>> d[200]='ravi'
>>> d[100]='mohini'
  File "<pyshell#32>", line 2
    d={}
    ^
IndentationError: unexpected indent
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> d={}
>>> d[100]='durga'
>>> d[200]='ravi'
>>> d[300]='mohini'
>>> print(d)
{200: 'ravi', 300: 'mohini', 100: 'durga'}
>>> d[100]='ovii'
>>> print(d)
{200: 'ravi', 300: 'mohini', 100: 'ovii'}
>>> 
>>> 
>>> 
>>> 
