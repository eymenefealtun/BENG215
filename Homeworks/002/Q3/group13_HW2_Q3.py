import numpy as np

file =open("../Resources/gene_expression.txt","r")
m = file.readlines()
mfirst = m[0]
m.pop(0)#The first line was all strings that defines the values. Therefore we removed that to be able to work with values.
list_of_values=[]
table = []
for i in m:
    #We created 6 variables to hold the values. The float values are in a, b, c, d and e variables. But e values were ending with \n. Therefore we removed it by using .strip() function.
    q,a,b,c,d,e=i.split("\t")
    table.append(q)
    e=e.strip()
    list_of_values.append([float(a),float(b),float(c),float(d),float(e)])

list_of_values_mean = []
standardized = []
#print("list: ",list_of_values)

def standardization(list_numbers):
    #We calculated the average and std for the all rows.
    meanX=np.mean(list_numbers)
    stdX=np.std(list_numbers)
    rowlist=[]
    for i in list_numbers:
        z = (i-meanX)/stdX
        n = round(z,4)
        rowlist.append(n)
    return rowlist#We returned the standardized list.

for i in list_of_values:
    row = standardization(i)
    standardized.append(row)#We standardized all the rows by using the function I've written
#We created an empty list to hold all the elements of the list named standardized
table = []
for i in standardized:
    table.append(i)
for i in range(len(m)):
    q,a,b,c,d,e = m[i].split("\t")
    q+=": " #at this time we used the q variable to create a list and a string that looks like a table.
    table[i].insert(0,q) #We concencenated the q variable with the nested list's elements. now it looks like this(['abcd: ', 2323, 1212, 1212, 5212, 1213] this is an example)
#We created a string to write to a file so it looks clean on the text file.
filestr = ""
for i in table:
    filestr+=str(i)
    filestr+="\n\n" #We added blank spaces.
filestr =filestr.replace('[', '')
filestr = filestr.replace(']', '')

newfile = open("../Q3/standardized_table.txt","w")
newfile.write(filestr) #We've written the string to a new file.