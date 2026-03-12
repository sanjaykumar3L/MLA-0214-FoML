import random

weights=[random.random(),random.random()]
bias=random.random()

data=[[1,1,1],[0,1,0],[1,0,0],[0,0,0]]

lr=0.1

for epoch in range(10):
    for x1,x2,y in data:
        output=1 if x1*weights[0]+x2*weights[1]+bias>0 else 0
        error=y-output
        
        weights[0]+=lr*error*x1
        weights[1]+=lr*error*x2
        bias+=lr*error

print("Weights:",weights)
print("Bias:",bias)
