# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created: Wed Mar 19 02:41:15 2014
#      by: PyQt5 UI code generator 5.1.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InfoBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoBar.sizePolicy().hasHeightForWidth())
        self.InfoBar.setSizePolicy(sizePolicy)
        self.InfoBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.InfoBar.setObjectName("InfoBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.InfoBar)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Player_Name = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Player_Name.sizePolicy().hasHeightForWidth())
        self.Player_Name.setSizePolicy(sizePolicy)
        self.Player_Name.setObjectName("Player_Name")
        self.horizontalLayout_3.addWidget(self.Player_Name)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Icon_Cannons_Equipped = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Cannons_Equipped.sizePolicy().hasHeightForWidth())
        self.Icon_Cannons_Equipped.setSizePolicy(sizePolicy)
        self.Icon_Cannons_Equipped.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Cannons_Equipped.setText("")
        self.Icon_Cannons_Equipped.setPixmap(QtGui.QPixmap(":/icons/Cannons.jpg"))
        self.Icon_Cannons_Equipped.setScaledContents(True)
        self.Icon_Cannons_Equipped.setObjectName("Icon_Cannons_Equipped")
        self.horizontalLayout_3.addWidget(self.Icon_Cannons_Equipped)
        self.Eq_Cannons = QtWidgets.QLabel(self.InfoBar)
        self.Eq_Cannons.setObjectName("Eq_Cannons")
        self.horizontalLayout_3.addWidget(self.Eq_Cannons)
        self.Icon_Crew = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Crew.sizePolicy().hasHeightForWidth())
        self.Icon_Crew.setSizePolicy(sizePolicy)
        self.Icon_Crew.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Crew.setText("")
        self.Icon_Crew.setPixmap(QtGui.QPixmap(":/icons/Crew.jpg"))
        self.Icon_Crew.setScaledContents(True)
        self.Icon_Crew.setObjectName("Icon_Crew")
        self.horizontalLayout_3.addWidget(self.Icon_Crew)
        self.Crew = QtWidgets.QLabel(self.InfoBar)
        self.Crew.setObjectName("Crew")
        self.horizontalLayout_3.addWidget(self.Crew)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Icon_Cannons = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Cannons.sizePolicy().hasHeightForWidth())
        self.Icon_Cannons.setSizePolicy(sizePolicy)
        self.Icon_Cannons.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Cannons.setText("")
        self.Icon_Cannons.setPixmap(QtGui.QPixmap(":/icons/Cannon_unequipped.png"))
        self.Icon_Cannons.setScaledContents(True)
        self.Icon_Cannons.setObjectName("Icon_Cannons")
        self.horizontalLayout_3.addWidget(self.Icon_Cannons)
        self.Cannons = QtWidgets.QLabel(self.InfoBar)
        self.Cannons.setObjectName("Cannons")
        self.horizontalLayout_3.addWidget(self.Cannons)
        self.Icon_Contraband = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Contraband.sizePolicy().hasHeightForWidth())
        self.Icon_Contraband.setSizePolicy(sizePolicy)
        self.Icon_Contraband.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Contraband.setText("")
        self.Icon_Contraband.setPixmap(QtGui.QPixmap(":/icons/Contraband.jpg"))
        self.Icon_Contraband.setScaledContents(True)
        self.Icon_Contraband.setObjectName("Icon_Contraband")
        self.horizontalLayout_3.addWidget(self.Icon_Contraband)
        self.Contraband = QtWidgets.QLabel(self.InfoBar)
        self.Contraband.setObjectName("Contraband")
        self.horizontalLayout_3.addWidget(self.Contraband)
        self.Icon_Fruit = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Fruit.sizePolicy().hasHeightForWidth())
        self.Icon_Fruit.setSizePolicy(sizePolicy)
        self.Icon_Fruit.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Fruit.setText("")
        self.Icon_Fruit.setPixmap(QtGui.QPixmap(":/icons/Fruit.jpg"))
        self.Icon_Fruit.setScaledContents(True)
        self.Icon_Fruit.setObjectName("Icon_Fruit")
        self.horizontalLayout_3.addWidget(self.Icon_Fruit)
        self.Fruit = QtWidgets.QLabel(self.InfoBar)
        self.Fruit.setObjectName("Fruit")
        self.horizontalLayout_3.addWidget(self.Fruit)
        self.Icon_Spices = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Spices.sizePolicy().hasHeightForWidth())
        self.Icon_Spices.setSizePolicy(sizePolicy)
        self.Icon_Spices.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Spices.setText("")
        self.Icon_Spices.setPixmap(QtGui.QPixmap(":/icons/Spices.jpg"))
        self.Icon_Spices.setScaledContents(True)
        self.Icon_Spices.setObjectName("Icon_Spices")
        self.horizontalLayout_3.addWidget(self.Icon_Spices)
        self.Spices = QtWidgets.QLabel(self.InfoBar)
        self.Spices.setObjectName("Spices")
        self.horizontalLayout_3.addWidget(self.Spices)
        self.Icon_Tea = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Tea.sizePolicy().hasHeightForWidth())
        self.Icon_Tea.setSizePolicy(sizePolicy)
        self.Icon_Tea.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Tea.setText("")
        self.Icon_Tea.setPixmap(QtGui.QPixmap(":/icons/Tea.jpg"))
        self.Icon_Tea.setScaledContents(True)
        self.Icon_Tea.setObjectName("Icon_Tea")
        self.horizontalLayout_3.addWidget(self.Icon_Tea)
        self.Tea = QtWidgets.QLabel(self.InfoBar)
        self.Tea.setObjectName("Tea")
        self.horizontalLayout_3.addWidget(self.Tea)
        self.Icon_Textiles = QtWidgets.QLabel(self.InfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon_Textiles.sizePolicy().hasHeightForWidth())
        self.Icon_Textiles.setSizePolicy(sizePolicy)
        self.Icon_Textiles.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Textiles.setText("")
        self.Icon_Textiles.setPixmap(QtGui.QPixmap(":/icons/Textiles.jpg"))
        self.Icon_Textiles.setScaledContents(True)
        self.Icon_Textiles.setObjectName("Icon_Textiles")
        self.horizontalLayout_3.addWidget(self.Icon_Textiles)
        self.Textiles = QtWidgets.QLabel(self.InfoBar)
        self.Textiles.setObjectName("Textiles")
        self.horizontalLayout_3.addWidget(self.Textiles)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.Icon_Health = QtWidgets.QLabel(self.InfoBar)
        self.Icon_Health.setMaximumSize(QtCore.QSize(20, 20))
        self.Icon_Health.setText("")
        self.Icon_Health.setPixmap(QtGui.QPixmap(":/icons/Raft.jpg"))
        self.Icon_Health.setScaledContents(True)
        self.Icon_Health.setObjectName("Icon_Health")
        self.horizontalLayout_3.addWidget(self.Icon_Health)
        self.Health = QtWidgets.QLabel(self.InfoBar)
        self.Health.setObjectName("Health")
        self.horizontalLayout_3.addWidget(self.Health)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.H_Money = QtWidgets.QLabel(self.InfoBar)
        self.H_Money.setObjectName("H_Money")
        self.horizontalLayout_3.addWidget(self.H_Money)
        self.V_Money = QtWidgets.QLabel(self.InfoBar)
        self.V_Money.setObjectName("V_Money")
        self.horizontalLayout_3.addWidget(self.V_Money)
        self.verticalLayout_2.addWidget(self.InfoBar)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.stackedWidget = QtWidgets.QStackedWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Start = QtWidgets.QWidget()
        self.Start.setObjectName("Start")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Start)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.Start)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.Start)
        self.Pier = QtWidgets.QWidget()
        self.Pier.setObjectName("Pier")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Pier)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Welcome = QtWidgets.QLabel(self.Pier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Welcome.sizePolicy().hasHeightForWidth())
        self.Welcome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Welcome.setFont(font)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.gridLayout_3.addWidget(self.Welcome, 0, 0, 1, 2)
        self.btn_to_shipyard = QtWidgets.QToolButton(self.Pier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_to_shipyard.sizePolicy().hasHeightForWidth())
        self.btn_to_shipyard.setSizePolicy(sizePolicy)
        self.btn_to_shipyard.setObjectName("btn_to_shipyard")
        self.gridLayout_3.addWidget(self.btn_to_shipyard, 1, 0, 1, 1)
        self.btn_to_pe = QtWidgets.QToolButton(self.Pier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_to_pe.sizePolicy().hasHeightForWidth())
        self.btn_to_pe.setSizePolicy(sizePolicy)
        self.btn_to_pe.setObjectName("btn_to_pe")
        self.gridLayout_3.addWidget(self.btn_to_pe, 1, 1, 1, 1)
        self.btn_sail = QtWidgets.QToolButton(self.Pier)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sail.sizePolicy().hasHeightForWidth())
        self.btn_sail.setSizePolicy(sizePolicy)
        self.btn_sail.setObjectName("btn_sail")
        self.gridLayout_3.addWidget(self.btn_sail, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.Pier)
        self.ShipYard = QtWidgets.QWidget()
        self.ShipYard.setObjectName("ShipYard")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ShipYard)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_buy_ship = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buy_ship.sizePolicy().hasHeightForWidth())
        self.btn_buy_ship.setSizePolicy(sizePolicy)
        self.btn_buy_ship.setObjectName("btn_buy_ship")
        self.gridLayout_4.addWidget(self.btn_buy_ship, 0, 0, 1, 1)
        self.btn_buy_repair = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buy_repair.sizePolicy().hasHeightForWidth())
        self.btn_buy_repair.setSizePolicy(sizePolicy)
        self.btn_buy_repair.setObjectName("btn_buy_repair")
        self.gridLayout_4.addWidget(self.btn_buy_repair, 1, 0, 1, 1)
        self.btn_equip_cannons = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equip_cannons.sizePolicy().hasHeightForWidth())
        self.btn_equip_cannons.setSizePolicy(sizePolicy)
        self.btn_equip_cannons.setObjectName("btn_equip_cannons")
        self.gridLayout_4.addWidget(self.btn_equip_cannons, 2, 0, 1, 1)
        self.btn_to_pier_2 = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_to_pier_2.sizePolicy().hasHeightForWidth())
        self.btn_to_pier_2.setSizePolicy(sizePolicy)
        self.btn_to_pier_2.setObjectName("btn_to_pier_2")
        self.gridLayout_4.addWidget(self.btn_to_pier_2, 3, 0, 1, 2)
        self.btn_unequip_cannons = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_unequip_cannons.sizePolicy().hasHeightForWidth())
        self.btn_unequip_cannons.setSizePolicy(sizePolicy)
        self.btn_unequip_cannons.setObjectName("btn_unequip_cannons")
        self.gridLayout_4.addWidget(self.btn_unequip_cannons, 2, 1, 1, 1)
        self.btn_diy_repair = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_diy_repair.sizePolicy().hasHeightForWidth())
        self.btn_diy_repair.setSizePolicy(sizePolicy)
        self.btn_diy_repair.setObjectName("btn_diy_repair")
        self.gridLayout_4.addWidget(self.btn_diy_repair, 1, 1, 1, 1)
        self.btn_upgrade_ship = QtWidgets.QToolButton(self.ShipYard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_upgrade_ship.sizePolicy().hasHeightForWidth())
        self.btn_upgrade_ship.setSizePolicy(sizePolicy)
        self.btn_upgrade_ship.setObjectName("btn_upgrade_ship")
        self.gridLayout_4.addWidget(self.btn_upgrade_ship, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.ShipYard)
        self.PE = QtWidgets.QWidget()
        self.PE.setObjectName("PE")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.PE)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btn_hire_crew = QtWidgets.QToolButton(self.PE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_hire_crew.sizePolicy().hasHeightForWidth())
        self.btn_hire_crew.setSizePolicy(sizePolicy)
        self.btn_hire_crew.setObjectName("btn_hire_crew")
        self.gridLayout_5.addWidget(self.btn_hire_crew, 0, 0, 1, 1)
        self.btn_buy_cargo = QtWidgets.QToolButton(self.PE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buy_cargo.sizePolicy().hasHeightForWidth())
        self.btn_buy_cargo.setSizePolicy(sizePolicy)
        self.btn_buy_cargo.setObjectName("btn_buy_cargo")
        self.gridLayout_5.addWidget(self.btn_buy_cargo, 2, 0, 1, 1)
        self.btn_to_pier = QtWidgets.QToolButton(self.PE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_to_pier.sizePolicy().hasHeightForWidth())
        self.btn_to_pier.setSizePolicy(sizePolicy)
        self.btn_to_pier.setObjectName("btn_to_pier")
        self.gridLayout_5.addWidget(self.btn_to_pier, 3, 0, 1, 2)
        self.btn_sell_cargo = QtWidgets.QToolButton(self.PE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sell_cargo.sizePolicy().hasHeightForWidth())
        self.btn_sell_cargo.setSizePolicy(sizePolicy)
        self.btn_sell_cargo.setObjectName("btn_sell_cargo")
        self.gridLayout_5.addWidget(self.btn_sell_cargo, 2, 1, 1, 1)
        self.btn_fire_crew = QtWidgets.QToolButton(self.PE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fire_crew.sizePolicy().hasHeightForWidth())
        self.btn_fire_crew.setSizePolicy(sizePolicy)
        self.btn_fire_crew.setObjectName("btn_fire_crew")
        self.gridLayout_5.addWidget(self.btn_fire_crew, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.PE)
        self.Buy_Shipyard = QtWidgets.QWidget()
        self.Buy_Shipyard.setStyleSheet("QLabel{\n"
"border: 1px solid rgb(0, 0, 0)\n"
"}")
        self.Buy_Shipyard.setObjectName("Buy_Shipyard")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Buy_Shipyard)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ship_pic = QtWidgets.QLabel(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ship_pic.sizePolicy().hasHeightForWidth())
        self.ship_pic.setSizePolicy(sizePolicy)
        self.ship_pic.setMinimumSize(QtCore.QSize(300, 250))
        self.ship_pic.setMaximumSize(QtCore.QSize(300, 250))
        self.ship_pic.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ship_pic.setText("")
        self.ship_pic.setPixmap(QtGui.QPixmap(":/icons/Exit.png"))
        self.ship_pic.setScaledContents(True)
        self.ship_pic.setObjectName("ship_pic")
        self.gridLayout_2.addWidget(self.ship_pic, 2, 2, 1, 1)
        self.btn_buy = QtWidgets.QToolButton(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_buy.sizePolicy().hasHeightForWidth())
        self.btn_buy.setSizePolicy(sizePolicy)
        self.btn_buy.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_buy.setMaximumSize(QtCore.QSize(75, 75))
        self.btn_buy.setObjectName("btn_buy")
        self.gridLayout_2.addWidget(self.btn_buy, 3, 4, 1, 1)
        self.btn_back_to_SY = QtWidgets.QToolButton(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_back_to_SY.sizePolicy().hasHeightForWidth())
        self.btn_back_to_SY.setSizePolicy(sizePolicy)
        self.btn_back_to_SY.setMinimumSize(QtCore.QSize(75, 75))
        self.btn_back_to_SY.setMaximumSize(QtCore.QSize(75, 75))
        self.btn_back_to_SY.setObjectName("btn_back_to_SY")
        self.gridLayout_2.addWidget(self.btn_back_to_SY, 3, 0, 1, 1)
        self.H_Ship_Name = QtWidgets.QLabel(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.H_Ship_Name.sizePolicy().hasHeightForWidth())
        self.H_Ship_Name.setSizePolicy(sizePolicy)
        self.H_Ship_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Ship_Name.setObjectName("H_Ship_Name")
        self.gridLayout_2.addWidget(self.H_Ship_Name, 1, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.V_Price = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Price.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Price.setObjectName("V_Price")
        self.gridLayout.addWidget(self.V_Price, 2, 0, 1, 1)
        self.H_Cannon = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Cannon.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Cannon.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Cannon.setObjectName("H_Cannon")
        self.gridLayout.addWidget(self.H_Cannon, 0, 1, 1, 1)
        self.H_Price = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Price.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Price.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Price.setObjectName("H_Price")
        self.gridLayout.addWidget(self.H_Price, 0, 0, 1, 1)
        self.V_Speed = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Speed.setObjectName("V_Speed")
        self.gridLayout.addWidget(self.V_Speed, 4, 1, 1, 1)
        self.H_Speed = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Speed.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Speed.setObjectName("H_Speed")
        self.gridLayout.addWidget(self.H_Speed, 3, 1, 1, 1)
        self.H_Crew = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Crew.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Crew.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Crew.setObjectName("H_Crew")
        self.gridLayout.addWidget(self.H_Crew, 3, 0, 1, 1)
        self.H_Cargo = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Cargo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Cargo.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Cargo.setObjectName("H_Cargo")
        self.gridLayout.addWidget(self.H_Cargo, 0, 2, 1, 1)
        self.H_Health = QtWidgets.QLabel(self.Buy_Shipyard)
        self.H_Health.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(155, 155, 155, 255), stop:1 rgba(255, 255, 255, 255));")
        self.H_Health.setAlignment(QtCore.Qt.AlignCenter)
        self.H_Health.setObjectName("H_Health")
        self.gridLayout.addWidget(self.H_Health, 3, 2, 1, 1)
        self.V_Cannon = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Cannon.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Cannon.setObjectName("V_Cannon")
        self.gridLayout.addWidget(self.V_Cannon, 2, 1, 1, 1)
        self.V_Cargo = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Cargo.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Cargo.setObjectName("V_Cargo")
        self.gridLayout.addWidget(self.V_Cargo, 2, 2, 1, 1)
        self.V_Health = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Health.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Health.setObjectName("V_Health")
        self.gridLayout.addWidget(self.V_Health, 4, 2, 1, 1)
        self.V_Crew = QtWidgets.QLabel(self.Buy_Shipyard)
        self.V_Crew.setAlignment(QtCore.Qt.AlignCenter)
        self.V_Crew.setObjectName("V_Crew")
        self.gridLayout.addWidget(self.V_Crew, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 2, 1, 1)
        self.btn_prev_ship = QtWidgets.QToolButton(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_prev_ship.sizePolicy().hasHeightForWidth())
        self.btn_prev_ship.setSizePolicy(sizePolicy)
        self.btn_prev_ship.setArrowType(QtCore.Qt.LeftArrow)
        self.btn_prev_ship.setObjectName("btn_prev_ship")
        self.gridLayout_2.addWidget(self.btn_prev_ship, 2, 0, 1, 1)
        self.btn_next_ship = QtWidgets.QToolButton(self.Buy_Shipyard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.btn_next_ship.sizePolicy().hasHeightForWidth())
        self.btn_next_ship.setSizePolicy(sizePolicy)
        self.btn_next_ship.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_next_ship.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_next_ship.setArrowType(QtCore.Qt.RightArrow)
        self.btn_next_ship.setObjectName("btn_next_ship")
        self.gridLayout_2.addWidget(self.btn_next_ship, 2, 4, 1, 1)
        self.stackedWidget.addWidget(self.Buy_Shipyard)
        self.Battle = QtWidgets.QWidget()
        self.Battle.setObjectName("Battle")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Battle)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btn_attack = QtWidgets.QToolButton(self.Battle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_attack.sizePolicy().hasHeightForWidth())
        self.btn_attack.setSizePolicy(sizePolicy)
        self.btn_attack.setObjectName("btn_attack")
        self.gridLayout_6.addWidget(self.btn_attack, 0, 0, 1, 1)
        self.btn_flee = QtWidgets.QToolButton(self.Battle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_flee.sizePolicy().hasHeightForWidth())
        self.btn_flee.setSizePolicy(sizePolicy)
        self.btn_flee.setObjectName("btn_flee")
        self.gridLayout_6.addWidget(self.btn_flee, 0, 1, 1, 1)
        self.btn_board = QtWidgets.QToolButton(self.Battle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_board.sizePolicy().hasHeightForWidth())
        self.btn_board.setSizePolicy(sizePolicy)
        self.btn_board.setObjectName("btn_board")
        self.gridLayout_6.addWidget(self.btn_board, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.Battle)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_debug = QtWidgets.QPushButton(self.widget_2)
        self.btn_debug.setObjectName("btn_debug")
        self.horizontalLayout_2.addWidget(self.btn_debug)
        self.lE_debug = QtWidgets.QLineEdit(self.widget_2)
        self.lE_debug.setObjectName("lE_debug")
        self.horizontalLayout_2.addWidget(self.lE_debug)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/New.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon2)
        self.actionLoad.setObjectName("actionLoad")
        self.menuGame.addAction(self.actionNew)
        self.menuGame.addAction(self.actionLoad)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Player_Name.setText(_translate("MainWindow", "Name"))
        self.Eq_Cannons.setText(_translate("MainWindow", "0"))
        self.Crew.setText(_translate("MainWindow", "0"))
        self.Cannons.setText(_translate("MainWindow", "0"))
        self.Contraband.setText(_translate("MainWindow", "0"))
        self.Fruit.setText(_translate("MainWindow", "0"))
        self.Spices.setText(_translate("MainWindow", "0"))
        self.Tea.setText(_translate("MainWindow", "0"))
        self.Textiles.setText(_translate("MainWindow", "0"))
        self.Health.setText(_translate("MainWindow", "0/0"))
        self.H_Money.setText(_translate("MainWindow", "\u06de"))
        self.V_Money.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Faller\'s the best at \n"
