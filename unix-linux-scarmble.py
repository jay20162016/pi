#!/usr/bin/python2.7

# do not execute using the python command, add the execute chmod using 'chmod a+x ./scramble then execute using the ./unix-linux-scramble.py command , both commands in this file's directory/folder

import sys
from __builtin__ import raw_input

print(sys.argv)


try:
  num1  = sys.argv[1]
else:
  num1 = raw_input('what is number 1?')
oldnum1 = num1
try:
  num2  = sys.argv[2]
except:
  num2 = raw_input('what is number 2?')
oldnum2 = num2
try:
  num3  = sys.argv[3]
except:
  num3 = raw_input('what is number 3?')
oldnum3 = num3
try:
  num4 = sys.argv[4]
except:
  num4 = raw_input('what is number 4?')
oldnum4 = num4
try:
  num5 = sys.argv[5]
except:
  num5 = raw_input('what is number 5?')
oldnum5 = num5

#the functions
def shownums():
  print str(num1) + ' ' + str(num2) + ' ' + str(num3) + ' ' + str(num4) + ' ' + str(num5)
def update():
  oldnum1 = num1
  oldnum2 = num2
  oldnum3 = num3
  oldnum4 = num4
  oldnum5 = num5
#the nested loops
for i in range(1,6):
  for j in range(1,5):
    for k in range(1,4):
      for u in range(1,3):
          num2 = num1
          num1 = oldnum2
          update()
          print 'in loop 2 :'
          shownums()
      num3 = num1
      num2 = oldnum3
      num1 = oldnum2
      update()
      print 'in loop 3 :'
      shownums()
    num4 = num1
    num3 = oldnum4
    num2 = oldnum3
    num1 = oldnum2
    update()
    print 'in loop 4 :'
    shownums()
  num5 = num1
  num4 = oldnum5
  num3 = oldnum4
  num2 = oldnum3
  num1 = oldnum2
  update()
  print 'in loop  5 :'
  shownums()
