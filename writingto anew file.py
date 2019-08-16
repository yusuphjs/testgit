import os
import sys
import csv


for raw in data:
    newline = newline[2].lower()
    newline[2] = newline[2].lower()









try:
    infile_name = os.path.splitext(input_file)[0]
    infile.ext = os.path.splitext(input_file)[1]

    outfile = ("{}{}{}".format(infile_name,'_cleaned',input_ext))
    writer = csv.writer(open(outfile,'w'), delimiter =',')

except:
    print("you have a problem wiith your input_file")


for line in data :
    writer.writerow(line)
