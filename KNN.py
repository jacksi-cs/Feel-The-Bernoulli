#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sklearn is a machine learning library in python
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA


# In[2]:


train = pd.read_csv("train_KWH.csv")


# In[5]:


train = train[train["month"] == 1]


# In[6]:


train_y = train.pop("hourly_kwh")
train_X = train[["humidity","apparent_temperature","pressure","wind_bearing","hourly_solar_kWh"]]


# In[37]:


test = pd.read_csv("test_KWH2.csv")[["humidity","apparent_temperature","pressure","wind_bearing","hourly_solar_kWh"]]
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(train_X)
train_X_scaled = scaler.transform(train_X)

test_scaled = scaler.transform(test)


# In[38]:


pca = PCA(n_components=4)
pca.fit(train_X_scaled)
train_X_scaled = pca.transform(train_X_scaled)
test_scaled = pca.transform(test_scaled)


# In[39]:


pca.explained_variance_ratio_


# In[41]:


knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(train_X_scaled, train_y)
y_pred = knn.predict(test_scaled)

pd.DataFrame(y_pred).to_csv("preds.kwh", index=False, header = False)

