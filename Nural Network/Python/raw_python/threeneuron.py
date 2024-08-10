#this are 4 inputs here with 3 neurons where each neuron has a it's own weight, it's own bias and there will be 3 outputs
inputs = [1,2,3,0.2,0.8]
weights1 = [1.5,2.3,4.3,-1.2]
weights2 = [1.5,2.3,4.3,-1.2]
weights3 = [1.5,2.3,4.3,-1.2]
bias1 = 2
bias2 = 3
bias3 = 0.5
#here we'll put everything in a list and then execute
output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + bias3]

print(output)
