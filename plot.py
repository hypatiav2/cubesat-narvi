import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import sys
from sensor_calc import *


i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c)
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
y1 = []
y2 = []
y3 = []
rpy = [0,0,0]

def animate(i, xs, type,y1,y2,y3, mag_offset, gyro_offset, initial_angle):
    if len(y1) ==0:
        prev_ang = initial_angle
    else:
        a = y1[-1]
        b = y2[-1]
        c = y3[-1]
        prev_ang = [a,b,c]
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings
    magX = magX - mag_offset[0]
    magY = magY - mag_offset[1]
    magZ = magZ - mag_offset[2]
    gyroX, gyroY, gyroZ = sensor2.gyroscope #rad/s
    gyroX = gyroX * (180/np.pi)- gyro_offset[0]
    gyroY = gyroY * (180/np.pi)- gyro_offset[1]
    gyroZ = gyroZ * (180/np.pi)- gyro_offset[2]
    xs.append(time.time())

    if type == 'am':
       y1.append(roll_am(accelX,accelY,accelZ))
       y2.append(pitch_am(accelX,accelY,accelZ))
       y3.append(yaw_am(accelX,accelY,accelZ,magX,magY,magZ))
       ax.clear()
       ax.plot(xs,y1,label = "Roll")
       ax.plot(xs,y2,label = "Pitch")
       ax.plot(xs,y3,label = "Yaw")
       plt.title('Roll Pitch Yaw, Using Accelerometer and Magnetometer')
       plt.ylabel('deg')

    elif type =='gyro':
       if len(xs) == 1:
           y1.append(prev_ang[0])
           y2.append(prev_ang[1])
           y3.append(prev_ang[2])
       else:
           delT = xs[-1] - xs[-2]
           y1.append(roll_gy(prev_ang[0],delT,gyroY))
           y2.append(pitch_gy(prev_ang[1],delT,gyroX))
           y3.append(yaw_gy(prev_ang[2],delT,gyroZ))

       ax.clear()
       ax.plot(xs,y1,label = "Roll")
       ax.plot(xs,y2,label = "Pitch")
       ax.plot(xs,y3,label = "Yaw")
       plt.title('Roll Pitch Yaw, Using Gyro')
       plt.ylabel('deg')

    else:
       print("Not a valid argument.")
       return
    #Keep the plot from being too long
    xs = xs[-20:]
    y1 = y1[-20:]
    y2 = y2[-20:]
    y3 = y3[-20:]
    plt.grid()
    plt.legend()
    plt.xlabel('Time')

def plot_data(type = 'am'):
    mag_offset = calibrate_mag()
    #initial_angle = set_initial(mag_offset)
    gyro_offset = calibrate_gyro()
    ani = animation.FuncAnimation(fig, animate, fargs =(xs,type,y1,y2,y3,mag_offset,gyro_offset,initial_angle), interval = 1000)
    plt.show()


if __name__ == '__main__':
    plot_data(*sys.argv[1:])
