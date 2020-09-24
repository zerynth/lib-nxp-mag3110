
################################################################################
# Magnetometer Sensor Example with Triggered Measurement
# This saves power but may affect the accuracy of the data.
#
# Created: 2020-08-26
# Author: S. Torneo
#
################################################################################

import streams
from nxp.mag3110 import mag3110
import timers

streams.serial()

try:
    # Setup sensor 
    print("start...")
    mag = mag3110.MAG3110(I2C0)
    # set triggered measurement mode
    mag.set_measurement(mode=1)
    print("Ready!")
    print("--------------------------------------------------------")
except Exception as e:
    print("Error: ",e)

# create a new timer
t=timers.timer()
# start the timer
t.start()

try:
    while True:
        # Trigger a measurement every 2 seconds
        if (t.get() >= 2000):
            mag.trigger_measurement()
            t.reset()
        # check if magnetometer values are ready
        if (mag.is_data_ready()):
            # get magnetometer values
            values = mag.get_values()
            print("Magnetometer:", values)
        # get temperature value
        temp = mag.get_temp()
        print("Temperature: ", temp, "C")
        print("--------------------------------------------------------")
        sleep(1000)
except Exception as e:
    print("Error2: ",e)

