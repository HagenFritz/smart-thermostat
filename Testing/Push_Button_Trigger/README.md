# Documentation and Code to Create a Triggering Event from a Push Button
This document outlines how to wire and program a push button to trigger an LED to power on. This code should be applicable to any tiggering event so long as the hardware is setup correctly. 

![push_button](https://electrosome.com/wp-content/uploads/2012/12/Push-Button-Switch.jpg)

## Connecting a Push Button and LED
The schematic below shows how to connect a push button and LED to the RPi. In this instance, GPIO 17 was used to hook up the LED and GPIO 27 for the push button. The LED is ableto draw from the 5V power pin while the button only requires 3.3V. You might notice we also use a [field effect transistor](https://elinux.org/RPi_GPIO_Interface_Circuits) to help with the triggering process. 

![push_button_trigger_layout](https://github.com/HagenFritz/smart-thermostat/blob/master/Testing/Layouts/push_button_trigger_led_bb.png)

## Programming the Push Button Trigger
With the hardware successfully connected to the RPi, we can use the [code](push_button_trigger_led.py) in this same directory to test it. Commenting in the program itself helps to explain the purpose of different lines and is excluded from this document. 

# Resources
1. [Connecting and Programming](https://myhydropi.com/connect-an-led-and-button-to-a-raspberry-pi)
