
import numpy as np
from numpy import array
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import decomposition
from sklearn.metrics import precision_score, recall_score, f1_score, jaccard_score, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

df = pd.read_excel (r'C:\Users\ggers\Downloads\features cleaned (1).xlsx')
data = df.drop(['file'], axis = 1)
data = data.drop(['Diagnosis'], axis = 1)
data = data.drop(['Diagnosis Binary'], axis = 1)
labels = df['Diagnosis Binary']
X_train, X_test, Y_train, Y_test = train_test_split(data, labels, test_size = 0.3, shuffle=True)

def visualize_and_metrics(ytrue, ypred, title):
    """
    General function for obtaining basic classification metrics and visualizing confusion matrix.
    :param ytrue: Ground truth target values
    :param ypred: Predictions of target values
    """
    print("Accuracy: ", accuracy_score(ytrue, ypred))
    print("Precision: ", precision_score(ytrue, ypred))
    print("Recall: ", recall_score(ytrue, ypred))
    print("F1 Score: ", f1_score(ytrue, ypred))
    print("Jaccard Score: ", jaccard_score(ytrue, ypred))

    cm = confusion_matrix(ytrue, ypred,  normalize="all")
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.title(title)
    plt.show()
#Bayes Net
gnb = GaussianNB()
model = gnb.fit(X_train, Y_train)
Y_predict = model.predict(X_test)
visualize_and_metrics(Y_test, Y_predict, "Gaussian Unreduced")

#Neural Net
model_nn_2 = MLPClassifier(random_state=1, max_iter=600, hidden_layer_sizes=(22, 22)).fit(X_train, Y_train)
hard_Y_pred_nn_2 = model_nn_2.predict(X_test)
visualize_and_metrics(Y_test, hard_Y_pred_nn_2, "Neural Net Unreduced")

#Reducing Data with PCA
pca = decomposition.PCA(n_components=2)
pca.fit(X_train)
reduced = pca.transform(X_train)
z = reduced[np.where(Y_train==0)]
o = reduced[np.where(Y_train==1)]
#visualizing reduced data
plt.scatter(z[:, 0], z[:, 1], c='blue', marker='x', label='Not Healthy')
plt.scatter(o[:, 0], o[:, 1], c='magenta', marker='x', label='Healthy')
plt.legend()
plt.show()

#reduced data gaussian
pca2 = decomposition.PCA(n_components=2)
pca2.fit(X_test)
reduced2 = pca2.transform(X_test)
gnb = GaussianNB()
model = gnb.fit(reduced, Y_train)
Y_predict = model.predict(reduced2)
visualize_and_metrics(Y_test, Y_predict, "Gaussian Reduced")

#reduced data NN
model_nn_2 = MLPClassifier(random_state=1, max_iter=600, hidden_layer_sizes=(22, 22)).fit(reduced, Y_train)
hard_Y_pred_nn_2 = model_nn_2.predict(reduced2)
visualize_and_metrics(Y_test, hard_Y_pred_nn_2, "Neural Net Reduced")