#include "mbed.h"
#include "FXAS21002.h"
#include "FXOS8700.h"

/*  Check out the full featured example application for interfacing to the 
 *  Gyro device at the following URL
 *  https://developer.mbed.org/teams/ATT-Hackathon/code/Accel_Mag_Gyro_SensorStream_K64F_AGM01_M/
*/

DigitalOut led1(LED_GREEN);
Serial pc(USBTX, USBRX);

// Pin connections for Hexiwear
FXAS21002 gyro(PTC11,PTC10);
// Pin connections & address for Hexiwear
FXOS8700 accel(PTC11, PTC10);
FXOS8700 mag(PTC11, PTC10);

// Storage for the data from the sensor
float gyro_data[3];  float gyro_rms=0.0;


// main() runs in its own thread in the OS
// (note the calls to Thread::wait below for delays)
int main() {
        
    gyro.gyro_config();
    accel.accel_config();
    mag.mag_config();

    float accel_data[3]; float accel_rms=0.0;
    float mag_data[3];   float mag_rms=0.0;

    while (true) {
    
      gyro.acquire_gyro_data_dps(gyro_data);
      pc.printf("%4.2f %4.2f %4.2f\n",gyro_data[0],gyro_data[1],gyro_data[2]);
      //gyro_rms = sqrt(((gyro_data[0]*gyro_data[0])+(gyro_data[1]*gyro_data[1])+(gyro_data[2]*gyro_data[2]))/3);
      //pc.printf("Gyroscope RMS %f \r\n\n",gyro_rms);
 
      accel.acquire_accel_data_g(accel_data);
      printf("%4.2f %4.2f %4.2f\n",accel_data[0],accel_data[1],accel_data[2]);
      wait(0.01);
      
      mag.acquire_mag_data_uT(mag_data);
      printf("%4.2f %4.2f %4.2f\n",mag_data[0],mag_data[1],mag_data[2]);
      wait(0.01);

      led1 = !led1;
      Thread::wait(1000);
    }
}

