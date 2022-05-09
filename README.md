# Seeduino Xiao - ARTSEYIO

This is an ARTSEYIO keyboard using the Seeduino Xiao running Circuit Python
and Adafruit's HID keyboard modules.


# Features
This board only applies a basic subset of QMK features

- Combos (Max 6 keys)
- One-shot modifiers
- Layer switching

As of now, it does not support

- Layer Tap
- Mod Tap
- One Shot Layer
- Other advanced features 

# Installation

Copy over the files into the CIRCUITPY folder.
Rename the artseyio.py to code.py and save.

The led will blink five times, then the keyboard should be ready.



# Debugging

In macOs terminal, run the following command to find the device name

```
ls -l /dev/tty.*
```

It should return something like the following

```
crw-rw-rw-  1 root  wheel   22,   0  9 May 08:48 /dev/tty.Bluetooth-Incoming-Port
crw-rw-rw-  1 root  wheel   22,   2  9 May 21:09 /dev/tty.usbmodem14201
```

Open `screen` program with the usbmodem from above like this

```
screen /dev/tty.usbmodem14201 115200
```

