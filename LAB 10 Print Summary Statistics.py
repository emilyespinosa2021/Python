"""
Assignment 11 - Pandas Table with Temperature Data
Submitted by Emily Espinosa
Submitted: March 23, 2025
Assignment 11: This program implements print_temp_by_day_time() to print a table
that shows the average temperature in our labs by day of week and hour of day.
"""
import pandas as pd

DAYS = {
    0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 
    5: "FRI", 6: "SAT"
}

HOURS = {
    0: "Mid-1AM  ", 1: "1AM-2AM  ", 2: "2AM-3AM  ", 3: "3AM-4AM  ", 
    4: "4AM-5AM  ", 5: "5AM-6AM  ", 6: "6AM-7AM  ", 7: "7AM-8AM  ", 
    8: "8AM-9AM  ", 9: "9AM-10AM ", 10: "10AM-11AM", 11: "11AM-NOON", 
    12: "NOON-1PM ", 13: "1PM-2PM  ", 14: "2PM-3PM  ", 15: "3PM-4PM  ", 
    16: "4PM-5PM  ", 17: "5PM-6PM  ", 18: "6PM-7PM  ", 19: "7PM-8PM  ", 
    20: "8PM-9PM  ", 21: "9PM-10PM ", 22: "10PM-11PM", 23: "11PM-MID "
}

class TempDataset:
    """Class to handle temperature data for different days and hours."""

    def __init__(self, name):
        self.name = name
        self.data_loaded = True
        self.sample_data = {
            (0, 0): 68.8, (1, 0): 68.4, (2, 0): 72.7, (3, 0): 71.3, 
            (4, 0): 70.6, (5, 0): 70.7, (6, 0): 66.8,
            (0, 1): 69.0, (1, 1): 68.3, (2, 1): 72.5, (3, 1): 71.1, 
            (4, 1): 70.3, (5, 1): 70.5, (6, 1): 66.9,
            (0, 2): 69.1, (1, 2): 68.3, (2, 2): 72.3, (3, 2): 70.9, 
            (4, 2): 70.0, (5, 2): 70.4, (6, 2): 67.0,
            (0, 3): 69.2, (1, 3): 68.1, (2, 3): 72.2, (3, 3): 70.8, 
            (4, 3): 69.8, (5, 3): 70.3, (6, 3): 67.0
        }

    def get_loaded_temps(self):
        """Check if temperature data is loaded."""
        return self.data_loaded

    def get_avg_temperature_day_time(self, day, hour):
        """Retrieve the average temperature for a specific day and hour."""
        return self.sample_data.get((day, hour), None)

def print_temp_by_day_time(dataset):
    """Prints a formatted table of average temperatures by day and hour."""
    
    if not dataset.get_loaded_temps():
        print("No data loaded.")
        return

    temp_data = {day: [] for day in DAYS.values()}
    
    for hour in HOURS.keys():
        for day in DAYS.keys():
            avg_temp = dataset.get_avg_temperature_day_time(day, hour)
            temp_data[DAYS[day]].append(f"{avg_temp:.1f}" if avg_temp is not None else "---")

    df = pd.DataFrame(temp_data, index=[HOURS[h] for h in HOURS.keys()])
    
    print(f"\nAverage Temperatures for {dataset.name}")
    print("Units are in Fahrenheit\n")
    print(df.to_string())

dataset = TempDataset("Test Week")
print_temp_by_day_time(dataset)


            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    68.8  68.4  72.7  71.3  70.6  70.7  66.8
1AM-2AM    69.0  68.3  72.5  71.1  70.3  70.5  66.9
2AM-3AM    69.1  68.3  72.3  70.9  70.0  70.4  67.0
3AM-4AM    69.2  68.1  72.2  70.8  69.8  70.3  67.0
4AM-5AM     ---   ---   ---   ---   ---   ---   ---
5AM-6AM     ---   ---   ---   ---   ---   ---   ---
6AM-7AM     ---   ---   ---   ---   ---   ---   ---
7AM-8AM     ---   ---   ---   ---   ---   ---   ---
8AM-9AM     ---   ---   ---   ---   ---   ---   ---
9AM-10AM    ---   ---   ---   ---   ---   ---   ---
10AM-11AM   ---   ---   ---   ---   ---   ---   ---
11AM-NOON   ---   ---   ---   ---   ---   ---   ---
NOON-1PM    ---   ---   ---   ---   ---   ---   ---
1PM-2PM     ---   ---   ---   ---   ---   ---   ---
2PM-3PM     ---   ---   ---   ---   ---   ---   ---
3PM-4PM     ---   ---   ---   ---   ---   ---   ---
4PM-5PM     ---   ---   ---   ---   ---   ---   ---
5PM-6PM     ---   ---   ---   ---   ---   ---   ---
6PM-7PM     ---   ---   ---   ---   ---   ---   ---
7PM-8PM     ---   ---   ---   ---   ---   ---   ---
8PM-9PM     ---   ---   ---   ---   ---   ---   ---
9PM-10PM    ---   ---   ---   ---   ---   ---   ---
10PM-11PM   ---   ---   ---   ---   ---   ---   ---
11PM-MID    ---   ---   ---   ---   ---   ---   ---
