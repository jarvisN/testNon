import pandas as pd
import numpy as np
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

# Convert data to tensors
X_tensor = torch.tensor(X, dtype=torch.float)
y_tensor = torch.tensor(y, dtype=torch.long)

# Ensure labels are sequential starting from 0 if they're not
unique_labels, y_tensor = torch.unique(y_tensor, return_inverse=True)

# Creating edge_index
edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)

# Create graph data object
graph_data = Data(x=X_tensor, edge_index=edge_index.contiguous(), y=y_tensor)

print("X_tensor shape:", X_tensor.shape)  # Should show (num_samples, num_features)
print("y_tensor shape:", y_tensor.shape)  # Should show (num_samples,) or (num_samples, num_classes)

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
input_dim = X_tensor.size(1)
hidden_dim = 16  # This is adjustable
output_dim = len(unique_labels)  # Adjusted based on unique labels

model = GCN(input_dim, hidden_dim, output_dim)
print(model)

# Set optimizer and loss function
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
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

# Training loop
for epoch in range(100000):
    loss = train(graph_data)
    print(f'Epoch {epoch+1}: Loss: {loss:.4f}')
    # Append the loss to the loss_values list
    loss_values.append(loss)

# After the training loop, find the epoch with the minimum loss
min_loss_value = min(loss_values)
min_loss_epoch = loss_values.index(min_loss_value) + 1  # Adding 1 because epochs start at 1, not 0

print(f'Minimum loss of {min_loss_value:.4f} occurred at epoch {min_loss_epoch}.')
