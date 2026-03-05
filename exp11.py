import csv
import math
from collections import Counter

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

def distance(a,b):
    return math.sqrt((float(a[0])-float(b[0]))**2 + (float(a[1])-float(b[1]))**2)

data=load_data("credit_data.csv")

test=[42000,16000]
k=3

distances=[]

for row in data:
    d=distance(test,row)
    distances.append((d,row[2]))

distances.sort()

neighbors=[label for _,label in distances[:k]]

prediction=Counter(neighbors).most_common(1)[0][0]

print("Test Data:",test)
print("Predicted Credit Score:",prediction)
