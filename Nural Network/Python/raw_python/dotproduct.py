#now the dot product begins
import numpy as np

inputs = [1,2,3,2.5]
weights = [[1.5,2.3,4.3,-1.2],
            [2.8,4,7,5.9,-1],
            [2.9,4.3,8.7,-0.3]]

biases = [2,3,0.5]

outputs = np.dot(weights, inputs) + biases
print(outputs)
#can't figure out the answer to this yet