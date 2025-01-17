import math
import statistics

values = []
for i in range(24):
    x = i * math.pi / 12
    values.append(math.fabs(math.sin(x)))

mean = statistics.mean(values)
print("Average absolute value of sin in the interval [0, 2π) is", mean)
