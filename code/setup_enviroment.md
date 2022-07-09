# HOW TO 

How to set up the develop enviroment for programming a raspberry Pi Pico using VSCode und Windows/WSL 2 

## Install 

### Prerequisits
* Installed VSCode 
* Installed WSL 2 
* Installed Ubuntu on WSL 2, the used version in for this enviroment is Ubuntu 22.04 




### microp-cli 
The python extension does not know micropython, therefore MicroPy-CLI is used 

* follow the insttructions on https://github.com/BradenM/micropy-cli
This enables Pylint and Pylance in VSCode to work korrectly 

* make shure, the correct stubs are added with ```micropy stubs add``` command in this enviroment the stubs are from [this](https://github.com/cpwood/Pico-Stub/blob/main/micropy.md#using-the-stubs) repository 

### Connect to the board 


1. The connection is done via [rshell](https://github.com/dhylands/rshell) or [ampy](https://github.com/scientifichackers/ampy).
Follow the instructions. 
    * The board should be in ```/dev/tty*.``` 

2. To connect to the board over WSL, [this](https://docs.microsoft.com/en-us/windows/wsl/connect-usb) follow this guide. WSL does not suppert connecting to USB devices. 
    * set the privileges with ```sudo chmod a+rw /dev/ttyACM0```


