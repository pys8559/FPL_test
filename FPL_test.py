#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.svm import SVC
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
import streamlit as st


# In[6]:


st.header('Artificial Intelligence Prediction of US wheat variety')

st.write('made by Sejong Univ.')

st.write(' ')

st.write('(밀가루 특성을 토대로 미국 밀가루의 품종 예측)')



uploaded_file = st.file_uploader("Choose an excel file", type="xlsx")



if uploaded_file:

    df1 = pd.read_excel(uploaded_file)

    st.write('[입력 데이터] ')

    st.dataframe(df1)

    new_sample1 = df1.drop(["Year", "Variety", "Volume"], axis = 1)

     

    df_train = pd.read_excel("US wheat-dataset-sample.xlsx", header = 0)

    df_train1 = df_train.drop(["Year", "Variety", "Volume"], axis = 1)

    scaler = MinMaxScaler()

    df_train1_normal = scaler.fit_transform(df_train1.values)



    model1 = joblib.load('wheat_svc.pkl') 

    

    new_x_data = scaler.transform(new_sample1.values)    

    

    result = model1.predict(new_x_data)

    

#    new_normal[0][30] = result[0]

#    pred = scaler.inverse_transform(new_normal)



    st.write(' ')

    st.write('[결과] ')

    st.write('예측되는 품종', result[0])

    st.write(' ')


# In[ ]:





# In[ ]:




