import csv

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("house_data.csv")

X=[float(r[0]) for r in data]
Y=[float(r[2]) for r in data]

n=len(X)

mean_x=sum(X)/n
mean_y=sum(Y)/n

num=sum((X[i]-mean_x)*(Y[i]-mean_y) for i in range(n))
den=sum((X[i]-mean_x)**2 for i in range(n))

m=num/den
c=mean_y-m*mean_x

print("Model: Price =",round(m,2),"* Area +",round(c,2))

area=1600
price=m*area+c

print("Predicted Price:",round(price))
