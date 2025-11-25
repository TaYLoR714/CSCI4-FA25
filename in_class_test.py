#python
import array as array


def f(x,y,z):
    if (z==0):
        print("sum", x+y)
    elif (z==1):
        print("difference", abs(x-y))
    else:
        print("z =/= {0,1}")

f(1,1,0) #guess sum 3
f(1,2,1) #guess difference 1
f(1,2,5) #guess string in the else statement


x = 5  #x represents left right
y = 6  #y represnets down up
# index 0 represnes x coord, index 1 represents y coord
point = [x,y]

point_dict = {'x': 5, 'y': 6}

print("point at 0:", point[0])
print("point_dict at 'x':", point_dict['x'])


import math

def euclidean_distance(point1, point2):
    #Calculates the Euclidean distance between two points.

    
    #point1 : Coordinates of the first point.
    #point2 : Coordinates of the second point.

    #Returns: float: The Euclidean distance between the two points.

    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")

    squared_diff_sum = 0
    for i in range(len(point1)):
        squared_diff_sum += (point2[i] - point1[i]) ** 2

    return math.sqrt(squared_diff_sum)

# Example usage
p1 = [1, 2, 3]
p2 = [4, 6, 9]
distance = euclidean_distance(p1, p2)
print(f"Euclidean distance between {p1} and {p2}: {distance}")
p1 = [2, 4, 6]
p2 = [1, 8, 7]
distance = euclidean_distance(p1, p2)
print(f"Second Euclidean distance between {p1} and {p2}: {distance}")
p1 = [2, 4]
p2 = [-1, -8]
distance = euclidean_distance(p1, p2)
print(f"Second Euclidean distance between {p1} and {p2}: {distance}")

