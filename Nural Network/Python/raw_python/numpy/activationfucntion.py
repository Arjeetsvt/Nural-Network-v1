#now the main idea over here is, that as the code get's bigger we'll need a forward method and a backward method
#which can be possibe in a ReLu
import numpy as np

np.random.seed(0)

#using a used dataset
def spiral_data(points, classes):#point is classes and classes is how many classes
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

X =  [[2.5,2.6,4.5,8.7],
     [9.8,10.0,4.5,5.6],
     [3.4,2.3,9.6,4.5]]


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons) -> None:
        self.weights = 0.5*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,3)

print("Layer 1")
layer1.forward(X)
print(layer1.output)
print("Layer 2")
layer2.forward(layer1.output)
print(layer2.output)

#not complete yet

