from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


debug = False
if debug:
    import pyqt5ac

    pyqt5ac.main(config='config.yml')

from Widgets import VirtualNumpad_ui
class VirtualNumpad(QDialog, VirtualNumpad_ui.Ui_VirtualNumpad):

    def __init__(self, parent=None, parentLineEdit=None, signalFromParentLineEdit=None):
        super(VirtualNumpad, self).__init__(parent)
        self.setupUi(self)
        self.parentLineEdit = parentLineEdit
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
        #self.setStyleSheet("background-color: black;")
        self.setGeometry(0, 0, 800, 480)

        self.signalFromParentLineEdit = None
        if signalFromParentLineEdit:
            self.signalFromParentLineEdit = signalFromParentLineEdit

        self.numberButtons = \
            [[self.zeroButton, 0],
             [self.oneButton,  1],
             [self.twoButton, 2],
             [self.threeButton,   3],
             [self.fourButton,   4],
             [self.fiveButton,   5],
             [self.sixButton,   6],
             [self.sevenButton,   7],
             [self.eightButton,   8],
             [self.nineButton,   9]]

        for button in self.numberButtons:
            button[0].pressed.connect(self.numberButtonsPressed)


    # def close(self):
    #     self.parentLineEdit.setFocus()
    #     self.close()

    @pyqtSlot()
    def numberButtonsPressed(self):

        # Get which button is pressed
        sender = self.sender()
        for button in self.numberButtons:
            if button[0] is sender:
                self.weightEdit.insert(str(button[1]))
                self.weightEdit.setFocus()

    @pyqtSlot()
    def on_enterButton_clicked(self):
        self.parentLineEdit.setText(self.weightEdit.text())

        # Emit a signal of done editing to parent line edit
        if self.signalFromParentLineEdit:
            self.signalFromParentLineEdit.emit()

        self.close()

    @pyqtSlot()
    def on_periodButton_clicked(self):
        self.weightEdit.insert('.')

    @pyqtSlot()
    def on_deleteButton_clicked(self):
        self.weightEdit.backspace()
        if len(self.weightEdit.text()) != 0:
            self.weightEdit.setFocus()

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.weightEdit.clear()
        if len(self.weightEdit.text()) != 0:
            self.weightEdit.setFocus()

    @pyqtSlot()
    def on_goBackButton_clicked(self):
        self.parentLineEdit.setText(self.weightEdit.text())
        self.close()

    @pyqtSlot()
    def on_leftArrowButton_clicked(self):
        if len(self.weightEdit.text()) > 0:
            currentPos = self.weightEdit.cursorPosition()
            self.weightEdit.setCursorPosition(currentPos - 1)
            self.weightEdit.setFocus()

    @pyqtSlot()
    def on_rightArrowButton_clicked(self):
        if len(self.weightEdit.text()) > 0:
            currentPos = self.weightEdit.cursorPosition()
            self.weightEdit.setCursorPosition(currentPos + 1)
            self.weightEdit.setFocus()

if debug:
    app = QApplication([])
    mw = VirtualNumpad()
    mw.show()
    app.exec()