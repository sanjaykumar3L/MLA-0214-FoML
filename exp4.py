import csv
import random
import math

# -----------------------------
# Load CSV Data
# -----------------------------
def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

# -----------------------------
# Activation Function
# -----------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# -----------------------------
# Initialize Weights
# -----------------------------
def initialize_network():
    network = [
        [[random.uniform(-1,1) for _ in range(3)] for _ in range(2)],  # Hidden layer (2 neurons, 2 inputs + bias)
        [[random.uniform(-1,1) for _ in range(3)]]  # Output layer (1 neuron, 2 hidden + bias)
    ]
    return network

# -----------------------------
# Forward Propagation
# -----------------------------
def forward_propagate(network, inputs):
    hidden_outputs = []
    
    for neuron in network[0]:
        activation = neuron[-1]  # bias
        for i in range(len(inputs)):
            activation += neuron[i] * inputs[i]
        hidden_outputs.append(sigmoid(activation))
    
    final_outputs = []
    for neuron in network[1]:
        activation = neuron[-1]
        for i in range(len(hidden_outputs)):
            activation += neuron[i] * hidden_outputs[i]
        final_outputs.append(sigmoid(activation))
    
    return hidden_outputs, final_outputs

# -----------------------------
# Backpropagation
# -----------------------------
def train_network(network, training_data, lr, epochs):
    for epoch in range(epochs):
        total_error = 0
        
        for row in training_data:
            inputs = list(map(float, row[:-1]))
            expected = float(row[-1])
            
            hidden_outputs, outputs = forward_propagate(network, inputs)
            
            error = expected - outputs[0]
            total_error += error**2
            
            # Output layer delta
            delta_output = error * sigmoid_derivative(outputs[0])
            
            # Hidden layer deltas
            deltas_hidden = []
            for i in range(len(hidden_outputs)):
                deltas_hidden.append(
                    delta_output * network[1][0][i] * sigmoid_derivative(hidden_outputs[i])
                )
            
            # Update output weights
            for i in range(len(hidden_outputs)):
                network[1][0][i] += lr * delta_output * hidden_outputs[i]
            network[1][0][-1] += lr * delta_output  # bias
            
            # Update hidden weights
            for i in range(len(network[0])):
                for j in range(len(inputs)):
                    network[0][i][j] += lr * deltas_hidden[i] * inputs[j]
                network[0][i][-1] += lr * deltas_hidden[i]  # bias
        
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error = {total_error:.4f}")

# -----------------------------
# Predict
# -----------------------------
def predict(network, row):
    _, outputs = forward_propagate(network, row)
    return round(outputs[0])

# -----------------------------
# Main
# -----------------------------
data = load_data("ann_data.csv")
training_data = data[1:]

network = initialize_network()

train_network(network, training_data, lr=0.5, epochs=5000)

print("\nTesting Network:")

for row in training_data:
    inputs = list(map(float, row[:-1]))
    prediction = predict(network, inputs)
    print(f"Input: {inputs} -> Predicted: {prediction}")
