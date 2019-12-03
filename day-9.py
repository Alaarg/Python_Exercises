# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:32:25 2019

@author: Ahmad ALaarg
"""



"""
import statistics as st
X = [3,1.5,4.5,6.75,2.25, 5.75,2.25]

If X = [3,1.5,4.5,6.75,2.25, 5.75,2.25], find :
print(st.mean00 )
print(st.harmonic_mean00 )
print(st.median00 ) 
print(st.median_low00 ) 
print(st.median.high00 ) 
print(st.median.grouped00 ) 
print(st.mode00 ) 
print(st.pstdev00 ) 
print(st.pvariance00 ) 
print(st.stdev00 ) 
print(st.variance00 )
  
    
import random
print( random.random() )
print ( random.randrange(100) )
print ( random.choice(['Jordan', 'USA', 'UK']) )
print ( random.sample(range(100), 5) )
print ( random.choice('abcdefghij') )
items = [11, 12, 30, 14, 35, 66, 17]
random.shuffle(items)
print( items )
print ( random.randint(10, 20) )
print ( random.randrange(0, 101, 2) )
print  ( random.uniform(1, 100))
print()

 """ 
 
from PIL import Image
im = Image.open('me.jpg')
print(im.format, im.size, im.mode)
#im.show()


 
size =(128, 128)
saved = "me.jpg"
try :
    im = Image.open("me.jpg")
except :
    print ("unable to load image ")
     
im.thumbnail(size)
im.save(saved)
#im.show()

from PIL import Image
from PIL import ImageDraw
im=Image.open('me.jpg')
draw=ImageDraw.Draw(im)
draw.line((0,0)+im.size, fill = (225,225,225))
draw.line((0,im.size[1], im.size[0],0),fill=(225,225,225))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2+20),'Asma',fill=(225,225,0))
draw.text((im.size[0]/2-im.size[0]/2,im.size[1]/2-60),'Image',fill=(225,225,0))
im.show()




 
 
 
     
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 