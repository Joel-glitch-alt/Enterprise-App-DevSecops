import sys
import os

# Add root directory (parent of test/) to Python's import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main import sum_of_squares

def test_sum_of_squares_default():
    assert sum_of_squares() == 385  # 1^2 + 2^2 + ... + 10^2 = 385

def test_sum_of_squares_custom():
    assert sum_of_squares(3) == 14  # 1^2 + 2^2 + 3^2 = 14
