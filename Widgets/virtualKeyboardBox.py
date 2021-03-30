from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Widgets import VirtualKeyboardBox_ui
from util.enum import *

debug = False
if debug:
    import pyqt5ac

    pyqt5ac.main(config='config.yml')

class VirtualFullSizeKeyboard(QDialog, VirtualKeyboardBox_ui.Ui_VirtualKeyboardBox):

    lowerCapButtonStyleSheet = "QPushButton{ font-weight: bold; color: white; background-color: rgb(36, 36, 36);" \
                               "border-radius: 5px;} " \
                               "QPushButton:hover{" \
                               "background-color: rgb(207, 207, 207)}"

    upperCapButtonStyleSheet = "QPushButton{ font-weight: bold; color: white; background-color: rgb(207, 207, 207);" \
                               "border-radius: 5px;} " \
                               "QPushButton:hover{" \
                               "background-color: rgb(207, 207, 207)}"

    def __init__(self, parent=None, parentLineEdit=None):
        super(VirtualFullSizeKeyboard, self).__init__(parent)
        self.setupUi(self)
        self.parentLineEdit = parentLineEdit
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(0, 0, 800, 480)

        # self.nameEdit.setFocus()

        self.lCapButton.setIcon(QIcon('./Icons/up_arrow.png'))
        self.rCapButton.setIcon(QIcon('./Icons/up_arrow.png'))
        self.enterButton.setIcon(QIcon('./Icons/enter.png'))
        self.deleteButton.setIcon(QIcon('./Icons/backspace.png'))
        self.leftArrowButton.setIcon(QIcon('./Icons/left_arrow.png'))
        self.rightArrowButton.setIcon(QIcon('./Icons/right_arrow.png'))

        self.alphabetButtons = \
            [[self.qButton,                ['q', 'Q', 'Q']],
             [self.wButton,                ['w', 'W', 'W']],
             [self.eButton,                ['e', 'E', 'E']],
             [self.rButton,                ['r', 'R', 'R']],
             [self.tButton,                ['t', 'T', 'T']],
             [self.yButton,                ['y', 'Y', 'Y']],
             [self.uButton,                ['u', 'U', 'U']],
             [self.iButton,                ['i', 'I', 'I']],
             [self.oButton,                ['o', 'O', 'O']],
             [self.pButton,                ['p', 'P', 'P']],

             [self.aButton,                ['a', 'A', 'A']],
             [self.sButton,                ['s', 'S', 'S']],
             [self.dButton,                ['d', 'D', 'D']],
             [self.fButton,                ['f', 'F', 'F']],
             [self.gButton,                ['g', 'G', 'G']],
             [self.hButton,                ['h', 'H', 'H']],
             [self.jButton,                ['j', 'J', 'J']],
             [self.kButton,                ['k', 'K', 'K']],
             [self.lButton,                ['l', 'L', 'L']],

             [self.zButton,                ['z', 'Z', 'Z']],
             [self.xButton,                ['x', 'X', 'X']],
             [self.cButton,                ['c', 'C', 'C']],
             [self.vButton,                ['v', 'V', 'V']],
             [self.bButton,                ['b', 'B', 'B']],
             [self.nButton,                ['n', 'N', 'N']],
             [self.mButton,                ['m', 'M', 'M']]]

        for button in self.alphabetButtons:
            button[0].pressed.connect(self.alphabetButtonsPressed)

        self.changeKeyboardLayoutToUpper()

    def updateState(self):
        for button in self.alphabetButtons:
            if self.keyboardState == KeyboardState.Lower:
                button[0].setText(button[1][0])
            else:
                button[0].setText(button[1][1])

    def changeKeyboardLayoutToUpper(self):
        self.keyboardState = KeyboardState.Lower
        self.lCapButton.click()

    def changeKeyboardLayoutToLower(self):
        self.keyboardState = KeyboardState.Upper
        self.lCapButton.click()

    @pyqtSlot()
    def alphabetButtonsPressed(self):

        # Get which button is pressed
        sender = self.sender()
        for button in self.alphabetButtons:
            if button[0] is sender:
                if self.keyboardState == KeyboardState.Lower:
                    self.nameEdit.insert(button[1][0])
                else:
                    if len(self.nameEdit.text()) == 0:
                        self.nameEdit.insert((button[1][1]).upper())
                        self.changeKeyboardLayoutToLower()
                    else:
                        self.nameEdit.insert((button[1][1]))
                self.nameEdit.setFocus()

    @pyqtSlot()
    def on_enterButton_clicked(self):
        self.parentLineEdit.setText(self.nameEdit.text().capitalize())
        self.close()

    @pyqtSlot()
    def on_spaceButton_clicked(self):
        self.nameEdit.insert(" ")
        self.nameEdit.setFocus()

    @pyqtSlot()
    def on_deleteButton_clicked(self):
        self.nameEdit.backspace()
        if len(self.nameEdit.text()) != 0:
            self.nameEdit.setFocus()
        else:
            self.changeKeyboardLayoutToUpper()

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.nameEdit.clear()
        if len(self.nameEdit.text()) != 0:
            self.nameEdit.setFocus()
        else:
            self.changeKeyboardLayoutToUpper()

    @pyqtSlot()
    def on_goBackButton_clicked(self):
        self.nameEdit.setText(self.nameEdit.text())
        self.close()

    @pyqtSlot()
    def on_lCapButton_clicked(self):
        if self.keyboardState == KeyboardState.Lower:
            self.keyboardState = KeyboardState.Upper
            self.rCapButton.setStyleSheet(self.upperCapButtonStyleSheet)
            self.lCapButton.setStyleSheet(self.upperCapButtonStyleSheet)
            self.updateState()
        else:
            self.keyboardState = KeyboardState.Lower
            self.rCapButton.setStyleSheet(self.lowerCapButtonStyleSheet)
            self.lCapButton.setStyleSheet(self.lowerCapButtonStyleSheet)
            self.updateState()

    @pyqtSlot()
    def on_rCapButton_clicked(self):
        if self.keyboardState == KeyboardState.Lower:
            self.keyboardState = KeyboardState.Upper
            self.rCapButton.setStyleSheet(self.upperCapButtonStyleSheet)
            self.lCapButton.setStyleSheet(self.upperCapButtonStyleSheet)
            self.updateState()
        else:
            self.keyboardState = KeyboardState.Lower
            self.rCapButton.setStyleSheet(self.lowerCapButtonStyleSheet)
            self.lCapButton.setStyleSheet(self.lowerCapButtonStyleSheet)
            self.updateState()

    @pyqtSlot()
    def on_leftArrowButton_clicked(self):
        if len(self.nameEdit.text()) > 0:
            currentPos = self.nameEdit.cursorPosition()
            self.nameEdit.setCursorPosition(currentPos - 1)
            self.nameEdit.setFocus()

    @pyqtSlot()
    def on_rightArrowButton_clicked(self):
        if len(self.nameEdit.text()) > 0:
            currentPos = self.nameEdit.cursorPosition()
            self.nameEdit.setCursorPosition(currentPos + 1)
            self.nameEdit.setFocus()

if debug:
    app = QApplication([])
    mw = VirtualFullSizeKeyboard()
    mw.show()
    app.exec()