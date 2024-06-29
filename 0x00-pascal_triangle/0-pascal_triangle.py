def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    
    :param n: Number of rows of Pascal's Triangle to generate.
    :type n: int
    :return: A list of lists representing Pascal's Triangle.
    :rtype: list
    """
    # If n is 0 or negative, return an empty list
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate each row from 1 to n-1
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        
        # Calculate the values inside the row
        for j in range(1, i):
            # Each value is the sum of the two values directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

