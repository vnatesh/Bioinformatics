#!/usr/bin/env python
import re,string,time
import numpy as np



# open('/Users/vikasnatesh/Documents/Sachin_test.txt','r') 
# open('/Users/vikasnatesh/Downloads/SAM-COOH_Contact.txt','r')
# open('/Users/vikasnatesh/Downloads/SAM-CH3_Contact.txt','r')

start=time.time()

with open('/Users/vikasnatesh/Downloads/SAM-CH3_Contact.txt','r') as file1, \
     open('/Users/vikasnatesh/Documents/Sachin_test_output_mod.txt','w') as file2:
    entries = re.split('\n+', file1.read()) # regex split the whole file by the
                                            # newline character
    total=1461440  # 26240#36 set total number of data pts. i.e. numframes * 40
    numframes=36536  # 656 #12 set number of frames (set to 54800)
    allData = np.empty((0,numframes-2), int) # create an empty array (row) of
                                             # length numframes-2 so we can append
                                             # to it later to create the allData matrix
    t=0.75
 #   i=0
    i=9  # we set i=9 instead of 0 because the first 9 rows, by default
         # are useless text and file information
         # this next loop is complicated...
    while i<len(entries):
        try:
            if entries[i]==entries[i+total]==entries[i+2*total]==entries[i+3*total]==entries[i+4*total]:
                a=np.array([int(g[-2:]) for g in entries[i+2:i+numframes]])
                b=np.array([int(g[-2:]) for g in entries[i+2+total:i+total+numframes]])
                c=np.array([int(g[-2:]) for g in entries[i+2+(2*total):i+(2*total)+numframes]])
                d=np.array([int(g[-2:]) for g in entries[i+2+(3*total):i+(3*total)+numframes]])
                e=np.array([int(g[-2:]) for g in entries[i+2+(4*total):i+(4*total)+numframes]])
                allData = np.concatenate((allData, [(a+b+c+d+e)/5.0]))
## TEST               allData = np.concatenate((allData, [(a+b+c)/3.0]))                  
## TEST                average=(a+b+c+d+e)/5.0
## TEST                print average
            i=i+numframes
        except IndexError:
            break

    for i in allData:
        compare= i >= 0.25*max(i)
        file2.write(str(sum(compare.astype(int))/float(len(i)))+'\n')



file1.close()
file2.close()
end=time.time()
print end-start


#********************************* TEST CODE **********************************

##    for i in allData:
##        file2.write(str(sum([1 for x in i if x>=max(i)*t]) / float(len(i))) +'\n')
##        compare=greater_equal(i,max_i)
        

#print allData


# The good thing about the file we are dealing with is that it has a definitve
# structure...i.e., there are 40 AA's, 5 groups, and 654 frames...we can exploit
# these numbers to accurately process the file


##    for i in xrange(len(entries)):
##        if entries[i]=='freeSelLabel ASP 1==name C12':
##            a.append(entries[i+2:i+12])

##numframes=10
##i=0             
##while entries[i]==entries[i+numframes+2]:
##    a.append(entries[i+2:i+numframes+2])
##

##while i<len(entries):
##    if entries[i]==entries[i+12]
##             
##    else: i=i+numframes
