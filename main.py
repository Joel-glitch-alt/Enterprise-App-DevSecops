# main.py
def sum_of_squares(n=10):
    return sum(i ** 2 for i in range(1, n + 1))

if __name__ == '__main__':
    print(sum_of_squares())  # Optional: for manual testing
