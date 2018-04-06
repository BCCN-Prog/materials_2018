import numpy as np

from maxima import find_maxima

def test_simple_sequence_two_maxima():
    inp = [0, 1, 2, 1, 2, 1, 0]
    out = find_maxima(inp)
    exp = [2, 4]
    assert exp == out

def test_simple_sequence_one_maximum():
    inp = [-i**2 for i in range(-3, 4)]
    out = find_maxima(inp)
    exp = [3]
    assert exp == out

def test_sine_wave():
    inp = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    out = find_maxima(inp)
    exp = [16,78]
    assert exp == out

# additional tests for
# - max on both borders
#   x = [4, 2, 1, 3, 1, 2]
# - max on both borders, absolute max on right border
#   x = [4, 2, 1, 3, 1, 5]
# - one max (absolute) on left border
#   x = [4, 2, 1, 3, 1]
# - plateau
#   x = [1, 2, 2, 1]
#   (decide for a sensible output in this case)
# - test cases for plateau
#   x = [1, 2, 2, 3, 1]
#   x = [1, 3, 2, 2, 1]
#   x = [3, 2, 2, 3]
