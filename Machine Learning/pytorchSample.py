import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Step 1: Create a simple dataset
# Let's create a dataset for a simple linear regression: y = 2x + 1
x = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[3.0], [5.0], [7.0], [9.0], [11.0]])

dataset = TensorDataset(x, y)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Step 2: Define a neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleNet()

# Step 3: Define loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Step 4: Train the network
num_epochs = 100
for epoch in range(num_epochs):
    for batch_x, batch_y in dataloader:
        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 5: Make predictions
with torch.no_grad():
    test_input = torch.tensor([[6.0]])
    prediction = model(test_input)
    print(f'Prediction for input 6.0: {prediction.item():.4f}')
