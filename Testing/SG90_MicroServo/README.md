# Documentation and Usage for the SG90 Micro-Servo Motor
For this project, a micro-serveo - the SG90 - is used to help move the original thermostat lever up and down when prompted. This document introduces the servo motor, how to connect it to the Raspberry Pi, and some test code to operate and calibrate the actuator. 

![sg90](https://www.electronics-lab.com/wp-content/uploads/2018/06/SG90-micro-9g-servo-for-Rc-Helicopter.jpg)

## Connecting the SG90
The wires connected to the SG90 are shown below where: 
- **red**: voltage in (5V)
- **brown**: ground
- **orange**: pulse-width-modulator 

![sg90_pinout](https://components101.com/sites/default/files/component_pin/Servo-Motor-Wires.png)

The RPi pinout is shown below. The red wire should be connected to the RPi physical pin 2 or 4, the brown wire to physical pin 6, 9, etc., and the orange wire should be connected to any other gpio - in my case, I used physical pin 12 or GPIO 18.

![rpi_pinout](https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png)

## Calibrating the Servo-Motor
Since we are using a Raspberry Pi to control the servo-motor, we have to specify the duty cycle - not the PWM. The factory setting should be a minimum of 5% (-90 degrees), a mximum of 10% (90 degrees), and centered at 7.5%. However, these won't necessarily be correct and need to be adjusted based on the hardware you have. To do so, you should copy and run the [code](sg90_calibration.py). 

### -90 Degrees
At the prompt, continue to reduce the the duty cycle percentage by 0.1 until the servo-motor starts to have trouble (a small "whirring" noise). This is the lower limit to your duty cycle - in may case it ended up being 2.2%. 

### 90 Degrees
At the prompt, continue to increase the the duty cycle percentage by 0.1 until the servo-motor starts to have trouble (a small "whirring" noise). This is the upper limit to your duty cycle - in may case it ended up being 12.4%. 

## Scanning the Range of the Servo-Motor


# Resources
1. [Connecting, Calibrating, and Scanning](https://reefwingrobotics.blogspot.com/2017/02/raspberry-pi-and-towerpro-sg90-micro.html)
