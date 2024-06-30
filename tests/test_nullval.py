from nullval import __version__
from nullval import linear_interpolation

def test_version():
    assert __version__ == '0.1.0'


def test_linear_interpolation():
    results = linear_interpolation.li_int(2,3,)

