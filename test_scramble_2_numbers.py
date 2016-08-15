#!C:\Python27\python.exe

import sys


try:
  num1  = sys.argv[1]
except:
  num1 = raw_input('what is number 1?')
oldnum1 = num1
try:
  num2  = sys.argv[2]
except:
  num2 = raw_input('what is number 2?')
oldnum2 = num2

#the functions
def shownums():
  print str(num1) + ' ' + str(num2)
def update():
  oldnum1 = num1
  oldnum2 = num2


for u in range(0,2):
    # loop 2
    update()
    shownums()
    num1 = num2
    num2 = oldnum1


"""
error:

2 1
1 1

"""