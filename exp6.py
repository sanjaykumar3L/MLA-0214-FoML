import csv
from collections import defaultdict

# -------------------------
# Load CSV Data
# -------------------------
def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

# -------------------------
# Train Naive Bayes
# -------------------------
def train_nb(data):
    total = len(data)
    class_counts = defaultdict(int)
    feature_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    
    for row in data:
        label = row[-1]
        class_counts[label] += 1
        
        for i in range(len(row)-1):
            feature_counts[i][row[i]][label] += 1
    
    return class_counts, feature_counts, total

# -------------------------
# Predict
# -------------------------
def predict(row, class_counts, feature_counts, total):
    probabilities = {}
    
    for label in class_counts:
        prior = class_counts[label] / total
        likelihood = 1
        
        for i in range(len(row)):
            count = feature_counts[i][row[i]][label]
            if count == 0:
                likelihood *= 1e-6   # small smoothing
            else:
                likelihood *= count / class_counts[label]
        
        probabilities[label] = prior * likelihood
    
    return max(probabilities, key=probabilities.get)

# -------------------------
# Confusion Matrix
# -------------------------
def confusion_matrix(actual, predicted):
    classes = list(set(actual))
    matrix = {c: {c2:0 for c2 in classes} for c in classes}
    
    for a, p in zip(actual, predicted):
        matrix[a][p] += 1
    
    return matrix

# -------------------------
# Main
# -------------------------
data = load_data("naive_bayes_data.csv")
dataset = data[1:]

class_counts, feature_counts, total = train_nb(dataset)

actual = []
predicted = []

for row in dataset:
    actual.append(row[-1])
    pred = predict(row[:-1], class_counts, feature_counts, total)
    predicted.append(pred)

matrix = confusion_matrix(actual, predicted)

print("Confusion Matrix:")
for row in matrix:
    print(row, matrix[row])

accuracy = sum([1 for a,p in zip(actual,predicted) if a==p]) / len(actual)
print("\nAccuracy:", round(accuracy*100,2), "%")
