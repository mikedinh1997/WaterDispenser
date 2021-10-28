from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Windows import MainWindow_ui
from Windows.addingNewUser import AddingNewUser
from Widgets.virtualKeyboard import VirtualKeyboard

from Database.UserDatabase import *
from Windows.weightScreen import WeightScreen


class MainWindow(QWidget, MainWindow_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('./Icons/water-dispenser.png'))
        QtWidgets.QApplication.instance().focusChanged.connect(self.on_focusChanged)

        self.powerOffButton.setIcon(QIcon('./Icons/turn-off.png'))

        self.userDatabase = UserDatabase()
        self.searchKeyboard = None

        self.instantiateUserListWidget()

    @pyqtSlot()
    def on_addNewUserButton_clicked(self):

        addingNewUserDialog = AddingNewUser(parent=self, userDatabase=self.userDatabase)
        addingNewUserDialog.show()

        self.instantiateUserListWidget()

    def instantiateUserListWidget(self):
        usersList = self.userDatabase.getUsersList()
        self.userListWidget.clear()
        for user in usersList:
            self.userListWidget.addItem("%s %s" % (user.lastName, user.firstName))

        self.userListWidget.sortItems(Qt.AscendingOrder)

    @pyqtSlot()
    def on_powerOffButton_clicked(self):
        resp = QMessageBox.question(self, 'Restart', 'Do you want to turn off the device?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resp == QMessageBox.Yes:
            print('Power off')
            exit(0)

    @pyqtSlot("QWidget*", "QWidget*")
    def on_focusChanged(self, old, currentWidget):
        if self.nameSearchEdit == currentWidget:
            if not self.searchKeyboard:
                self.searchKeyboard = VirtualKeyboard(parent=self, parentLineEdit=self.nameSearchEdit)
            self.searchKeyboard.exec()

    @pyqtSlot(QListWidgetItem)
    def on_userListWidget_itemClicked(self, item):
        lastName = item.text().split()[0]
        firstName = item.text().split()[1]
        user, status = self.userDatabase.findUserFromNames(firstName, lastName)

        if status == NOT_FOUND:
            return

        weightScreenDialog = WeightScreen(parent=self, user=user, userDatabase=self.userDatabase)
        weightScreenDialog.show()

        self.instantiateUserListWidget()

    @pyqtSlot(str)
    def on_nameSearchEdit_textChanged(self, keyword):
        self.userListWidget.clear()
        usersList = self.userDatabase.getUsersList()
        filtered_usersList = list(filter(lambda u: str("%s %s" % (u.lastName, u.firstName)).lower().startswith(keyword.lower())
                                                or str("%s %s" % (u.firstName, u.lastName)).lower().startswith(keyword.lower())
                                                or u.firstName.lower().startswith(keyword.lower())
                                         or u.lastName.lower().startswith(keyword.lower()),
                                         usersList))

        for user in filtered_usersList:
            self.userListWidget.addItem("%s %s" % (user.lastName, user.firstName))

        self.userListWidget.sortItems(Qt.AscendingOrder)




