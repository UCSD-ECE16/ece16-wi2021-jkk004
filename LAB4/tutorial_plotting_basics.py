
import matplotlib.pyplot as plt
import numpy as np
a = np.array([[1,2,3,4],[1,4,9,16]])
plt.clf()
plt.plot(a)
plt.show()
x = [1,2,3,4]  # x data vector (as a list)
y = [1,4,9,16] # y data vector (as a list)
plt.clf()      # clear any existing plot
plt.plot(x,y)  # write the data onto the figure buffer
plt.show()     # show the figure

#I believe for the numpy array, the first array was the starting Y intercept and the 2nd array is where the numbers end
#up when the value of x is 1. 4 went to 16, 3 went to 9, etc,

a = np.array([[1,2,3,4],[1,4,9,16]])
x = a[0,:] #index from a to get [1,2,3,4]
y = a[1,:] #index from a to get [1,4,9,16]
plt.title("First plot!")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,x)
plt.plot(x,y)
plt.show()
plt.clf()
plt.subplot(211)
plt.plot([1,2,3,4],[1,4,9,16])
plt.subplot(212)
plt.plot([1,2,3,4],[4,2,1,6])
plt.show()
