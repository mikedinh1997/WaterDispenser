# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\quang\OneDrive - Southern Illinois University Edwardsville\Water-Dispenser\Windows\WeightScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WeightScreen(object):
    def setupUi(self, WeightScreen):
        WeightScreen.setObjectName("WeightScreen")
        WeightScreen.resize(800, 480)
        WeightScreen.setMinimumSize(QtCore.QSize(800, 480))
        WeightScreen.setMaximumSize(QtCore.QSize(800, 480))
        self.gridLayout = QtWidgets.QGridLayout(WeightScreen)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.userNamelabel = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userNamelabel.sizePolicy().hasHeightForWidth())
        self.userNamelabel.setSizePolicy(sizePolicy)
        self.userNamelabel.setStyleSheet("border-style: outset;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"font-size: 15px;\n"
"color: rgb(0, 0, 255)")
        self.userNamelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNamelabel.setObjectName("userNamelabel")
        self.horizontalLayout_5.addWidget(self.userNamelabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.remainLabel = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remainLabel.sizePolicy().hasHeightForWidth())
        self.remainLabel.setSizePolicy(sizePolicy)
        self.remainLabel.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"    color: rgb(0, 170, 0)\n"
"}")
        self.remainLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.remainLabel.setWordWrap(True)
        self.remainLabel.setObjectName("remainLabel")
        self.horizontalLayout_7.addWidget(self.remainLabel)
        self.label_10 = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"    color: rgb(0, 170, 0)\n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(WeightScreen)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(WeightScreen)
        self.label_5.setStyleSheet("font-size: 13px;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.startWeightEdit = QtWidgets.QLineEdit(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startWeightEdit.sizePolicy().hasHeightForWidth())
        self.startWeightEdit.setSizePolicy(sizePolicy)
        self.startWeightEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.startWeightEdit.setStyleSheet("border-radius: 5px;\n"
"font-size: 13px;")
        self.startWeightEdit.setObjectName("startWeightEdit")
        self.horizontalLayout.addWidget(self.startWeightEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(WeightScreen)
        self.label_6.setStyleSheet("font-size: 13px;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.endWeightEdit = QtWidgets.QLineEdit(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endWeightEdit.sizePolicy().hasHeightForWidth())
        self.endWeightEdit.setSizePolicy(sizePolicy)
        self.endWeightEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.endWeightEdit.setStyleSheet("border-radius: 5px;\n"
"font-size: 13px;")
        self.endWeightEdit.setObjectName("endWeightEdit")
        self.horizontalLayout_2.addWidget(self.endWeightEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"}")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dispenseAmountLabel = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispenseAmountLabel.sizePolicy().hasHeightForWidth())
        self.dispenseAmountLabel.setSizePolicy(sizePolicy)
        self.dispenseAmountLabel.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"    color: rgb(0, 170, 0);\n"
"}")
        self.dispenseAmountLabel.setScaledContents(False)
        self.dispenseAmountLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dispenseAmountLabel.setWordWrap(True)
        self.dispenseAmountLabel.setObjectName("dispenseAmountLabel")
        self.horizontalLayout_3.addWidget(self.dispenseAmountLabel)
        self.label_8 = QtWidgets.QLabel(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("QLabel{\n"
"    font-size: 15px;\n"
"    color: rgb(0, 170, 0);\n"
"}")
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.notifyLabel = QtWidgets.QLabel(WeightScreen)
        self.notifyLabel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notifyLabel.sizePolicy().hasHeightForWidth())
        self.notifyLabel.setSizePolicy(sizePolicy)
        self.notifyLabel.setStyleSheet("QLabel{\n"
"    color:red;\n"
"    font-size: 15px;\n"
"}")
        self.notifyLabel.setText("")
        self.notifyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notifyLabel.setObjectName("notifyLabel")
        self.horizontalLayout_6.addWidget(self.notifyLabel)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem11, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.backButton = QtWidgets.QPushButton(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setStyleSheet("font-size: 13px;")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_4.addWidget(self.backButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.dispenseButton = QtWidgets.QPushButton(WeightScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispenseButton.sizePolicy().hasHeightForWidth())
        self.dispenseButton.setSizePolicy(sizePolicy)
        self.dispenseButton.setStyleSheet("font-size: 13px;")
        self.dispenseButton.setObjectName("dispenseButton")
        self.horizontalLayout_4.addWidget(self.dispenseButton)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 42, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 8, 0, 1, 1)

        self.retranslateUi(WeightScreen)
        QtCore.QMetaObject.connectSlotsByName(WeightScreen)

    def retranslateUi(self, WeightScreen):
        _translate = QtCore.QCoreApplication.translate
        WeightScreen.setWindowTitle(_translate("WeightScreen", "WeightScreen"))
        self.userNamelabel.setText(_translate("WeightScreen", "User name"))
        self.label_3.setText(_translate("WeightScreen", "Remaining Water"))
        self.remainLabel.setText(_translate("WeightScreen", "10"))
        self.label_10.setText(_translate("WeightScreen", "oz"))
        self.label_5.setText(_translate("WeightScreen", "Starting Weight:"))
        self.label_6.setText(_translate("WeightScreen", "Ending Weight:"))
        self.label_4.setText(_translate("WeightScreen", "Dispensed Amount"))
        self.dispenseAmountLabel.setText(_translate("WeightScreen", "10"))
        self.label_8.setText(_translate("WeightScreen", "oz"))
        self.backButton.setText(_translate("WeightScreen", "Back"))
        self.dispenseButton.setText(_translate("WeightScreen", "Dispense"))
