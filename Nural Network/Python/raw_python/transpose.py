#just wanted to see how fun doing transpose actully is
import numpy as np

matrix = [[2.5,2.6,4.5,8.7],
          [9.8,10.0,4.5,5.6],
          [3.4,2.3,9.6,4.5]]
orignal_output = (np.array(matrix))
print(orignal_output)
print("#----------------------------#")
new_output = (np.array(matrix).T)
print(new_output)