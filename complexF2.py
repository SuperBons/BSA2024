from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()


def drone_change_color():
    color = drone.get_back_color()
    if color == "Blue":
        drone.set_drone_LED(0, 0, 255, 100)  # Change to blue
    elif color == "Red":
        drone.set_drone_LED(255, 0, 0, 100)  # Change to red
    elif color == "Green":
        drone.set_drone_LED(0, 255, 0, 100)  # Change to green
    elif color == "Yellow":
        drone.set_drone_LED(255, 255, 0, 100)  # Change to yellow
    elif color == "Purple":
        drone.set_drone_LED(255, 0, 255, 100)  # Change to purple
    elif color == "Cyan":
        drone.set_drone_LED(0, 255, 255, 100)  # Change to cyan
    elif color == "White":
        drone.set_drone_LED(255, 255, 255, 100)  # Change to white
    else:
        drone.set_drone_LED(0, 0, 0, 100)  # Turn off


def land_change_color_takeoff():
    drone.land()
    time.sleep(3)
    drone_change_color()
    time.sleep(1)
    drone.takeoff()
    time.sleep(3)

# Initial takeoff
drone.takeoff()
time.sleep(3)

# Move 1: forward 1.5 meters
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn right 90 degrees
drone.turn_right(90)
time.sleep(3)

# Move 2: forward 30 cm
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn right 90 degrees
drone.turn_right(90)
time.sleep(3)

# Move 3: forward 1.5 meters
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn left 90 degrees
drone.turn_left(90)
time.sleep(3)

# Move 4: forward 30 cm
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn left 90 degrees
drone.turn_left(90)
time.sleep(3)

# Move 5: forward 1.5 meters
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn right 90 degrees
drone.turn_right(90)
time.sleep(3)

# Move 6: forward 30 cm
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn right 90 degrees
drone.turn_right(90)
time.sleep(3)

# Move 7: forward 1.5 meters
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn left 90 degrees
drone.turn_left(90)
time.sleep(3)

# Move 8: forward 30 cm
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn left 90 degrees
drone.turn_left(90)
time.sleep(3)

# Move 9: forward 1.5 meters
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Turn right 90 degrees
drone.turn_right(90)
time.sleep(3)

# Move 10: forward 30 cm
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)
land_change_color_takeoff()

# Final landing
drone.land()
time.sleep(3)
drone.close()