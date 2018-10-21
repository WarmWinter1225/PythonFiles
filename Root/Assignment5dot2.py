'''
Created on Oct 20, 2017

@author: AK
'''

#None is equivalent to null
smallest = None
largest = None
number = None

while True:
          
    number = input("Enter a number: ")
    if number == 'done': break
                 
    try:
        x = int(number)
        if smallest is None and largest is None:
            smallest = x
            largest = x
        if x < smallest:
            smallest = x
        elif x >=  largest:
            largest = x
    except:
        print('Invalid input')    
        continue
        
print("Maximum is", largest)
print("Minimum is", smallest)
