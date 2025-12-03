# main.py
import matplotlib.pyplot as plt
from data_processing import load_and_merge_data, calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from models import MeterReading, Building, BuildingManager
import os

# ----------------------------
# Step 1: Load and merge data
# ----------------------------
df = load_and_merge_data()

if df.empty:
    print("No data available to process.")
    exit()

# ----------------------------
# Step 2: Aggregations
# ----------------------------
daily = calculate_daily_totals(df)
weekly = calculate_weekly_aggregates(df)
summary = building_wise_summary(df)

os.makedirs("output", exist_ok=True)
df.to_csv("output/cleaned_energy_data.csv", index=False)
summary.to_csv("output/building_summary.csv", index=False)

# ----------------------------
# Step 3: OOP
# ----------------------------
manager = BuildingManager()
for b_name in df['building'].unique():
    building = Building(b_name)
    for _, row in df[df['building']==b_name].iterrows():
        building.add_reading(MeterReading(row['timestamp'], row['kwh']))
    manager.add_building(building)

# ----------------------------
# Step 4: Visualization
# ----------------------------
fig, axs = plt.subplots(3,1, figsize=(10,15))

# Trend line
for b_name, group in daily.groupby('building'):
    axs[0].plot(group['timestamp'], group['kwh'], label=b_name)
axs[0].set_title("Daily Consumption Trend")
axs[0].set_xlabel("Date")
axs[0].set_ylabel("kWh")
axs[0].legend()

# Weekly bar chart
weekly_avg = weekly.groupby('building')['kwh'].mean()
axs[1].bar(weekly_avg.index, weekly_avg.values, color='skyblue')
axs[1].set_title("Average Weekly Consumption per Building")
axs[1].set_ylabel("kWh")

# Scatter plot: peak per building
peak_per_building = df.groupby('building')['kwh'].max()
axs[2].scatter(peak_per_building.index, peak_per_building.values, color='red')
axs[2].set_title("Peak Hour Consumption per Building")
axs[2].set_ylabel("kWh")

plt.tight_layout()
plt.savefig("output/dashboard.png")
plt.show()

# ----------------------------
# Step 5: Summary
# ----------------------------
total_consumption = df['kwh'].sum()
highest_building = summary.loc[summary['total_kwh'].idxmax(), 'building']
peak_time = df.loc[df['kwh'].idxmax(), 'timestamp']

summary_text = f"""
Campus Energy Summary
----------------------
Total Campus Consumption: {total_consumption} kWh
Highest Consuming Building: {highest_building}
Peak Load Time: {peak_time}
Daily and weekly trends are visualized in dashboard.png
"""

with open("output/summary.txt","w") as f:
    f.write(summary_text)

print(summary_text)
