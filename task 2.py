""" program to find the sum of even valued terms by considering the terms in the fibonacci series
 whose value do not exceed four million"""
def fibonacci_sum_even(limit):
    # Initialize variables
    a, b = 1, 2
    sum_even = 0

    while a <= limit:
        # Check if the current term is even
        if a % 2 == 0:
            sum_even += a

        # Generate the next Fibonacci term
        c = a
        a = b
        b = c+b

    return sum_even

# Find the sum of even-valued Fibonacci terms below four million
limit = 4000000
result = fibonacci_sum_even(limit)
print(result)



