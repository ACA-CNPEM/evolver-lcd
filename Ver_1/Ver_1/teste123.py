#!/usr/bin/env python
# coding: utf-8

# ### TEMPERATURA

# In[1]:


from PyQt5 import QtWidgets 
from PyQt5 import QtCore
import random
import redis
r = redis.Redis(host="192.168.0.55")
import pandas as pd
df = pd.read_excel('Temperaturas.xlsx')
xl = pd.ExcelFile("Temperaturas.xlsx")


# In[2]:


verde = "rgb(14, 191, 110);\n"
amarelo = "rgb(255, 255, 0);\n"
vermelho = "rgb(255, 63, 68);\n"


# In[3]:


CORES = [verde, amarelo, vermelho]
#CORES = ["background-color: rgb(14, 191, 110);", "background-color: rgb(255, 255, 0);", "background-color: rgb(255, 63, 68);"]


# In[4]:


display(df)


# In[5]:


SST = df["SST"].values
EI = df["ERRO INFERIOR"].values
LI = df["LIMITE INFERIOR"].values
LS = df["LIMITE SUPERIOR"].values
ES = df["ERRO SUPERIOR"].values


# In[6]:


SST[0] = int(r.get("temp_ss_0"))
SST[1] = int(r.get("temp_ss_1"))
SST[2] = int(r.get("temp_ss_2"))
SST[3] = int(r.get("temp_ss_3"))
SST[4] = int(r.get("temp_ss_4"))
SST[5] = int(r.get("temp_ss_5"))
SST[6] = int(r.get("temp_ss_6"))
SST[7] = int(r.get("temp_ss_7"))
SST[8] = int(r.get("temp_ss_8"))
SST[9] = int(r.get("temp_ss_9"))
SST[10] = int(r.get("temp_ss_10"))
SST[11] = int(r.get("temp_ss_11"))
SST[12] = int(r.get("temp_ss_12"))
SST[13] = int(r.get("temp_ss_13"))
SST[14] = int(r.get("temp_ss_14"))
SST[15] = int(r.get("temp_ss_15"))


# In[7]:


# se a temperatura da ss1 for menor ou igual ao erro inferior, cor igual a vermelho
if SST[0] <= EI[0]:
    cor_sst0 = vermelho
    
if SST[0] <= LI[0] and SST[0] > EI[0]:
    cor_sst0 = amarelo
    
if SST[0] > LI[0] and SST[0] <= LS[0]:
    cor_sst0 = verde

if SST[0] <= ES[0] and SST[0] > LS[0]:
    cor_sst0 = amarelo

if SST[0] >= ES[0]:
    cor_sst0 = vermelho
print(SST[0])
print(cor_sst0)


# In[8]:


if SST[1] <= EI[1]:
    cor_sst1 = vermelho
    
if SST[1] <= LI[1] and SST[1] > EI[1]:
    cor_sst1 = amarelo
    
if SST[1] > LI[1] and SST[1] <= LS[1]:
    cor_sst1 = verde

if SST[1] <= ES[1] and SST[1] > LS[1]:
    cor_sst1 = amarelo

if SST[1] >= ES[1]:
    cor_sst1 = vermelho
print(SST[1])
print(cor_sst1)


# In[9]:


if SST[2] <= EI[2]:
    cor_sst2 = vermelho
    
if SST[2] <= LI[2] and SST[2] > EI[2]:
    cor_sst2 = amarelo
    
if SST[2] > LI[2] and SST[2] <= LS[2]:
    cor_sst2 = verde

if SST[2] <= ES[2] and SST[2] > LS[2]:
    cor_sst2 = amarelo

if SST[2] >= ES[2]:
    cor_sst2 = vermelho
print(SST[2])
print(cor_sst2)


# In[10]:


if SST[3] <= EI[3]:
    cor_sst3 = vermelho
    
if SST[3] <= LI[3] and SST[3] > EI[3]:
    cor_sst3 = amarelo
    
if SST[3] > LI[3] and SST[3] <= LS[3]:
    cor_sst3 = verde

if SST[3] <= ES[3] and SST[3] > LS[3]:
    cor_sst3 = amarelo

if SST[3] >= ES[3]:
    cor_sst3 = vermelho
print(SST[3])
print(cor_sst3)


# In[11]:


if SST[4] <= EI[4]:
    cor_sst4 = vermelho
    
if SST[4] <= LI[4] and SST[4] > EI[4]:
    cor_sst4 = amarelo
    
if SST[4] > LI[4] and SST[4] <= LS[4]:
    cor_sst4 = verde

if SST[4] <= ES[4] and SST[4] > LS[4]:
    cor_sst4 = amarelo

if SST[4] >= ES[4]:
    cor_sst4 = vermelho
print(SST[4])
print(cor_sst4)


# In[12]:


if SST[5] <= EI[5]:
    cor_sst5 = vermelho
    
if SST[5] <= LI[5] and SST[5] > EI[5]:
    cor_sst5 = amarelo
    
if SST[5] > LI[5] and SST[5] <= LS[5]:
    cor_sst5 = verde

if SST[5] <= ES[5] and SST[5] > LS[5]:
    cor_sst5 = amarelo

if SST[5] >= ES[5]:
    cor_sst5 = vermelho
print(SST[5])
print(cor_sst5)


# In[13]:


if SST[6] <= EI[6]:
    cor_sst6 = vermelho
    
if SST[6] <= LI[6] and SST[6] > EI[6]:
    cor_sst6 = amarelo
    
if SST[6] > LI[6] and SST[6] <= LS[6]:
    cor_sst6 = verde

if SST[6] <= ES[6] and SST[6] > LS[6]:
    cor_sst6 = amarelo

if SST[6] >= ES[6]:
    cor_sst6 = vermelho
print(SST[6])
print(cor_sst6)


# In[14]:


if SST[7] <= EI[7]:
    cor_sst7 = vermelho
    
if SST[7] <= LI[7] and SST[7] > EI[7]:
    cor_sst7 = amarelo
    
if SST[7] > LI[7] and SST[7] <= LS[7]:
    cor_sst7 = verde

if SST[7] <= ES[7] and SST[7] > LS[7]:
    cor_sst7 = amarelo

if SST[7] >= ES[7]:
    cor_sst7 = vermelho
print(SST[7])
print(cor_sst7)


# In[15]:


if SST[8] <= EI[8]:
    cor_sst8 = vermelho
    
if SST[8] <= LI[8] and SST[8] > EI[8]:
    cor_sst8 = amarelo
    
if SST[8] > LI[8] and SST[8] <= LS[8]:
    cor_sst8 = verde

if SST[8] <= ES[8] and SST[8] > LS[8]:
    cor_sst8 = amarelo

if SST[8] >= ES[8]:
    cor_sst8 = vermelho
print(SST[8])
print(cor_sst8)


# In[16]:


if SST[9] <= EI[9]:
    cor_sst9 = vermelho
    
if SST[9] <= LI[9] and SST[9] > EI[9]:
    cor_sst9 = amarelo
    
if SST[9] > LI[9] and SST[9] <= LS[9]:
    cor_sst9 = verde

if SST[9] <= ES[9] and SST[9] > LS[9]:
    cor_sst9 = amarelo

if SST[9] >= ES[9]:
    cor_sst9 = vermelho
print(SST[9])
print(cor_sst9)


# In[17]:


if SST[10] <= EI[10]:
    cor_sst10 = vermelho
    
if SST[10] <= LI[10] and SST[10] > EI[10]:
    cor_sst10 = amarelo
    
if SST[10] > LI[10] and SST[10] <= LS[10]:
    cor_sst10 = verde

if SST[10] <= ES[10] and SST[10] > LS[10]:
    cor_sst10 = amarelo

if SST[10] >= ES[10]:
    cor_sst10 = vermelho
print(SST[10])
print(cor_sst10)


# In[18]:


if SST[11] <= EI[11]:
    cor_sst11 = vermelho
    
if SST[11] <= LI[11] and SST[11] > EI[11]:
    cor_sst11 = amarelo
    
if SST[11] > LI[11] and SST[11] <= LS[11]:
    cor_sst11 = verde

if SST[11] <= ES[11] and SST[11] > LS[11]:
    cor_sst11 = amarelo

if SST[11] >= ES[11]:
    cor_sst11 = vermelho
print(SST[11])
print(cor_sst11)


# In[19]:


if SST[12] <= EI[12]:
    cor_sst12 = vermelho
    
if SST[12] <= LI[12] and SST[12] > EI[12]:
    cor_sst12 = amarelo
    
if SST[12] > LI[12] and SST[12] <= LS[12]:
    cor_sst12 = verde

if SST[12] <= ES[12] and SST[12] > LS[12]:
    cor_sst12 = amarelo

if SST[12] >= ES[12]:
    cor_sst12 = vermelho
print(SST[12])
print(cor_sst12)


# In[20]:


if SST[13] <= EI[13]:
    cor_sst13 = vermelho
    
if SST[13] <= LI[13] and SST[13] > EI[13]:
    cor_sst13 = amarelo
    
if SST[13] > LI[13] and SST[13] <= LS[13]:
    cor_sst13 = verde

if SST[13] <= ES[13] and SST[13] > LS[13]:
    cor_sst13 = amarelo

if SST[13] >= ES[13]:
    cor_sst13 = vermelho
print(SST[13])
print(cor_sst13)


# In[21]:


if SST[14] <= EI[14]:
    cor_sst14 = vermelho
    
if SST[14] <= LI[14] and SST[14] > EI[14]:
    cor_sst14 = amarelo
    
if SST[14] > LI[14] and SST[14] <= LS[14]:
    cor_sst14 = verde

if SST[14] <= ES[14] and SST[14] > LS[14]:
    cor_sst14 = amarelo

if SST[14] >= ES[14]:
    cor_sst14 = vermelho
print(SST[14])
print(cor_sst14)


# In[22]:


