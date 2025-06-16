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

