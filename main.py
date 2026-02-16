# Onboarding Project
# Author: Alexander Ezigbo
# Date: February 15, 2026

# This code accomplishes the following:
#   -Converts the timestamps from the can_data.csv into a more readable format,
#   -Generates a Line Graph that shows the change in RPM over time
#   -Generates a Bar Graph to represent the Top 10 most frequent RPM values

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("can_data.csv")


# Convert the timestamps into a more readable format
t0 = df["timestamp"].iloc[0]
df["time (sec)"] = (df["timestamp"] - t0)
df.drop(columns=["timestamp"], inplace=True)

# Reorder the data to move the new column to the front of the data file
new_column = df.pop("time (sec)")
df.insert(0, "time (sec)", new_column)


# Graph #1: Plotting the RPM Over Time
time_in_minutes = df["time (sec)"] / 60

plt.figure()

plt.plot(time_in_minutes ,df["RPM"])

plt.title("RPM Over Time")
plt.ylabel("RPM")
plt.xlabel("Time (mins)")

plt.grid(True)
plt.yscale("linear")
plt.xscale("linear")
plt.tight_layout()

plt.savefig("RPMot.png")
plt.show()




# Graph #2: Plotting the Top 10 most frequent RPM values

# Count how many times each unique number appears
counts = df["RPM"].value_counts().sort_index()

# Create a new series containing the top 10 most frequent RPM values
top_10_counts = counts.sort_values(ascending=False)[:10]

plt.figure()

bars = plt.bar(top_10_counts.index, top_10_counts.values, color="skyblue")

# Add a text above each bar the contains the RPM value
for bar, x_val in zip(bars, top_10_counts.index):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{x_val}",
        ha="center",
        va="bottom"
    )

# Plot the RPM Values
plt.xlabel("RPM")
plt.ylabel("Frequency")
plt.title("Frequency of Top 10 RPM Values")
plt.tight_layout()

plt.savefig("RPMfreq.png")
plt.show()

