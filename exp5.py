import csv
import math
from collections import Counter

# ----------------------------
# Load CSV Data
# ----------------------------
def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

# ----------------------------
# Euclidean Distance
# ----------------------------
def euclidean_distance(row1, row2):
    distance = 0
    for i in range(len(row1)):
        distance += (float(row1[i]) - float(row2[i])) ** 2
    return math.sqrt(distance)

# ----------------------------
# KNN Algorithm
# ----------------------------
def knn(training_data, test_instance, k):
    distances = []
    
    for row in training_data:
        features = row[:-1]
        label = row[-1]
        dist = euclidean_distance(features, test_instance)
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])
    
    neighbors = distances[:k]
    labels = [neighbor[1] for neighbor in neighbors]
    
    prediction = Counter(labels).most_common(1)[0][0]
    return prediction

# ----------------------------
# Main
# ----------------------------
data = load_data("knn_data.csv")
training_data = data[1:]

# Test Sample (Height, Weight)
test_sample = [5.7, 62]

k = 3

prediction = knn(training_data, test_sample, k)

print("Test Sample:", test_sample)
print("K =", k)
print("Predicted Class:", prediction)
