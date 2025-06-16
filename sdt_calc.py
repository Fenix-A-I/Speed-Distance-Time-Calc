'''
Speed Distance Time Calculator
Goal: Refresh on using Python
Author: Alexandr Iapara
'''

# Importing math module
import math

def calculate_speed(distance, time):
    """
    Calculate speed given distance and time.
    
    Parameters:
    distance (float): The distance traveled.
    time (float): The time taken to travel the distance.
    
    Returns:
    float: The speed calculated as distance divided by time.
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return round(distance / time, 2)

def calculate_distance(speed, time):
    """
    Calculate distance given speed and time.
    
    Parameters:
    speed (float): The speed of the object.
    time (float): The time traveled.
    
    Returns:
    float: The distance calculated as speed multiplied by time.
    """
    if time < 0:
        raise ValueError("Time cannot be negative.")
    return round(speed * time, 2)

def calculate_time(distance, speed):
    """
    Calculate time given distance and speed.
    
    Parameters:
    distance (float): The distance to be traveled.
    speed (float): The speed of the object.
    
    Returns:
    float: The time calculated as distance divided by speed.
    """
    if speed <= 0:
        raise ValueError("Speed must be greater than zero.")
    return round(distance / speed, 2)

def main():
    """
    The main function to run the Speed Distance Time Calculator.
    """

    print("\033[93m\n========== Speed Distance Time Calculator ==========\n\033[0m")
    while True:
        try:
            choice = input("Which value would you like to calculate? (time/speed/distance): ").strip().lower()
            
            if choice == "speed":
                print("\033[93m\nCalculating Speed...\n\033[0m")
                distance = float(input("Enter distance (in km): "))
                time = float(input("Enter time (in hours): "))
                calc_speed = calculate_speed(distance, time)
                print(f"\033[92m\nSpeed: {calc_speed} km/h\n\033[0m")
                break

            elif choice == "distance":
                print("\033[93m\nCalculating Distance...\n\033[0m")
                speed = float(input("Enter speed (in km/h): "))
                time = float(input("Enter time (in hours): "))
                calc_dist = calculate_distance(speed, time)
                print(f"\033[92m\nDistance: {calc_dist} km\n\033[0m")
                break

            elif choice == "time":
                print("\033[93m\nCalculating Time...\n\033[0m")
                distance = float(input("Enter distance (in km): "))
                speed = float(input("Enter speed (in km/h): "))
                time_calculated = calculate_time(distance, speed)
                print(f"\033[92m\nTime: {time_calculated} hours\n\033[0m")
                break

            elif choice == "exit":
                print("\033[93m\nExiting the calculator.\n\033[0m")
                return
            
            else:
                print("\033[91mInvalid choice. Please select from time, speed, or distance.\033[0m\n")
            
        except ValueError as err:
            print(f"\033[91mError: {err}\033[0m\n")

if __name__ == "__main__":
    main()