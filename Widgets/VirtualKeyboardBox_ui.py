# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Senior Design\WaterDispenser\Widgets\VirtualKeyboardBox.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VirtualKeyboardBox(object):
    def setupUi(self, VirtualKeyboardBox):
        VirtualKeyboardBox.setObjectName("VirtualKeyboardBox")
        VirtualKeyboardBox.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VirtualKeyboardBox.sizePolicy().hasHeightForWidth())
        VirtualKeyboardBox.setSizePolicy(sizePolicy)
        VirtualKeyboardBox.setMinimumSize(QtCore.QSize(800, 480))
        VirtualKeyboardBox.setMaximumSize(QtCore.QSize(800, 480))
        VirtualKeyboardBox.setStyleSheet("QDialog{\n"
"    background-color: black;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(VirtualKeyboardBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 10)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.nameEdit = QtWidgets.QLineEdit(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QtCore.QSize(800, 240))
        self.nameEdit.setMaximumSize(QtCore.QSize(800, 240))
        self.nameEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nameEdit.setStyleSheet("QLineEdit#nameEdit{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-size: 24px;\n"
"}")
        self.nameEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.qButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qButton.sizePolicy().hasHeightForWidth())
        self.qButton.setSizePolicy(sizePolicy)
        self.qButton.setMinimumSize(QtCore.QSize(0, 0))
        self.qButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.qButton.setStyleSheet("QPushButton{\n"
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
        self.qButton.setObjectName("qButton")
        self.horizontalLayout_11.addWidget(self.qButton)
        self.wButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wButton.sizePolicy().hasHeightForWidth())
        self.wButton.setSizePolicy(sizePolicy)
        self.wButton.setStyleSheet("QPushButton{\n"
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
        self.wButton.setObjectName("wButton")
        self.horizontalLayout_11.addWidget(self.wButton)
        self.eButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eButton.sizePolicy().hasHeightForWidth())
        self.eButton.setSizePolicy(sizePolicy)
        self.eButton.setStyleSheet("QPushButton{\n"
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
        self.eButton.setObjectName("eButton")
        self.horizontalLayout_11.addWidget(self.eButton)
        self.rButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rButton.sizePolicy().hasHeightForWidth())
        self.rButton.setSizePolicy(sizePolicy)
        self.rButton.setStyleSheet("QPushButton{\n"
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
        self.rButton.setObjectName("rButton")
        self.horizontalLayout_11.addWidget(self.rButton)
        self.tButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tButton.sizePolicy().hasHeightForWidth())
        self.tButton.setSizePolicy(sizePolicy)
        self.tButton.setStyleSheet("QPushButton{\n"
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
        self.tButton.setObjectName("tButton")
        self.horizontalLayout_11.addWidget(self.tButton)
        self.yButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yButton.sizePolicy().hasHeightForWidth())
        self.yButton.setSizePolicy(sizePolicy)
        self.yButton.setStyleSheet("QPushButton{\n"
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
        self.yButton.setObjectName("yButton")
        self.horizontalLayout_11.addWidget(self.yButton)
        self.uButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uButton.sizePolicy().hasHeightForWidth())
        self.uButton.setSizePolicy(sizePolicy)
        self.uButton.setStyleSheet("QPushButton{\n"
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
        self.uButton.setObjectName("uButton")
        self.horizontalLayout_11.addWidget(self.uButton)
        self.iButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iButton.sizePolicy().hasHeightForWidth())
        self.iButton.setSizePolicy(sizePolicy)
        self.iButton.setStyleSheet("QPushButton{\n"
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
        self.iButton.setObjectName("iButton")
        self.horizontalLayout_11.addWidget(self.iButton)
        self.oButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oButton.sizePolicy().hasHeightForWidth())
        self.oButton.setSizePolicy(sizePolicy)
        self.oButton.setStyleSheet("QPushButton{\n"
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
        self.oButton.setObjectName("oButton")
        self.horizontalLayout_11.addWidget(self.oButton)
        self.pButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pButton.sizePolicy().hasHeightForWidth())
        self.pButton.setSizePolicy(sizePolicy)
        self.pButton.setStyleSheet("QPushButton{\n"
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
        self.pButton.setObjectName("pButton")
        self.horizontalLayout_11.addWidget(self.pButton)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)
        self.deleteButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setMinimumSize(QtCore.QSize(60, 0))
        self.deleteButton.setMaximumSize(QtCore.QSize(60, 16777215))
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
        self.deleteButton.setText("")
        self.deleteButton.setIconSize(QtCore.QSize(60, 52))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_14.addWidget(self.deleteButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem2 = QtWidgets.QSpacerItem(60, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.aButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aButton.sizePolicy().hasHeightForWidth())
        self.aButton.setSizePolicy(sizePolicy)
        self.aButton.setStyleSheet("QPushButton{\n"
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
        self.aButton.setObjectName("aButton")
        self.horizontalLayout_12.addWidget(self.aButton)
        self.sButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sButton.sizePolicy().hasHeightForWidth())
        self.sButton.setSizePolicy(sizePolicy)
        self.sButton.setStyleSheet("QPushButton{\n"
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
        self.sButton.setObjectName("sButton")
        self.horizontalLayout_12.addWidget(self.sButton)
        self.dButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dButton.sizePolicy().hasHeightForWidth())
        self.dButton.setSizePolicy(sizePolicy)
        self.dButton.setStyleSheet("QPushButton{\n"
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
        self.dButton.setObjectName("dButton")
        self.horizontalLayout_12.addWidget(self.dButton)
        self.fButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fButton.sizePolicy().hasHeightForWidth())
        self.fButton.setSizePolicy(sizePolicy)
        self.fButton.setStyleSheet("QPushButton{\n"
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
        self.fButton.setObjectName("fButton")
        self.horizontalLayout_12.addWidget(self.fButton)
        self.gButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gButton.sizePolicy().hasHeightForWidth())
        self.gButton.setSizePolicy(sizePolicy)
        self.gButton.setStyleSheet("QPushButton{\n"
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
        self.gButton.setObjectName("gButton")
        self.horizontalLayout_12.addWidget(self.gButton)
        self.hButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hButton.sizePolicy().hasHeightForWidth())
        self.hButton.setSizePolicy(sizePolicy)
        self.hButton.setStyleSheet("QPushButton{\n"
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
        self.hButton.setObjectName("hButton")
        self.horizontalLayout_12.addWidget(self.hButton)
        self.jButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jButton.sizePolicy().hasHeightForWidth())
        self.jButton.setSizePolicy(sizePolicy)
        self.jButton.setStyleSheet("QPushButton{\n"
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
        self.jButton.setObjectName("jButton")
        self.horizontalLayout_12.addWidget(self.jButton)
        self.kButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kButton.sizePolicy().hasHeightForWidth())
        self.kButton.setSizePolicy(sizePolicy)
        self.kButton.setStyleSheet("QPushButton{\n"
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
        self.kButton.setObjectName("kButton")
        self.horizontalLayout_12.addWidget(self.kButton)
        self.lButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lButton.sizePolicy().hasHeightForWidth())
        self.lButton.setSizePolicy(sizePolicy)
        self.lButton.setStyleSheet("QPushButton{\n"
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
        self.lButton.setObjectName("lButton")
        self.horizontalLayout_12.addWidget(self.lButton)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)
        self.enterButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enterButton.sizePolicy().hasHeightForWidth())
        self.enterButton.setSizePolicy(sizePolicy)
        self.enterButton.setMinimumSize(QtCore.QSize(100, 0))
        self.enterButton.setMaximumSize(QtCore.QSize(100, 16777215))
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
        self.enterButton.setText("")
        self.enterButton.setIconSize(QtCore.QSize(100, 51))
        self.enterButton.setObjectName("enterButton")
        self.horizontalLayout_15.addWidget(self.enterButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.lCapButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lCapButton.sizePolicy().hasHeightForWidth())
        self.lCapButton.setSizePolicy(sizePolicy)
        self.lCapButton.setMinimumSize(QtCore.QSize(120, 0))
        self.lCapButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lCapButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.lCapButton.setText("")
        self.lCapButton.setIconSize(QtCore.QSize(120, 52))
        self.lCapButton.setObjectName("lCapButton")
        self.horizontalLayout_16.addWidget(self.lCapButton)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.zButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zButton.sizePolicy().hasHeightForWidth())
        self.zButton.setSizePolicy(sizePolicy)
        self.zButton.setStyleSheet("QPushButton{\n"
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
        self.zButton.setObjectName("zButton")
        self.horizontalLayout_13.addWidget(self.zButton)
        self.xButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xButton.sizePolicy().hasHeightForWidth())
        self.xButton.setSizePolicy(sizePolicy)
        self.xButton.setStyleSheet("QPushButton{\n"
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
        self.xButton.setObjectName("xButton")
        self.horizontalLayout_13.addWidget(self.xButton)
        self.cButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cButton.sizePolicy().hasHeightForWidth())
        self.cButton.setSizePolicy(sizePolicy)
        self.cButton.setStyleSheet("QPushButton{\n"
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
        self.cButton.setObjectName("cButton")
        self.horizontalLayout_13.addWidget(self.cButton)
        self.vButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vButton.sizePolicy().hasHeightForWidth())
        self.vButton.setSizePolicy(sizePolicy)
        self.vButton.setStyleSheet("QPushButton{\n"
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
        self.vButton.setObjectName("vButton")
        self.horizontalLayout_13.addWidget(self.vButton)
        self.bButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bButton.sizePolicy().hasHeightForWidth())
        self.bButton.setSizePolicy(sizePolicy)
        self.bButton.setStyleSheet("QPushButton{\n"
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
        self.bButton.setObjectName("bButton")
        self.horizontalLayout_13.addWidget(self.bButton)
        self.nButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nButton.sizePolicy().hasHeightForWidth())
        self.nButton.setSizePolicy(sizePolicy)
        self.nButton.setStyleSheet("QPushButton{\n"
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
        self.nButton.setObjectName("nButton")
        self.horizontalLayout_13.addWidget(self.nButton)
        self.mButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mButton.sizePolicy().hasHeightForWidth())
        self.mButton.setSizePolicy(sizePolicy)
        self.mButton.setStyleSheet("QPushButton{\n"
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
        self.mButton.setObjectName("mButton")
        self.horizontalLayout_13.addWidget(self.mButton)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)
        self.rCapButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rCapButton.sizePolicy().hasHeightForWidth())
        self.rCapButton.setSizePolicy(sizePolicy)
        self.rCapButton.setMinimumSize(QtCore.QSize(120, 0))
        self.rCapButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rCapButton.setStyleSheet("QPushButton{\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.rCapButton.setText("")
        self.rCapButton.setIconSize(QtCore.QSize(120, 50))
        self.rCapButton.setObjectName("rCapButton")
        self.horizontalLayout_16.addWidget(self.rCapButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.goBackButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goBackButton.sizePolicy().hasHeightForWidth())
        self.goBackButton.setSizePolicy(sizePolicy)
        self.goBackButton.setMinimumSize(QtCore.QSize(70, 0))
        self.goBackButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.goBackButton.setStyleSheet("QPushButton{\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.goBackButton.setObjectName("goBackButton")
        self.horizontalLayout.addWidget(self.goBackButton)
        self.clearButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(70, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.clearButton.setStyleSheet("QPushButton{\n"
"    font-size: 11px;\n"
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
        self.horizontalLayout.addWidget(self.clearButton)
        self.spaceButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spaceButton.sizePolicy().hasHeightForWidth())
        self.spaceButton.setSizePolicy(sizePolicy)
        self.spaceButton.setMinimumSize(QtCore.QSize(400, 0))
        self.spaceButton.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: white;\n"
"    background-color: rgb(36, 36, 36);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(207, 207, 207)\n"
"}")
        self.spaceButton.setObjectName("spaceButton")
        self.horizontalLayout.addWidget(self.spaceButton)
        self.leftArrowButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftArrowButton.sizePolicy().hasHeightForWidth())
        self.leftArrowButton.setSizePolicy(sizePolicy)
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
        self.leftArrowButton.setText("")
        self.leftArrowButton.setIconSize(QtCore.QSize(70, 51))
        self.leftArrowButton.setObjectName("leftArrowButton")
        self.horizontalLayout.addWidget(self.leftArrowButton)
        self.rightArrowButton = QtWidgets.QPushButton(VirtualKeyboardBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightArrowButton.sizePolicy().hasHeightForWidth())
        self.rightArrowButton.setSizePolicy(sizePolicy)
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
        self.rightArrowButton.setText("")
        self.rightArrowButton.setIconSize(QtCore.QSize(70, 51))
        self.rightArrowButton.setObjectName("rightArrowButton")
        self.horizontalLayout.addWidget(self.rightArrowButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(VirtualKeyboardBox)
        QtCore.QMetaObject.connectSlotsByName(VirtualKeyboardBox)

    def retranslateUi(self, VirtualKeyboardBox):
        _translate = QtCore.QCoreApplication.translate
        VirtualKeyboardBox.setWindowTitle(_translate("VirtualKeyboardBox", "VirtualKeyboardBox"))
        self.nameEdit.setPlaceholderText(_translate("VirtualKeyboardBox", "Name"))
        self.qButton.setText(_translate("VirtualKeyboardBox", "q"))
        self.wButton.setText(_translate("VirtualKeyboardBox", "w"))
        self.eButton.setText(_translate("VirtualKeyboardBox", "e"))
        self.rButton.setText(_translate("VirtualKeyboardBox", "r"))
        self.tButton.setText(_translate("VirtualKeyboardBox", "t"))
        self.yButton.setText(_translate("VirtualKeyboardBox", "y"))
        self.uButton.setText(_translate("VirtualKeyboardBox", "u"))
        self.iButton.setText(_translate("VirtualKeyboardBox", "i"))
        self.oButton.setText(_translate("VirtualKeyboardBox", "o"))
        self.pButton.setText(_translate("VirtualKeyboardBox", "p"))
        self.aButton.setText(_translate("VirtualKeyboardBox", "a"))
        self.sButton.setText(_translate("VirtualKeyboardBox", "s"))
        self.dButton.setText(_translate("VirtualKeyboardBox", "d"))
        self.fButton.setText(_translate("VirtualKeyboardBox", "f"))
        self.gButton.setText(_translate("VirtualKeyboardBox", "g"))
        self.hButton.setText(_translate("VirtualKeyboardBox", "h"))
        self.jButton.setText(_translate("VirtualKeyboardBox", "j"))
        self.kButton.setText(_translate("VirtualKeyboardBox", "k"))
        self.lButton.setText(_translate("VirtualKeyboardBox", "l"))
        self.zButton.setText(_translate("VirtualKeyboardBox", "z"))
        self.xButton.setText(_translate("VirtualKeyboardBox", "x"))
        self.cButton.setText(_translate("VirtualKeyboardBox", "c"))
        self.vButton.setText(_translate("VirtualKeyboardBox", "v"))
        self.bButton.setText(_translate("VirtualKeyboardBox", "b"))
        self.nButton.setText(_translate("VirtualKeyboardBox", "n"))
        self.mButton.setText(_translate("VirtualKeyboardBox", "m"))
        self.goBackButton.setText(_translate("VirtualKeyboardBox", "GO BACK"))
        self.clearButton.setText(_translate("VirtualKeyboardBox", "CLEAR"))
        self.spaceButton.setText(_translate("VirtualKeyboardBox", "SPACE"))
