#Author: John Jennings
#Date: December 10, 2017

#----------INPUT FILE INFO----------
fileIn = raw_input("Input file: ")
infile = file(fileIn + ".csv")
#-----------------------------------
#----------OUTPUT FILE INFO----------
fileOut = raw_input("Output file: ")
outfile = open(fileOut + ".sql", 'a')
#-----------------------------------
fileInfo = [] #array for file content
#-----------------------------------
print "Using '", fileIn, "' to create '", fileOut +"'"
#output note for user to ensure fileIn is being used to create
#SQL script for fileOut

for line in infile:
    fileInfo.append(line.replace("=","").strip("\n"))
del fileInfo[0]
#-----------------------------

for line in fileInfo:
    outfile.write('INSERT INTO * VALUES (' + line + ');\n') #DEFAULT FOR mySQL INTEGRATION
    #outfile.write(line)
#print '"'+info[0]+'", "'+info[1]+'", "'+info[2]+'", "'+ info[3]+'"'
print 'New file created!\nDone...'
outfile.close() #Closes and ends program
