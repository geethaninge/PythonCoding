'''
Created on Apr 9, 2017

@author: Geetha
'''
def palindrome():
  sname = input("enter a string to check for palindrome : ")
  #if sname == sname[::-1]:
  #sname = input("enter a number to check for palindrome : ")   
  #if int(sname) == int(sname[::-1]):
  if list(sname) == list(reversed(sname)):
    print("{} is palindrome".format(sname))
  else:
    print(" {} is not a palindrome".format(sname))
      
palindrome()          