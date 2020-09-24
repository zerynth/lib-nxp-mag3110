
################################################################################
# Magnetometer Sensor Example
#
# Created: 2020-08-24
# Author: S. Torneo
#
################################################################################

import streams
from nxp.mag3110 import mag3110

streams.serial()

try:
    # Setup sensor 
    print("start...")
    mag = mag3110.MAG3110(I2C0)
    print("Ready!")
    print("--------------------------------------------------------")
except Exception as e:
    print("Error: ",e)

try:
    while True:
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
