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
for i in range(0,5):
  # loop 5
  for j in range(0,4):
    # loop 4
    for k in range(0,3):
    # loop 3
      for u in range(0,2):
          # loop 2
          num4 = num5
          num5 = oldnum4
          update()
          print 'in loop 2 :'
          shownums()
      num3 = num5
      num4 = oldnum3
      num5 = oldnum4
      update()
      print 'in loop 3 :'
      shownums()
    num2 = num5
    num3 = oldnum2
    num4 = oldnum3
    num5 = oldnum4
    update()
    print 'in loop 4 :'
    shownums()
  num1 = num5
  num2 = oldnum1
  num3 = oldnum2
  num4 = oldnum3
  num5 = oldnum4
  update()
  print 'in loop 5 :'
  shownums()
