import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots




def trigonometric_interpolation(x, y, x_new):
    """
    Performs trigonometric interpolation for the given data points.

    Parameters:
    x (array-like): x-coordinates of the data points.
    y (array-like): y-coordinates of the data points.
    x_new (array-like): New x-coordinates for which to compute interpolated y values.

    Returns:
    np.ndarray: Interpolated y-values corresponding to x_new.
    """
    N = len(x)
    if N % 2 == 0:
        k = np.arange(-N//2, N//2)
    else:
        k = np.arange(-(N-1)//2, (N+1)//2)
    
    Y_k = np.fft.fftshift(np.fft.fft(y)) / N
    y_new = np.zeros_like(x_new, dtype=np.complex128)

    for i, k_val in enumerate(k):
        y_new += Y_k[i] * np.exp(2j * np.pi * k_val * x_new / N)
    
    return y_new.real

def plot_trigonometric_interpolation(x_points, y_points, x_new, y_new):
    """
    Plot the original data points and the interpolated values using Plotly.

    Parameters:
    x_points (array-like): Known x-values of the data points.
    y_points (array-like): Known y-values of the data points.
    x_new (array-like): New x-values at which y-values were interpolated.
    y_new (array-like): Interpolated y-values at x_new points.
    """
    fig = make_subplots(rows=1, cols=1)

    # Scatter plot of original data points
    fig.add_trace(
        go.Scatter(x=x_points, y=y_points, mode='markers', name='Data Points', marker=dict(color='black')),
        row=1, col=1
    )

    # Line plot of interpolated values
    fig.add_trace(
        go.Scatter(x=x_new, y=y_new, mode='lines', name='Trigonometric Interpolation', line=dict(color='red')),
        row=1, col=1
    )

    # Update layout
    fig.update_layout(
        title='Trigonometric Interpolation',
        xaxis_title='x',
        yaxis_title='y',
        showlegend=True,
        legend=dict(x=0.7, y=1.1),
        template='plotly_white'
    )

    # Show plot
    fig.show()

'''
# Example usage:
x_points = np.linspace(0, 2 * np.pi, 10)
y_points = np.sin(x_points)

# Generate new x values for plotting
x_new = np.linspace(min(x_points), max(x_points), 1000)
# Compute interpolated y values
y_new = trigonometric_interpolation(x_points, y_points, x_new)

# Plot using plot_trigonometric_interpolation function
plot_trigonometric_interpolation(x_points, y_points, x_new, y_new)
'''
