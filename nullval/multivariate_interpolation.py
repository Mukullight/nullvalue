# Bilinear interpolation 
"""
def bilinear_interpolation(x, y, points):

    Perform bilinear interpolation to find the value at point (x, y) given
    the points around it.

    Parameters:
    - x (float): x-coordinate where interpolation is performed.
    - y (float): y-coordinate where interpolation is performed.
    - points (dict): Dictionary containing the corner points and their values:
                     { (x1, y1): f(x1, y1), (x1, y2): f(x1, y2),
                       (x2, y1): f(x2, y1), (x2, y2): f(x2, y2) }

    Returns:
    - interpolated_value (float): Interpolated value at point (x, y).

    # Extract points
    (x1, y1), (x2, y2) = points.keys()

    # Ensure the points are in the correct order
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    # Ensure (x, y) is within the range
    x = max(min(x, x2), x1)
    y = max(min(y, y2), y1)

    # Bilinear interpolation formula
    fQ11 = points[(x1, y1)] * (x2 - x) * (y2 - y)
    fQ21 = points[(x2, y1)] * (x - x1) * (y2 - y)
    fQ12 = points[(x1, y2)] * (x2 - x) * (y - y1)
    fQ22 = points[(x2, y2)] * (x - x1) * (y - y1)

    interpolated_value = (fQ11 + fQ21 + fQ12 + fQ22) / ((x2 - x1) * (y2 - y1))

    return interpolated_value
"""




# Bicubic interpolation 





# trilinear interpolation 

# multivariate interpolation 

# Radical basis interpolation 
