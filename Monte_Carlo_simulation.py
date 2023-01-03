import random

# Triangular distribution function
def triangular(min_val, mode, max_val):
    u = random.uniform(0, 1)
    if u < (mode - min_val) / (max_val - min_val):
        return min_val + (max_val - min_val) * (u * (mode - min_val)) ** 0.5
    else:
        return max_val - (max_val - min_val) * ((1 - u) * (max_val - mode)) ** 0.5

# Monte Carlo simulation
num_simulations = 500
durations = []

for i in range(num_simulations):
    duration_a = triangular(8, 10, 12)
    duration_b = triangular(10, 12, 14)
    duration_c = triangular(12, 14, 16)
    total_duration = duration_a + duration_b + duration_c
    durations.append(total_duration)

# Compute likelihood of completion for each range
range_30_35 = 0
range_36_38 = 0
range_39_42 = 0

for duration in durations:
    if duration >= 30 and duration <= 35:
        range_30_35 += 1
    elif duration > 35 and duration <= 38:
        range_36_38 += 1
    elif duration > 38 and duration <= 42:
        range_39_42 += 1

# Print results
print("Duration (in days)   Likelihood of Completion")
print("30 - 35              {}".format(range_30_35 / num_simulations))
print("36 - 38              {}".format(range_36_38 / num_simulations))
print("39 - 42              {}".format(range_39_42 / num_simulations))