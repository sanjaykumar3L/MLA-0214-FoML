import csv
import numpy as np

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("poly_data.csv")

X=np.array([float(r[0]) for r in data])
Y=np.array([float(r[1]) for r in data])

# Linear regression
linear_coef=np.polyfit(X,Y,1)

# Polynomial regression degree 2
poly_coef=np.polyfit(X,Y,2)

print("Linear Regression Equation:")
print("y =",round(linear_coef[0],2),"x +",round(linear_coef[1],2))

print("\nPolynomial Regression Equation:")
print("y =",round(poly_coef[0],2),"x² +",round(poly_coef[1],2),"x +",round(poly_coef[2],2))
