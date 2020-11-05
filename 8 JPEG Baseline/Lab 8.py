#!/usr/bin/env python
# coding: utf-8

# In[76]:


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct,idct
import random
from skimage import io
from skimage.color import rgb2gray


# In[77]:


A=np.array([[183,160,94,153,194,163,132,165],
                    [183,153,116,176,187,166,130,169],
                    [179,168,171,182,179,170,131,167],
                    [177,177,179,177,179,165,131,167],
                    [178,178,179,176,182,164,130,171],
                    [179,180,180,179,183,164,130,171],
                    [179,179,180,182,183,170,129,173],
                    [180,179,181,179,181,170,130,169]])


# In[78]:


q=np.array([[16,11,10,16,24,40,51,61],
                   [12,12,14,19,26,58,60,55],
                   [14,13,16,24,40,57,69,56],
                   [14,17,22,29,51,87,80,62],
                   [18,22,37,56,68,109,103,77],
                   [24,35,55,64,81,104,113,92],
                   [49,64,78,87,103,121,120,101],
                   [72,92,95,98,112,100,103,99]])


# In[79]:


#level shifting
A = A-128


# In[80]:


def dct2(a):
    return dct(dct(a,axis=0, norm='ortho'),axis=1,norm='ortho')


# In[81]:


dct_mat = dct2(A)
dct_mat


# In[82]:


#quantized matrix
quant=np.divide(dct_mat,q).round().astype(int)
print(quant)


# In[83]:


def idct2(a):
    return idct(idct(a,axis=0, norm='ortho'),axis=1,norm='ortho')


# In[84]:


idct_mat = idct2(quant).round().astype(int)
idct_mat


# In[85]:


Ainv = idct_mat + 128
Ainv


# In[86]:


MSE = np.square(np.subtract(Ainv,A)).mean() 
MSE


# In[137]:


q=np.array([[16,11,10,16,24,40,51,61],
                   [12,12,14,19,26,58,60,55],
                   [14,13,16,24,40,57,69,56],
                   [14,17,22,29,51,87,80,62],
                   [18,22,37,56,68,109,103,77],
                   [24,35,55,64,81,104,113,92],
                   [49,64,78,87,103,121,120,101],
                   [72,92,95,98,112,100,103,99]])
def jpeg (A):
    #A = A-128
    dct_mat = dct2(A)
    quant=np.divide(dct_mat,q).round().astype(int)
    return quant

def invJPEG (A):
    Ainv = idct2(A).round().astype(int)
    #Ainv = Ainv + 128
    return Ainv


# In[142]:


image_ori=io.imread('Lena.tif')
image=rgb2gray(image_ori)
io.imshow (image)


# In[139]:


row,col = image.shape
image_quant = np.zeros ((row,col),dtype=int)
for r in range (0,row//8):
    for c in range (0,col//8):
        image_quant[r*8:(r+1)*8, c*8:(c+1)*8]=jpeg(image[r*8:(r+1)*8, c*8:(c+1)*8])
        
io.imshow (image_quant,cmap = 'gray')


# In[144]:


image_inv = np.zeros ((row,col),dtype=int)
for r in range (0,row//8):
    for c in range (0,col//8):
        image_inv[r*8:(r+1)*8, c*8:(c+1)*8]=invJPEG(image_quant[r*8:(r+1)*8, c*8:(c+1)*8])
        
io.imshow (image_inv,cmap = 'gray',vmin=0,vmax=None)


# In[ ]:




