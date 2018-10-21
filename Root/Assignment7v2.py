'''
Created on Dec 8, 2017

@author: Anthony Kang
'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
#values for float average
denominator = float(0)
numerator = float(0)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    '''.find()'s value is index location
    initial=line.find('0') = [20]
    Upon every iteration
    find string values representing numbers
    convert string to float
    run total for numerator/denominator
    '''    
    numToAdd=line[20:26]
    #convert string to float value
    floatStr=float(numToAdd)
    denominator=float(denominator+1)
    numerator += floatStr
    float(numToAdd)
    average = float(numerator/denominator)
#using round to specify to desired accuracy in decimal place (12)
print('Average spam confidence:',round(average,12))

