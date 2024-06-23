import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the ReLU activation function class


class ReLUActivateFunction(nn.Module):
    def __init__(self):
        super(ReLUActivateFunction, self).__init__()

    def forward(self, x):
        return F.relu(x)

# Define the Sigmoid activation function class


class SigmoidActivateFunction(nn.Module):
    def __init__(self):
        super(SigmoidActivateFunction, self).__init__()

    def forward(self, x):
        return torch.sigmoid(x)


# Create instances of the activation function classes
relu_function = ReLUActivateFunction()
sigmoid_function = SigmoidActivateFunction()

# Define the input tensor
input_tensor = torch.tensor([1, -5, 1.5, 2.7, -5])

# Apply the ReLU and Sigmoid functions to the input tensor
relu_output = relu_function(input_tensor)
sigmoid_output = sigmoid_function(input_tensor)

print(f"ReLU: {relu_output}")
print(f"Sigmoid: {sigmoid_output}")
