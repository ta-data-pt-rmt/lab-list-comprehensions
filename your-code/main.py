#!/usr/bin/env python
# coding: utf-8

# # List Comprehensions Lab
# 
# Complete the following set of exercises to solidify your knowledge of list comprehensions.

# In[ ]:


import os
import numpy as np
import pandas as pd


# ### 1. Use a list comprehension to create and print a list of consecutive integers starting with 1 and ending with 50.

# In[4]:


consecutive_integers = [i for i in range(1, 51)]

# Print the list
print(consecutive_integers)


# ### 2. Use a list comprehension to create and print a list of even numbers starting with 2 and ending with 200.

# In[5]:


even_numbers = [i for i in range(2, 201) if i % 2 == 0]

# Print the list
print(even_numbers)


# ## 3. Use a list comprehension to create and print a list containing all elements of the 10 x 4 list below.
# 

# In[1]:


a = [[0.84062117, 0.48006452, 0.7876326 , 0.77109654],
       [0.44409793, 0.09014516, 0.81835917, 0.87645456],
       [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
       [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
       [0.17003563, 0.46843998, 0.92796258, 0.69814654],
       [0.41290051, 0.19561071, 0.16284783, 0.97016248],
       [0.71725408, 0.87702738, 0.31244595, 0.76615487],
       [0.20754036, 0.57871812, 0.07214068, 0.40356048],
       [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
       [0.80930099, 0.50962849, 0.94555126, 0.33364763]]


# In[6]:


a = [
    [0.84062117, 0.48006452, 0.7876326 , 0.77109654],
    [0.44409793, 0.09014516, 0.81835917, 0.87645456],
    [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
    [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
    [0.17003563, 0.46843998, 0.92796258, 0.69814654],
    [0.41290051, 0.19561071, 0.16284783, 0.97016248],
    [0.71725408, 0.87702738, 0.31244595, 0.76615487],
    [0.20754036, 0.57871812, 0.07214068, 0.40356048],
    [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
    [0.80930099, 0.50962849, 0.94555126, 0.33364763]
]

# Flatten the 10 x 4 list using list comprehension
flattened_list = [item for sublist in a for item in sublist]

# Print the flattened list
print(flattened_list)


# ### 4. Add a condition to the list comprehension above so that only values greater than or equal to 0.5 are printed.

# In[7]:


# The given 10 x 4 list
a = [
    [0.84062117, 0.48006452, 0.7876326 , 0.77109654],
    [0.44409793, 0.09014516, 0.81835917, 0.87645456],
    [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
    [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
    [0.17003563, 0.46843998, 0.92796258, 0.69814654],
    [0.41290051, 0.19561071, 0.16284783, 0.97016248],
    [0.71725408, 0.87702738, 0.31244595, 0.76615487],
    [0.20754036, 0.57871812, 0.07214068, 0.40356048],
    [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
    [0.80930099, 0.50962849, 0.94555126, 0.33364763]
]

# Flatten the list and filter values greater than or equal to 0.5
filtered_list = [item for sublist in a for item in sublist if item >= 0.5]

# Print the filtered list
print(filtered_list)


# ### 5. Use a list comprehension to create and print a list containing all elements of the 5 x 2 x 3 list below.

# In[3]:


b = [[[0.55867166, 0.06210792, 0.08147297],
        [0.82579068, 0.91512478, 0.06833034]],

       [[0.05440634, 0.65857693, 0.30296619],
        [0.06769833, 0.96031863, 0.51293743]],

       [[0.09143215, 0.71893382, 0.45850679],
        [0.58256464, 0.59005654, 0.56266457]],

       [[0.71600294, 0.87392666, 0.11434044],
        [0.8694668 , 0.65669313, 0.10708681]],

       [[0.07529684, 0.46470767, 0.47984544],
        [0.65368638, 0.14901286, 0.23760688]]]


# In[9]:


# The given 5 x 2 x 3 list
b = [
    [
        [0.55867166, 0.06210792, 0.08147297],
        [0.82579068, 0.91512478, 0.06833034]
    ],
    [
        [0.05440634, 0.65857693, 0.30296619],
        [0.06769833, 0.96031863, 0.51293743]
    ],
    [
        [0.09143215, 0.71893382, 0.45850679],
        [0.58256464, 0.59005654, 0.56266457]
    ],
    [
        [0.71600294, 0.87392666, 0.11434044],
        [0.8694668 , 0.65669313, 0.10708681]
    ],
    [
        [0.07529684, 0.46470767, 0.47984544],
        [0.65368638, 0.14901286, 0.23760688]
    ]
]

# Flatten the 5 x 2 x 3 list using list comprehension
flattened_list = [item for sublist1 in b for sublist2 in sublist1 for item in sublist2]

# Print the flattened list
print(flattened_list)


# ### 6. Add a condition to the list comprehension above so that the last value in each sublist is printed, but only if it is less than or equal to 0.5.

# In[8]:


# The given 10 x 4 list
a = [
    [0.84062117, 0.48006452, 0.7876326 , 0.77109654],
    [0.44409793, 0.09014516, 0.81835917, 0.87645456],
    [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
    [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
    [0.17003563, 0.46843998, 0.92796258, 0.69814654],
    [0.41290051, 0.19561071, 0.16284783, 0.97016248],
    [0.71725408, 0.87702738, 0.31244595, 0.76615487],
    [0.20754036, 0.57871812, 0.07214068, 0.40356048],
    [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
    [0.80930099, 0.50962849, 0.94555126, 0.33364763]
]

# Flatten the list and filter values greater than or equal to 0.5
filtered_list = [item for sublist in a for item in sublist if item <= 0.5]

# Print the filtered list
print(filtered_list)


# ### 7. (optional - revisit once we cover this material)  Use a list comprehension to select and print the names of all CSV files in the */data* directory.

# In[ ]:





# ### 8. (optional - revisit once we cover this material)  Use a list comprehension and the Pandas `read_csv` and `concat` methods to read all CSV files in the */data* directory and combine them into a single data frame. Display the top 10 rows of the resulting data frame.

# In[ ]:





# ### 9. (optional - revisit once we cover this material) Use a list comprehension to select and print the column numbers for columns from the data set whose median is less than 0.48.

# In[ ]:





# ### 10. (optional - revisit once we cover this material)  Use a list comprehension to add a new column (20) to the data frame whose values are the values in column 19 minus 0.1. Display the top 10 rows of the resulting data frame.

# In[ ]:





# ### 11. (optional - revisit once we cover this material)  Use a list comprehension to extract and print all values from the data set that are between 0.7 and 0.75.

# In[ ]:




