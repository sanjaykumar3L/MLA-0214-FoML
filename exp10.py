import csv
import random

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return [float(r[0]) for r in data[1:]]

data=load_data("em_data.csv")

mu1=random.choice(data)
mu2=random.choice(data)

for iteration in range(10):
    
    cluster1=[]
    cluster2=[]
    
    for x in data:
        if abs(x-mu1) < abs(x-mu2):
            cluster1.append(x)
        else:
            cluster2.append(x)
    
    mu1=sum(cluster1)/len(cluster1)
    mu2=sum(cluster2)/len(cluster2)

print("Cluster 1 Mean:",round(mu1,2))
print("Cluster 2 Mean:",round(mu2,2))
