'''
Created on Nov 4, 2017

@author: AK
'''
#text to extract number
text = "X-DSPAM-Confidence:    0.8475"
#variable desiredNumb translates text to array index with corresponding values 
initialPos = text.find('0.8475')
#will print 23 as index value, ending pos is+1 for inclusion.
desiredNum = text[initialPos : 29]
# 0.8475 = pos 23-28
newFloat = float(desiredNum)
#print(initialPos)
#print(desiredNum)
print(newFloat)