if SST[15] <= EI[15]:
    cor_sst15 = vermelho
    
if SST[15] <= LI[15] and SST[15] > EI[15]:
    cor_sst15 = amarelo
    
if SST[15] > LI[15] and SST[15] <= LS[15]:
    cor_sst15 = verde

if SST[15] <= ES[15] and SST[15] > LS[15]:
    cor_sst15 = amarelo

if SST[15] >= ES[15]:
    cor_sst15 = vermelho
print(SST[15])
print(cor_sst15)


# ### TURBIDEZ

# In[23]:


df2 = pd.read_excel('OD.xlsx')
#print (df2)
xl2 = pd.ExcelFile("OD.xlsx")
SSOD = df2["SSOD"].values
EI2 = df2["ERRO INFERIOR"].values
LI2 = df2["LIMITE INFERIOR"].values
LS2 = df2["LIMITE SUPERIOR"].values
ES2 = df2["ERRO SUPERIOR"].values
display(df2)
SSOD[0] = int(r.get("od_135_ss_0"))
SSOD[1] = int(r.get("od_135_ss_1"))
SSOD[2] = int(r.get("od_135_ss_2"))
SSOD[3] = int(r.get("od_135_ss_3"))
SSOD[4] = int(r.get("od_135_ss_4"))
SSOD[5] = int(r.get("od_135_ss_5"))
SSOD[6] = int(r.get("od_135_ss_6"))
SSOD[7] = int(r.get("od_135_ss_7"))
SSOD[8] = int(r.get("od_135_ss_8"))
SSOD[9] = int(r.get("od_135_ss_9"))
SSOD[10] = int(r.get("od_135_ss_10"))
SSOD[11] = int(r.get("od_135_ss_11"))
SSOD[12] = int(r.get("od_135_ss_12"))
SSOD[13] = int(r.get("od_135_ss_13"))
SSOD[14] = int(r.get("od_135_ss_14"))
SSOD[15] = int(r.get("od_135_ss_15"))


# In[24]:


if SSOD[0] <= EI2[0]:
    cor_ssod0 = vermelho
    
if SSOD[0] <= LI2[0] and SSOD[0] > EI2[0]:
    cor_ssod0 = amarelo
    
if SSOD[0] > LI2[0] and SSOD[0] <= LS2[0]:
    cor_ssod0 = verde

if SSOD[0] <= ES2[0] and SSOD[0] > LS2[0]:
    cor_ssod0 = amarelo

if SSOD[0] >= ES2[0]:
    cor_ssod0 = vermelho
print(SSOD[0])
print(cor_ssod0)


# In[25]:


if SSOD[1] <= EI2[1]:
    cor_ssod1 = vermelho
    
if SSOD[1] <= LI2[1] and SSOD[1] > EI2[1]:
    cor_ssod1 = amarelo
    
if SSOD[1] > LI2[1] and SSOD[1] <= LS2[1]:
    cor_ssod1 = verde

if SSOD[1] <= ES2[1] and SSOD[1] > LS2[1]:
    cor_ssod1 = amarelo

if SSOD[1] >= ES2[1]:
    cor_ssod1 = vermelho
print(SSOD[1])
print(cor_ssod1)


# In[26]:


if SSOD[2] <= EI2[2]:
    cor_ssod2 = vermelho
    
if SSOD[2] <= LI2[2] and SSOD[2] > EI2[2]:
    cor_ssod2 = amarelo
    
if SSOD[2] > LI2[2] and SSOD[2] <= LS2[2]:
    cor_ssod2 = verde

if SSOD[2] <= ES2[2] and SSOD[2] > LS2[2]:
    cor_ssod2 = amarelo

if SSOD[2] >= ES2[2]:
    cor_ssod2 = vermelho
print(SSOD[2])
print(cor_ssod2)


# In[27]:


if SSOD[3] <= EI2[3]:
    cor_ssod3 = vermelho
    
if SSOD[3] <= LI2[3] and SSOD[3] > EI2[3]:
    cor_ssod3 = amarelo
    
if SSOD[3] > LI2[3] and SSOD[3] <= LS2[3]:
    cor_ssod3 = verde

if SSOD[3] <= ES2[3] and SSOD[3] > LS2[3]:
    cor_ssod3 = amarelo

if SSOD[3] >= ES2[3]:
    cor_ssod3 = vermelho
print(SSOD[3])
print(cor_ssod3)


# In[28]:


if SSOD[4] <= EI2[4]:
    cor_ssod4 = vermelho
    
if SSOD[4] <= LI2[4] and SSOD[4] > EI2[4]:
    cor_ssod4 = amarelo
    
if SSOD[4] > LI2[4] and SSOD[4] <= LS2[4]:
    cor_ssod4 = verde

if SSOD[4] <= ES2[4] and SSOD[4] > LS2[4]:
    cor_ssod4 = amarelo

if SSOD[4] >= ES2[4]:
    cor_ssod4 = vermelho
print(SSOD[4])
print(cor_ssod4)


# In[29]:


if SSOD[5] <= EI2[5]:
    cor_ssod5 = vermelho
    
if SSOD[5] <= LI2[5] and SSOD[5] > EI2[5]:
    cor_ssod5 = amarelo
    
if SSOD[5] > LI2[5] and SSOD[5] <= LS2[5]:
    cor_ssod5 = verde

if SSOD[5] <= ES2[5] and SSOD[5] > LS2[5]:
    cor_ssod5 = amarelo

if SSOD[5] >= ES2[5]:
    cor_ssod5 = vermelho
print(SSOD[5])
print(cor_ssod5)


# In[30]:


if SSOD[6] <= EI2[6]:
    cor_ssod6 = vermelho
    
if SSOD[6] <= LI2[6] and SSOD[6] > EI2[6]:
    cor_ssod6 = amarelo
    
if SSOD[6] > LI2[6] and SSOD[6] <= LS2[6]:
    cor_ssod6 = verde

if SSOD[6] <= ES2[6] and SSOD[6] > LS2[6]:
    cor_ssod6 = amarelo

if SSOD[6] >= ES2[6]:
    cor_ssod6 = vermelho
print(SSOD[6])
print(cor_ssod6)


# In[31]:


if SSOD[7] <= EI2[7]:
    cor_ssod7 = vermelho
    
if SSOD[7] <= LI2[7] and SSOD[7] > EI2[7]:
    cor_ssod7 = amarelo
    
if SSOD[7] > LI2[7] and SSOD[7] <= LS2[7]:
    cor_ssod7 = verde

if SSOD[7] <= ES2[7] and SSOD[7] > LS2[7]:
    cor_ssod7 = amarelo

if SSOD[7] >= ES2[7]:
    cor_ssod7 = vermelho
print(SSOD[7])
print(cor_ssod7)


# In[32]:


if SSOD[8] <= EI2[8]:
    cor_ssod8 = vermelho
    
if SSOD[8] <= LI2[8] and SSOD[8] > EI2[8]:
    cor_ssod8 = amarelo
    
if SSOD[8] > LI2[8] and SSOD[8] <= LS2[8]:
    cor_ssod8 = verde

if SSOD[8] <= ES2[8] and SSOD[8] > LS2[8]:
    cor_ssod8 = amarelo

if SSOD[8] >= ES2[8]:
    cor_ssod8 = vermelho
print(SSOD[8])
print(cor_ssod8)


# In[33]:


if SSOD[9] <= EI2[9]:
    cor_ssod9 = vermelho
    
if SSOD[9] <= LI2[9] and SSOD[9] > EI2[9]:
    cor_ssod9 = amarelo
    
if SSOD[9] > LI2[9] and SSOD[9] <= LS2[9]:
    cor_ssod9 = verde

if SSOD[9] <= ES2[9] and SSOD[9] > LS2[9]:
    cor_ssod9 = amarelo

if SSOD[9] >= ES2[9]:
    cor_ssod9 = vermelho
print(SSOD[9])
print(cor_ssod9)


# In[34]:


if SSOD[10] <= EI2[10]:
    cor_ssod10 = vermelho
    
if SSOD[10] <= LI2[10] and SSOD[10] > EI2[10]:
    cor_ssod10 = amarelo
    
if SSOD[10] > LI2[10] and SSOD[10] <= LS2[10]:
    cor_ssod10 = verde

if SSOD[10] <= ES2[10] and SSOD[10] > LS2[10]:
    cor_ssod10 = amarelo

if SSOD[10] >= ES2[10]:
    cor_ssod10 = vermelho
print(SSOD[10])
print(cor_ssod10)


# In[35]:


if SSOD[11] <= EI2[11]:
    cor_ssod11 = vermelho
    
if SSOD[11] <= LI2[11] and SSOD[11] > EI2[11]:
    cor_ssod11 = amarelo
    
if SSOD[11] > LI2[11] and SSOD[11] <= LS2[11]:
    cor_ssod11 = verde

if SSOD[11] <= ES2[11] and SSOD[11] > LS2[11]:
    cor_ssod11 = amarelo

if SSOD[11] >= ES2[11]:
    cor_ssod11 = vermelho
print(SSOD[11])
print(cor_ssod11)


# In[36]:


if SSOD[12] <= EI2[12]:
    cor_ssod12 = vermelho
    
if SSOD[12] <= LI2[12] and SSOD[12] > EI2[12]:
    cor_ssod12 = amarelo
    
if SSOD[12] > LI2[12] and SSOD[12] <= LS2[12]:
    cor_ssod12 = verde

if SSOD[12] <= ES2[12] and SSOD[12] > LS2[12]:
    cor_ssod12 = amarelo

if SSOD[12] >= ES2[12]:
    cor_ssod12 = vermelho
print(SSOD[12])
print(cor_ssod12)


# In[37]:


if SSOD[13] <= EI2[13]:
    cor_ssod13 = vermelho
    
if SSOD[13] <= LI2[13] and SSOD[13] > EI2[13]:
    cor_ssod13 = amarelo
    
