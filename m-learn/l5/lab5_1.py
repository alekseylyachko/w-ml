import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("data/reglab1.txt", sep="\t")
# print(df)

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 1])
clf = LinearRegression().fit(X, y)
print("\nx(y):", clf.score(X, y))

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("x(z):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("y(x):", clf.score(X, y))

X = np.asarray(df.iloc[:, 0]).reshape(-1, 1)
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("y(z):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("z(x):", clf.score(X, y))

X = np.asarray(df.iloc[:, -1]).reshape(-1, 1)
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("z(y):", clf.score(X, y))

X = np.asarray(df.iloc[:, 1:])
y = np.asarray(df.iloc[:, 0])
clf = LinearRegression().fit(X, y)
print("z(x, y):", clf.score(X, y))

X = np.asarray(df.iloc[:, 0:-1])
y = np.asarray(df.iloc[:, -1])
clf = LinearRegression().fit(X, y)
print("y(x, z):", clf.score(X, y))

y = np.asarray(df.iloc[:, 1])
df.drop('x', axis=1, inplace=True)
X = np.asarray(df)
clf = LinearRegression().fit(X, y)
print("x(y, z):", clf.score(X, y))
