#!/usr/bin/python
oldnum1 = num1  = int(raw_input('what is number 1?'))
oldnum2 = num2  = int(raw_input('what is number 2?'))
oldnum3 = num3  = int(raw_input('what is number 3?'))
oldnum4 = num4 = int(raw_input('what is number 4?'))
numbers = [num1,num2,num3,num4]

#the functions
def update():
  oldnum1 = num1
  oldnum2 = num2
  oldnum3 = num3
  oldnum4 = num4
  num1 = numbers[0]
  num2 = numbers[1]
  num3 = numbers[2]
  num4 = numbers[3]

