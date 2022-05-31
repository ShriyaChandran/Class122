import pandas as pd
import seaborn as sns
import numpy as np
import cv2 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml

X, y = fetch_openml('mnist_784', version = 1, return_X_y = True)
print(pd.Series(y).value_counts())
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n_classes = len(classes)

samples_per_class = 5
figure = plt.figure(figsize=(n_classes*2,(1+samples_per_class*2)))

idx_cls = 0
for cls in classes:
  idxs = np.flatnonzero(y == cls)
  idxs = np.random.choice(idxs, samples_per_class, replace=False)
  i = 0
  for idx in idxs:
    plt_idx = i * n_classes + idx_cls + 1
    p = plt.subplot(samples_per_class, n_classes, plt_idx);
    p = sns.heatmap(np.array(X.loc[idx]).reshape(28,28), cmap=plt.cm.gray, 
             xticklabels=False, yticklabels=False, cbar=False);
    p = plt.axis('off');
    i += 1
  idx_cls += 1

idxs = np.flatnonzero(y == '0')
print(np.array(X.loc[idxs[0]]))

#plot on confusion matrix(carried in 123)


