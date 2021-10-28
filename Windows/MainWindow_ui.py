# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Senior Design\WaterDispenser\Windows\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.userListWidget = QtWidgets.QListWidget(MainWindow)
        self.userListWidget.setStyleSheet("QListWidget {\n"
"    font-size: 20px;\n"
"}\n"
" QListView::item:selected\n"
"{\n"
"    border : 2px solid black;\n"
"    background : rgb(207, 207, 207);\n"
"}")
        self.userListWidget.setObjectName("userListWidget")
        self.horizontalLayout_4.addWidget(self.userListWidget)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.nameSearchEdit = QtWidgets.QLineEdit(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameSearchEdit.sizePolicy().hasHeightForWidth())
        self.nameSearchEdit.setSizePolicy(sizePolicy)
        self.nameSearchEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.nameSearchEdit.setStyleSheet("QLineEdit{ \n"
"    border-style: outset;\n"
"    border-color: black;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    font-size: 20px;\n"
"}")
        self.nameSearchEdit.setText("")
        self.nameSearchEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nameSearchEdit.setObjectName("nameSearchEdit")
        self.horizontalLayout_2.addWidget(self.nameSearchEdit)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(650, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.powerOffButton = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.powerOffButton.sizePolicy().hasHeightForWidth())
        self.powerOffButton.setSizePolicy(sizePolicy)
        self.powerOffButton.setMinimumSize(QtCore.QSize(50, 50))
        self.powerOffButton.setMaximumSize(QtCore.QSize(50, 50))
        self.powerOffButton.setStyleSheet("font-size: 13px;\n"
" background-color: red;\n"
" border-radius:20px;\n"
" border-color: blue;\n"
" max-width:50px;\n"
" max-height:50px;\n"
" min-width:50px;\n"
" min-height:50px;\n"
"")
        self.powerOffButton.setText("")
        self.powerOffButton.setObjectName("powerOffButton")
        self.horizontalLayout_3.addWidget(self.powerOffButton)
        spacerItem6 = QtWidgets.QSpacerItem(5, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 5, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.addNewUserButton = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNewUserButton.sizePolicy().hasHeightForWidth())
        self.addNewUserButton.setSizePolicy(sizePolicy)
        self.addNewUserButton.setMinimumSize(QtCore.QSize(0, 100))
        self.addNewUserButton.setStyleSheet("font-size: 20px;")
        self.addNewUserButton.setObjectName("addNewUserButton")
        self.horizontalLayout.addWidget(self.addNewUserButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameSearchEdit.setPlaceholderText(_translate("MainWindow", "Search your name"))
        self.addNewUserButton.setText(_translate("MainWindow", "Add new user"))
