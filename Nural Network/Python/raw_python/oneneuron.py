inputs = [2.5,5.6,6.9] #each input of a neuron
weights = [2.6,2.3,3.4]#earch neuron has a weight
bias = 3#each neuron has a unique bias

#now it's time to output this basic neural network
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
#make sure to go in a whole number sequence
#now print it
print(output)