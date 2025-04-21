"""
Assignment 9: Reading and using the contents of a file
Submitted by Emily Espinosa
Submitted: March 09, 2025
Assignment 9: This program demonstrates reading and using the contents of a file in Python
"""
import math

class TempDataset:
    """Handles temperature data processing."""
    
    def __init__(self):
        """Sets up an empty dataset."""
        self._data_set = None
    
    def process_file(self, filename):
        """Reads temperature data from a file."""
        try:
            with open(filename, 'r') as file:
                self._data_set = []  
                for line in file:
                    fields = line.strip().split(',')
                    
                    if fields[3] != "TEMP":
                        continue
                    
                    day = int(fields[0])
                    time = math.floor(float(fields[1]) * 24)  
                    sensor = int(fields[2])
                    temp = float(fields[4])
                    
                    self._data_set.append((day, time, sensor, temp))
            return True
        except FileNotFoundError as e:
            print(f"Error reading file: {e}")
            return False
    
    def get_loaded_temps(self):
        """Returns the number of temperature readings loaded."""
        return len(self._data_set) if self._data_set else None

def new_file(dataset):
    """Loads a file and names the dataset."""
    filename = input("Please enter the file name of the new dataset: ")
    
    if not dataset.process_file(filename):
        print("Unable to load the file.")
        return
    
    print(f"Loaded {dataset.get_loaded_temps()} samples")
    
    while True:
        name = input("Please provide a 3 to 20 character name for the dataset: ")
        if 3 <= len(name) <= 20:
            break
        print("Invalid name. Try again.")
    
    print("Dataset successfully named.")

def main():
    """Runs the menu system."""
    current_set = TempDataset()
    
    while True:
        print("\nSTEM Center Temperature Project")
        print("Emily Espinosa\n")
        print("Main Menu")
        print("---------")
        print("1 - Process a new data file")
        print("2 - Choose units")
        print("3 - Edit room filter")
        print("4 - Show summary statistics")
        print("5 - Show temperature by date and time")
        print("6 - Show histogram of temperatures")
        print("7 - Quit\n")
        choice = input("What is your choice? ")
        
        if choice == "1":
            new_file(current_set)
        elif choice in ["2", "3", "4", "5", "6"]:
            print("Not implemented yet.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
    
if __name__ == "__main__":
    main()
    
STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 1
Please enter the file name of the new dataset: file
Error reading file: [Errno 2] No such file or directory: 'file'
Unable to load the file.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 2
Not implemented yet.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 3
Not implemented yet.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 4
Not implemented yet.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 5
Not implemented yet.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 6
Not implemented yet.

STEM Center Temperature Project
Emily Espinosa

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7