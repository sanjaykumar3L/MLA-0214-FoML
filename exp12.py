import csv
import math
from collections import Counter

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

def distance(a,b):
    d=0
    for i in range(4):
        d+=(float(a[i])-float(b[i]))**2
    return math.sqrt(d)

data=load_data("iris_data.csv")

test=[5.8,3.0,4.1,1.3]
k=3

distances=[]

for row in data:
    d=distance(test,row)
    distances.append((d,row[4]))

distances.sort()

neighbors=[label for _,label in distances[:k]]

prediction=Counter(neighbors).most_common(1)[0][0]

print("Test Sample:",test)
print("Predicted Flower:",prediction)
