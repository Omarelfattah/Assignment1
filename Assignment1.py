#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_tuple = (1,2,3,4,5)
print(my_tuple)
my_list = list (my_tuple)
print(my_list)
my_list.insert(8,10)
print(my_list)
my_tuple_insert = tuple(my_list)
print(my_tuple_insert)
print(type(my_list))


# In[13]:


my_list = [1,2,3,4,5,6,7,8,9,10]
i = 0
Sum = 0
while i < len(my_list):
    Sum = Sum+my_list[i]
    i = i+1
else:
    print (Sum)
    


# In[15]:


my_list = [1,2,3,4,5,6,7,8,9,10]
i = 0
Mul = 1
while i < len(my_list):
    Mul = Mul*my_list[i]
    i = i+1
else:
    print (Mul)
    


# In[2]:


my_list = [1,2,3,4,5,6,7,8,9,10]
Smallest = my_list[0]
for number in my_list:
    if number < Smallest:
        Smallest = number
print (Smallest)


# In[3]:


heights = [100, 2, 300, 10, 11, 1000]
largest_number = heights[0]
for number in heights:
    if number > largest_number:
        largest_number = number
print(largest_number)


# In[8]:


my_list = ["Omar","Bilal","Esraa","Mohamed","Abdo","Abduallah","Ibrahim"]
i = 0
Num_Str = 0
while i < len(my_list):
    if type(my_list[i]) == str:
        Num_Str = Num_Str+1
    i = i+1
else:
    print(Num_Str)


# In[9]:


heights = [100, 2, 300, 10, 11, 1000]
new_list = list(heights)
print(heights)
print(new_list)


# In[14]:


thisset = {"apple","banana","cherry"}
thisset.remove("banana")
thisset.discard("cherry")
print(thisset)


# In[17]:


thisset1 = {"apple","banana","cherry",True,1,2}
thisset2 = {"apple","banana","cherry"}
print (thisset2.issubset(thisset1))


# In[22]:


thisset = {"apple","banana","cherry",True,1,2}
del thisset
print(thisset)


# In[23]:


thisset = {100, 2, 300, 10, 11, 1000}
my_list = list (thisset)
maximum  = max(my_list)
minimum  = min(my_list)
print ("Maximum:",maximum)
print("Minimum:",minimum)


# In[40]:


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(5)
y = thistuple.count(8)
print(x)
print(y)


# In[38]:


sub_names = ('English', 'Hindi', 'Mathematics', 'Computer Science', 'Physics', 'Chemistry')  
sub_codes = (2001, 2002, 2003, 2004, 2005, 2006)  
print("The values in sub_names are: ", sub_names)  
print("The values in sub_codes are: ", sub_codes)  
if len(sub_names) == len(sub_codes):  
    res_dict = {sub_names[i]: sub_codes[i] for i, _ in enumerate(sub_codes)}  
    print("The resultant dictionary is: ", res_dict) 


# In[39]:


l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))


# In[41]:


tuple_values = (1, 2, 'Python', 'Java', 23.4, 77, 10)    
print("The original tuple is: ", tuple_values)    
tuple_values = tuple(reversed(tuple_values))   
print("The reversed tuple is: ", tuple_values) 


# In[42]:


tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = dict(tuples)
print(result)


# In[43]:


l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])


# In[44]:


price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))

