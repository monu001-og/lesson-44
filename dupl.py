#creating the output file
outputFile = open("UpdatedFile,txt",'w')

#reading the input file
inputFile = open('Repeated.txt',"r")

#holds lines already file
lines_seen_so_far =set()
print("Eliminatinating duplicate lines......")
#iterating each line in the file
for line in inputFile:
    
    #checking if line is uniquee if 
     if line not in lines_seen_so_far:
         
              #write unique lines in out[ut file
            outputFile.write(line)
        
            #adds uniue lines to lines_seen_so_far
            lines_seen_so_far.add(line)
        

#closing the file
inputFile.close()
outputFile.close()
