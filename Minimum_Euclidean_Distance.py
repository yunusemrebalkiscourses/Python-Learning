#!/usr/bin/env python
# coding: utf-8

# In[11]:


import math
points = [(2,3), (1,6)]
print(points)


# In[12]:


def euclideanDistance(point1, point2) :
    x, y = point1
    a, b = point2
    distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    return distance
    


# In[13]:


distances = []
for i in range(len(points)-1):
    res = euclideanDistance(points[i],points[i+1])
    distances.append(res)
min(distances)


# In[ ]:




