# input_processing.py
# Danish Shahid, ENSF 692 Spring 2025
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
        # status attributes
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # Function takes main_input and status_input as arguments and update the vision related attributes
    # It returns a boolean in case the status change was successful and false if no status was updated
    def update_status(self, main_input, status_input):
        # default return value to false
        updated = False

        match main_input:
            case "1": # if its changing lights
                # checking to make sure that only allowed values get updated
                if status_input == "green" or status_input == "yellow" or status_input == "red":
                    self.light = status_input
                    updated = True
            case "2":
                # same for boolean whether yes or no
                if status_input == "yes" or status_input == "no":
                    self.pedestrian = status_input
                    updated = True
            case "3":
                if status_input == "yes" or status_input == "no":
                    self.vehicle = status_input
                    updated = True

        # return the status of the function
        return updated

    # Function prints the action message
    # It based on various rules create print statements
    def print_action(self):
        # overall status strings
        if self.light == "red" or self.pedestrian == "yes" or self.vehicle == "yes":
            print("STOP")
        elif self.light == "green" and self.pedestrian == "no" and self.vehicle == "no":
            print("Proceed")
        elif self.light == "yellow" and self.pedestrian == "no" and self.vehicle == "no":
            print("Caution")
        print()

    # Function prints the current status
    def print_status(self):
        # logic for preparing print strings
        print(f"Light = {self.light} , Pedestrian = {self.pedestrian} , Vehicle = {self.vehicle} .\n")


# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    sensor.print_action()
    sensor.print_status()



# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    s1 = Sensor()

    while True:

        print("Are changes detected in the vision input?")

        try:
            main_input = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

            # check for program quit before anything
            if main_input == "0":
                break
            elif main_input != "1" and main_input != "2" and main_input != "3":
                raise ValueError()

            status_input = input("What change has been identified?: ")

            if not(s1.update_status(main_input, status_input)):
                print("Invalid vision change.")

            print()
            print_message(s1)

        except ValueError:
            print("You must select either 1, 2, 3 or 0.\n")


# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

