import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from pydantic 

def li_int(x_points, y_points, x_new):
    """
    Perform linear interpolation on a set of data points.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which to interpolate the y-values.

    Returns:
    array-like: Interpolated y-values at x_new points.
    """
    # Input validation
    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length")
    if not (np.all(np.diff(x_points) > 0) or np.all(np.diff(x_points) < 0)):
        raise ValueError("x_points must be strictly monotonic (either increasing or decreasing)")

    # Perform linear interpolation
    interpolator = interp1d(x_points, y_points, kind='linear')
    y_new = interpolator(x_new)

    return y_new

def plot_li_int(x_points, y_points, x_new, y_new):
    """
    Plot the original data points and the interpolated values.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which y-values were interpolated.
    y_new (array-like): Interpolated y-values at x_new points.
    """
    plt.scatter(x_points, y_points, label='Data points', color='black')
    plt.plot(x_new, y_new, label='Linear Interpolation', linestyle='--', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Interpolation')
    plt.legend()
    plt.grid(True)
    plt.show()


