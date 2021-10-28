import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Widgets.VirtualNumpad import VirtualNumpad

from Windows import WeightScreen_ui
from Database.UserDatabase import *


debug = False
if debug:
    import pyqt5ac

    pyqt5ac.main(config='config.yml')

class WeightScreen(QDialog, WeightScreen_ui.Ui_WeightScreen):

    endWeightEditFinished = pyqtSignal()

    def __init__(self, parent=None, user=None, userDatabase=None):
        super(WeightScreen, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        QtWidgets.QApplication.instance().focusChanged.connect(self.on_focusChanged)

        self.moveToCenter()

        if isinstance(user, User):
            self.currentUser = user
            self.initialize()

        if isinstance(userDatabase, UserDatabase):
            self.userDatabase = userDatabase


        self.numpadForStartWeight = None
        self.numpadForEndWeight = None

        self.endWeightEditFinished.connect(self.on_endWeightEditFinished)

    def show(self):
        self.exec()

    # The function is customed to center the dialog
    def moveToCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def initialize(self):
        self.userNamelabel.setText(self.currentUser.firstName + ' ' + self.currentUser.lastName)


        startWeight = float(self.currentUser.startWeight)
        endWeight = float(self.currentUser.endWeight)

        if startWeight < endWeight:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('Weight before workout is smaller than weight after workout \n'
                                     'Please enter your post-workout weight again')
            return
        else:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('')

        self.startWeightEdit.setText(str(startWeight))
        self.endWeightEdit.setText((str(endWeight)))

        amountDispensed = (startWeight - endWeight) * 16

        self.dispenseAmountLabel.setText(str(amountDispensed))


    @pyqtSlot("QWidget*", "QWidget*")
    def on_focusChanged(self, old, currentWidget):
        if self.startWeightEdit == currentWidget:
            if not self.numpadForStartWeight:
                self.numpadForStartWeight = VirtualNumpad(parent=self, parentLineEdit=self.startWeightEdit)
            self.numpadForStartWeight.exec()

        elif self.endWeightEdit == currentWidget:
            if not self.numpadForEndWeight:
                self.numpadForEndWeight = VirtualNumpad(parent=self, parentLineEdit=self.endWeightEdit,
                                                        signalFromParentLineEdit=self.endWeightEditFinished)
            self.numpadForEndWeight.exec()


    @pyqtSlot()
    def on_backButton_clicked(self):
        self.close()

    @pyqtSlot()
    def on_dispenseButton_clicked(self):
        if len(self.startWeightEdit.text()) == 0 or len(self.endWeightEdit.text()) == 0:
            return

        startWeight = float(self.startWeightEdit.text())
        endWeight = float(self.endWeightEdit.text())

        if startWeight < endWeight:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('Weight before workout is smaller than weight after workout \n'
                                     'Please enter your post-workout weight again')
            return

        if float(startWeight) == 0.0 or float(endWeight) == 0.0:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('Weight cannot be zero')
            return


        self.currentUser.setStartWeight(startWeight)
        self.currentUser.setEndWeight(endWeight)

        self.userDatabase.updateUser(self.currentUser)

        # Calculate amount of water to dipense
        amountInOz = (startWeight - endWeight) * 16;

        # Convert the calculated amount of water from oz to gram
        # 1 oz = 28.35 grams
        amountInGram = amountInOz * 28.35

        try:

            from Function.dispenser import dispense
            dispense(goalVal=amountInGram)

            self.notifyLabel.setText('Water dispensing is done. Please check your cup')
        except Exception as e:
            print('Failed to dispense water or check your wires.')

    @pyqtSlot()
    def on_endWeightEditFinished(self):
        if len(self.startWeightEdit.text()) == 0 or len(self.endWeightEdit.text()) == 0:
            return

        startWeight = float(self.startWeightEdit.text())
        endWeight = float(self.endWeightEdit.text())

        if startWeight < endWeight:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('Weight before workout is smaller than weight after workout \n'
                                     'Please enter your post-workout weight again')
            return
        else:
            self.notifyLabel.setEnabled(True)
            self.notifyLabel.setText('')

        amountDispensed = (startWeight - endWeight) * 16

        self.dispenseAmountLabel.setText(str(amountDispensed))


    @pyqtSlot()
    def on_deleteUserButton_clicked(self):

        buttonReply = QMessageBox.question(self, 'Delete user', "Are you sure to remove yourself from the device?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            self.userDatabase.deleteUser(self.currentUser)
            self.close()
            return
        else:
            return
if debug:
    app = QApplication([])
    mw = WeightScreen()
    mw.show()
    app.exec()
