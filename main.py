from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

# Automatically convert .ui files to .py file
import pyqt5ac

pyqt5ac.main(config='pyqt5ac_config.yml')

from Windows.mainWindow import MainWindow


app = QApplication([])
mw = MainWindow()
mw.show()
app.exec()