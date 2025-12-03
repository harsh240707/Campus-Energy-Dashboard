# models.py
class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        peak = max(self.meter_readings, key=lambda r: r.kwh).kwh if self.meter_readings else 0
        return f"Building: {self.name}\nTotal Consumption: {total} kWh\nPeak Reading: {peak} kWh\n"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_building(self, building):
        self.buildings[building.name] = building

    def get_building(self, name):
        return self.buildings.get(name)
