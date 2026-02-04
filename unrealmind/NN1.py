import math
#activation function (sigmoid)
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

#single neuron function
def neuron(inputs, weights, bias):
    #weighted sum
    z=0
    for i in range(len(inputs)):
        z += inputs[i] * weights[i]
    z += bias
    #activation
    output = sigmoid(z)
    return output
# example values
inputs = [1.0, 0.5, -1.5]
weights = [0.8, -0.2, 0.1]
bias = 0.5

result = neuron(inputs, weights, bias)
print("Neuron output:", result)

print("inputs:", inputs)
print("weights:", weights)
print("bias:", bias)
print("result:", result)