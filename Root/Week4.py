'''
Created on Oct 15, 2017

@author: AK
'''
#generate function to calculate pay using h,r for hours and rate

def computePay(h,r):
    pay = float(h*r)
    if h > 40:
        pay = ((h-40)*(r*1.5) + 40*r)
        return pay
    elif h <= 40:        
        return pay
h = input("Enter hours")
hours = float(h)
r = input("Enter pay rate")
rate = float(r)

print("Pay: ", computePay(hours,rate))