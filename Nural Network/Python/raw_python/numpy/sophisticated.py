import numpy as np
#over here we'll set a randomizer so that we can give radom values to weights
np.random.seed(0)

X =  [[2.5,2.6,4.5,8.7],
     [9.8,10.0,4.5,5.6],
     [3.4,2.3,9.6,4.5]]
#over here our input is x
#now we are going to work on the hidden layer as behaviour is not upto us so,
#but it's upto the nural network
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons) -> None:#defining init method
        #-------------------------------------------------------------------------------------------------------------------
        #here we are going to define weights and biasis where weights is set as random 
        # values are in a range like -1<x>1 we want small vlaue so it's range is in negative to positive
        #if we pass value like 1 it will start getting bigger and cause problem, so we are going to nomalize the data set
        #now to actully use the random function on line 3, here is a way to intialize weights
        #-------------------------------------------------------------------------------------------------------------------
        self.weights = 0.5*np.random.randn(n_inputs, n_neurons)
        #in the fucntion "randn()" which tells what's the size of the neuron and how many neurons do we need so here we'll pass
        #a branch tho here we know about the size of our branch but let's put 'n' as it will help in the long run
        #here is how to output this "np.random.randn(4 , 3)" 4 is the inputs form the branch and 3 is the no of neurons
        self.biases = np.zeros((1, n_neurons))
        #here the biases's shape will be 1 multiplied with the number of neurons required
    def forward(self, inputs):#forward method is gonna only take inputs or outputs from the previous layer
        self.output = np.dot(inputs, self.weights) + self.biases

#here we are gonna work on our layers
layer1 = Layer_Dense(4,5)
#now for the layer2 the output of layer 1 will be the input for layer 2 where output can be anything
layer2 = Layer_Dense(5,3)

print("Layer 1")
layer1.forward(X)
print(layer1.output)
print("Layer 2")
layer2.forward(layer1.output)
print(layer2.output)



#here is how to output this "np.random.randn(4 , 3)" 4 is the inputs form the branch and 3 is the no of neurons
#print(0.5*np.random.randn(4, 3))
#specific to code on line 19^^^^ but if the out put which is our weights ofc is coming greater than 1 then multiply it by a 
#whole number which will reuduce that, here I did with 0.5 