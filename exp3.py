import pandas as pd
import numpy as np
import math

def entropy(target):
    values, counts = np.unique(target, return_counts=True)
    ent = 0
    for i in range(len(values)):
        p = counts[i] / np.sum(counts)
        ent -= p * math.log2(p)
    return ent	

def information_gain(data, attribute, target):
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[attribute], return_counts=True)
    
    weighted_entropy = 0
    for i in range(len(values)):
        subset = data[data[attribute] == values[i]]
        weighted_entropy += (counts[i]/np.sum(counts)) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

def id3(data, attributes, target):
    if len(np.unique(data[target])) == 1:
        return np.unique(data[target])[0]
    
    if len(attributes) == 0:
        return data[target].mode()[0]
    
    gains = [information_gain(data, attr, target) for attr in attributes]
    best_attr = attributes[np.argmax(gains)]
    
    tree = {best_attr: {}}
    
    for value in np.unique(data[best_attr]):
        subset = data[data[best_attr] == value]
        subtree = id3(
            subset,
            [attr for attr in attributes if attr != best_attr],
            target
        )
        tree[best_attr][value] = subtree
    
    return tree

def classify(sample, tree):
    if not isinstance(tree, dict):
        return tree
    root = next(iter(tree))
    value = sample[root]
    return classify(sample, tree[root][value])

data = pd.read_csv("temp.csv")

attributes = list(data.columns[:-1])
target = data.columns[-1]

tree = id3(data, attributes, target)

print("Decision Tree:")
print(tree)

new_sample = {
    "Outlook": "Sunny",
    "Temperature": "Cool",
    "Humidity": "High",
    "Wind": "Strong"
}

result = classify(new_sample, tree)

print("\nNew Sample Classification:", result)
