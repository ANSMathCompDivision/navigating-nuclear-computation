import math
import matplotlib as plt


#### Objective 1 solution:

def calculate_activity_with_time(nuclide_decay_constant,
                                 initial_concentration, time):
    activity = initial_concentration * math.exp(-1.0 * nuclide_decay_constant * time)
    return activity

# Answers to discussion questions:

# What happens as you vary the initial concentration of atoms?
# The resulting activity increases or decreases proportionally

# How does the activity compare if you have a very short half-life vs. a very long half-life?

# What happens if the length of time you wait is very different from the time of your half life?

# What other functions could you write that would make this function easier to use?


#### Objective 2 solution:

# output: particle rate [particles/second]
def calculate_particles_with_distance(distance_from_source, body_surface_area, initial_concentration):
    particle_rate = initial_concentration * body_surface_area / (4.0 * math.pi * distance_from_source * distance_from_source)
    return particle_rate

# Answers to discussion questions:

# How does changing the distance away from the source affect the total particle rate hitting the body?

# Imagine if Michael Jordan and Simone Biles were both in the room with this source. Would the particle rate that each of them sees be different? How would it differ?
# What would happen if instead of facing the source, you turned sideways so your shoulder was pointing to it?

# Do you think there are assumptions to this equation? What are they? Hint: what happens if you make the distance from the source very small?

# What other functions could you write that would make this function easier to use?


#### Objective 3 solution:
# input: macroscopic_cross_section [1/cm], thickness [cm], initial_intensity [particles/second]
# output: particle intensity [particles/second]
def calculate_shield_attenuation(macroscopic_cross_section, thickness, initial_intensity):
    particle_intensity = initial_intensity * math.exp(-1.0 * thickness * macroscopic_cross_section)
    return particle_intensity

# Answers to discussion questions:
# If you were choosing a shielding material, what type of macroscopic cross section would you look for and why?
# Do you think there are assumptions to this equation?  What are they?

#### Objective 4 solution:
def calculate_activity_of_all_effects(elapsed_time, distance_away, shield_thickness, initial_concentration):
    activity_time = calculate_activity_with_time(1.0, initial_concentration, elapsed_time)
    activity_distance = calculate_particles_with_distance(distance_away, 1.0, 1.0)
    activity_shield = calculate_shield_attenuation(0.5, shield_thickness, 1.0)
    particle_rate = activity_time * activity_distance * activity_shield
    return particle_rate

#### Extra Credit plots:

# Plot of activity versus time
# A plot of particle rate versus distance
# A plot of particle intensity versus shield thickness
# A plot of particle intensity versus shield material
