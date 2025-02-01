import pandas as pd
import matplotlib.pyplot as plt

# Load the data with the correct file path
df = pd.read_csv("data/sc_waterdata.csv")

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["Temperature"], df["Dissolved Oxygen"], color='blue', alpha=0.7, edgecolors='black')

# Labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Dissolved Oxygen (mg/L)")
plt.title("Scatter Plot of Dissolved Oxygen vs. Temperature")
plt.grid(True)

# Save the plot
plt.savefig("images/scatter_plot.png")  # Saves the plot to the images folder
plt.show()
