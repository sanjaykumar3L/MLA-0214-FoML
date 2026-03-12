import csv
from collections import Counter

data=[]
with open("loan_data.csv") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

labels=[r[2] for r in data]

prediction=Counter(labels).most_common(1)[0][0]

print("Loan Prediction:",prediction)
