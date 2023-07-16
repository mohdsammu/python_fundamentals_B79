#!/usr/bin/env python
# coding: utf-8

# # Introduction to list datatype

# In[2]:


students = ['vinith','ramya','ayesha','sara','david','naveen','ahmed']#0,1,2,3,4,5,6....


# In[3]:


print(students)


# In[4]:


type(students)


# # introduction to indexing

# In[5]:


#i want to access ramya name on the output ....?


# In[6]:


print(students[1])


# In[7]:


print(students[1].title())


# In[8]:


print(students[3].title())


# In[9]:


#req: i want add kunal in the above list 


# In[10]:


students.append('kunal')


# In[11]:


print(students)


# In[12]:


students.append('kalyani')


# In[13]:


print(students)


# In[14]:


#i want to add firdous to the 2nd index postion


# In[16]:


students.insert(2,'firdous')


# In[17]:


print(students)


# In[18]:


print(students[2].title())


# In[19]:


#i want to change the name from vinoth to vani


# In[20]:


students[0]='vani'


# In[21]:


print(students)


# In[22]:


#deleting


# In[23]:


x = students.pop()


# In[24]:


print(students)


# In[25]:


print(x)


# In[26]:


#req: i want to delete ramya.....


# In[27]:


y = students.pop(1)


# In[28]:


print(students)


# In[29]:


print(y)


# In[30]:


#req : to delete vani from the above


# In[31]:


print(students)


# In[40]:


del students[0]


# In[41]:


print(students)


# In[ ]:




