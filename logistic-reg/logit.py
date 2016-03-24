

# import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression

# df = pd.read_csv("sample.csv")

# print df.head()

logit = LogisticRegression(C=10000)

# y = df.hon.values
# x = df.female.values

# y.shape = (y.shape[0],1)
# x.shape = (x.shape[0],1)

x = np.array([2,20,20])
x.shape = (3,1)
y = np.array([0,1,1])

logit.fit(x,y.ravel())

print logit.intercept_
print logit.coef_