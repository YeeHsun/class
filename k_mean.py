import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

k=4 #number of clusters
n_samples=1500
random_state=17

X,y=make_blobs(n_samples=n_samples,centers=k,n_features=2,random_state=random_state)

color='black'
size=1

plt.figure()
plt.scatter(X[:,0],X[:,1],c=color,s=size)

