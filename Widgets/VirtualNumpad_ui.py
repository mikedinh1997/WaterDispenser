# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\quang\OneDrive - Southern Illinois University Edwardsville\Water-Dispenser\Widgets\VirtualNumpad.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VirtualNumpad(object):
    def setupUi(self, VirtualNumpad):
        VirtualNumpad.setObjectName("VirtualNumpad")
        VirtualNumpad.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VirtualNumpad.sizePolicy().hasHeightForWidth())
        VirtualNumpad.setSizePolicy(sizePolicy)
        VirtualNumpad.setMinimumSize(QtCore.QSize(800, 480))
        VirtualNumpad.setMaximumSize(QtCore.QSize(800, 480))
        VirtualNumpad.setStyleSheet("QDialog{\n"
"    background-color: black;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(VirtualNumpad)
        self.gridLayout_2.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.weightEdit = QtWidgets.QLineEdit(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightEdit.sizePolicy().hasHeightForWidth())
        self.weightEdit.setSizePolicy(sizePolicy)
        self.weightEdit.setMinimumSize(QtCore.QSize(800, 150))
        self.weightEdit.setMaximumSize(QtCore.QSize(800, 240))
        self.weightEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weightEdit.setStyleSheet("QLineEdit#weightEdit{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 24px;\n"
"}")
        self.weightEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.weightEdit.setObjectName("weightEdit")
        self.gridLayout_2.addWidget(self.weightEdit, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.clearButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(50, 55))
        self.clearButton.setMaximumSize(QtCore.QSize(50, 55))
        self.clearButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 0, 1, 1)
        self.leftArrowButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftArrowButton.sizePolicy().hasHeightForWidth())
        self.leftArrowButton.setSizePolicy(sizePolicy)
        self.leftArrowButton.setMinimumSize(QtCore.QSize(50, 55))
        self.leftArrowButton.setMaximumSize(QtCore.QSize(50, 55))
        self.leftArrowButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.leftArrowButton.setIconSize(QtCore.QSize(70, 51))
        self.leftArrowButton.setObjectName("leftArrowButton")
        self.gridLayout.addWidget(self.leftArrowButton, 0, 1, 1, 1)
        self.rightArrowButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightArrowButton.sizePolicy().hasHeightForWidth())
        self.rightArrowButton.setSizePolicy(sizePolicy)
        self.rightArrowButton.setMinimumSize(QtCore.QSize(50, 55))
        self.rightArrowButton.setMaximumSize(QtCore.QSize(50, 55))
        self.rightArrowButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.rightArrowButton.setIconSize(QtCore.QSize(70, 51))
        self.rightArrowButton.setObjectName("rightArrowButton")
        self.gridLayout.addWidget(self.rightArrowButton, 0, 2, 1, 1)
        self.goBackButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goBackButton.sizePolicy().hasHeightForWidth())
        self.goBackButton.setSizePolicy(sizePolicy)
        self.goBackButton.setMinimumSize(QtCore.QSize(50, 55))
        self.goBackButton.setMaximumSize(QtCore.QSize(50, 55))
        self.goBackButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.goBackButton.setIconSize(QtCore.QSize(70, 51))
        self.goBackButton.setObjectName("goBackButton")
        self.gridLayout.addWidget(self.goBackButton, 0, 3, 1, 1)
        self.sevenButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sevenButton.sizePolicy().hasHeightForWidth())
        self.sevenButton.setSizePolicy(sizePolicy)
        self.sevenButton.setMinimumSize(QtCore.QSize(50, 55))
        self.sevenButton.setMaximumSize(QtCore.QSize(50, 55))
        self.sevenButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.sevenButton.setObjectName("sevenButton")
        self.gridLayout.addWidget(self.sevenButton, 1, 0, 1, 1)
        self.eightButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eightButton.sizePolicy().hasHeightForWidth())
        self.eightButton.setSizePolicy(sizePolicy)
        self.eightButton.setMinimumSize(QtCore.QSize(50, 55))
        self.eightButton.setMaximumSize(QtCore.QSize(50, 55))
        self.eightButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.eightButton.setObjectName("eightButton")
        self.gridLayout.addWidget(self.eightButton, 1, 1, 1, 1)
        self.nineButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nineButton.sizePolicy().hasHeightForWidth())
        self.nineButton.setSizePolicy(sizePolicy)
        self.nineButton.setMinimumSize(QtCore.QSize(50, 55))
        self.nineButton.setMaximumSize(QtCore.QSize(50, 55))
        self.nineButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.nineButton.setObjectName("nineButton")
        self.gridLayout.addWidget(self.nineButton, 1, 2, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(50, 120))
        self.deleteButton.setMaximumSize(QtCore.QSize(50, 120))
        self.deleteButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.deleteButton.setIconSize(QtCore.QSize(60, 52))
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 1, 3, 2, 1)
        self.fourButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fourButton.sizePolicy().hasHeightForWidth())
        self.fourButton.setSizePolicy(sizePolicy)
        self.fourButton.setMinimumSize(QtCore.QSize(50, 55))
        self.fourButton.setMaximumSize(QtCore.QSize(50, 55))
        self.fourButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.fourButton.setObjectName("fourButton")
        self.gridLayout.addWidget(self.fourButton, 2, 0, 1, 1)
        self.fiveButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fiveButton.sizePolicy().hasHeightForWidth())
        self.fiveButton.setSizePolicy(sizePolicy)
        self.fiveButton.setMinimumSize(QtCore.QSize(50, 55))
        self.fiveButton.setMaximumSize(QtCore.QSize(50, 55))
        self.fiveButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.fiveButton.setObjectName("fiveButton")
        self.gridLayout.addWidget(self.fiveButton, 2, 1, 1, 1)
        self.sixButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sixButton.sizePolicy().hasHeightForWidth())
        self.sixButton.setSizePolicy(sizePolicy)
        self.sixButton.setMinimumSize(QtCore.QSize(50, 55))
        self.sixButton.setMaximumSize(QtCore.QSize(50, 55))
        self.sixButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.sixButton.setObjectName("sixButton")
        self.gridLayout.addWidget(self.sixButton, 2, 2, 1, 1)
        self.oneButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneButton.sizePolicy().hasHeightForWidth())
        self.oneButton.setSizePolicy(sizePolicy)
        self.oneButton.setMinimumSize(QtCore.QSize(50, 55))
        self.oneButton.setMaximumSize(QtCore.QSize(50, 55))
        self.oneButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.oneButton.setObjectName("oneButton")
        self.gridLayout.addWidget(self.oneButton, 3, 0, 1, 1)
        self.twoButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoButton.sizePolicy().hasHeightForWidth())
        self.twoButton.setSizePolicy(sizePolicy)
        self.twoButton.setMinimumSize(QtCore.QSize(50, 55))
        self.twoButton.setMaximumSize(QtCore.QSize(50, 55))
        self.twoButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.twoButton.setObjectName("twoButton")
        self.gridLayout.addWidget(self.twoButton, 3, 1, 1, 1)
        self.threeButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threeButton.sizePolicy().hasHeightForWidth())
        self.threeButton.setSizePolicy(sizePolicy)
        self.threeButton.setMinimumSize(QtCore.QSize(50, 55))
        self.threeButton.setMaximumSize(QtCore.QSize(50, 55))
        self.threeButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.threeButton.setObjectName("threeButton")
        self.gridLayout.addWidget(self.threeButton, 3, 2, 1, 1)
        self.enterButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setMinimumSize(QtCore.QSize(50, 120))
        self.enterButton.setMaximumSize(QtCore.QSize(50, 120))
        self.enterButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.enterButton.setIconSize(QtCore.QSize(100, 51))
        self.enterButton.setObjectName("enterButton")
        self.gridLayout.addWidget(self.enterButton, 3, 3, 2, 1)
        self.zeroButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroButton.sizePolicy().hasHeightForWidth())
        self.zeroButton.setSizePolicy(sizePolicy)
        self.zeroButton.setMinimumSize(QtCore.QSize(114, 55))
        self.zeroButton.setMaximumSize(QtCore.QSize(106, 55))
        self.zeroButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.zeroButton.setObjectName("zeroButton")
        self.gridLayout.addWidget(self.zeroButton, 4, 0, 1, 2)
        self.periodButton = QtWidgets.QPushButton(VirtualNumpad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.periodButton.sizePolicy().hasHeightForWidth())
        self.periodButton.setSizePolicy(sizePolicy)
        self.periodButton.setMinimumSize(QtCore.QSize(50, 55))
        self.periodButton.setMaximumSize(QtCore.QSize(50, 55))
        self.periodButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(79, 79, 79);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.periodButton.setObjectName("periodButton")
        self.gridLayout.addWidget(self.periodButton, 4, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(VirtualNumpad)
        QtCore.QMetaObject.connectSlotsByName(VirtualNumpad)

    def retranslateUi(self, VirtualNumpad):
        _translate = QtCore.QCoreApplication.translate
        VirtualNumpad.setWindowTitle(_translate("VirtualNumpad", "VirtualNumpad"))
        self.weightEdit.setPlaceholderText(_translate("VirtualNumpad", "Weight"))
        self.clearButton.setText(_translate("VirtualNumpad", "CLR"))
        self.leftArrowButton.setText(_translate("VirtualNumpad", "LEFT"))
        self.rightArrowButton.setText(_translate("VirtualNumpad", "RIGHT"))
        self.goBackButton.setText(_translate("VirtualNumpad", "GO BACK"))
        self.sevenButton.setText(_translate("VirtualNumpad", "7"))
        self.eightButton.setText(_translate("VirtualNumpad", "8"))
        self.nineButton.setText(_translate("VirtualNumpad", "9"))
        self.deleteButton.setText(_translate("VirtualNumpad", "DEL"))
        self.fourButton.setText(_translate("VirtualNumpad", "4"))
        self.fiveButton.setText(_translate("VirtualNumpad", "5"))
        self.sixButton.setText(_translate("VirtualNumpad", "6"))
        self.oneButton.setText(_translate("VirtualNumpad", "1"))
        self.twoButton.setText(_translate("VirtualNumpad", "2"))
        self.threeButton.setText(_translate("VirtualNumpad", "3"))
        self.enterButton.setText(_translate("VirtualNumpad", "ENTER"))
        self.zeroButton.setText(_translate("VirtualNumpad", "0"))
        self.periodButton.setText(_translate("VirtualNumpad", "."))
