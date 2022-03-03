#!/usr/bin/env python
# coding: utf-8

# ## 1. 테이블 만들기

# ※ 기존 SCRAP_label_merged_data.csv 를 이용하여 데이터 추출하기

# ## (1) split file

# ### 데이터 불러오기

# In[20]:


import os
import pandas as pd
import numpy as np


# In[13]:


src_table = pd.read_csv('../Tan/SCRAP_label_merged_data.csv')


# In[38]:


src_table[0:5]


# In[27]:


type(src_table)


# In[127]:


len(src_table)


# ### 컬럼 데이터 추출하기

# In[31]:


table = src_table[['ecg_id','AlsUnitNo','(실명)생년월일','RestingECG.TestDemographics.AcquisitionDate']]


# In[33]:


type(table)


# In[36]:


table.columns = ['ecg_id', 'patient_id', 'birth_date','ecg_date']


# In[37]:


table


# ## 2. 그룹 나누기

# In[88]:


254657//5


# In[89]:


254657%5


# In[90]:


group_1=table[0:50932]
group_2=table[50932:50932*2-1]
group_3=table[50932*2-1:50932*3-2]
group_4=table[50932*3-2:50932*4-3]
group_5=table[50932*4-3:254658]


# In[109]:


print(len(group_1), len(group_2), len(group_3), len(group_4), len(group_5))


# ### group_id 지정

# In[122]:


group1 = group_1.copy()
group1['group_id'] = 1

group1.head()


# In[123]:


group2 = group_2.copy()
group2['group_id'] = 2

group2.head()


# In[124]:


group3 = group_3.copy()
group3['group_id'] = 3

group3.head()


# In[125]:


group4 = group_4.copy()
group4['group_id'] = 4

group4.head()


# In[126]:


group5 = group_5.copy()
group5['group_id'] = 5

group5.head()


# ## 3. 각 그룹을 csv 파일로 저장하기

# In[128]:


group1.to_csv("group1.csv")


# In[129]:


group2.to_csv("group2.csv")


# In[130]:


group3.to_csv("group3.csv")


# In[131]:


group4.to_csv("group4.csv")


# In[132]:


group5.to_csv("group5.csv")

