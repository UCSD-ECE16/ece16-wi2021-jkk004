import numpy as np
import random


#Question 1
a = np.array([0, 10, 4, 12])
b = a -12
print(b)
#When I subtract, every element in the array got subtracted by 12. INTERESTING!

#Question 2
c = np.array([[0, 10, 4, 12], [1, 20, 3, 41]])
array_2 = c[0, 2:4], c[1, 0:2]
print(array_2)

#I just sliced each array individually

#Question 3
t = [0, 10, 4, 12]
jimmy = np.hstack((t,t))
timmy = np.vstack((jimmy, jimmy, jimmy, jimmy))
print(timmy)
#I made jimmy have two arrays combined to make one row, then I vertically stacked all the jimmy to make a full timmy

#Question 4
array41 = np.arange(-3, 21, 6)
print(array41)
array42 = np.arange(-7,-21,-2)
print(array42)

#Question 5
haha = np.linspace(0, 100, 49, True)
print(haha)
#I feel numbers that include decimals will use linspace but Im not too sure

#Question 6
array6 = np.array([[12, 3, 1, 2], [0, 0, 1, 2], [4,2,3, 1]])
#FUN!

#Question 7
string7 = "1,2,3,4"
arr = []
start = -2
while len(arr) != 4:
    arr += (string7[start+2])
    start += 2
massive = []
while len(massive) != 100:
    random.shuffle(arr)
    if len(massive) == 0:
        massive += arr
    else:
        massive = np.vstack((massive, arr))
print(massive)
#I wasn't sure if you wanted it randomized so I just included the random.shuffle(arr) just in case to shuffle the array
