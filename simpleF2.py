from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

drone.takeoff()
time.sleep(3)

drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.turn_left(90)
time.sleep(3)
drone.move_forward(distance=1.5, units="m", speed=1)
time.sleep(3)

drone.turn_right(90)
time.sleep(3)
drone.move_forward(distance=30, units="cm", speed=1)
time.sleep(3)

drone.land()
time.sleep(3)

drone.close()