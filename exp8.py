import csv

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("linear_data.csv")

X=[float(r[0]) for r in data]
Y=[float(r[1]) for r in data]

n=len(X)

mean_x=sum(X)/n
mean_y=sum(Y)/n

num=sum((X[i]-mean_x)*(Y[i]-mean_y) for i in range(n))
den=sum((X[i]-mean_x)**2 for i in range(n))

m=num/den
c=mean_y-m*mean_x

print("Slope:",round(m,3))
print("Intercept:",round(c,3))

x_test=8
y_pred=m*x_test+c
print("Prediction for x=8:",round(y_pred,3))
