import time
import serial
import matplotlib.pyplot as plt

# configure the serial connections 
ser = serial.Serial(
    port='COM22',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()
time_of_sample=1

while 1 :

        out = ''        
        time.sleep(0.5)
        out = ser.readline()
        (roll, sep, restOfString) = out.partition(' ')
        (pitch, sep, yaw) = restOfString.partition(' ')
        
        out = ser.readline()
        (accel_x, sep, restOfString) = out.partition(' ')
        (accel_y, sep, accel_z) = restOfString.partition(' ')

        out = ser.readline()
        (mag_x, sep, restOfString) = out.partition(' ')
        (mag_y, sep, mag_z) = restOfString.partition(' ')


        print "roll " + roll
        print "pitch " + pitch
        print "yaw " + yaw
        try:
            roll_float = float(roll)
            pitch_float = float(pitch)
            yaw_float = float(yaw)
            accel_x_f = float(accel_x)
            accel_y_f = float(accel_y)
            accel_z_f = float(accel_z)
            mag_x_f = float(mag_x)
            mag_y_f = float(mag_y)
            mag_z_f = float(mag_z)
        except:
            continue
        
        plt.subplot(331)
        plt.scatter(time_of_sample, roll_float)
        plt.ylabel("Gyroscope Roll")
        plt.ylim(-200, 200)
        plt.xlim(0,100)

        plt.subplot(334)
        plt.scatter(time_of_sample, pitch_float)
        plt.ylabel("Gyroscope Pitch")
        plt.ylim(-200, 200)
        plt.xlim(0,100)
        
        plt.subplot(337)
        plt.scatter(time_of_sample, yaw_float)
        plt.ylabel("Gyroscope Yaw")
        plt.xlabel("time")
        plt.ylim(-200, 200)
        plt.xlim(0,100)
        
#        plt.figure(2)
#        plt.suptitle("Accelorometer")
        plt.subplot(332)
        plt.scatter(time_of_sample, accel_x_f)
        plt.ylabel("Accelorometer X-axis")
        plt.ylim(-5, 5)
        plt.xlim(0,100)

        plt.subplot(335)
        plt.scatter(time_of_sample, accel_y_f)
        plt.ylabel("Accelorometer Y-axis")
        plt.ylim(-5, 5)
        plt.xlim(0,100)

        plt.subplot(338)
        plt.scatter(time_of_sample, accel_z_f)
        plt.ylabel("Accelorometer Z-axis")
        plt.ylim(-5, 5)
        plt.xlim(0,100)


        plt.subplot(333)
        plt.scatter(time_of_sample, mag_x_f)
        plt.ylabel("Magnetometer X-axis")
        plt.ylim(-200, 200)
        plt.xlim(0,100)
        

        plt.subplot(336)
        plt.scatter(time_of_sample, mag_y_f)
        plt.ylabel("Magnetometer Y-axis")
        plt.ylim(-200, 200)
        plt.xlim(0,100)

        plt.subplot(339)
        plt.scatter(time_of_sample, mag_z_f)
        plt.ylabel("Magnetometer Z-axis")
        plt.ylim(-200, 200)
        plt.xlim(0,100)

        plt.pause(0.1)
        plt.show(block=False)
        time_of_sample += 1
