import pytest
import numpy as np
from plotly.io import to_json
import nullval
from nullval import trigonometric_interpolation
#from trigonometric_interpolation import trigonometric_interpolation, plot_trigonometric_interpolation
'''
def test_trigonometric_interpolation_simple():
    """
    Test trigonometric interpolation with simple known data points.
    """
    N = 100000000000
    x = np.linspace(0, 2 * np.pi, N)
    y = np.sin(x)
    x_new = np.linspace(0, 2 * np.pi, 1000)
    y_new = trigonometric_interpolation(x, y, x_new)
    mae = np.mean(np.abs(y_new - np.sin(x_new)))
    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert mae <= 0.01, f"Mean Absolute Error {mae} is greater than 0.01"


def test_trigonometric_interpolation_single_point():
    """
    Test trigonometric interpolation with a single data point.
    """
    x = np.array([0])
    y = np.array([1])
    x_new = np.linspace(-np.pi, np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)
    
    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.all(y_new == 1), "Interpolated values do not match expected constant value"

def test_trigonometric_interpolation_cosine():
    """
    Test trigonometric interpolation with cosine data points.
    """
    x = np.linspace(0, 2 * np.pi, 10)
    y = np.cos(x)
    x_new = np.linspace(0, 2 * np.pi, 100)
    y_new = trigonometric_interpolation(x, y, x_new)
    
    assert len(y_new) == len(x_new), "Interpolated y-values length mismatch"
    assert np.allclose(y_new, np.cos(x_new), atol=0.1), "Interpolated values do not match expected cosine values"

@pytest.mark.timeout(30)
def test_plot_trigonometric_interpolation_runs():
    """
    Test that the plot_trigonometric_interpolation function runs without errors.
    """
    x_points = np.linspace(0, 2 * np.pi, 10)
    y_points = np.sin(x_points)
    x_new = np.linspace(0, 2 * np.pi, 100)
    y_new = trigonometric_interpolation(x_points, y_points, x_new)
    
    fig = trigonometric_interpolation.plot_trigonometric_interpolation(x_points, y_points, x_new, y_new)
    fig_json = to_json(fig)
    assert fig_json is not None, "Plotly figure JSON is None"




'''
