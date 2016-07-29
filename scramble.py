#!/usr/bin/python2.7

import sys

num1  = int(sys.argv[0])
oldnum1 = num1
num2  = int(sys.argv[1])
oldnum2 = num2
num3  = int(sys.argv[2])
oldnum3 = num3
num4 = int(sys.argv[3])
oldnum4 = num4
num5 = int(sys.argv[4])
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
          shownums()
      num3 = num1
      num2 = oldnum3
      num1 = oldnum2
      update()
      shownums()
    num4 = num1
    num3 = oldnum4
    num2 = oldnum3
    num1 = oldnum2
    update()
    shownums()
  num5 = num1
  num4 = oldnum5
  num3 = oldnum4
  num2 = oldnum3
  num1 = oldnum2
  update()
  shownums()
