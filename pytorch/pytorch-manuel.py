import torch

# Our batch of data will have 10 data points
N = 10
# Each data point ahas 1 input feature and 1 output value
D_in = 1
D_out = 1

#Create our input data X
x = torch.randn(N, D_in)

#Create our true targe labels y by using the "true" W and b
true_W = torch.tensor([[2.0]])
true_b = torch.tensor([[1.0]])
y_true = x @ true_W + true_b + torch.randn(N, D_out) * .1
 
#Initialize our parameters with random values
#Shapes must be correct for matrix multiplication!

W = torch.randn(D_in, D_out, requires_grad=True)
b = torch.randn(1, requires_grad=True)

print(f"Initial weight W:{W}\n")
print(f"Initial bias b:{b}\n")

y_hat = x @ W + b

print(f"y-hat = {y_hat}\n")
print(f"true y = {y_true[:3]}\n")

error = y_hat - y_true
squared_error = error ** 2
loss = squared_error.mean()

print(f"Our loss is: {loss}\n ")

#computes gradients
loss.backward()

print(f"Gradient for W: {W.grad}\n")
print(f"Gradient for b: {b.grad}\n")

#Hyperparameters
learning_rate , epochs = 0.05, 100

W, b = torch.randn(1, 1, requires_grad=True), torch.randn(1, requires_grad=True)

for epoch in range(epochs):
    #First do our Forward pass:
    y_hat = x @ W + b
    #Second calculate our loss:
    loss = torch.mean((y_hat - y_true)**2)

    #Third do our backward pass to find our gradients and direction
    loss.backward()

    #Fourth update/nudge our parameters to the correct value and direction gathered from loss.backward()
    with torch.no_grad():
        W -= learning_rate * W.grad; b -= learning_rate * b.grad
    
    #Fith, Zero out or reset our gradiendts for the next round of learning
    W.grad.zero_(); b.grad.zero_()

    if epoch % 10 == 0:
        print(f"Epoch {epoch:02d}: Loss = {loss.item():.4f}, W = {W.item():.3f}, b = {b.item():.3f}")

print(f"\nFinal parameters: W = {W.item():.3f}, b = {b.item():.3f}")
print(f"True Parameters: W = {true_W}, b = {true_b}\n")


# input will has 1 feature, the output has 1 value
D_in = 1
D_out = 1

x = torch.randn(10, D_in)


linear_layer = torch.nn.Linear(in_features=D_in, out_features=D_out)

print(f"Layer's Weight (W): {linear_layer.weight}\n")
print(f"Layer's bias (b): {linear_layer.bias}\n")

y_hat_nn = linear_layer(x)

print(f"Output of nn.Linear (first 3 rows): {y_hat_nn[:3]}")