if SSOD[13] > LI2[13] and SSOD[13] <= LS2[13]:
    cor_ssod13 = verde

if SSOD[13] <= ES2[13] and SSOD[13] > LS2[13]:
    cor_ssod13 = amarelo

if SSOD[13] >= ES2[13]:
    cor_ssod13 = vermelho
print(SSOD[13])
print(cor_ssod13)


# In[38]:


if SSOD[14] <= EI2[14]:
    cor_ssod14 = vermelho
    
if SSOD[14] <= LI2[14] and SSOD[14] > EI2[14]:
    cor_ssod14 = amarelo
    
if SSOD[14] > LI2[14] and SSOD[14] <= LS2[14]:
    cor_ssod14 = verde

if SSOD[14] <= ES2[14] and SSOD[14] > LS2[14]:
    cor_ssod14 = amarelo

if SSOD[14] >= ES2[14]:
    cor_ssod14 = vermelho
print(SSOD[14])
print(cor_ssod14)


# In[39]:


if SSOD[15] <= EI2[15]:
    cor_ssod15 = vermelho
    
if SSOD[15] <= LI2[15] and SSOD[15] > EI2[15]:
    cor_ssod15 = amarelo
    
if SSOD[15] > LI2[15] and SSOD[15] <= LS2[15]:
    cor_ssod15 = verde

if SSOD[15] <= ES2[15] and SSOD[15] > LS2[15]:
    cor_ssod15 = amarelo

if SSOD[15] >= ES2[15]:
    cor_ssod15 = vermelho
print(SSOD[15])
print(cor_ssod15)


# ### AGITAÇÃO

# In[40]:


df3 = pd.read_excel('agit.xlsx')
xl3 = pd.ExcelFile("agit.xlsx")


# In[41]:


display(df3)


# In[42]:


SSS = df3["Ssstir"].values
EI3 = df3["ERRO INFERIOR"].values
LI3 = df3["LIMITE INFERIOR"].values
LS3 = df3["LIMITE SUPERIOR"].values
ES3 = df3["ERRO SUPERIOR"].values


# In[43]:


SSS[0] = int(r.get("stir_ss_0"))
SSS[1] = int(r.get("stir_ss_1"))
SSS[2] = int(r.get("stir_ss_2"))
SSS[3] = int(r.get("stir_ss_3"))
SSS[4] = int(r.get("stir_ss_4"))
SSS[5] = int(r.get("stir_ss_5"))
SSS[6] = int(r.get("stir_ss_6"))
SSS[7] = int(r.get("stir_ss_7"))
SSS[8] = int(r.get("stir_ss_8"))
SSS[9] = int(r.get("stir_ss_9"))
SSS[10] = int(r.get("stir_ss_10"))
SSS[11] = int(r.get("stir_ss_11"))
SSS[12] = int(r.get("stir_ss_12"))
SSS[13] = int(r.get("stir_ss_13"))
SSS[14] = int(r.get("stir_ss_14"))
SSS[15] = int(r.get("stir_ss_15"))


# In[44]:


if SSS[0] <= EI3[0]:
    cor_sss0 = vermelho
    
if SSS[0] <= LI3[0] and SSS[0] > EI3[0]:
    cor_sss0 = amarelo
    
if SSS[0] > LI3[0] and SSS[0] <= LS3[0]:
    cor_sss0 = verde

if SSS[0] <= ES3[0] and SSS[0] > LS3[0]:
    cor_sss0 = amarelo

if SSS[0] >= ES3[0]:
    cor_sss0 = vermelho
print(SSS[0])
print(cor_sss0)


# In[45]:


if SSS[1] <= EI3[1]:
    cor_sss1 = vermelho
    
if SSS[1] <= LI3[1] and SSS[1] > EI3[1]:
    cor_sss1 = amarelo
    
if SSS[1] > LI3[1] and SSS[1] <= LS3[1]:
    cor_sss1 = verde

if SSS[1] <= ES3[1] and SSS[1] > LS3[1]:
    cor_sss1 = amarelo

if SSS[1] >= ES3[1]:
    cor_sss1 = vermelho
print(SSS[1])
print(cor_sss1)


# In[46]:


if SSS[2] <= EI3[2]:
    cor_sss2 = vermelho
    
if SSS[2] <= LI3[2] and SSS[2] > EI3[2]:
    cor_sss2 = amarelo
    
if SSS[2] > LI3[2] and SSS[2] <= LS3[2]:
    cor_sss2 = verde

if SSS[2] <= ES3[2] and SSS[2] > LS3[2]:
    cor_sss2 = amarelo

if SSS[2] >= ES3[2]:
    cor_sss2 = vermelho
print(SSS[2])
print(cor_sss2)


# In[47]:


if SSS[3] <= EI3[3]:
    cor_sss3 = vermelho
    
if SSS[3] <= LI3[3] and SSS[3] > EI3[3]:
    cor_sss3 = amarelo
    
if SSS[3] > LI3[3] and SSS[3] <= LS3[3]:
    cor_sss3 = verde

if SSS[3] <= ES3[3] and SSS[3] > LS3[3]:
    cor_sss3 = amarelo

if SSS[3] >= ES3[3]:
    cor_sss3 = vermelho
print(SSS[3])
print(cor_sss3)


# In[48]:


if SSS[4] <= EI3[4]:
    cor_sss4 = vermelho
    
if SSS[4] <= LI3[4] and SSS[4] > EI3[4]:
    cor_sss4 = amarelo
    
if SSS[4] > LI3[4] and SSS[4] <= LS3[4]:
    cor_sss4 = verde

if SSS[4] <= ES3[4] and SSS[4] > LS3[4]:
    cor_sss4 = amarelo

if SSS[4] >= ES3[4]:
    cor_sss4 = vermelho
print(SSS[4])
print(cor_sss4)


# In[49]:


if SSS[5] <= EI3[5]:
    cor_sss5 = vermelho
    
if SSS[5] <= LI3[5] and SSS[5] > EI3[5]:
    cor_sss5 = amarelo
    
if SSS[5] > LI3[5] and SSS[5] <= LS3[5]:
    cor_sss5 = verde

if SSS[5] <= ES3[5] and SSS[5] > LS3[5]:
    cor_sss5 = amarelo

if SSS[5] >= ES3[5]:
    cor_sss5 = vermelho
print(SSS[5])
print(cor_sss5)


# In[50]:


if SSS[6] <= EI3[6]:
    cor_sss6 = vermelho
    
if SSS[6] <= LI3[6] and SSS[6] > EI3[6]:
    cor_sss6 = amarelo
    
if SSS[6] > LI3[6] and SSS[6] <= LS3[6]:
    cor_sss6 = verde

if SSS[6] <= ES3[6] and SSS[6] > LS3[6]:
    cor_sss6 = amarelo

if SSS[6] >= ES3[6]:
    cor_sss6 = vermelho
print(SSS[6])
print(cor_sss6)


# In[51]:


if SSS[7] <= EI3[7]:
    cor_sss7 = vermelho
    
if SSS[7] <= LI3[7] and SSS[7] > EI3[7]:
    cor_sss7 = amarelo
    
if SSS[7] > LI3[7] and SSS[7] <= LS3[7]:
    cor_sss7 = verde

if SSS[7] <= ES3[7] and SSS[7] > LS3[7]:
    cor_sss7 = amarelo

if SSS[7] >= ES3[7]:
    cor_sss7 = vermelho
print(SSS[7])
print(cor_sss7)


# In[52]:


if SSS[8] <= EI3[8]:
    cor_sss8 = vermelho
    
if SSS[8] <= LI3[8] and SSS[8] > EI3[8]:
    cor_sss8 = amarelo
    
if SSS[8] > LI3[8] and SSS[8] <= LS3[8]:
    cor_sss8 = verde

if SSS[8] <= ES3[8] and SSS[8] > LS3[8]:
    cor_sss8 = amarelo

if SSS[8] >= ES3[8]:
    cor_sss8 = vermelho
print(SSS[8])
print(cor_sss8)


# In[53]:


if SSS[9] <= EI3[9]:
    cor_sss9 = vermelho
    
if SSS[9] <= LI3[9] and SSS[9] > EI3[9]:
    cor_sss9 = amarelo
    
if SSS[9] > LI3[9] and SSS[9] <= LS3[9]:
    cor_sss9 = verde

if SSS[9] <= ES3[9] and SSS[9] > LS3[9]:
    cor_sss9 = amarelo

if SSS[9] >= ES3[9]:
    cor_sss9 = vermelho
print(SSS[9])
print(cor_sss9)


# In[54]:


if SSS[10] <= EI3[10]:
    cor_sss10 = vermelho
    
if SSS[10] <= LI3[10] and SSS[10] > EI3[10]:
    cor_sss10 = amarelo
    
if SSS[10] > LI3[10] and SSS[10] <= LS3[10]:
    cor_sss10 = verde

if SSS[10] <= ES3[10] and SSS[10] > LS3[10]:
    cor_sss10 = amarelo

if SSS[10] >= ES3[10]:
    cor_sss10 = vermelho
print(SSS[10])
print(cor_sss10)


# In[55]:


if SSS[11] <= EI3[11]:
    cor_sss11 = vermelho
    
if SSS[11] <= LI3[11] and SSS[11] > EI3[11]:
    cor_sss11 = amarelo
    
if SSS[11] > LI3[11] and SSS[11] <= LS3[11]:
    cor_sss11 = verde

if SSS[11] <= ES3[11] and SSS[11] > LS3[11]:
    cor_sss11 = amarelo

if SSS[11] >= ES3[11]:
    cor_sss11 = vermelho
print(SSS[11])
print(cor_sss11)


# In[56]:


if SSS[12] <= EI3[12]:
    cor_sss12 = vermelho
    
if SSS[12] <= LI3[12] and SSS[12] > EI3[12]:
    cor_sss12 = amarelo
    
