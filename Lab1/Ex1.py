import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction 

df = pd.read_csv('iris.csv',names=['sepal length','sepal width','petal length','petal width','target'])
mean =df.groupby('target').mean()
covariance =df.groupby('target').cov()
variance =df.groupby('target').var()
correlation =df.groupby('target').corr()
w1= np.random.randn(5,30) * np.sqrt(2/30)
w2 = np.random.randn(3,5) * np.sqrt(2/5)

print(w1)
print("----------")
print(w2)
print("---------")


