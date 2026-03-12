import csv

data=[]
with open("sales.csv") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

month=[int(r[0]) for r in data]
sales=[int(r[1]) for r in data]

avg_increase=(sales[-1]-sales[0])/(month[-1]-month[0])

future_month=7

prediction=sales[-1]+avg_increase

print("Predicted Sales for Month",future_month,":",round(prediction))
