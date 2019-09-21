# About

This application is used to turn a RaspberryPi Zero into something that
resembles the Sun Lights-Out Management software that can be used to remotely
control the power state and boot sequence of a server box. The only thing
required is a way to connect a USB device into your box from the inside, a
few female-to-female single-pin cables or one female-to-female two-pin cable,
and an RPi Zero with some kind of remote login enabled.  

# Setup

Enabling modules and drivers:  
	`$ echo 'dtoverlay=dwc2' | sudo tee -a /boot/config.txt`  
	`$ echo 'dwc2' | sudo tee -a /etc/modules`  
	`$ echo 'libcomposite' | sudo tee -a /etc/modules`  

Installing the config scripts  
	`# cp /extra/blythe/usb-keyboard /usr/bin/`  
	`# chmod +x /usr/bin/usb-keyboard`  

Initialize program group  
	`# addgroup blythe`  
	`# usermod -aG blythe root <your_user> <any_others>`   

We want this script to run at startup automatically;
add this line to /etc/rc.local before
the line containing 'exit 0':  
	`/usr/bin/usb-keyboard # configure libcomposite`  

If using the provided config script, the output device is  
	`/dev/hidg0`  

The default permissions for this should be 600. We want
users to be able to run the scripts if they belong
to the blythe group, so the config script should also do  
	`# chmod 660 /dev/hidg0`  
	`# chgrp blythe /dev/hidg0`  

# Sending the reset signal

## Python script:
`>>> from gpiozero import LED`  
`>>> from time import sleep`  

## Bash script:
Currently we don't have a Bash script to handle sending the signals
over the GPIO pins. This is preferred over the Python script.

# Sending keyboard events  

## Python script:  
- Method 1: Hexadecimal char encoding  
	`>>> with open('/dev/hidg0', 'rb+') as fd:`  
	`>>> .. fd.write(<HID Event>.encode())`  
    
	We can use the character representation of decimal
	integers along with *.encode() to get some hex to send
	to the HID interface.  
	`>>> (chr(0)*2+chr(4)+chr(0)*5).encode()`  

- Method 2: Raw hexadecimal  
	`>>> with open('/dev/hidg0', 'rb+') as fd:`  
	`>>> .. fd.write(<HID Event>)`  

	Use Python's hexadecimal representation as the raw event
	to write to the HID interface.  
	`>>> b'\x00\x00\x00\x00\x00\x00\x00\x00'`  

## Bash script:  
Just write raw hexadecimal to the HID interface. Easy!  
	`$ echo -en \\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00 >> /dev/hidg0`  


  
  
  
  
  

### To-Do  
HID event documentation  
write reset script for windows and linux  
wrap up and stick in /usr/bin/  
