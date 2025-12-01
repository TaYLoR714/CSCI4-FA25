#python



def calculate_euclid_distance(point_1, point_2):
    
#Euclidean Distance
#Input: x1, y1  /  x2, y2
#Output: Euclidean distance
    
    
    x1, y1 = point_1     # Coords
    x2, y2 = point_2
    
    x_diff = x2 - x1    # Calculate the line of the triangle
    y_diff = y2 - y1
    

    a_squared = x_diff ** 2     # a^2 + b^2 = c^2 
    b_squared = y_diff ** 2     
    
     
    
    distance = (a_squared + b_squared) ** 0.5     # Power of 0.5 is the same as square root (google helped me find out this operation)
    
    return distance




point_x = (2.5, 5.0)     # Define points
point_y = (5.5, 8.0)


result = calculate_euclid_distance(point_x, point_y)   

print(f"Point X: {point_x}")
print(f"Point Y: {point_y}")
print(f"Euclidean distance = {result}")