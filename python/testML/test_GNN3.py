import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import torch
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

# Load data
sugar = pd.read_csv("ความหวาน.csv")
# Ensure 'brix(%)' column is numeric and replace NaNs with 0
sugar['brix(%)'] = pd.to_numeric(sugar['brix(%)'], errors='coerce').fillna(0)
# Select a subset of the 'brix(%)' column
valueSugar = sugar['brix(%)'][130:250].to_numpy()

dataSam = pd.read_csv('all_files_t.csv')
dataGraph = dataSam.iloc[:, 1:].values
X = dataGraph.transpose()
y = valueSugar

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Convert data to tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float)
X_test_tensor = torch.tensor(X_test, dtype=torch.float)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# Ensure labels are sequential starting from 0 for the training set
unique_labels, y_train_tensor = torch.unique(y_train_tensor, return_inverse=True)

# For the testing set, you would usually convert labels in a similar way. 
# Ensure the testing set labels match the training label encoding if necessary.

# Creating edge_index
edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)

# Create graph data object for training
graph_data_train = Data(x=X_train_tensor, edge_index=edge_index.contiguous(), y=y_train_tensor)

# It's also a good idea to prepare a graph data object for testing, though its use might differ depending on your evaluation strategy
graph_data_test = Data(x=X_test_tensor, edge_index=edge_index.contiguous(), y=y_test_tensor)

# Define GCN model
class GCN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, output_dim)

    def forward(self, data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x

# Model parameters
input_dim = X_train_tensor.size(1)
hidden_dim = 16
output_dim = len(unique_labels)

model = GCN(input_dim, hidden_dim, output_dim)
print(model)

# Set optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

# Training function
def train(data):
    model.train()
    optimizer.zero_grad()
    out = model(data)
    loss = criterion(out, data.y)
    loss.backward()
    optimizer.step()
    return loss.item()

# Initialize list to store loss values
loss_values = []

# Adjust the training loop to use the graph_data_train
for epoch in range(10):
    loss = train(graph_data_train)
    print(f'Epoch {epoch+1}: Loss: {loss:.4f}')
    loss_values.append(loss)

# Find the epoch with the minimum loss
min_loss_value = min(loss_values)
min_loss_epoch = loss_values.index(min_loss_value) + 1

print(f'Minimum loss of {min_loss_value:.4f} occurred at epoch {min_loss_epoch}.')


# Here, you would add additional code to evaluate the model on the test dataset
