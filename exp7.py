import csv
import math

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

def sigmoid(z):
    return 1/(1+math.exp(-z))

data=load_data("logistic_data.csv")

X=[float(row[0]) for row in data]
Y=[float(row[1]) for row in data]

w=0
b=0
lr=0.01
epochs=5000

for _ in range(epochs):
    for x,y in zip(X,Y):
        z=w*x+b
        y_pred=sigmoid(z)
        error=y-y_pred
        w+=lr*error*x
        b+=lr*error

print("Weight:",round(w,3))
print("Bias:",round(b,3))

test=5
pred=sigmoid(w*test+b)
print("Prediction for study hours =",test,"->",round(pred))