"making shitty games\n"
"Press Ctrl+N"))
        self.Welcome.setText(_translate("MainWindow", "Welcome to {}"))
        self.btn_to_shipyard.setText(_translate("MainWindow", "Head to Shipyard"))
        self.btn_to_pe.setText(_translate("MainWindow", "Head to Pirate Emporium"))
        self.btn_sail.setText(_translate("MainWindow", "Sail"))
        self.btn_buy_ship.setText(_translate("MainWindow", "Buy New Ship"))
        self.btn_buy_repair.setText(_translate("MainWindow", "Buy Repair"))
        self.btn_equip_cannons.setText(_translate("MainWindow", "Equip Cannons"))
        self.btn_to_pier_2.setText(_translate("MainWindow", "Head to Pier"))
        self.btn_unequip_cannons.setText(_translate("MainWindow", "Unequip Cannons"))
        self.btn_diy_repair.setText(_translate("MainWindow", "DIY Repair"))
        self.btn_upgrade_ship.setText(_translate("MainWindow", "Upgrade Ship"))
        self.btn_hire_crew.setText(_translate("MainWindow", "Hire Crew"))
        self.btn_buy_cargo.setText(_translate("MainWindow", "Buy Cargo"))
        self.btn_to_pier.setText(_translate("MainWindow", "Head to pier"))
        self.btn_sell_cargo.setText(_translate("MainWindow", "Sell Cargo"))
        self.btn_fire_crew.setText(_translate("MainWindow", "Fire Crew"))
        self.btn_buy.setText(_translate("MainWindow", "BUY!"))
        self.btn_back_to_SY.setText(_translate("MainWindow", "Back to \n"
" Shipyard"))
        self.H_Ship_Name.setText(_translate("MainWindow", "Ship Name"))
        self.V_Price.setText(_translate("MainWindow", "TextLabel"))
        self.H_Cannon.setText(_translate("MainWindow", "Cannon Capacity"))
        self.H_Price.setText(_translate("MainWindow", "Price"))
        self.V_Speed.setText(_translate("MainWindow", "TextLabel"))
        self.H_Speed.setText(_translate("MainWindow", "Speed"))
        self.H_Crew.setText(_translate("MainWindow", "Crew Capacity"))
        self.H_Cargo.setText(_translate("MainWindow", "Cargo Capacity"))
        self.H_Health.setText(_translate("MainWindow", "Hull Integrity"))
        self.V_Cannon.setText(_translate("MainWindow", "TextLabel"))
        self.V_Cargo.setText(_translate("MainWindow", "TextLabel"))
        self.V_Health.setText(_translate("MainWindow", "TextLabel"))
        self.V_Crew.setText(_translate("MainWindow", "TextLabel"))
        self.btn_prev_ship.setText(_translate("MainWindow", "<---"))
        self.btn_next_ship.setText(_translate("MainWindow", "--->"))
        self.btn_attack.setText(_translate("MainWindow", "Attack"))
        self.btn_flee.setText(_translate("MainWindow", "Flee"))
        self.btn_board.setText(_translate("MainWindow", "Attempt to Board"))
        self.btn_debug.setText(_translate("MainWindow", "Debug"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+O"))

import Icons.icons_rc
