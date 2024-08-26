#number of rows in the pattern 
rows = 5

#outer loop for each row  
for i in range(1,rows+1):
#inner loop for each column in the current row
    for j in range (1,i+1):
        print(" * ",end=" ")
    print() #move to the next line after each row