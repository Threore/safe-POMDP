# Constants file
#
# SampleForSafeMDP and sampleForSafeMDPTU both use this file to instantiate constants.
# This means that you only have 1 place that both testing method use so you can more easily compare them.

# Safety threshold
h = -0.25

# Lipschitz
L = 0

# Scaling factor for confidence interval
beta = 2

# Define world
world_shape = (10, 10)
step_size = (1.0, 1.0)
num_iterations = 100


#  choose world
pylonWorld = True  # Use pylon world if true, otherwise use normal GP sampling
offset = 20  # pylon world size
scaling = 0.3  # scaling factor in z direction
