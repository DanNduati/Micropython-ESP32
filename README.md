# Micropython
python for microcontrollers
## Installation / dependencies
You will need either.[Python 2.7 or Python 3.4]. or newer(https://www.python.org/downloads/) installed on your system.

The latest stable esptool.py release can be installed from [pypi](http://pypi.python.org/pypi/esptool) via pip:

```
$ pip install esptool
```
[![Build Status](https://travis-ci.org/espressif/esptool.svg?branch=master)](https://travis-ci.org/espressif/esptool)
## Flashing MicroPython Firmware to ESP32
To download the latest version of MicroPython firmware for the ESP32, go to the [MicroPython Downloads page](https://micropython.org/download#esp32) and scroll all the way down to the ESP32 section
Using esptool.py you can erase the entire flash chip (all data replaced with 0xFF bytes)::
```
esptool.py --port /dev/ttyUSB0 erase_flash
```
Binary data can be written to the ESP's flash chip via the serial write_flash command:
```
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
```
Hold down the “BOOT/FLASH“, before running the flash command.
## The repl
REPL stands for Read Evaluate Print Loop, and is the name given to the interactive MicroPython prompt that you can access on the ESP32. Using the REPL is by far the easiest way to test out your code and run commands.There are two ways to access the REPL: either via a wired connection through the UART serial port, or via WiFi.
### Repl over the serial port
The REPL is always available on the UART0 serial peripheral, which is connected to the pins GPIO1 for TX and GPIO3 for RX. The baudrate of the REPL is 115200. If your board has a USB-serial convertor on it then you should be able to access the REPL directly from your PC. Otherwise you will need to have a way of communicating with the UART.To access the prompt over USB-serial you need to use a terminal emulator program on Linux picocom is a good choise you can install it with
```
sudo apt-get install picocom
```
### connecting to the ESP32 repl via picocom
```
picocom /dev/ttyUSB0 -b115200
```

Once you have made the connection over the serial port you can test if it is working by hitting enter a few times. You should see the Python REPL prompt, indicated by ```>>>``` If the following symbol does not appear, it means that other programs are being executed and you need to interrupt the program first CTRL+C Interrupt the program, then you can type Python commands in the terminal. Once you have a prompt you can start experimenting! Anything you type at the prompt will be executed after you press the Enter key. MicroPython will run the code that you enter and print the result (if there is one). If there is an error with the text that you enter then an error message is printed.

## File synchronization and upload with ampy
I went for adafruit ampy tool because it is a simple cross-platform command line tool that provides just enough functionality to access MicroPython's filesystem without being too complicated.It can be used to .pysynchronize local files to the ESP32 file system.The principle of Ampy is to enter the REPL and complete file synchronization in the REPL. So before using Ampy, you need to disconnect the original picocom connection .In addition, if the original program is always printprinting out, ampy cannot be used normally. You need to interrupt the original loop statement in Picocom's REPL before using it.
## installing ampy
```
pip install adafruit-ampy
```
### running a local program
Using ampy you can take Python code written on your computer and run it on a connected MicroPython board.In a terminal in the same directory as your script say hello.py run the following ampy command to execute the script on a connected MicroPython board
```
ampy --port /serial/port run test.py
```
Where /serial/port is the path or name of the serial port connected to the MicroPython board.Also be aware ampy does not support talking to boards without a serial/USB REPL connection.
### uploading a file 
File upload put instructions, upload the previously written program file example led.py files to the ESP32 file system with
```
ampy --port /dev/ttyUSB0 put led.py
```
### delete files
```
ampy --port /dev/ttyUSB0 rm led.py 
```
### Uploading Py files in bulk