if SSS[12] > LI3[12] and SSS[12] <= LS3[12]:
    cor_sss12 = verde

if SSS[12] <= ES3[12] and SSS[12] > LS3[12]:
    cor_sss12 = amarelo

if SSS[12] >= ES3[12]:
    cor_sss12 = vermelho
print(SSS[12])
print(cor_sss12)


# In[57]:


if SSS[13] <= EI3[13]:
    cor_sss13 = vermelho
    
if SSS[13] <= LI3[13] and SSS[13] > EI3[13]:
    cor_sss13 = amarelo
    
if SSS[13] > LI3[13] and SSS[13] <= LS3[13]:
    cor_sss13 = verde

if SSS[13] <= ES3[13] and SSS[13] > LS3[13]:
    cor_sss13 = amarelo

if SSS[13] >= ES3[13]:
    cor_sss13 = vermelho
print(SSS[13])
print(cor_sss13)


# In[58]:


if SSS[14] <= EI3[14]:
    cor_sss14 = vermelho
    
if SSS[14] <= LI3[14] and SSS[14] > EI3[14]:
    cor_sss14 = amarelo
    
if SSS[14] > LI3[14] and SSS[14] <= LS3[14]:
    cor_sss14 = verde

if SSS[14] <= ES3[14] and SSS[14] > LS3[14]:
    cor_sss14 = amarelo

if SSS[14] >= ES3[14]:
    cor_sss14 = vermelho
print(SSS[14])
print(cor_sss14)


# In[59]:


if SSS[15] <= EI3[15]:
    cor_sss15 = vermelho
    
if SSS[15] <= LI3[15] and SSS[15] > EI3[15]:
    cor_sss15 = amarelo
    
if SSS[15] > LI3[15] and SSS[15] <= LS3[15]:
    cor_sss15 = verde

if SSS[15] <= ES3[15] and SSS[15] > LS3[15]:
    cor_sss15 = amarelo

if SSS[15] >= ES3[15]:
    cor_sss15 = vermelho
print(SSS[15])
print(cor_sss15)


# ### VOLUME

# In[60]:


df4 = pd.read_excel('volume.xlsx')
xl4 = pd.ExcelFile("volume.xlsx")


# In[61]:


display(df4)


# In[62]:


SSV = df4["SSV"].values
EI4 = df4["ERRO INFERIOR"].values
LI4 = df4["LIMITE INFERIOR"].values
LS4 = df4["LIMITE SUPERIOR"].values
ES4 = df4["ERRO SUPERIOR"].values


# In[63]:


SSV[0] = int(r.get("volume_ss_0"))
SSV[1] = int(r.get("volume_ss_1"))
SSV[2] = int(r.get("volume_ss_2"))
SSV[3] = int(r.get("volume_ss_3"))
SSV[4] = int(r.get("volume_ss_4"))
SSV[5] = int(r.get("volume_ss_5"))
SSV[6] = int(r.get("volume_ss_6"))
SSV[7] = int(r.get("volume_ss_7"))
SSV[8] = int(r.get("volume_ss_8"))
SSV[9] = int(r.get("volume_ss_9"))
SSV[10] = int(r.get("volume_ss_10"))
SSV[11] = int(r.get("volume_ss_11"))
SSV[12] = int(r.get("volume_ss_12"))
SSV[13] = int(r.get("volume_ss_13"))
SSV[14] = int(r.get("volume_ss_14"))
SSV[15] = int(r.get("volume_ss_15"))


# In[64]:


if SSV[0] <= EI4[0]:
    cor_ssv0 = vermelho
    
if SSV[0] <= LI4[0] and SSV[0] > EI4[0]:
    cor_ssv0 = amarelo
    
if SSV[0] > LI4[0] and SSV[0] <= LS4[0]:
    cor_ssv0 = verde

if SSV[0] <= ES4[0] and SSV[0] > LS4[0]:
    cor_ssv0 = amarelo

if SSV[0] >= ES4[0]:
    cor_ssv0 = vermelho
print(SSV[0])
print(cor_ssv0)


# In[65]:


if SSV[1] <= EI4[1]:
    cor_ssv1 = vermelho
    
if SSV[1] <= LI4[1] and SSV[1] > EI4[1]:
    cor_ssv1 = amarelo
    
if SSV[1] > LI4[1] and SSV[1] <= LS4[1]:
    cor_ssv1 = verde

if SSV[1] <= ES4[1] and SSV[1] > LS4[1]:
    cor_ssv1 = amarelo

if SSV[1] >= ES4[1]:
    cor_ssv1 = vermelho
print(SSV[1])
print(cor_ssv1)


# In[66]:


if SSV[2] <= EI4[2]:
    cor_ssv2 = vermelho
    
if SSV[2] <= LI4[2] and SSV[2] > EI4[2]:
    cor_ssv2 = amarelo
    
if SSV[2] > LI4[2] and SSV[2] <= LS4[2]:
    cor_ssv2 = verde

if SSV[2] <= ES4[2] and SSV[2] > LS4[2]:
    cor_ssv2 = amarelo

if SSV[2] >= ES4[2]:
    cor_ssv2 = vermelho
print(SSV[2])
print(cor_ssv2)


# In[67]:


if SSV[3] <= EI4[3]:
    cor_ssv3 = vermelho
    
if SSV[3] <= LI4[3] and SSV[3] > EI4[3]:
    cor_ssv3 = amarelo
    
if SSV[3] > LI4[3] and SSV[3] <= LS4[3]:
    cor_ssv3 = verde

if SSV[3] <= ES4[3] and SSV[3] > LS4[3]:
    cor_ssv3 = amarelo

if SSV[3] >= ES4[3]:
    cor_ssv3 = vermelho
print(SSV[3])
print(cor_ssv3)


# In[68]:


if SSV[4] <= EI4[4]:
    cor_ssv4 = vermelho
    
if SSV[4] <= LI4[4] and SSV[4] > EI4[4]:
    cor_ssv4 = amarelo
    
if SSV[4] > LI4[4] and SSV[4] <= LS4[4]:
    cor_ssv4 = verde

if SSV[4] <= ES4[4] and SSV[4] > LS4[4]:
    cor_ssv4 = amarelo

if SSV[4] >= ES4[4]:
    cor_ssv4 = vermelho
print(SSV[4])
print(cor_ssv4)


# In[69]:


if SSV[5] <= EI4[5]:
    cor_ssv5 = vermelho
    
if SSV[5] <= LI4[5] and SSV[5] > EI4[5]:
    cor_ssv5 = amarelo
    
if SSV[5] > LI4[5] and SSV[5] <= LS4[5]:
    cor_ssv5 = verde

if SSV[5] <= ES4[5] and SSV[5] > LS4[5]:
    cor_ssv5 = amarelo

if SSV[5] >= ES4[5]:
    cor_ssv5 = vermelho
print(SSV[5])
print(cor_ssv5)


# In[70]:


if SSV[6] <= EI4[6]:
    cor_ssv6 = vermelho
    
if SSV[6] <= LI4[6] and SSV[6] > EI4[6]:
    cor_ssv6 = amarelo
    
if SSV[6] > LI4[6] and SSV[6] <= LS4[6]:
    cor_ssv6 = verde

if SSV[6] <= ES4[6] and SSV[6] > LS4[6]:
    cor_ssv6 = amarelo

if SSV[6] >= ES4[6]:
    cor_ssv6 = vermelho
print(SSV[6])
print(cor_ssv6)


# In[71]:


if SSV[7] <= EI4[7]:
    cor_ssv7 = vermelho
    
if SSV[7] <= LI4[7] and SSV[7] > EI4[7]:
    cor_ssv7 = amarelo
    
if SSV[7] > LI4[7] and SSV[7] <= LS4[7]:
    cor_ssv7 = verde

if SSV[7] <= ES4[7] and SSV[7] > LS4[7]:
    cor_ssv7 = amarelo

if SSV[7] >= ES4[7]:
    cor_ssv7 = vermelho
print(SSV[7])
print(cor_ssv7)


# In[72]:


if SSV[8] <= EI4[8]:
    cor_ssv8 = vermelho
    
if SSV[8] <= LI4[8] and SSV[8] > EI4[8]:
    cor_ssv8 = amarelo
    
if SSV[8] > LI4[8] and SSV[8] <= LS4[8]:
    cor_ssv8 = verde

if SSV[8] <= ES4[8] and SSV[8] > LS4[8]:
    cor_ssv8 = amarelo

if SSV[8] >= ES4[8]:
    cor_ssv8 = vermelho
print(SSV[8])
print(cor_ssv8)


# In[73]:


if SSV[9] <= EI4[9]:
    cor_ssv9 = vermelho
    
if SSV[9] <= LI4[9] and SSV[9] > EI4[9]:
    cor_ssv9 = amarelo
    
if SSV[9] > LI4[9] and SSV[9] <= LS4[9]:
    cor_ssv9 = verde

if SSV[9] <= ES4[9] and SSV[9] > LS4[9]:
    cor_ssv9 = amarelo

if SSV[9] >= ES4[9]:
    cor_ssv9 = vermelho
print(SSV[9])
print(cor_ssv9)


# In[74]:


if SSV[10] <= EI4[10]:
    cor_ssv10 = vermelho
    
if SSV[10] <= LI4[10] and SSV[10] > EI4[10]:
    cor_ssv10 = amarelo
    
if SSV[10] > LI4[10] and SSV[10] <= LS4[10]:
    cor_ssv10 = verde

if SSV[10] <= ES4[10] and SSV[10] > LS4[10]:
    cor_ssv10 = amarelo

if SSV[10] >= ES4[10]:
    cor_ssv10 = vermelho
print(SSV[10])
print(cor_ssv10)


# In[75]:


if SSV[11] <= EI4[11]:
    cor_ssv11 = vermelho
    
if SSV[11] <= LI4[11] and SSV[11] > EI4[11]:
    cor_ssv11 = amarelo
    
