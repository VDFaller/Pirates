# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Buy Cargo.ui'
#
# Created: Tue Dec 24 17:30:20 2013
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 307)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 361, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 39, 360, 185))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icons/Spices.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        self.H_Spices = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Spices.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Spices.setObjectName("H_Spices")
        self.horizontalLayout_14.addWidget(self.H_Spices)
        self.gridLayout.addLayout(self.horizontalLayout_14, 0, 2, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/Cannon_unequipped.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.H_Cannons = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Cannons.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Cannons.setObjectName("H_Cannons")
        self.horizontalLayout_13.addWidget(self.H_Cannons)
        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/Contraband.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.H_Contraband = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Contraband.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Contraband.setObjectName("H_Contraband")
        self.horizontalLayout_3.addWidget(self.H_Contraband)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.btn_Fruit_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Fruit_down.setAutoRepeat(True)
        self.btn_Fruit_down.setAutoRepeatDelay(400)
        self.btn_Fruit_down.setAutoRepeatInterval(100)
        self.btn_Fruit_down.setObjectName("btn_Fruit_down")
        self.horizontalLayout_12.addWidget(self.btn_Fruit_down)
        self.V_Fruit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Fruit.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Fruit.setObjectName("V_Fruit")
        self.horizontalLayout_12.addWidget(self.V_Fruit)
        self.btn_Fruit_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Fruit_up.setAutoRepeat(True)
        self.btn_Fruit_up.setAutoRepeatDelay(400)
        self.btn_Fruit_up.setAutoRepeatInterval(100)
        self.btn_Fruit_up.setObjectName("btn_Fruit_up")
        self.horizontalLayout_12.addWidget(self.btn_Fruit_up)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_Spices_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Spices_down.setAutoRepeat(True)
        self.btn_Spices_down.setAutoRepeatDelay(400)
        self.btn_Spices_down.setAutoRepeatInterval(100)
        self.btn_Spices_down.setObjectName("btn_Spices_down")
        self.horizontalLayout_5.addWidget(self.btn_Spices_down)
        self.V_Spices = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Spices.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Spices.setObjectName("V_Spices")
        self.horizontalLayout_5.addWidget(self.V_Spices)
        self.btn_Spices_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Spices_up.setAutoRepeat(True)
        self.btn_Spices_up.setAutoRepeatDelay(400)
        self.btn_Spices_up.setAutoRepeatInterval(100)
        self.btn_Spices_up.setObjectName("btn_Spices_up")
        self.horizontalLayout_5.addWidget(self.btn_Spices_up)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_Tea_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Tea_down.setAutoRepeat(True)
        self.btn_Tea_down.setAutoRepeatDelay(400)
        self.btn_Tea_down.setAutoRepeatInterval(100)
        self.btn_Tea_down.setObjectName("btn_Tea_down")
        self.horizontalLayout_6.addWidget(self.btn_Tea_down)
        self.V_Tea = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Tea.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Tea.setObjectName("V_Tea")
        self.horizontalLayout_6.addWidget(self.V_Tea)
        self.btn_Tea_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Tea_up.setAutoRepeat(True)
        self.btn_Tea_up.setAutoRepeatDelay(400)
        self.btn_Tea_up.setAutoRepeatInterval(100)
        self.btn_Tea_up.setObjectName("btn_Tea_up")
        self.horizontalLayout_6.addWidget(self.btn_Tea_up)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_Textiles_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Textiles_down.setAutoRepeat(True)
        self.btn_Textiles_down.setAutoRepeatDelay(400)
        self.btn_Textiles_down.setAutoRepeatInterval(100)
        self.btn_Textiles_down.setObjectName("btn_Textiles_down")
        self.horizontalLayout_11.addWidget(self.btn_Textiles_down)
        self.V_Textiles = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Textiles.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Textiles.setObjectName("V_Textiles")
        self.horizontalLayout_11.addWidget(self.V_Textiles)
        self.btn_Textiles_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Textiles_up.setAutoRepeat(True)
        self.btn_Textiles_up.setAutoRepeatDelay(400)
        self.btn_Textiles_up.setAutoRepeatInterval(100)
        self.btn_Textiles_up.setObjectName("btn_Textiles_up")
        self.horizontalLayout_11.addWidget(self.btn_Textiles_up)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_Cannons_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Cannons_down.setAutoRepeat(True)
        self.btn_Cannons_down.setAutoRepeatDelay(400)
        self.btn_Cannons_down.setAutoRepeatInterval(100)
        self.btn_Cannons_down.setObjectName("btn_Cannons_down")
        self.horizontalLayout_4.addWidget(self.btn_Cannons_down)
        self.V_Cannons = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Cannons.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Cannons.setObjectName("V_Cannons")
        self.horizontalLayout_4.addWidget(self.V_Cannons)
        self.btn_Cannons_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Cannons_up.setAutoRepeat(True)
        self.btn_Cannons_up.setAutoRepeatDelay(400)
        self.btn_Cannons_up.setAutoRepeatInterval(100)
        self.btn_Cannons_up.setObjectName("btn_Cannons_up")
        self.horizontalLayout_4.addWidget(self.btn_Cannons_up)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_Contraband_down = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Contraband_down.setAutoRepeat(True)
        self.btn_Contraband_down.setAutoRepeatDelay(400)
        self.btn_Contraband_down.setAutoRepeatInterval(100)
        self.btn_Contraband_down.setObjectName("btn_Contraband_down")
        self.horizontalLayout_10.addWidget(self.btn_Contraband_down)
        self.V_Contraband = QtWidgets.QLabel(self.gridLayoutWidget)
        self.V_Contraband.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Contraband.setObjectName("V_Contraband")
        self.horizontalLayout_10.addWidget(self.V_Contraband)
        self.btn_Contraband_up = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.btn_Contraband_up.setAutoRepeat(True)
        self.btn_Contraband_up.setAutoRepeatDelay(400)
        self.btn_Contraband_up.setAutoRepeatInterval(100)
        self.btn_Contraband_up.setObjectName("btn_Contraband_up")
        self.horizontalLayout_10.addWidget(self.btn_Contraband_up)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icons/Tea.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4)
        self.H_Tea = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Tea.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Tea.setObjectName("H_Tea")
        self.horizontalLayout_15.addWidget(self.H_Tea)
        self.gridLayout.addLayout(self.horizontalLayout_15, 3, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(20, 20))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icons/Textiles.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        self.H_Textiles = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Textiles.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Textiles.setObjectName("H_Textiles")
        self.horizontalLayout_16.addWidget(self.H_Textiles)
        self.gridLayout.addLayout(self.horizontalLayout_16, 3, 1, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(20, 20))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/icons/Fruit.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_17.addWidget(self.label_6)
        self.H_Fruit = QtWidgets.QLabel(self.gridLayoutWidget)
        self.H_Fruit.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Fruit.setObjectName("H_Fruit")
        self.horizontalLayout_17.addWidget(self.H_Fruit)
        self.gridLayout.addLayout(self.horizontalLayout_17, 3, 2, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 240, 91, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.H_Total = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.H_Total.setObjectName("H_Total")
        self.horizontalLayout.addWidget(self.H_Total)
        self.V_Total = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.V_Total.setObjectName("V_Total")
        self.horizontalLayout.addWidget(self.V_Total)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.H_Spices.setText(_translate("Dialog", "Spices"))
        self.H_Cannons.setText(_translate("Dialog", "Cannons"))
        self.H_Contraband.setText(_translate("Dialog", "Contraband"))
        self.btn_Fruit_down.setText(_translate("Dialog", "\\/"))
        self.V_Fruit.setText(_translate("Dialog", "0"))
        self.btn_Fruit_up.setText(_translate("Dialog", "/\\"))
        self.btn_Spices_down.setText(_translate("Dialog", "\\/"))
        self.V_Spices.setText(_translate("Dialog", "0"))
        self.btn_Spices_up.setText(_translate("Dialog", "/\\"))
        self.btn_Tea_down.setText(_translate("Dialog", "\\/"))
        self.V_Tea.setText(_translate("Dialog", "0"))
        self.btn_Tea_up.setText(_translate("Dialog", "/\\"))
        self.btn_Textiles_down.setText(_translate("Dialog", "\\/"))
        self.V_Textiles.setText(_translate("Dialog", "0"))
        self.btn_Textiles_up.setText(_translate("Dialog", "/\\"))
        self.btn_Cannons_down.setText(_translate("Dialog", "\\/"))
        self.V_Cannons.setText(_translate("Dialog", "0"))
        self.btn_Cannons_up.setText(_translate("Dialog", "/\\"))
        self.btn_Contraband_down.setText(_translate("Dialog", "\\/"))
        self.V_Contraband.setText(_translate("Dialog", "0"))
        self.btn_Contraband_up.setText(_translate("Dialog", "/\\"))
        self.H_Tea.setText(_translate("Dialog", "Tea"))
        self.H_Textiles.setText(_translate("Dialog", "Textiles"))
        self.H_Fruit.setText(_translate("Dialog", "Fruit"))
        self.H_Total.setText(_translate("Dialog", "Total:"))
        self.V_Total.setText(_translate("Dialog", "0"))

import Icons.icons_rc

