def main():
  with open("file2.txt","w+") as myFile:
    for i in range(1,10):
      myFile.write("This is line  : {} \n".format(i))
  with open("file1.txt","a+") as f:
    for i in range(2):
      f.write("appended line :{}\n".format(i+1))
  with open("file2.txt","r") as f1:
    if f1.mode == 'r':
      contents = f1.read();
      print(contents )


if __name__ == "__main__":
  main()      