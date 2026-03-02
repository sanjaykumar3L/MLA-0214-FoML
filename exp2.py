import csv
import copy

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def candidate_elimination(data):
    num_attributes = len(data[0]) - 1
    
    S = ['0'] * num_attributes
    G = [['?'] * num_attributes]

    print("Initial S:", S)
    print("Initial G:", G)

    for row in data:
        attributes = row[:-1]
        label = row[-1]

        if label == "Yes":
            G = [g for g in G if all(
                g[i] == '?' or g[i] == attributes[i]
                for i in range(num_attributes)
            )]

            for i in range(num_attributes):
                if S[i] == '0':
                    S[i] = attributes[i]
                elif S[i] != attributes[i]:
                    S[i] = '?'

        elif label == "No":
            new_G = []
            for g in G:
                if all(g[i] == '?' or g[i] == attributes[i] for i in range(num_attributes)):
                    for i in range(num_attributes):
                        if g[i] == '?':
                            if S[i] != attributes[i]:
                                new_h = g.copy()
                                new_h[i] = S[i]
                                new_G.append(new_h)
                else:
                    new_G.append(g)
            G = new_G

        print("\nAfter processing:", row)
        print("S:", S)
        print("G:", G)

    return S, G

data = read_csv("enjoysport.csv")
S_final, G_final = candidate_elimination(data)

print("\nFinal Specific Boundary S:", S_final)
print("Final General Boundary G:", G_final)
