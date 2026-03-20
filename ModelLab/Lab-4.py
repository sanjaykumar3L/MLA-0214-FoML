data = [
    ["Premium", "Low", "Good", "Yes"],
    ["Premium", "High", "Good", "Yes"],
    ["Basic", "High", "Poor", "No"],
    ["Basic", "Low", "Poor", "No"]
]

def predict(test):
    yes = [r for r in data if r[-1] == "Yes"]
    no = [r for r in data if r[-1] == "No"]

    py = len(yes)/len(data)
    pn = len(no)/len(data)

    for i in range(3):
        py *= sum(1 for r in yes if r[i]==test[i]) / len(yes)
        pn *= sum(1 for r in no if r[i]==test[i]) / len(no)

    return "Yes" if py > pn else "No"

print(predict(["Premium","Low","Good"]))
