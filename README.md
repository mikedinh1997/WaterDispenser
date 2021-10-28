# Water Dispenser

## Installation

### Raspberry Pi OS
Install pip3 and Python 3
```
sudo apt-get install python3-pip
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install python3
``` 
Clone HX711 repo to the project folder: https://github.com/tatobari/hx711py
<br/>

On Raspberry Pi OS, clone pyqt5ac repo to the project folder: https://github.com/addisonElliott/pyqt5ac/ 
<br />

Install each package in ```requirements.txt``` with ```pip3``` 
```
sudo pip3 install 'package_name'=='package_version'
```

In main.py, navigate path of ```pyqt5ac_config.yml``` to ```config``` argument. Try to run ```main.py``` now. 

### Windows 10
Download and install Anaconda for Python 3 at https://www.anaconda.com/products/individual-d

#### PyCharm
Download and install PyCharm at https://www.jetbrains.com/pycharm/download/#section=windows

In PyCharm, go to *File* -> *Setting* -> *Project* -> *Python Interpreter*, add new conda environment 
```
C:\Users\user_name\Anaconda3\python.exe
```

Install packages listed in ```requirements.txt``` with *Anaconda Command Line* or through PyCharm terminal
if Python interpreter is set up properly.

---
Note: hx771 package was only tested on Raspberry Pi OS. Developing the project on Windows strongly focuses on designing
GUIs with Qt Designer.

