# Python-program-that-implements-the-Monte-Carlo-simulation
Python program that implements the Monte Carlo simulation
Assume that the durations for each activity follow a triangular distribution, with the optimistic, most likely, and pessimistic durations as the minimum, mode, and maximum values, respectively. This assumption captures the uncertainty and variability in the durations.

Generate a random sample of durations for each activity using the triangular distribution. This can be done using a random number generator and the triangular distribution function in a programming language such as Python.

Calculate the total duration for the project by summing the durations for each activity.

Repeat steps 2 and 3 a certain number of times (e.g. 500 times) to obtain a sample of total durations for the project.

Analyze the sample of total durations to summarize the results. For example, we can group the durations into ranges (e.g. 30 - 35 days, 36 - 38 days, 39 - 42 days) and compute the likelihood of completion for each range. This can be done using the frequency of occurrence of each range in the sample.

Here is a Python program that implements the Monte Carlo simulation for the project described in the situation:
