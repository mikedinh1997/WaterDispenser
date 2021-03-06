from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Widgets import VirtualKeyboard_ui
from util.enum import *

debug = False
if debug:
    import pyqt5ac

    pyqt5ac.main(config='config.yml')

class VirtualKeyboard(QDialog, VirtualKeyboard_ui.Ui_VirtualKeyboard):

    lowerCapButtonStyleSheet = "QPushButton{ font-weight: bold; color: white; background-color: rgb(36, 36, 36);" \
                               "border-radius: 5px;} " \
                               "QPushButton:hover{" \
                               "background-color: rgb(207, 207, 207)}"

    upperCapButtonStyleSheet = "QPushButton{ font-weight: bold; color: white; background-color: rgb(207, 207, 207);" \
                               "border-radius: 5px;} " \
                               "QPushButton:hover{" \
                               "background-color: rgb(207, 207, 207)}"

    def __init__(self, parent=None, parentLineEdit=None):
        super(VirtualKeyboard, self).__init__(parent)
        self.setupUi(self)
        self.parentLineEdit = parentLineEdit
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
        self.setStyleSheet("background-color: black;")
        self.setGeometry(0, 240, 800, 240)

        # self.nameEdit.setFocus()

        # self.lCapButton.setIcon(QIcon('./Icons/up_arrow.png'))
        # self.rCapButton.setIcon(QIcon('./Icons/up_arrow.png'))
        self.enterButton.setIcon(QIcon('./Icons/enter.png'))
        self.deleteButton.setIcon(QIcon('./Icons/backspace.png'))
        # self.leftArrowButton.setIcon(QIcon('./Icons/left_arrow.png'))
        # self.rightArrowButton.setIcon(QIcon('./Icons/right_arrow.png'))

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
        
        self.currentCharacterBtn = None
        
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
        
        if self.currentCharacterBtn:
            if self.currentCharacterBtn is sender:
                return
            
        for button in self.alphabetButtons:
            if button[0] is sender:
                if self.keyboardState == KeyboardState.Lower:
                    self.parentLineEdit.insert(button[1][0])
                else:
                    if len(self.parentLineEdit.text()) == 0:
                        self.parentLineEdit.insert((button[1][1]).upper())
                        self.changeKeyboardLayoutToLower()
                    else:
                        self.parentLineEdit.insert((button[1][1]))
                self.currentCharacterBtn = sender
                self.parentLineEdit.setFocus()

    @pyqtSlot()
    def on_enterButton_clicked(self):
        self.parentLineEdit.setText(self.parentLineEdit.text().capitalize())
        self.close()

    @pyqtSlot()
    def on_spaceButton_clicked(self):
        self.parentLineEdit.insert(' ')
        self.parentLineEdit.setFocus()

    @pyqtSlot()
    def on_deleteButton_clicked(self):
        self.parentLineEdit.backspace()
        if len(self.parentLineEdit.text()) != 0:
            self.parentLineEdit.setFocus()
        else:
            self.changeKeyboardLayoutToUpper()

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.parentLineEdit.clear()
        if len(self.parentLineEdit.text()) != 0:
            self.parentLineEdit.setFocus()
        else:
            self.changeKeyboardLayoutToUpper()

    @pyqtSlot()
    def on_goBackButton_clicked(self):
        self.parentLineEdit.setText(self.parentLineEdit.text())
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
        if len(self.parentLineEdit.text()) > 0:
            currentPos = self.parentLineEdit.cursorPosition()
            self.parentLineEdit.setCursorPosition(currentPos - 1)
            self.parentLineEdit.setFocus()

    @pyqtSlot()
    def on_rightArrowButton_clicked(self):
        if len(self.parentLineEdit.text()) > 0:
            currentPos = self.parentLineEdit.cursorPosition()
            self.parentLineEdit.setCursorPosition(currentPos + 1)
            self.parentLineEdit.setFocus()

if debug:
    app = QApplication([])
    mw = VirtualKeyboard()
    mw.show()
    app.exec()