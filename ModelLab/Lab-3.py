import math

data = [
    ["Premium", "Low", "Good", "Yes"],
    ["Premium", "High", "Good", "Yes"],
    ["Basic", "High", "Poor", "No"],
    ["Basic", "Low", "Poor", "No"]
]

def entropy(rows):
    yes = sum(1 for r in rows if r[-1] == "Yes")
    no = len(rows) - yes
    if yes == 0 or no == 0:
        return 0
    p1, p2 = yes/len(rows), no/len(rows)
    return -p1*math.log2(p1) - p2*math.log2(p2)

def gain(data, i):
    total = entropy(data)
    vals = set(r[i] for r in data)
    sub = 0
    for v in vals:
        subset = [r for r in data if r[i] == v]
        sub += (len(subset)/len(data)) * entropy(subset)
    return total - sub

gains = [gain(data, i) for i in range(3)]
print("Best Attribute Index:", gains.index(max(gains)))
