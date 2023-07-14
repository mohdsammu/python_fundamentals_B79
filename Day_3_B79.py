#!/usr/bin/env python
# coding: utf-8

# # continuation with string datatypes

# In[1]:


#understanding the concept of  f strings
firstname = 'praveen'
lastname = 'kumar'


# In[2]:


#i want the fullname...?


# In[ ]:


f strings :


# In[ ]:


f "custom message, {place_holder-1}{place_holder 2}......{place_holder_n}"


# In[10]:


fullname = f"{firstname}{lastname}"


# In[11]:


print(fullname)


# In[17]:


message= f"keep up the goood work,{fullname}"
print(message)


# 

# In[ ]:


#to capital first letter


# In[18]:


message= f"keep up the good work,{fullname.title()}"
print(message)


# # adding white spaces to strings :

# 

# In[19]:


print("fav_lang:\npython\njava\nc\nc++\nswift\njavascript")


# In[20]:


print("Fav_lang:\n\tpython\n\tjava\n\tc\n\tc++\n\tswift\n\tjavascript")


# # removing whitespaces from strings

# In[27]:


language=' python'
print(language)


# In[26]:


language2='python  ' 
print(language2)


# In[29]:


language3=  ' python'
print(language3)


# In[30]:


language.lstrip()


# In[31]:


language2.rstrip()


# In[32]:


language3.strip()


# In[ ]:




