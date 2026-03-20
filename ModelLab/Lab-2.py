data = [
    ["Premium", "Low", "Good", "Yes"],
    ["Premium", "High", "Good", "Yes"],
    ["Basic", "High", "Poor", "No"],
    ["Basic", "Low", "Poor", "No"]
]
S = ["0", "0", "0"]
G = [["?", "?", "?"]]

for row in data:
    x, y = row[:-1], row[-1]

    if y == "Yes":
        for i in range(3):
            if S[i] == "0":
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = "?"
        G = [g for g in G if all(g[i] == "?" or g[i] == S[i] for i in range(3))]

    else:
        G = [[S[i] if g[i] == "?" else g[i] for i in range(3)] for g in G]

print("S:", S)
print("G:", G)
