import csv

data=[]
with open("mobile_price.csv") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

ram=[float(r[0]) for r in data]
price=[float(r[2]) for r in data]

m=sum(price)/sum(ram)

test_ram=10

pred=m*test_ram

print("Predicted Mobile Price:",round(pred))
