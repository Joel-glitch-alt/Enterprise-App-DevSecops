# main.py
def sum_of_squares(n=10):
    return sum(i ** 2 for i in range(1, n + 1))

if __name__ == '__main__':
    print("Calculating the sum of squares from 1 to 10...")
    print(f"Result: {sum_of_squares()}")  # Optional: for manual testing