if SSV[11] > LI4[11] and SSV[11] <= LS4[11]:
    cor_ssv11 = verde

if SSV[11] <= ES4[11] and SSV[11] > LS4[11]:
    cor_ssv11 = amarelo

if SSV[11] >= ES4[11]:
    cor_ssv11 = vermelho
print(SSV[11])
print(cor_ssv11)


# In[76]:


if SSV[12] <= EI4[12]:
    cor_ssv12 = vermelho
    
if SSV[12] <= LI4[12] and SSV[12] > EI4[12]:
    cor_ssv12 = amarelo
    
if SSV[12] > LI4[12] and SSV[12] <= LS4[12]:
    cor_ssv12 = verde

if SSV[12] <= ES4[12] and SSV[12] > LS4[12]:
    cor_ssv12 = amarelo

if SSV[12] >= ES4[12]:
    cor_ssv12 = vermelho
print(SSV[12])
print(cor_ssv12)


# In[77]:


if SSV[13] <= EI4[13]:
    cor_ssv13 = vermelho
    
if SSV[13] <= LI4[13] and SSV[13] > EI4[13]:
    cor_ssv13 = amarelo
    
if SSV[13] > LI4[13] and SSV[13] <= LS4[13]:
    cor_ssv13 = verde

if SSV[13] <= ES4[13] and SSV[13] > LS4[13]:
    cor_ssv13 = amarelo

if SSV[13] >= ES4[13]:
    cor_ssv13 = vermelho
print(SSV[13])
print(cor_ssv13)


# In[78]:


if SSV[14] <= EI4[14]:
    cor_ssv14 = vermelho
    
if SSV[14] <= LI4[14] and SSV[14] > EI4[14]:
    cor_ssv14 = amarelo
    
if SSV[14] > LI4[14] and SSV[14] <= LS4[14]:
    cor_ssv14 = verde

if SSV[14] <= ES4[14] and SSV[14] > LS4[14]:
    cor_ssv14 = amarelo

if SSV[14] >= ES4[14]:
    cor_ssv14 = vermelho
print(SSV[14])
print(cor_ssv14)


# In[79]:


if SSV[15] <= EI4[15]:
    cor_ssv15 = vermelho
    
if SSV[15] <= LI4[15] and SSV[15] > EI4[15]:
    cor_ssv15 = amarelo
    
if SSV[15] > LI4[15] and SSV[15] <= LS4[15]:
    cor_ssv15 = verde

if SSV[15] <= ES4[15] and SSV[15] > LS4[15]:
    cor_ssv15 = amarelo

if SSV[15] >= ES4[15]:
    cor_ssv15 = vermelho
print(SSV[15])
print(cor_ssv15)


# ### TIMESTAMP

# In[80]:


#df5 = pd.read_excel('time.xlsx')
#xl5 = pd.ExcelFile("time.xlsx")


# In[81]:


#display(df5)


# In[82]:


TIME = int(r.get("timestamp"))
print(TIME)


