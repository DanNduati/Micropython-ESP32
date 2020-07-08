# Micropython
python for microcontrollers
## Installation / dependencies
You will need [either Python 2.7 or Python 3.4 or newer](https://www.python.org/downloads/) installed on your system.

The latest stable esptool.py release can be installed from [pypi](http://pypi.python.org/pypi/esptool) via pip:

```
$ pip install esptool
```
[![Build Status](https://travis-ci.org/espressif/esptool.svg?branch=master)](https://travis-ci.org/espressif/esptool)
## Flashing MicroPython Firmware to ESP32/ESP8266
To download the latest version of MicroPython firmware for the ESP32, go to the [MicroPython Downloads page](https://micropython.org/download#esp32) and scroll all the way down to the ESP32 section
Using esptool.py you can erase the flash with the command:
```
esptool.py --port /dev/ttyUSB0 erase_flash
```
And then deploy the new firmware using:
```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
```

## Connecting and uploading code to the esp32
I went for adafruit ampy tool because it is a simple cross-platform command line tool that provides just enough functionality to access MicroPython's filesystem without being too complicated.
### installing ampy
```
pip install adafruit-ampy
```
Using ampy you can take Python code written on your computer and run it on a connected MicroPython board.In a terminal in the same directory as your script say hello.py run the following ampy command to execute the script on a connected MicroPython board
```
ampy --port /serial/port run test.py
```
Where /serial/port is the path or name of the serial port connected to the MicroPython board.Also be aware ampy does not support talking to boards without a serial/USB REPL connection.
