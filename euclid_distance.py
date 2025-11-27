def calculate_euclidean_distance(point1, point2):
    """
    Calculates the Euclidean distance between two Cartesian points.
    Input: Two tuples, e.g., (x1, y1) and (x2, y2)
    Output: The distance (float)
    """
    
    # 1. Unpack the coordinates (Store Cartesian coordinate )
    x1, y1 = point1
    x2, y2 = point2
    
    # 2. Calculate the differences (The legs of the triangle)
    x_diff = x2 - x1
    y_diff = y2 - y1
    
    # 3. Pythagorean Theorem: a^2 + b^2 = c^2 [cite: 6, 8]
    # We square the differences
    a_squared = x_diff ** 2
    b_squared = y_diff ** 2
    
    # 4. Solve for c (Distance) 
    # Taking the power of 0.5 is the same as square root, avoiding libraries 
    distance = (a_squared + b_squared) ** 0.5
    
    return distance

# --- Main Execution ---

# Define points using Tuples (Simple way to store coordinates)
# Using decimals (floats) hits Difficulty 3 
point_a = (1.5, 2.0) 
point_b = (4.5, 6.0)

# Link the actions together [cite: 8]
result = calculate_euclidean_distance(point_a, point_b)

print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print(f"The Euclidean distance is: {result}")