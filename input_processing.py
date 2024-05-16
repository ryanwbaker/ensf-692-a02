# input_processing.py
# RYAN BAKER, ENSF 692 P24
# 
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = 'green'
        self.pedestrian = 'no'
        self.vehicle = 'no'

    # updates self.light, self.pedestrian, and/or self.vehicle based on keywords
    # e.g. update_status(light="yellow") will update self.light to "yellow"
    # allows for updating multiple attributes at once
    # e.g. update_status(light="green", vehicle="yes") will update both self.light and self.vehicle 
    def update_status(self, **kwargs): # You may decide how to implement the arguments for this function
        if 'light' in kwargs:
            if kwargs['light'] in ['red', 'yellow', 'green']:
                self.light = kwargs['light']
            else:
                raise ValueError("Invalid Entry. Please try again.")
        if 'pedestrian' in kwargs:
            if kwargs['pedestrian'] in ['yes', 'no']:
                self.pedestrian = kwargs['pedestrian']
            else:
                raise ValueError("Invalid Entry. Please try again.")
        if 'vehicle' in kwargs:
            if kwargs['vehicle'] in ['yes', 'no']:
                self.vehicle = kwargs['vehicle']
            else:
                raise ValueError("Invalid Entry. Please try again.")



# The sensor object should be passed to this function to print the action message and current status
# Accepts a Sensor object. Prints 'STOP', 'CAUTION', or 'PROCEED' depending on the Sensor attributes (light, pedestrian, and vehicle)
def print_message(sensor):
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nSTOP\n")
    elif sensor.light == "yellow":
        print("\nCAUTION\n")
    else:
        print("\nPROCEED\n")
    print(f"Light = {sensor.light}, Pedestrian = {sensor.pedestrian}, Vehicle = {sensor.vehicle}.\n")


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    yes_no = ["yes", "no"]
    sensor = Sensor()

    while True:
        try:
            user_choice = input(f"""Are changes detected in the vision input?\nSelect 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: """)
            match user_choice:
                case "0":
                    print("Program Ended.")
                    break
                case "1":
                    light = input("What light change has been identified?: ")
                    try:
                        sensor.update_status(light=light)
                        print_message(sensor)
                    except Exception as e:
                        print(f"{e}")
                case "2":
                    pedestrian = input("What pedestrian change has been identified?: ")
                    try:
                        sensor.update_status(pedestrian=pedestrian)
                        print_message(sensor)
                    except Exception as e:
                          print(f"{e}")
                case "3":
                    vehicle = input("What vehicle change has been identified?: ")
                    try:
                        sensor.update_status(vehicle=vehicle)
                        print_message(sensor)
                    except Exception as e:
                        print(f"{e}")
                case _:  
                    raise ValueError("Invalid Entry")      
        except ValueError as e:
            print(f"{e}. Please choose a value between 0 and 3.")
            continue
        




# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

