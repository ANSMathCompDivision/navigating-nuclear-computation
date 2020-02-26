import math
import matplotlib.pyplot as plt

############################
#   Objective 1 solution   #
############################

def calculate_activity_with_time(nuclide_decay_constant,
                                 initial_concentration, time):
    """
    This function calculates the activity of a radionuclide

    input: decay constant for a radionuclide [1/seconds], initial
            concentration of atoms, time [seconds]
    output: activity [particles/second]
    """
    activity = initial_concentration * nuclide_decay_constant * math.exp(-1.0 * nuclide_decay_constant * time)
    return activity

# Solution to example question: 8.019e+17 particles/second

############################
#   Objective 2 solution   #
############################

def calculate_particles_with_distance(distance_from_source, body_surface_area, initial_concentration):
    """
    This function calculates the total number of particles hitting a body at distance
    `distance_from_source` away from the source.

    Assumptions:
    The area of a human body can be calculated as height*width.

    input: distance_from_source [cm], body_surface_area [cm^2], initial concentration of atoms.
    output: particle rate [particles/second]
    """
    particle_rate = initial_concentration * body_surface_area / (4.0 * math.pi * distance_from_source * distance_from_source)
    return particle_rate

# Solution to example question: 133.074 particles/second

############################
#   Objective 3 solution   #
############################

def calculate_shield_attenuation(macroscopic_cross_section, thickness, initial_intensity):
    """
    This function calculates the change in particle rate given a shield of a
    specific thickness.

    input: macroscopic_cross_section [1/cm], thickness [cm], initial_intensity
           [particles/second]
    output: particle intensity [particles/second]
    """
    particle_intensity = initial_intensity * math.exp(-1.0 * thickness * macroscopic_cross_section)
    return particle_intensity

# Solution to example question: 4.493e14 particles/second

############################
#   Objective 4 solution   #
############################

def calculate_activity_of_all_effects(elapsed_time, distance_away, shield_thickness, initial_concentration):
    activity_time = calculate_activity_with_time(1.0, initial_concentration, elapsed_time)
    activity_distance = calculate_particles_with_distance(distance_away, 1.0, 1.0)
    activity_shield = calculate_shield_attenuation(0.5, shield_thickness, 1.0)
    particle_rate = activity_time * activity_distance * activity_shield
    return particle_rate

# Solution to example question: 2.383e5 particles/second

############################
#  Extra credit solutions  #
############################

# Plot of activity versus time
# Assumptions:
times = [0, 1, 5, 10, 15, 25, 50]
activity = []
for t in times:
    activity.append(calculate_activity_with_time(1.0, 1e15, t))
plt.plot(times, activity)
# Or on a log scale
# plt.semilogy(times, activity)
plt.xlabel("Time [s]")
plt.ylabel("Activity [particles/s]")
plt.savefig("activity-vs-time.pdf")


# Plot of particle rate versus distance
# Assumptions:
distances = [1, 10, 20, 30, 40, 50, 100]
activity = []
for d in distances:
    activity.append(calculate_particles_with_distance(d, 1, 1e15))
plt.plot(distances, activity)
# Or on a log scale
# plt.semilogy(distances, activity)
plt.xlabel("Distance [cm]")
plt.ylabel("Activity [particles/s]")
plt.savefig("activity-vs-distance.pdf")

# Plot of particle intensity versus shield thickness
# Assumptions
thicknesses = [1, 10, 20, 30, 40, 50, 100]
activity = []
for t in thicknesses:
    activity.append(calculate_shield_attenuation(0.2, t, 1e15))
plt.plot(thickness, activity)
# Or on a log scale
# plt.semilogy(thickness, activity)
plt.xlabel("Thickness [cm]")
plt.ylabel("Intensity [particles/s]")
plt.savefig("activity-vs-thickness.pdf")

# Plot of particle intensity versus shield material
# Assumptions
macro_cross_section = [0.1, 0.2, 0.5, 0.9, 0.99999]
activity = []
for m in macro_cross_section:
    activity.append(calculate_shield_attenuation(m, 10, 1e15))
plt.plot(macro_cross_section, activity)
# Or on a log scale
# plt.semilogy(macro_cross_section, activity)
plt.xlabel("Macroscopic cross section [1/cm]")
plt.ylabel("Intensity [particles/s]")
plt.savefig("activity-vs-material.pdf")
