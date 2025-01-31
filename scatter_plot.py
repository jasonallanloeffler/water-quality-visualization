import pandas as pd
import matplotlib.pyplot as plt

# Load the data (replace 'sc_waterdata.csv' with your actual file name)
df = pd.read_csv("sc_waterdata.csv")

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["Temperature"], df["Dissolved Oxygen"], color='blue', alpha=0.7, edgecolors='black')

# Labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Dissolved Oxygen (mg/L)")
plt.title("Scatter Plot of Dissolved Oxygen vs. Temperature")
plt.grid(True)

# Show the plot
plt.show()
