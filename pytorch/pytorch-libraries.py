import torch
import torch.optim as optim
# This is the entire forward pass using torch.nn.Linear
# input will has 1 feature, the output has 1 value
D_in = 1
D_out = 1

x = torch.randn(10, D_in)

true_W = torch.tensor([[2.0]])
true_b = torch.tensor([[1.0]])
y_true = x @ true_W + true_b + torch.randn(10, D_out) * .1

linear_layer = torch.nn.Linear(in_features=D_in, out_features=D_out)

print(f"Layer's Weight (W): {linear_layer.weight}\n")
print(f"Layer's bias (b): {linear_layer.bias}\n")

y_hat_nn = linear_layer(x)

print(f"Output of nn.Linear (first 3 rows): {y_hat_nn[:3]}")


#Recreating the LinearRegressionModel and the forward pass without all of the loose tensors
class LinearRegressionModel(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.linear_layer = torch.nn.Linear(in_features, out_features)

    def forward(self, x):
        return self.linear_layer(x)
    
model = LinearRegressionModel(in_features=1, out_features=1)
print(f"Model Architecture:\n {model}")


#Optimizer
learning_rate = 0.05

optimizer = optim.Adam(model.parameters(), lr=learning_rate)

loss_fn = torch.nn.MSELoss()

#Professional Loop:
epochs = 100

for epoch in range(epochs):
    #Step 1: Forward pass
    y_hat = model(x)

    #Step 2: Loss Calculation
    loss = loss_fn(y_hat, y_true)

    #Step 3: The Three-line Mantra
    optimizer.zero_grad() #Zero our gradients

    loss.backward() #Go backward and find our gradients and direction

    optimizer.step() #Update the parameters

    if epoch % 10 == 0:
        print(f"Epoch {epoch:02d}: Loss = {loss.item():.4}")
