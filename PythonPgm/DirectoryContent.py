'''
Created on Apr 8, 2017

@author: Geetha
'''
'''
import os
class DirectoryContent():
'''
'''
   This function takes the name of a directory 
   and prints out the paths files within that 
   directory as well as any files contained in 
   contained directories. 
'''
def print_directory_contents(sPath):
  import os
  for sChild in os.listdir(sPath):
    sChildPath = os.path.join(sPath,sChild)
    if os.path.isdir(sChildPath):
      print_directory_contents(sChildPath)
    else:
      print(sChildPath)   
        							

print_directory_contents("C:\My Dude\KPSC_diploma_lecturer")