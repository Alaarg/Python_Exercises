# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:37:20 2019

@author: Ahmad ALaarg
"""


"""
s1= 'hello orange academy'

print ( s1 )
print ( s1[0 ])
print ( s1[ 2])
print ( s1[2:10])
print ( s1[5:])
print ( s1 * 2)
print ( s1.capitalize ())
print ( s1.upper ())
print (s1.center(20 ))
print (s1.replace('Orange', 'Amman '))
print ('   world    strip()')
s2='#'.join([' hello','Orange'])
print(s2)
"""

#-----------------
#Lists Practice
"""
Assume the following list list 1 1,20 1,0,1000 ],

1 append to list 1 the following list 2 ( list 2 23,546 ] )

2 find len , min, max, sum, sorted of the updated list 1 and print the results

3 Apply sort and pop and print the list
"""

# Lists Practice
"""
list1 = [1,20,-1,0,1000]
list2 = [23,5460]
list1.extend(list2)print (list1)
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))
print(sorted(list1))
"""

#Tuples

"""
my_list =['a','b']
t1 = ("Apple ",) # Note , is for one item
t2 = t1 + (1,2,3 ) + tuple (my_list)
print(t2)
print(t2 [0])
print(t2 [1:4])

"""

#Sets
"""
s1 = { 1,2,3,4,5,6}

s2 ={ 2,4,6 }
print ( s1 | s2 ) # OR
print ( s1 & s2 ) # AND
print ( s1 - s2 ) # SUPTRACT
print ( s1 ^ s2 ) # OR # in s 1 or s 2 but not in both
"""

#Dictionary

info = {
  "firstName": "Ahmad",
  "lastName": "Alaarg",
  "year": 1996
}
print(info)
x = info["year"]
print(x)


for x in info :
    print (x)
    print (info[x])