# In[83]:


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\IP_2\plano_b.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 480))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.frame.setMinimumSize(QtCore.QSize(800, 480))
        self.frame.setMaximumSize(QtCore.QSize(800, 480))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(670, 70, 800, 0))
        self.frame_2.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 100, 56, 121))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.layoutWidget_20 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_20.setGeometry(QtCore.QRect(35, 100, 31, 121))
        self.layoutWidget_20.setObjectName("layoutWidget_20")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.layoutWidget_20)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_20)
        self.label_13.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_22.addWidget(self.label_13)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_20)
        self.label_31.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_22.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_20)
        self.label_32.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_22.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_20)
        self.label_33.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_22.addWidget(self.label_33)
        self.layoutWidget_21 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_21.setGeometry(QtCore.QRect(30, 300, 31, 121))
        self.layoutWidget_21.setObjectName("layoutWidget_21")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.layoutWidget_21)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_106 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_106.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_106.setAlignment(QtCore.Qt.AlignCenter)
        self.label_106.setObjectName("label_106")
        self.verticalLayout_23.addWidget(self.label_106)
        self.label_107 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_107.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_107.setAlignment(QtCore.Qt.AlignCenter)
        self.label_107.setObjectName("label_107")
        self.verticalLayout_23.addWidget(self.label_107)
        self.label_108 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_108.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_108.setAlignment(QtCore.Qt.AlignCenter)
        self.label_108.setObjectName("label_108")
        self.verticalLayout_23.addWidget(self.label_108)
        self.label_109 = QtWidgets.QLabel(self.layoutWidget_21)
        self.label_109.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_109.setAlignment(QtCore.Qt.AlignCenter)
        self.label_109.setObjectName("label_109")
        self.verticalLayout_23.addWidget(self.label_109)
        self.layoutWidget_22 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_22.setGeometry(QtCore.QRect(70, 300, 61, 121))
        self.layoutWidget_22.setObjectName("layoutWidget_22")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.layoutWidget_22)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_110 = QtWidgets.QLabel(self.layoutWidget_22)
        self.label_110.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_110.setAlignment(QtCore.Qt.AlignCenter)
        self.label_110.setObjectName("label_110")
        self.verticalLayout_24.addWidget(self.label_110)
        self.label_111 = QtWidgets.QLabel(self.layoutWidget_22)
        self.label_111.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_111.setAlignment(QtCore.Qt.AlignCenter)
        self.label_111.setObjectName("label_111")
        self.verticalLayout_24.addWidget(self.label_111)
        self.label_112 = QtWidgets.QLabel(self.layoutWidget_22)
        self.label_112.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_112.setAlignment(QtCore.Qt.AlignCenter)
        self.label_112.setObjectName("label_112")
        self.verticalLayout_24.addWidget(self.label_112)
        self.label_113 = QtWidgets.QLabel(self.layoutWidget_22)
        self.label_113.setStyleSheet("color: rgb(166, 166, 166);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.verticalLayout_24.addWidget(self.label_113)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 20, 800, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(800, 20))
        self.frame_3.setMaximumSize(QtCore.QSize(800, 20))
        self.frame_3.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(6, 0, 791, 20))
        self.label.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(140, 270, 641, 161))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SS9 = QtWidgets.QFrame(self.widget)
        self.SS9.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS9.setObjectName("SS9")
        self.label_22 = QtWidgets.QLabel(self.SS9)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_22.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.layoutWidget_12 = QtWidgets.QWidget(self.SS9)
        self.layoutWidget_12.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_14.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_74 = QtWidgets.QLabel(self.layoutWidget_12)
        mensagem_sst8 = "color: " + cor_sst8
        self.label_74.setStyleSheet("{}".format(mensagem_sst8) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.verticalLayout_14.addWidget(self.label_74)
        self.label_75 = QtWidgets.QLabel(self.layoutWidget_12)
        mensagem_ssod8 = "color: " + cor_ssod8
        self.label_75.setStyleSheet("{}".format(mensagem_ssod8) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.verticalLayout_14.addWidget(self.label_75)
        self.label_76 = QtWidgets.QLabel(self.layoutWidget_12)
        mensagem_sss8 = "color: " + cor_sss8
        self.label_76.setStyleSheet("{}".format(mensagem_sss8) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.verticalLayout_14.addWidget(self.label_76)
        self.label_77 = QtWidgets.QLabel(self.layoutWidget_12)
        mensagem_ssv8 = "color: " + cor_ssv8
        self.label_77.setStyleSheet("{}".format(mensagem_ssv8) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.verticalLayout_14.addWidget(self.label_77)
        self.horizontalLayout.addWidget(self.SS9)
        self.SS_10 = QtWidgets.QFrame(self.widget)
        self.SS_10.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_10.setObjectName("SS_10")
        self.label_23 = QtWidgets.QLabel(self.SS_10)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_23.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.layoutWidget_13 = QtWidgets.QWidget(self.SS_10)
        self.layoutWidget_13.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_15.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_78 = QtWidgets.QLabel(self.layoutWidget_13)
        mensagem_sst9 = "color: " + cor_sst9
        self.label_78.setStyleSheet("{}".format(mensagem_sst9) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.verticalLayout_15.addWidget(self.label_78)
        self.label_79 = QtWidgets.QLabel(self.layoutWidget_13)
        mensagem_ssod9 = "color: " + cor_ssod9
        self.label_79.setStyleSheet("{}".format(mensagem_ssod9) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.verticalLayout_15.addWidget(self.label_79)
        self.label_80 = QtWidgets.QLabel(self.layoutWidget_13)
        mensagem_sss9 = "color: " + cor_sss9
        self.label_80.setStyleSheet("{}".format(mensagem_sss9) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.verticalLayout_15.addWidget(self.label_80)
        self.label_81 = QtWidgets.QLabel(self.layoutWidget_13)
        mensagem_ssv9 = "color: " + cor_ssv9
        self.label_81.setStyleSheet("{}".format(mensagem_ssv9) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.verticalLayout_15.addWidget(self.label_81)
        self.horizontalLayout.addWidget(self.SS_10)
        self.SS_11 = QtWidgets.QFrame(self.widget)
        self.SS_11.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_11.setObjectName("SS_11")
        self.label_24 = QtWidgets.QLabel(self.SS_11)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.layoutWidget_14 = QtWidgets.QWidget(self.SS_11)
        self.layoutWidget_14.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget_14)
        self.verticalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_82 = QtWidgets.QLabel(self.layoutWidget_14)
        mensagem_sst10 = "color: " + cor_sst10
        self.label_82.setStyleSheet("{}".format(mensagem_sst10) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_82.setAlignment(QtCore.Qt.AlignCenter)
        self.label_82.setObjectName("label_82")
        self.verticalLayout_16.addWidget(self.label_82)
        self.label_83 = QtWidgets.QLabel(self.layoutWidget_14)
        mensagem_ssod10 = "color: " + cor_ssod10
        self.label_83.setStyleSheet("{}".format(mensagem_ssod10) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_83.setAlignment(QtCore.Qt.AlignCenter)
        self.label_83.setObjectName("label_83")
        self.verticalLayout_16.addWidget(self.label_83)
        self.label_84 = QtWidgets.QLabel(self.layoutWidget_14)
        mensagem_sss10 = "color: " + cor_sss10
        self.label_84.setStyleSheet("{}".format(mensagem_sss10) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_84.setAlignment(QtCore.Qt.AlignCenter)
        self.label_84.setObjectName("label_84")
        self.verticalLayout_16.addWidget(self.label_84)
        self.label_85 = QtWidgets.QLabel(self.layoutWidget_14)
        mensagem_ssv10 = "color: " + cor_ssv10
        self.label_85.setStyleSheet("{}".format(mensagem_ssv10) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_85.setAlignment(QtCore.Qt.AlignCenter)
        self.label_85.setObjectName("label_85")
        self.verticalLayout_16.addWidget(self.label_85)
        self.horizontalLayout.addWidget(self.SS_11)
        self.SS_12 = QtWidgets.QFrame(self.widget)
        self.SS_12.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_12.setObjectName("SS_12")
        self.label_25 = QtWidgets.QLabel(self.SS_12)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_25.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.layoutWidget_15 = QtWidgets.QWidget(self.SS_12)
        self.layoutWidget_15.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.layoutWidget_15)
        self.verticalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_86 = QtWidgets.QLabel(self.layoutWidget_15)
        mensagem_sst11 = "color: " + cor_sst11
        self.label_86.setStyleSheet("{}".format(mensagem_sst11) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setObjectName("label_86")
        self.verticalLayout_17.addWidget(self.label_86)
        self.label_87 = QtWidgets.QLabel(self.layoutWidget_15)
        mensagem_ssod11 = "color: " + cor_ssod11
        self.label_87.setStyleSheet("{}".format(mensagem_ssod11) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_87.setAlignment(QtCore.Qt.AlignCenter)
        self.label_87.setObjectName("label_87")
        self.verticalLayout_17.addWidget(self.label_87)
        self.label_88 = QtWidgets.QLabel(self.layoutWidget_15)
        mensagem_sss11 = "color: " + cor_sss11
        self.label_88.setStyleSheet("{}".format(mensagem_sss11) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_88.setAlignment(QtCore.Qt.AlignCenter)
        self.label_88.setObjectName("label_88")
        self.verticalLayout_17.addWidget(self.label_88)
        self.label_89 = QtWidgets.QLabel(self.layoutWidget_15)
        mensagem_ssv11 = "color: " + cor_ssv11
        self.label_89.setStyleSheet("{}".format(mensagem_ssv11) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_89.setAlignment(QtCore.Qt.AlignCenter)
        self.label_89.setObjectName("label_89")
        self.verticalLayout_17.addWidget(self.label_89)
        self.horizontalLayout.addWidget(self.SS_12)
        self.SS_13 = QtWidgets.QFrame(self.widget)
        self.SS_13.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_13.setObjectName("SS_13")
        self.label_26 = QtWidgets.QLabel(self.SS_13)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_26.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.layoutWidget_16 = QtWidgets.QWidget(self.SS_13)
        self.layoutWidget_16.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_16.setObjectName("layoutWidget_16")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.layoutWidget_16)
        self.verticalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_90 = QtWidgets.QLabel(self.layoutWidget_16)
        mensagem_sst12 = "color: " + cor_sst12
        self.label_90.setStyleSheet("{}".format(mensagem_sst12) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_90.setAlignment(QtCore.Qt.AlignCenter)
        self.label_90.setObjectName("label_90")
        self.verticalLayout_18.addWidget(self.label_90)
        self.label_91 = QtWidgets.QLabel(self.layoutWidget_16)
        mensagem_ssod12 = "color: " + cor_ssod12
        self.label_91.setStyleSheet("{}".format(mensagem_ssod12) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_91.setAlignment(QtCore.Qt.AlignCenter)
        self.label_91.setObjectName("label_91")
        self.verticalLayout_18.addWidget(self.label_91)
        self.label_92 = QtWidgets.QLabel(self.layoutWidget_16)
        mensagem_sss12 = "color: " + cor_sss12
        self.label_92.setStyleSheet("{}".format(mensagem_sss12) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_92.setAlignment(QtCore.Qt.AlignCenter)
        self.label_92.setObjectName("label_92")
        self.verticalLayout_18.addWidget(self.label_92)
        self.label_93 = QtWidgets.QLabel(self.layoutWidget_16)
        mensagem_ssv12 = "color: " + cor_ssv12
        self.label_93.setStyleSheet("{}".format(mensagem_ssv12) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_93.setAlignment(QtCore.Qt.AlignCenter)
        self.label_93.setObjectName("label_93")
        self.verticalLayout_18.addWidget(self.label_93)
        self.horizontalLayout.addWidget(self.SS_13)
        self.SS_14 = QtWidgets.QFrame(self.widget)
        self.SS_14.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_14.setObjectName("SS_14")
        self.label_27 = QtWidgets.QLabel(self.SS_14)
        self.label_27.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_27.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.layoutWidget_17 = QtWidgets.QWidget(self.SS_14)
        self.layoutWidget_17.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_17.setObjectName("layoutWidget_17")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.layoutWidget_17)
        self.verticalLayout_19.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_94 = QtWidgets.QLabel(self.layoutWidget_17)
        mensagem_sst13 = "color: " + cor_sst13
        self.label_94.setStyleSheet("{}".format(mensagem_sst13) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_94.setAlignment(QtCore.Qt.AlignCenter)
        self.label_94.setObjectName("label_94")
        self.verticalLayout_19.addWidget(self.label_94)
        self.label_95 = QtWidgets.QLabel(self.layoutWidget_17)
        mensagem_ssod13 = "color: " + cor_ssod13
        self.label_95.setStyleSheet("{}".format(mensagem_ssod13) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_95.setAlignment(QtCore.Qt.AlignCenter)
        self.label_95.setObjectName("label_95")
        self.verticalLayout_19.addWidget(self.label_95)
        self.label_96 = QtWidgets.QLabel(self.layoutWidget_17)
        mensagem_sss13 = "color: " + cor_sss13
        self.label_96.setStyleSheet("{}".format(mensagem_sss13) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_96.setAlignment(QtCore.Qt.AlignCenter)
        self.label_96.setObjectName("label_96")
        self.verticalLayout_19.addWidget(self.label_96)
        self.label_97 = QtWidgets.QLabel(self.layoutWidget_17)
        mensagem_ssv13 = "color: " + cor_ssv13
        self.label_97.setStyleSheet("{}".format(mensagem_ssv13) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_97.setAlignment(QtCore.Qt.AlignCenter)
        self.label_97.setObjectName("label_97")
        self.verticalLayout_19.addWidget(self.label_97)
        self.horizontalLayout.addWidget(self.SS_14)
        self.SS_15 = QtWidgets.QFrame(self.widget)
        self.SS_15.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_15.setObjectName("SS_15")
        self.label_28 = QtWidgets.QLabel(self.SS_15)
        self.label_28.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_28.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.layoutWidget_18 = QtWidgets.QWidget(self.SS_15)
        self.layoutWidget_18.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_18.setObjectName("layoutWidget_18")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_20.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_98 = QtWidgets.QLabel(self.layoutWidget_18)
        mensagem_sst14 = "color: " + cor_sst14
        self.label_98.setStyleSheet("{}".format(mensagem_sst14) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_98.setAlignment(QtCore.Qt.AlignCenter)
        self.label_98.setObjectName("label_98")
        self.verticalLayout_20.addWidget(self.label_98)
        self.label_99 = QtWidgets.QLabel(self.layoutWidget_18)
        mensagem_ssod14 = "color: " + cor_ssod14
        self.label_99.setStyleSheet("{}".format(mensagem_ssod14) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.verticalLayout_20.addWidget(self.label_99)
        self.label_100 = QtWidgets.QLabel(self.layoutWidget_18)
        mensagem_sss14 = "color: " + cor_sss14
        self.label_100.setStyleSheet("{}".format(mensagem_sss14) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.verticalLayout_20.addWidget(self.label_100)
        self.label_101 = QtWidgets.QLabel(self.layoutWidget_18)
        mensagem_ssv14 = "color: " + cor_ssv14
        self.label_101.setStyleSheet("{}".format(mensagem_ssv14) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_101.setAlignment(QtCore.Qt.AlignCenter)
        self.label_101.setObjectName("label_101")
        self.verticalLayout_20.addWidget(self.label_101)
        self.horizontalLayout.addWidget(self.SS_15)
        self.SS_16 = QtWidgets.QFrame(self.widget)
        self.SS_16.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS_16.setObjectName("SS_16")
        self.label_29 = QtWidgets.QLabel(self.SS_16)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_29.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.layoutWidget_19 = QtWidgets.QWidget(self.SS_16)
        self.layoutWidget_19.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_19.setObjectName("layoutWidget_19")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.layoutWidget_19)
        self.verticalLayout_21.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_102 = QtWidgets.QLabel(self.layoutWidget_19)
        mensagem_sst15 = "color: " + cor_sst15
        self.label_102.setStyleSheet("{}".format(mensagem_sst15) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_102.setAlignment(QtCore.Qt.AlignCenter)
        self.label_102.setObjectName("label_102")
        self.verticalLayout_21.addWidget(self.label_102)
        self.label_103 = QtWidgets.QLabel(self.layoutWidget_19)
        mensagem_ssod15 = "color: " + cor_ssod15
        self.label_103.setStyleSheet("{}".format(mensagem_ssod15) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_103.setAlignment(QtCore.Qt.AlignCenter)
        self.label_103.setObjectName("label_103")
        self.verticalLayout_21.addWidget(self.label_103)
        self.label_104 = QtWidgets.QLabel(self.layoutWidget_19)
        mensagem_sss15 = "color: " + cor_sss15
        self.label_104.setStyleSheet("{}".format(mensagem_sss15) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_104.setAlignment(QtCore.Qt.AlignCenter)
        self.label_104.setObjectName("label_104")
        self.verticalLayout_21.addWidget(self.label_104)
        self.label_105 = QtWidgets.QLabel(self.layoutWidget_19)
        mensagem_ssv15 = "color: " + cor_ssv15
        self.label_105.setStyleSheet("{}".format(mensagem_ssv15) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_105.setAlignment(QtCore.Qt.AlignCenter)
        self.label_105.setObjectName("label_105")
        self.verticalLayout_21.addWidget(self.label_105)
        self.horizontalLayout.addWidget(self.SS_16)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(140, 70, 641, 161))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SS1 = QtWidgets.QFrame(self.widget1)
        self.SS1.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS1.setObjectName("SS1")
        self.label_14 = QtWidgets.QLabel(self.SS1)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_14.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.layoutWidget_6 = QtWidgets.QWidget(self.SS1)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_46 = QtWidgets.QLabel(self.layoutWidget_6)
        mensagem_sst0 = "color: " + cor_sst0
        self.label_46.setStyleSheet("{}".format(mensagem_sst0) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_7.addWidget(self.label_46)
        
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_6)
        mensagem_ssod0 = "color: " + cor_ssod0
        self.label_47.setStyleSheet("{}".format(mensagem_ssod0) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_7.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_6)
        mensagem_sss0 = "color: " + cor_sss0
        self.label_48.setStyleSheet("{}".format(mensagem_sss0) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_7.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_6)
        mensagem_ssv0 = "color: " + cor_ssv0
        self.label_49.setStyleSheet("{}".format(mensagem_ssv0) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_7.addWidget(self.label_49)
        self.horizontalLayout_2.addWidget(self.SS1)
        self.SS2 = QtWidgets.QFrame(self.widget1)
        self.SS2.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS2.setObjectName("SS2")
        self.label_15 = QtWidgets.QLabel(self.SS2)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_15.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.layoutWidget_3 = QtWidgets.QWidget(self.SS2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        mensagem_sst1 = "color: " + cor_sst1
        self.label_34.setStyleSheet("{}".format(mensagem_sst1) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_4.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_3)
        mensagem_ssod1 = "color: " + cor_ssod1
        self.label_35.setStyleSheet("{}".format(mensagem_ssod1) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_4.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_3)
        mensagem_sss1 = "color: " + cor_sss1
        self.label_36.setStyleSheet("{}".format(mensagem_sss1) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_4.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_3)
        mensagem_ssv1 = "color: " + cor_ssv1
        self.label_37.setStyleSheet("{}".format(mensagem_ssv1) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_4.addWidget(self.label_37)
        self.horizontalLayout_2.addWidget(self.SS2)
        self.SS3 = QtWidgets.QFrame(self.widget1)
        self.SS3.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS3.setObjectName("SS3")
        self.label_16 = QtWidgets.QLabel(self.SS3)
        self.label_16.setGeometry(QtCore.QRect(1, 0, 61, 25))
        self.label_16.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.layoutWidget_8 = QtWidgets.QWidget(self.SS3)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_58 = QtWidgets.QLabel(self.layoutWidget_8)
        mensagem_sst2 = "color: " + cor_sst2
        self.label_58.setStyleSheet("{}".format(mensagem_sst2) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_10.addWidget(self.label_58)
        self.label_59 = QtWidgets.QLabel(self.layoutWidget_8)
        mensagem_ssod2 = "color: " + cor_ssod2
        self.label_59.setStyleSheet("{}".format(mensagem_ssod2) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_10.addWidget(self.label_59)
        self.label_60 = QtWidgets.QLabel(self.layoutWidget_8)
        mensagem_sss2 = "color: " + cor_sss2
        self.label_60.setStyleSheet("{}".format(mensagem_sss2) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_10.addWidget(self.label_60)
        self.label_61 = QtWidgets.QLabel(self.layoutWidget_8)
        mensagem_ssv2 = "color: " + cor_ssv2
        self.label_61.setStyleSheet("{}".format(mensagem_ssv2) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_10.addWidget(self.label_61)
        self.horizontalLayout_2.addWidget(self.SS3)
        self.SS4 = QtWidgets.QFrame(self.widget1)
        self.SS4.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS4.setObjectName("SS4")
        self.label_17 = QtWidgets.QLabel(self.SS4)
        self.label_17.setGeometry(QtCore.QRect(2, 0, 61, 25))
        self.label_17.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.layoutWidget_5 = QtWidgets.QWidget(self.SS4)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_42 = QtWidgets.QLabel(self.layoutWidget_5)
        mensagem_sst3 = "color: " + cor_sst3
        self.label_42.setStyleSheet("{}".format(mensagem_sst3) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_6.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_5)
        mensagem_ssod3 = "color: " + cor_ssod3
        self.label_43.setStyleSheet("{}".format(mensagem_ssod3) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_6.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget_5)
        mensagem_sss3 = "color: " + cor_sss3
        self.label_44.setStyleSheet("{}".format(mensagem_sss3) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_6.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget_5)
        mensagem_ssv3 = "color: " + cor_ssv3
        self.label_45.setStyleSheet("{}".format(mensagem_ssv3) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_6.addWidget(self.label_45)
        self.horizontalLayout_2.addWidget(self.SS4)
        self.SS5 = QtWidgets.QFrame(self.widget1)
        self.SS5.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS5.setObjectName("SS5")
        self.label_18 = QtWidgets.QLabel(self.SS5)
        self.label_18.setGeometry(QtCore.QRect(4, 0, 61, 25))
        self.label_18.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.layoutWidget_7 = QtWidgets.QWidget(self.SS5)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_7)
        mensagem_sst4 = "color: " + cor_sst4
        self.label_50.setStyleSheet("{}".format(mensagem_sst4) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_8.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(self.layoutWidget_7)
        mensagem_ssod4 = "color: " + cor_ssod4
        self.label_51.setStyleSheet("{}".format(mensagem_ssod4) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_8.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.layoutWidget_7)
        mensagem_sss4 = "color: " + cor_sss4
        self.label_52.setStyleSheet("{}".format(mensagem_sss4) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_8.addWidget(self.label_52)
        self.label_53 = QtWidgets.QLabel(self.layoutWidget_7)
        mensagem_ssv4 = "color: " + cor_ssv4
        self.label_53.setStyleSheet("{}".format(mensagem_ssv4) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_8.addWidget(self.label_53)
        self.horizontalLayout_2.addWidget(self.SS5)
        self.SS6 = QtWidgets.QFrame(self.widget1)
        self.SS6.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS6.setObjectName("SS6")
        self.label_19 = QtWidgets.QLabel(self.SS6)
        self.label_19.setGeometry(QtCore.QRect(-2, 0, 71, 25))
        self.label_19.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.layoutWidget_9 = QtWidgets.QWidget(self.SS6)
        self.layoutWidget_9.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_62 = QtWidgets.QLabel(self.layoutWidget_9)
        mensagem_sst5 = "color: " + cor_sst5
        self.label_62.setStyleSheet("{}".format(mensagem_sst5) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.verticalLayout_11.addWidget(self.label_62)
        self.label_63 = QtWidgets.QLabel(self.layoutWidget_9)
        mensagem_ssod5 = "color: " + cor_ssod5
        self.label_63.setStyleSheet("{}".format(mensagem_ssod5) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_11.addWidget(self.label_63)
        self.label_64 = QtWidgets.QLabel(self.layoutWidget_9)
        mensagem_sss5 = "color: " + cor_sss5
        self.label_64.setStyleSheet("{}".format(mensagem_sss5) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_11.addWidget(self.label_64)
        self.label_65 = QtWidgets.QLabel(self.layoutWidget_9)
        mensagem_ssv5 = "color: " + cor_ssv5
        self.label_65.setStyleSheet("{}".format(mensagem_ssv5) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.verticalLayout_11.addWidget(self.label_65)
        self.horizontalLayout_2.addWidget(self.SS6)
        self.SS7 = QtWidgets.QFrame(self.widget1)
        self.SS7.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS7.setObjectName("SS7")
        self.label_20 = QtWidgets.QLabel(self.SS7)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 61, 25))
        self.label_20.setStyleSheet("color: rgb(217, 217, 217);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.layoutWidget_10 = QtWidgets.QWidget(self.SS7)
        self.layoutWidget_10.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_66 = QtWidgets.QLabel(self.layoutWidget_10)
        mensagem_sst6 = "color: " + cor_sst6
        self.label_66.setStyleSheet("{}".format(mensagem_sst6) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.verticalLayout_12.addWidget(self.label_66)
        self.label_67 = QtWidgets.QLabel(self.layoutWidget_10)
        mensagem_ssod6 = "color: " + cor_ssod6
        self.label_67.setStyleSheet("{}".format(mensagem_ssod6) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_12.addWidget(self.label_67)
        self.label_68 = QtWidgets.QLabel(self.layoutWidget_10)
        mensagem_sss6 = "color: " + cor_sss6
        self.label_68.setStyleSheet("{}".format(mensagem_sss6) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_12.addWidget(self.label_68)
        self.label_69 = QtWidgets.QLabel(self.layoutWidget_10)
        mensagem_ssv6 = "color: " + cor_ssv6
        self.label_69.setStyleSheet("{}".format(mensagem_ssv6) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_12.addWidget(self.label_69)
        self.horizontalLayout_2.addWidget(self.SS7)
        self.SS8 = QtWidgets.QFrame(self.widget1)
        self.SS8.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.SS8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SS8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SS8.setObjectName("SS8")
        self.label_21 = QtWidgets.QLabel(self.SS8)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 71, 25))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.layoutWidget_11 = QtWidgets.QWidget(self.SS8)
        self.layoutWidget_11.setGeometry(QtCore.QRect(0, 30, 71, 121))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_70 = QtWidgets.QLabel(self.layoutWidget_11)
        mensagem_sst7 = "color: " + cor_sst7
        self.label_70.setStyleSheet("{}".format(mensagem_sst7) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.verticalLayout_13.addWidget(self.label_70)
        self.label_71 = QtWidgets.QLabel(self.layoutWidget_11)
        mensagem_ssod7 = "color: " + cor_ssod7
        self.label_71.setStyleSheet("{}".format(mensagem_ssod7) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_13.addWidget(self.label_71)
        self.label_72 = QtWidgets.QLabel(self.layoutWidget_11)
        mensagem_sss7 = "color: " + cor_sss7
        self.label_72.setStyleSheet("{}".format(mensagem_sss7) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_13.addWidget(self.label_72)
        self.label_73 = QtWidgets.QLabel(self.layoutWidget_11)
        mensagem_ssv7 = "color: " + cor_ssv7
        self.label_73.setStyleSheet("{}".format(mensagem_ssv7) +
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setObjectName("label_73")
        self.verticalLayout_13.addWidget(self.label_73)
        self.horizontalLayout_2.addWidget(self.SS8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "(temp.)"))
        self.label_10.setText(_translate("MainWindow", "(turb.)"))
        self.label_11.setText(_translate("MainWindow", "(agit.)"))
        self.label_12.setText(_translate("MainWindow", "(lev.)"))
        self.label_13.setText(_translate("MainWindow", "ºC"))
        self.label_31.setText(_translate("MainWindow", "OD"))
        self.label_32.setText(_translate("MainWindow", "%"))
        self.label_33.setText(_translate("MainWindow", "%"))
        self.label_106.setText(_translate("MainWindow", "ºC"))
        self.label_107.setText(_translate("MainWindow", "OD"))
        self.label_108.setText(_translate("MainWindow", "%"))
        self.label_109.setText(_translate("MainWindow", "%"))
        self.label_110.setText(_translate("MainWindow", "(temp.)"))
        self.label_111.setText(_translate("MainWindow", "(turb.)"))
        self.label_112.setText(_translate("MainWindow", "(agit.)"))
        self.label_113.setText(_translate("MainWindow", "(lev.)"))
        self.label.setText(_translate("MainWindow", "eVOLVER™"))
        self.label_22.setText(_translate("MainWindow", "SS09"))
        self.label_74.setText(_translate("MainWindow", "{}".format(SST[8])))
        self.label_75.setText(_translate("MainWindow", "{}".format(SSOD[8])))
        self.label_76.setText(_translate("MainWindow", "{}".format(SSS[8])))
        self.label_77.setText(_translate("MainWindow", "{}".format(SSV[8])))
        self.label_23.setText(_translate("MainWindow", "SS10"))
        self.label_78.setText(_translate("MainWindow", "{}".format(SST[9])))
        self.label_79.setText(_translate("MainWindow", "{}".format(SSOD[9])))
        self.label_80.setText(_translate("MainWindow", "{}".format(SSS[9])))
        self.label_81.setText(_translate("MainWindow", "{}".format(SSV[9])))
        self.label_24.setText(_translate("MainWindow", "SS11"))
        self.label_82.setText(_translate("MainWindow", "{}".format(SST[10])))
        self.label_83.setText(_translate("MainWindow", "{}".format(SSOD[10])))
        self.label_84.setText(_translate("MainWindow", "{}".format(SSS[10])))
        self.label_85.setText(_translate("MainWindow", "{}".format(SSV[10])))
        self.label_25.setText(_translate("MainWindow", "SS12"))
        self.label_86.setText(_translate("MainWindow", "{}".format(SST[11])))
        self.label_87.setText(_translate("MainWindow", "{}".format(SSOD[11])))
        self.label_88.setText(_translate("MainWindow", "{}".format(SSS[11])))
        self.label_89.setText(_translate("MainWindow", "{}".format(SSV[11])))
        self.label_26.setText(_translate("MainWindow", "SS13"))
        self.label_90.setText(_translate("MainWindow", "{}".format(SST[12])))
        self.label_91.setText(_translate("MainWindow", "{}".format(SSOD[12])))
        self.label_92.setText(_translate("MainWindow", "{}".format(SSS[12])))
        self.label_93.setText(_translate("MainWindow", "{}".format(SSV[12])))
        self.label_27.setText(_translate("MainWindow", "SS14"))
        self.label_94.setText(_translate("MainWindow", "{}".format(SST[13])))
        self.label_95.setText(_translate("MainWindow", "{}".format(SSOD[13])))
        self.label_96.setText(_translate("MainWindow", "{}".format(SSS[13])))
        self.label_97.setText(_translate("MainWindow", "{}".format(SSV[13])))
        self.label_28.setText(_translate("MainWindow", "SS15"))
        self.label_98.setText(_translate("MainWindow", "{}".format(SST[14])))
        self.label_99.setText(_translate("MainWindow", "{}".format(SSOD[14])))
        self.label_100.setText(_translate("MainWindow", "{}".format(SSS[14])))
        self.label_101.setText(_translate("MainWindow", "{}".format(SSV[14])))
        self.label_29.setText(_translate("MainWindow", "SS16"))
        self.label_102.setText(_translate("MainWindow", "{}".format(SST[15])))
        self.label_103.setText(_translate("MainWindow", "{}".format(SSOD[15])))
        self.label_104.setText(_translate("MainWindow", "{}".format(SSS[15])))
        self.label_105.setText(_translate("MainWindow", "{}".format(SSV[15])))
        self.label_14.setText(_translate("MainWindow", "SS01"))
        self.label_46.setText(_translate("MainWindow", "{}".format(SST[0])))
        self.label_47.setText(_translate("MainWindow", "{}".format(SSOD[0])))
        self.label_48.setText(_translate("MainWindow", "{}".format(SSS[0])))
        self.label_49.setText(_translate("MainWindow", "{}".format(SSV[0])))
        self.label_15.setText(_translate("MainWindow", "SS02"))
        self.label_34.setText(_translate("MainWindow", "{}".format(SST[1])))
        self.label_35.setText(_translate("MainWindow", "{}".format(SSOD[1])))
        self.label_36.setText(_translate("MainWindow", "{}".format(SSS[1])))
        self.label_37.setText(_translate("MainWindow", "{}".format(SSV[1])))
        self.label_16.setText(_translate("MainWindow", "SS03"))
        self.label_58.setText(_translate("MainWindow", "{}".format(SST[2])))
        self.label_59.setText(_translate("MainWindow", "{}".format(SSOD[2])))
        self.label_60.setText(_translate("MainWindow", "{}".format(SSS[2])))
        self.label_61.setText(_translate("MainWindow", "{}".format(SSV[2])))
        self.label_17.setText(_translate("MainWindow", "SS04"))
        self.label_42.setText(_translate("MainWindow", "{}".format(SST[3])))
        self.label_43.setText(_translate("MainWindow", "{}".format(SSOD[3])))
        self.label_44.setText(_translate("MainWindow", "{}".format(SSS[3])))
        self.label_45.setText(_translate("MainWindow", "{}".format(SSV[3])))
        self.label_18.setText(_translate("MainWindow", "SS05"))
        self.label_50.setText(_translate("MainWindow", "{}".format(SST[4])))
        self.label_51.setText(_translate("MainWindow", "{}".format(SSOD[4])))
        self.label_52.setText(_translate("MainWindow", "{}".format(SSS[4])))
        self.label_53.setText(_translate("MainWindow", "{}".format(SSV[4])))
        self.label_19.setText(_translate("MainWindow", "SS06"))
        self.label_62.setText(_translate("MainWindow", "{}".format(SST[5])))
        self.label_63.setText(_translate("MainWindow", "{}".format(SSOD[5])))
        self.label_64.setText(_translate("MainWindow", "{}".format(SSS[5])))
        self.label_65.setText(_translate("MainWindow", "{}".format(SSV[5])))
        self.label_20.setText(_translate("MainWindow", "SS07"))
        self.label_66.setText(_translate("MainWindow", "{}".format(SST[6])))
        self.label_67.setText(_translate("MainWindow", "{}".format(SSOD[6])))
        self.label_68.setText(_translate("MainWindow", "{}".format(SSS[6])))
        self.label_69.setText(_translate("MainWindow", "{}".format(SSV[6])))
        self.label_21.setText(_translate("MainWindow", "SS08"))
        self.label_70.setText(_translate("MainWindow", "{}".format(SST[7])))
        self.label_71.setText(_translate("MainWindow", "{}".format(SSOD[7])))
        self.label_72.setText(_translate("MainWindow", "{}".format(SSS[7])))
        self.label_73.setText(_translate("MainWindow", "{}".format(SSV[7])))

        
################################ FIM DO CODIGO CONVERTIDO COM PYUIC5 #################################
# apos instalar py-redis no seu sistema
# importe o redis
import redis
import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
contador=0
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.tempo = QtCore.QTimer()
        self.tempo.setInterval(1000)
        self.tempo.timeout.connect(self.conta_click)
        self.tempo.start()
        
        
        
    
    def conta_click(self):
        global contador
        contador=contador+1
###############################################################################################
# conecto ao redis para teste
        r = redis.Redis(host="192.168.0.55") #no caso da rasp, utilizar o IP "192.168.0.55"
# uso o redis para salvar a variavale contador provisoriamente soh para teste
        r.set("conta_redis", contador)
# leio o valor de contador de volta
        contador=int(r.get("conta_redis"))
# fecho o redis
        r.close()
# fim do teste com o redis
###############################################################################################
      #  self.label.setText(str(contador))
 #       if (contador>10):
   #         self.label.setStyleSheet("color: rgb(255, 255, 0);")
    #    if (contador>20):
     #       self.label.setStyleSheet("color: rgb(255, 0, 0);")
 #       print("teste",contador)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


# In[ ]:




