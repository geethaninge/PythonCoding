import os,re
import matplotlib.pyplot as plt
import numpy as npy

root_dir = input('Enter root directory: ')
keyword = input('Enter keyword to search: ')

#search all files in given directory
def FileSearch(curr_dir, exp):
    results = {}
    count = 0
    matches=[]
    #list all files directory
    for filename in os.listdir(curr_dir):
        #check to make sure it is a file
        file_path = os.path.join(curr_dir,filename)
        if os.path.isfile(file_path):
            #open file, check for matches
            with open(file_path, 'r') as f:
                regx = re.compile(exp)
                for line in f:
                  matches = regx.findall(line)
                  for match in matches:
                      count += 1
                   #if exp in line: 
                       #count += 1
                   
    #store count into array for given subdir
        results[curr_dir] = count
    
    return results[curr_dir]
    
#initialize key:value array
output = {}
#recursively walk through all dirs & call FileSearch for each subdir
for root, dirs, files in os.walk(root_dir):
    output[root] = FileSearch(root, keyword)
#output array of all the data
print(output)


#output bar graph using matplotlib 
graph = npy.arange(len(output))
plt.bar(graph, output.values(), align='center', width=0.5)
plt.xticks(graph, output.keys())
plt.ylim(0, max(output.values())+2)

plt.title('Number of Files with Keyword')
plt.xlabel('Subdirectory Names')
plt.ylabel('Count Values')
plt.show()
plt.savefig()