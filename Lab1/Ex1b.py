import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv',names=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings'])
mean =df.groupby('Sex').mean()
covariance =df.groupby('Sex').cov()
variance =df.groupby('Sex').var()
correlation =df.groupby('Sex').corr()
print(mean)
print(covariance)
print(variance)
print(correlation)