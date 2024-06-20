"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def smallest_num_divisible():
    i = 1
    while True:
        if all(i % x == 0 for x in range(1,21)):
            return i
        i += 1

result = smallest_num_divisible()
print(result)
