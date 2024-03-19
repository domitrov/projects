import matplotlib.pyplot as plt

# Define stomatal density (number of stomata per unit area)
stomatal_densities = [100, 200, 300, 400, 500]

# Define transpiration rates (proportional to stomatal density)
transpiration_rates = [density * 1.5 for density in stomatal_densities]

# Create a bar chart
plt.bar(stomatal_densities, transpiration_rates)

# Set labels and title
plt.xlabel("Stomatal Density (#/unit area)")
plt.ylabel("Transpiration Rate (arbitrary units)")
plt.title("Relationship Between Stomatal Density and Transpiration Rate")

# Show the plot
plt.show()