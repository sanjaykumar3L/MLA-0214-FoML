import csv
import math
from collections import Counter

# Load Data
def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data = load_data("classification_data.csv")

X=[[float(r[0]),float(r[1])] for r in data]
Y=[r[2] for r in data]

# ---------------------------
# KNN CLASSIFIER
# ---------------------------
def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def knn_predict(test,k=3):
    distances=[]
    
    for i in range(len(X)):
        d=distance(test,X[i])
        distances.append((d,Y[i]))
    
    distances.sort()
    neighbors=[label for _,label in distances[:k]]
    
    return Counter(neighbors).most_common(1)[0][0]

# ---------------------------
# NAIVE BAYES (Simple)
# ---------------------------
def naive_bayes():
    return Counter(Y).most_common(1)[0][0]

# ---------------------------
# TEST DATA
# ---------------------------
test=[5,6]

knn_result=knn_predict(test)
nb_result=naive_bayes()

print("Test Sample:",test)

print("\nKNN Prediction:",knn_result)
print("Naive Bayes Prediction:",nb_result)

# Assume actual class
actual="B"

knn_accuracy=1 if knn_result==actual else 0
nb_accuracy=1 if nb_result==actual else 0

print("\nActual Class:",actual)

print("\nAccuracy Comparison")
print("KNN Accuracy:",knn_accuracy)
print("Naive Bayes Accuracy:",nb_accuracy)

if knn_accuracy>nb_accuracy:
    print("\nKNN performs better")
elif nb_accuracy>knn_accuracy:
    print("\nNaive Bayes performs better")
else:
    print("\nBoth perform equally")
