import csv

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("car_price.csv")

X=[float(r[0]) for r in data]
Y=[float(r[2]) for r in data]

n=len(X)

mean_x=sum(X)/n
mean_y=sum(Y)/n

num=sum((X[i]-mean_x)*(Y[i]-mean_y) for i in range(n))
den=sum((X[i]-mean_x)**2 for i in range(n))

m=num/den
c=mean_y-m*mean_x

print("Model: Price = ",round(m,2),"* EngineSize +",round(c,2))

engine=1600
price=m*engine+c

print("Predicted Car Price:",round(price))
