#!/usr/bin/env python

import string,re,time

start=time.time()

pattern=re.compile(r'\t')



# change the directories for file1 and file2 in this script when you download
# the input .txt and .bed files from github

with open('/Users/vikasnatesh/Documents/files/MASTER_LIST_coordinates_uniq.bed','r') \
     as file1, open('/Users/vikasnatesh/Documents/files/132.annotated.consize.aa.txt','r') as file2, \
     open('/Users/vikasnatesh/Documents/files/SNP_output.txt','w') as SNP_output:

## file1 is the small master bed file, file 2 is the large 132.annotated.consize.aa.txt file, SNP_output is
    # the output file
    
    coords=file1.readlines()
    variants=file2.readlines()
    for i in coords:
        x=re.split(pattern,i)
        for j in variants:
            y=re.split(pattern,j)
            if x[0]==y[0]:
                if int(x[1])<=int(y[1])<int(x[2]):
                    SNP_output.write(x[4][:-1]+'\t'+j)
                


file1.close()
file2.close()
SNP_output.close()
end=time.time()
print end-start




# Below is a command-line implementation for the above process

##def usage():
##        print 'Usage: '+sys.argv[0]+' -c <coordinate file> -v <variant file> -o <output file name>'
##		
##		
##
##def main(argv):
##        try:   
##                opts,args=getopt.getopt(sys.argv[1:], "hc:v:o:",["help","coords=","variants=","output="])
##        	if not opts:
##			print "No options supplied"
##			usage()
##			sys.exit(2)
##	except getopt.GetoptError as err:
##                print str(err)
##                usage()
##                sys.exit(2)
##        for o,a in opts:
##                if o in ("-h", "--help"):
##                        usage()
##                        sys.exit()
##                elif o in ("-c", "--coords"):
##                        coords=a
##		elif o in ("-v", "--variants"):
##			varts=a
##                elif o in ("-o", "--output"):
##                        output=a
##                else:  
##                        assert False, "unhandled option"
##
##	print 'Coords file is ',coords
##	print 'Variants file is ',varts
##	print 'Output file is ',output
##
##	process(coords,varts,output)
##
##
##if __name__=="__main__":
##        main(sys.argv[1:])
##
##
