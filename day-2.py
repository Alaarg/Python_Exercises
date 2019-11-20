# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:50:26 2019

@author: Ahmad ALaarg
"""

"""
1-Write a Python program to accept 2 numbers from the users and print the greatest
"""

#-----------------------------------------------------
"""
x = int(input('enter your first number '))
y = int(input('enter your sucend number '))
if (x > y):
    print(x)
else:
    print(y)
"""
#-----------------------------------------------------    
    
    
"""
2-Write a Python program to create the multiplication table for a specific number that is
accepted from the user
"""

#-----------------------------------------------------


"""
z = int(input ('plese enter the number : '))
i = 1
for i in range (10):
    print (z, '*' , i + 1  ,'=' ,  z  * (i + 1 ))
    
   """
#-----------------------------------------------------
   
   
"""
3. Write a Python program to construct the following pattern, using a nested for loop
"""
#-----------------------------------------------------
"""
i = 0

for i in range (6) :

    print('*'*i )
    
for i in range (6,0,-1) :

    print('*'*i )
"""
#-----------------------------------------------------
 # 4
"""
letters =["x","y","z","a","b","c"]
for i in letters :
        if i == "a" :
            continue
        elif i =="c" :
            break
        print(i)
"""
"""
output
 
x
y
z
b
"""
#-----------------------------------------------------

# 5 
"""
for x in range (12,25,3) :
    print (x)
"""
"""
output
12
15
18
21
24
"""
#-----------------------------------------------------
    
# 6 
"""
i = 1   
while i < 6 :
    print (i)
    if i == 3 :
        break
    i += 1 

"""    
"""
output
1
2
3 
"""

#-----------------------------------------------------

# 7 
"""
num = int(input("Enter a number :"))
total=0
for d in range(num):
    total=total+d+1

print("the total is : ",total)
 
"""

#-----------------------------------------------------

# 8
"""
num = int(input("the num : "))
 print ("even") if(num%2==0) else print ("odd")
"""
#-----------------------------------------------------

#9
"""
for a in range(1,10,1):
     for b in range(9-a):
         print (" ",end="")  
     for c in range(0,a,1):
         print (c+1,end="")
     for d in range(a-1,0,-1):
         print (d,end="")
     print()
for a in range(9,0,-1):
     for b in range(10-a):
         print (" ",end="")    
     for c in range(1,a,1):
         print (c,end="")
     for d in range(a-1,1,-1):
         print (d-1,end="")
     print()

"""

#-----------------------------------------------------

#10
"""
while True:
     try:
         n = input("Please enter an integer number : ")
         n = int(n)
         break
     except ValueError:
         print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")    
 
"""

#-----------------------------------------------------
#11

try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b = ",b)
except(ZeroDivisionError,NameError):
    print("\nError occurred and Handled")
       
      
#-----------------------------------------------------
#-----------------------------------------------------






















    