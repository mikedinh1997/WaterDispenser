from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

from Windows import AddingNewUser_ui
from Windows.weightScreen import WeightScreen
from Database.UserDatabase import *
from Widgets.virtualKeyboardBox import VirtualFullSizeKeyboard
from Widgets.VirtualNumpad import VirtualNumpad
from util.constant import *

EXCEL_FILE_DIR = './Database/' + EXCEL_FILE_NAME

class AddingNewUser(QDialog, AddingNewUser_ui.Ui_AddingNewUser):
    def __init__(self, parent=None, userDatabase = None):
        super(AddingNewUser, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        QtWidgets.QApplication.instance().focusChanged.connect(self.on_focusChanged)

        self.moveToCenter()

        self.saveAndReturnButton.setFocus()
        self.userDatabase = userDatabase
        self.currentUser = None

        self.keyboardForFirstName = None
        self.keyboardForLastName = None
        self.numpadForCurrentWeight = None

    def show(self):
        self.exec()

    # The function is customed to center the dialog
    def moveToCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def checkUserNameValidity(self, name):
        if len(name) == 0:
            return EMPTY_NAME
        if any(p in name for p in SPECIAL_CHARS):
            return INVALID_NAME
        if any(s.isdigit() for s in name):
            return INVALID_NAME

        return VALID_NAME

    @pyqtSlot()
    def on_saveAndContinueButton_clicked(self):
        # Open weightScreenDialog

        # Get user's first name
        newUserFirstName = self.firstNameEdit.text().lower().capitalize()
        # Get user's last name
        newUserLastName = self.lastNameEdit.text().lower().capitalize()

        # Check validity of newly entered first name
        firstNameCheck = self.checkUserNameValidity(newUserFirstName)

        # Check validity of newly entered last name
        lastNameCheck = self.checkUserNameValidity(newUserLastName)

        # Enable error Logging label
        self.errorLoggingLabel.setEnabled(True)

        # Check if any errors in first name or last name
        if firstNameCheck == EMPTY_NAME or lastNameCheck == EMPTY_NAME:
            return
        elif firstNameCheck == INVALID_NAME and lastNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('FIRST NAME AND LAST NAME CONTAINS PUNCTUATION OR NUMBER')
            return
        elif firstNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('FIRST NAME CONTAINS PUNCTUATION OR NUMBER')
            return
        elif lastNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('LAST NAME CONTAINS PUNCTUATION OR NUMBER')
            return

        startWeight = float(self.currentWeightEdit.text())
        newUser = User(firstName=newUserFirstName, lastName=newUserLastName, startWeight=startWeight, endWeight=0)
        # Save new user and check saving status
        savingStatus = self.userDatabase.addUserToDatabase(newUser)
        if savingStatus == USER_EXIST:
            self.errorLoggingLabel.setText('USER IS ALREADY ADDED TO THE DEVICE')
        elif savingStatus == USER_SAVED:
            self.currentUser = newUser
            self.errorLoggingLabel.setStyleSheet("QLabel {color: green; font-size: 15px;}")
            self.errorLoggingLabel.setText('USER IS SUCCESSFULLY ADDED TO THE DEVICE')

            weightScreenDialog = WeightScreen(parent=self, user=self.currentUser, userDatabase=self.userDatabase)
            weightScreenDialog.show()
            self.close()

    @pyqtSlot()
    def on_backButton_clicked(self):
        # Close the adding New User Dialog
        self.close()

    @pyqtSlot("QWidget*", "QWidget*")
    def on_focusChanged(self, old, currentWidget):
        if self.firstNameEdit == currentWidget:
            if not self.keyboardForFirstName:
                self.keyboardForFirstName = VirtualFullSizeKeyboard(parent=self, parentLineEdit=self.firstNameEdit)
            self.keyboardForFirstName.exec()

        elif self.lastNameEdit == currentWidget:
            if not self.keyboardForLastName:
                self.keyboardForLastName = VirtualFullSizeKeyboard(parent=self, parentLineEdit=self.lastNameEdit)
            self.keyboardForLastName.exec()

        elif self.currentWeightEdit == currentWidget:
            if not self.numpadForCurrentWeight:
                self.numpadForCurrentWeight = VirtualNumpad(parent=self, parentLineEdit=self.currentWeightEdit)
            self.numpadForCurrentWeight.exec()


    @pyqtSlot()
    def on_saveAndReturnButton_clicked(self):
        # Get user's first name
        newUserFirstName = self.firstNameEdit.text().lower().capitalize()
        # Get user's last name
        newUserLastName = self.lastNameEdit.text().lower().capitalize()

        # Check validity of newly entered first name
        firstNameCheck = self.checkUserNameValidity(newUserFirstName)

        # Check validity of newly entered last name
        lastNameCheck = self.checkUserNameValidity(newUserLastName)

        # Enable error Logging label
        self.errorLoggingLabel.setEnabled(True)

        # Check if any errors in first name or last name
        if firstNameCheck == EMPTY_NAME or lastNameCheck == EMPTY_NAME:
            return
        elif firstNameCheck == INVALID_NAME and lastNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('FIRST NAME AND LAST NAME CONTAINS PUNCTUATION OR NUMBER')
            return
        elif firstNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('FIRST NAME CONTAINS PUNCTUATION OR NUMBER')
            return
        elif lastNameCheck == INVALID_NAME:
            self.errorLoggingLabel.setText('LAST NAME CONTAINS PUNCTUATION OR NUMBER')
            return

        startWeight = float(self.currentWeightEdit.text())
        newUser = User(firstName=newUserFirstName, lastName=newUserLastName, startWeight=startWeight, endWeight=0)
        # Save new user and check saving status
        savingStatus = self.userDatabase.addUserToDatabase(newUser)
        if savingStatus == USER_EXIST:
            self.errorLoggingLabel.setText('USER IS ALREADY ADDED TO THE DEVICE')
        elif savingStatus == USER_SAVED:
            self.currentUser = newUser
            self.errorLoggingLabel.setStyleSheet("QLabel {color: green; font-size: 15px;}")
            self.errorLoggingLabel.setText('USER IS SUCCESSFULLY ADDED TO THE DEVICE')

            self.close()



