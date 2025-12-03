# Campus-Energy-Dashboard

## Project Overview
The **Campus Energy Dashboard** is a comprehensive Python-based project designed to help campus facilities teams analyze electricity usage across multiple buildings. By ingesting raw meter data, performing data validation, aggregating statistics, applying object-oriented modeling, and generating visual dashboards, this project enables administrators to make informed energy-saving decisions.

This project serves as a capstone example of **data handling, analytical logic, OOP design, and visual storytelling** in Python.

---

## Objectives
By completing this project, you will be able to:
- Read and validate multiple datasets using **Pandas**.
- Design **object-oriented models** for real-world energy systems.
- Perform **time-series** and **categorical aggregations**.
- Create effective **multi-chart visualizations** for analysis.
- Automate **data export** and **report generation**.
- Summarize insights to aid **administrative decision-making**.

---

## Key Features
1. **Data Ingestion and Validation**
   - Automatically detects and reads all CSV files in the `/data/` folder.
   - Handles missing files or corrupt rows using error handling.
   - Adds metadata such as building name and month if missing.
   - Produces a merged DataFrame (`df_combined`) containing all buildings' electricity data.

2. **Aggregation Logic**
   - Calculates **daily totals** and **weekly aggregates** using `.groupby()` and `.resample()`.
   - Generates building-wise summary tables with metrics: total, mean, min, and max consumption.
   - Uses Python functions and dictionaries for clean and modular calculations.

3. **Object-Oriented Design**
   - `MeterReading` class stores individual readings with timestamp and kWh.
   - `Building` class holds multiple readings and methods to calculate totals and generate reports.
   - `BuildingManager` manages multiple building instances, enabling scalability and code reuse.

4. **Visualization**
   - **Trend Line:** Displays daily consumption over time for all buildings.
   - **Bar Chart:** Compares average weekly usage per building.
   - **Scatter Plot:** Highlights peak-hour consumption per building.
   - All charts combined in a single dashboard-style figure (`dashboard.png`).

5. **Persistence and Reporting**
   - Exports cleaned and processed dataset: `cleaned_energy_data.csv`.
   - Saves building summary statistics: `building_summary.csv`.
   - Generates a concise textual report: `summary.txt`.
   - Summary includes total campus consumption, highest-consuming building, peak load time, and visual trend references.

---

## Folder Structure
campus-energy-dashboard/
│
├─ main.py # Runs the full pipeline
├─ data_processing.py # Task 1 & Task 2: Data ingestion, validation, aggregation
├─ models.py # Task 3: OOP classes for buildings and meter readings
└─ README.md # Project documentation

                                                                ****************************************

## Folder Structure

