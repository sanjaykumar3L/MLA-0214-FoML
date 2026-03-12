import csv
from collections import Counter

def load_data(file):
    with open(file,'r') as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("iris_nb.csv")

species=[row[4] for row in data]

prediction=Counter(species).most_common(1)[0][0]

print("Most common class:",prediction)
