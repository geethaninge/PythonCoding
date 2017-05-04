'''
x^y x pow y if x=2 and y =3 then output should be 8 x**y
'''
def power():
  x= int(input("enter base number:"))
  y =int(input("enter power number:"))
  xpowy = x**y 
  print ("{} pow {} is :{}".format(x,y,xpowy))
  
power()  