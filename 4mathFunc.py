# WAP to illustrate various functions of Statistics module

import statistics

# Create a list of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9]

# Printing mean
mean = statistics.mean(numbers)
print("Mean: {}".format(mean))

# Printing the median
median = statistics.median(numbers)
print("Median: {}".format(median))

# Printing the mode (if it exists)
try:
    mode = statistics.mode(numbers)
    print("Mode: {}".format(mode))
except statistics.StatisticsError:
    print("There is no mode.")

# Print the standard deviation
stdev = statistics.stdev(numbers)
print("Standard deviation: {}".format(stdev))
