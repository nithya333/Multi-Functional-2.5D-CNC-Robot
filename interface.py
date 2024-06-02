# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import os
class Ui_MainWindow(object):
    def update_angle_val(self, val):
        self.label_33.setText(f'{val}')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Minicapa TCC.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"background-color: rgb(240, 244, 245);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(6, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_10.setStyleSheet("\n"
"background-color: rgb(240, 244, 245);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_2.addWidget(self.frame_10, 0, 4, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_8.setStyleSheet("\n"
"background-color: rgb(240, 244, 245);\n"
"\n"
"\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_8)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem)
        self.frame_14 = QtWidgets.QFrame(self.frame)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_14.setStyleSheet("QFrame:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-radius:5px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_toggle = QtWidgets.QPushButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QtCore.QSize(0, 59))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btn_toggle.setFont(font)
        self.btn_toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_toggle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_toggle.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-image: url(:/16x16/icons/16x16/cil-menu.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 5px;\n"
"    border-left: 24px solid  rgb(240, 244, 245);\n"
"    background-color: rgb(240, 244, 245);\n"
"    text-align: left;\n"
"    padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-left: 24px solid rgb(231, 235, 237);\n"
"}\n"
"")
        self.btn_toggle.setObjectName("btn_toggle")
        self.horizontalLayout_8.addWidget(self.btn_toggle)
        self.verticalLayout_7.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_15.setStyleSheet("QFrame:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-radius:5px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_home = QtWidgets.QPushButton(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 59))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_home.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-image: url(:/16x16/icons/16x16/cil-home.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 5px;\n"
"    border-left: 24px solid  rgb(240, 244, 245);\n"
"    background-color: rgb(240, 244, 245);\n"
"    text-align: left;\n"
"    padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-left: 24px solid rgb(231, 235, 237);\n"
"}\n"
"")
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout_9.addWidget(self.btn_home)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_17.setStyleSheet("QFrame:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-radius:5px;\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btn_info = QtWidgets.QPushButton(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMinimumSize(QtCore.QSize(0, 59))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.btn_info.setFont(font)
        self.btn_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_info.setStyleSheet("QPushButton {    \n"
"    \n"
"    background-image: url(:/16x16/icons/16x16/icons8-ajuda-16.png);\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 5px;\n"
"    border-left: 24px solid  rgb(240, 244, 245);\n"
"    background-color: rgb(240, 244, 245);\n"
"    text-align: left;\n"
"    padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(231, 235, 237);\n"
"    border-left: 24px solid rgb(231, 235, 237);\n"
"}\n"
"")
        self.btn_info.setObjectName("btn_info")
        self.horizontalLayout_13.addWidget(self.btn_info)
        self.verticalLayout_7.addWidget(self.frame_17)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.verticalLayout_5.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.frame_8, 0, 0, 3, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_20 = QtWidgets.QFrame(self.page_3)
        self.frame_20.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_20.setStyleSheet("background-color: rgb(251, 252, 252);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_10.addWidget(self.frame_20)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_25 = QtWidgets.QLabel(self.frame_20)
        self.label_25.setMinimumSize(QtCore.QSize(16777215, 16777215))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        # self.label_25.setMaximumSize(QtCore.QSize(16777915, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("border:none;")
        self.label_25.setObjectName("label_25")
        # self.verticalLayout_14.addWidget(self.label_25)
        self.verticalLayout_14.addWidget(self.frame_20)

#         # Beginning of vel. displacement
#         self.frame_30 = QtWidgets.QFrame(self.frame_20)
#         self.frame_30.setMinimumSize(QtCore.QSize(230, 55))
#         self.frame_30.setMaximumSize(QtCore.QSize(230, 55))
#         self.frame_30.setStyleSheet("border:none;")
#         self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_30.setObjectName("frame_30")
#         self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_30)
#         self.horizontalLayout_17.setObjectName("horizontalLayout_17")
#         self.label_25 = QtWidgets.QLabel(self.frame_30)
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         font.setStrikeOut(False)
#         self.label_25.setFont(font)
#         self.label_25.setStyleSheet("border: none;")
#         self.label_25.setObjectName("label_25")
#         self.horizontalLayout_17.addWidget(self.label_25)
#         self.vel_displacement = QtWidgets.QSpinBox(self.frame_30)
#         self.vel_displacement.setMinimumSize(QtCore.QSize(65, 35))
#         self.vel_displacement.setMaximumSize(QtCore.QSize(65, 35))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         self.vel_displacement.setFont(font)
#         self.vel_displacement.setStyleSheet("QSpinBox{\n"
# "    padding-left: 5px;\n"
# "    background: #FFF;\n"
# "    color: rgb(0, 0, 0);\n"
# "    border: 1px solid rgb(225, 230, 232);\n"
# "    border-radius:5px;\n"
# "}\n"
# "\n"
# "QSpinBox:hover{\n"
# "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
# "}\n"
# "\n"
# "\n"
# "QSpinBox:focus{\n"
# "    border:2px solid rgb(85, 170, 255);\n"
# "}")
#         self.vel_displacement.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.vel_displacement.setMaximum(10000)
#         self.vel_displacement.setProperty("value", 2000)
#         self.vel_displacement.setObjectName("vel_displacement")
#         self.horizontalLayout_17.addWidget(self.vel_displacement)
#         # End of Vel displacement

        self.stackedWidget.addWidget(self.page_3)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_9 = QtWidgets.QFrame(self.page_1)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_18 = QtWidgets.QFrame(self.frame_9)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_18.setMaximumSize(QtCore.QSize(1000, 50))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.load_btn = QtWidgets.QPushButton(self.frame_18)
        self.load_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.load_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.load_btn.setFont(font)
        self.load_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(85, 170, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_btn.setIcon(icon1)
        self.load_btn.setObjectName("load_btn")
        self.horizontalLayout_2.addWidget(self.load_btn)
        self.save_btn = QtWidgets.QPushButton(self.frame_18)
        self.save_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.save_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.line = QtWidgets.QFrame(self.frame_18)
        self.line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line.setStyleSheet("color: rgb(212, 215, 216);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.gcode_btn = QtWidgets.QPushButton(self.frame_18)
        self.gcode_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.gcode_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.gcode_btn.setFont(font)
        self.gcode_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gcode_btn.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(85, 170, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gcode_btn.setIcon(icon3)
        self.gcode_btn.setObjectName("gcode_btn")
        self.horizontalLayout_2.addWidget(self.gcode_btn)

        
        self.line = QtWidgets.QFrame(self.frame_18)
        self.line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line.setStyleSheet("color: rgb(212, 215, 216);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.visualise_btn = QtWidgets.QPushButton(self.frame_18)
        self.visualise_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.visualise_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.visualise_btn.setFont(font)
        self.visualise_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualise_btn.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(85, 170, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.visualise_btn.setIcon(icon3)
        self.visualise_btn.setObjectName("visualise_btn")
        self.horizontalLayout_2.addWidget(self.visualise_btn)

        self.line = QtWidgets.QFrame(self.frame_18)
        self.line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line.setStyleSheet("color: rgb(212, 215, 216);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)

        self.print_btn = QtWidgets.QPushButton(self.frame_18)
        self.print_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.print_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.print_btn.setFont(font)
        self.print_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.print_btn.setStyleSheet("\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(85, 170, 255);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_btn.setIcon(icon3)
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout_2.addWidget(self.print_btn)

        self.gridLayout_7.addWidget(self.frame_18, 3, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame_9)
        self.frame_5.setMinimumSize(QtCore.QSize(250, 80))
        self.frame_5.setMaximumSize(QtCore.QSize(250, 80))
        self.frame_5.setStyleSheet("background-color: rgb(251, 252, 252);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_16 = QtWidgets.QFrame(self.frame_5)
        self.frame_16.setMinimumSize(QtCore.QSize(250, 80))
        self.frame_16.setMaximumSize(QtCore.QSize(250, 80))
        self.frame_16.setStyleSheet("border:none;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_3.setContentsMargins(-1, 9, 9, 9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: none;\n"
"")
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.invert_btn = QtWidgets.QPushButton(self.frame_16)
        self.invert_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.invert_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.invert_btn.setFont(font)
        self.invert_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:  rgb(85, 170, 255);\n"
"}")
        self.invert_btn.setObjectName("invert_btn")
        self.gridLayout_3.addWidget(self.invert_btn, 1, 2, 1, 1)
        self.sharpness_btn = QtWidgets.QPushButton(self.frame_16)
        self.sharpness_btn.setMinimumSize(QtCore.QSize(100, 35))
        self.sharpness_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.sharpness_btn.setFont(font)
        self.sharpness_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.sharpness_btn.setObjectName("sharpness_btn")
        self.gridLayout_3.addWidget(self.sharpness_btn, 1, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_16)
        self.gridLayout_7.addWidget(self.frame_5, 6, 3, 1, 1)
        # End of sharpness and invert buttons

#         # Beginning of operation preferences
#         self.frame_27 = QtWidgets.QFrame(self.frame_9)
#         self.frame_27.setMinimumSize(QtCore.QSize(250, 80))
#         self.frame_27.setMaximumSize(QtCore.QSize(250, 80))
#         self.frame_27.setStyleSheet("background-color: rgb(251, 252, 252);\n"
# "border: 1px solid rgb(225, 230, 232);\n"
# "border-radius:10px;\n"
# "")
#         self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_27.setObjectName("frame_27")
#         self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_27)
#         self.verticalLayout_13.setObjectName("verticalLayout_13")
#         self.label_17 = QtWidgets.QLabel(self.frame_27)
#         self.label_17.setMinimumSize(QtCore.QSize(0, 20))
#         self.label_17.setMaximumSize(QtCore.QSize(16777215, 20))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(11)
#         font.setBold(False)
#         font.setWeight(50)
#         self.label_17.setFont(font)
#         self.label_17.setStyleSheet("border:none;")
#         self.label_17.setObjectName("label_17")
#         self.verticalLayout_13.addWidget(self.label_17)
#         # End of operation preferences

#         # Beginning of vel. displacement
#         self.frame_21 = QtWidgets.QFrame(self.frame_27)
#         self.frame_21.setMinimumSize(QtCore.QSize(230, 55))
#         self.frame_21.setMaximumSize(QtCore.QSize(230, 55))
#         self.frame_21.setStyleSheet("border:none;")
#         self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_21.setObjectName("frame_21")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_21)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.label_23 = QtWidgets.QLabel(self.frame_21)
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         font.setStrikeOut(False)
#         self.label_23.setFont(font)
#         self.label_23.setStyleSheet("border: none;")
#         self.label_23.setObjectName("label_23")
#         self.horizontalLayout_3.addWidget(self.label_23)
#         self.vel_displacement = QtWidgets.QSpinBox(self.frame_21)
#         self.vel_displacement.setMinimumSize(QtCore.QSize(65, 35))
#         self.vel_displacement.setMaximumSize(QtCore.QSize(65, 35))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         self.vel_displacement.setFont(font)
#         self.vel_displacement.setStyleSheet("QSpinBox{\n"
# "    padding-left: 5px;\n"
# "    background: #FFF;\n"
# "    color: rgb(0, 0, 0);\n"
# "    border: 1px solid rgb(225, 230, 232);\n"
# "    border-radius:5px;\n"
# "}\n"
# "\n"
# "QSpinBox:hover{\n"
# "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
# "}\n"
# "\n"
# "\n"
# "QSpinBox:focus{\n"
# "    border:2px solid rgb(85, 170, 255);\n"
# "}")
#         self.vel_displacement.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.vel_displacement.setMaximum(10000)
#         self.vel_displacement.setProperty("value", 2000)
#         self.vel_displacement.setObjectName("vel_displacement")
#         self.horizontalLayout_3.addWidget(self.vel_displacement)
#         # End of Vel displacement
        
#         # Beginning of mm/s after vel deisplacement
#         self.label_13 = QtWidgets.QLabel(self.frame_21)
#         self.label_13.setMaximumSize(QtCore.QSize(30, 20))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(8)
#         self.label_13.setFont(font)
#         self.label_13.setStyleSheet("border:none;")
#         self.label_13.setObjectName("label_13")
#         self.horizontalLayout_3.addWidget(self.label_13)
#         self.verticalLayout_13.addWidget(self.frame_21)
#         # End of mm/s after vel deisplacement
        
#         #  Beginning of Set button
#         self.frame_23 = QtWidgets.QFrame(self.frame_27)
#         self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_23.setObjectName("frame_23")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_23)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.set_btn = QtWidgets.QPushButton(self.frame_23)
#         self.set_btn.setMinimumSize(QtCore.QSize(100, 30))
#         self.set_btn.setStyleSheet("\n"
# "QPushButton{\n"
# "    background-color: rgb(76, 95, 107);\n"
# "    border-bottom: 1px solid  rgb(46, 57, 64);\n"
# "    border-radius:5px;\n"
# "    color: rgb(250, 252, 252);\n"
# "}\n"
# "QPushButton:hover{\n"
# "    background-color: rgb(96, 121, 136);\n"
# "    border-bottom: 1px solid  rgb(46, 57, 64);\n"
# "    border-radius:5px;\n"
# "    color: rgb(250, 252, 252);\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(85, 170, 255);\n"
# "}")
#         self.set_btn.setObjectName("set_btn")
#         self.horizontalLayout.addWidget(self.set_btn)
#         self.verticalLayout_13.addWidget(self.frame_23)
        # self.gridLayout_7.addWidget(self.frame_27, 6, 3, 1, 1)

        # End of Set button



        self.frame_4 = QtWidgets.QFrame(self.frame_9)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setStyleSheet("background-color: rgb(251, 252, 252);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView.setAutoFillBackground(False)
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.BoundingRectViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 4, 0, 3, 3)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_9)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 250))
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    background-color: rgb(251, 252, 252);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: rgb(251, 252, 252);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-bottom:none;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(251, 252, 252);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setContentsMargins(2, 6, 2, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.tab)
        self.frame_7.setStyleSheet("\n"
"border:none;\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:none;")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_9.addWidget(self.label_18)
        
        # Voice input
        self.frame_38 = QtWidgets.QFrame(self.frame_7)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setMinimumSize(QtCore.QSize(230, 65))
        self.frame_38.setMaximumSize(QtCore.QSize(230, 65))
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")  
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")

        self.label_35 = QtWidgets.QLabel(self.frame_38)
        self.label_35.setMinimumSize(QtCore.QSize(140, 20))
        self.label_35.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("border:none;")
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_36.addWidget(self.label_35)

        self.speak_btn_img = QtWidgets.QPushButton(self.frame_38)
        self.speak_btn_img.setMinimumSize(QtCore.QSize(60, 25))
        self.speak_btn_img.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.speak_btn_img.setObjectName("speak_btn_img")
        self.horizontalLayout_36.addWidget(self.speak_btn_img)
        self.verticalLayout_9.addWidget(self.frame_38)

        # Beginning of height box
        self.frame_24 = QtWidgets.QFrame(self.frame_7)
        self.frame_24.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_24.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_24.setStyleSheet("border:none;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.frame_24)
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.height_box = QtWidgets.QDoubleSpinBox(self.frame_24)
        self.height_box.setMinimumSize(QtCore.QSize(130, 35))
        self.height_box.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.height_box.setFont(font)
        self.height_box.setStyleSheet("QDoubleSpinBox{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.height_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.height_box.setMaximum(10000.0)
        self.height_box.setObjectName("height_box")
        self.horizontalLayout_11.addWidget(self.height_box)
        # end of height box
        
        # beginning of mm after height box
        self.label_21 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border: none;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_11.addWidget(self.label_21, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame_24)
        # end of mm after height box
        
        # beginning of width box
        self.frame_25 = QtWidgets.QFrame(self.frame_7)
        self.frame_25.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_25.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_25.setStyleSheet("border:none;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.frame_25)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.width_box = QtWidgets.QDoubleSpinBox(self.frame_25)
        self.width_box.setMinimumSize(QtCore.QSize(130, 35))
        self.width_box.setMaximumSize(QtCore.QSize(130, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.width_box.setFont(font)
        self.width_box.setStyleSheet("QDoubleSpinBox{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.width_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.width_box.setDecimals(2)
        self.width_box.setMinimum(0.0)
        self.width_box.setMaximum(100000.0)
        self.width_box.setProperty("value", 0.0)
        self.width_box.setObjectName("width_box")
        self.horizontalLayout_12.addWidget(self.width_box)
        # end of width box
        
        # beginning of mm after width box
        self.label_22 = QtWidgets.QLabel(self.frame_25)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border:none;")
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_9.addWidget(self.frame_25, 0, QtCore.Qt.AlignHCenter)
        # end of mm after width box
        
        # Beginning of Change button
        self.frame_26 = QtWidgets.QFrame(self.frame_7)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.resize_btn = QtWidgets.QPushButton(self.frame_26)
        self.resize_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.resize_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.resize_btn.setObjectName("resize_btn")
        self.horizontalLayout_14.addWidget(self.resize_btn)
        self.verticalLayout_9.addWidget(self.frame_26)
        self.verticalLayout_8.addWidget(self.frame_7)
        # End of Change button

        # ~~~~~~~ Testingg ~~~~~~~~~~~~
        # Operation Preferences
        self.frame_36 = QtWidgets.QFrame(self.tab)
        self.frame_36.setStyleSheet("\n"
"border:none;\n"
"")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_21.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_17= QtWidgets.QLabel(self.frame_36)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("border:none;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_21.addWidget(self.label_17)
        
        # Beginning of speed box
        self.frame_32 = QtWidgets.QFrame(self.frame_36)
        self.frame_32.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_32.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_32.setStyleSheet("border:none;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_23 = QtWidgets.QLabel(self.frame_32)
        self.label_23.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("border: none;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_22.addWidget(self.label_23)
        self.vel_displacement = QtWidgets.QSpinBox(self.frame_32)
        self.vel_displacement.setMinimumSize(QtCore.QSize(65, 35))
        self.vel_displacement.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.height_box.setFont(font)
        self.height_box.setStyleSheet("QDoubleSpinBox{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"\n"
"QDoubleSpinBox:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.vel_displacement.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.vel_displacement.setMaximum(10000)
        self.vel_displacement.setProperty("value", 2000)
        self.vel_displacement.setObjectName("vel_displacement")
        self.horizontalLayout_22.addWidget(self.vel_displacement)
        # end of speed box
        
        # beginning of mm after height box
        self.label_13 = QtWidgets.QLabel(self.frame_32)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border: none;")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_22.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_21.addWidget(self.frame_32)
        # end of mm after height box
        
        # Beginning of Change button
        self.frame_35 = QtWidgets.QFrame(self.frame_36)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.set_btn = QtWidgets.QPushButton(self.frame_35)
        self.set_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.set_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.set_btn.setObjectName("set_btn")
        self.horizontalLayout_23.addWidget(self.set_btn)
        self.verticalLayout_21.addWidget(self.frame_35)
        self.verticalLayout_8.addWidget(self.frame_36)
        # End of Change button
        # ~~~~~~~ Testingg ~~~~~~~~~~~~


        self.frame_13 = QtWidgets.QFrame(self.tab)
        self.frame_13.setStyleSheet("\n"
"border:none;\n"
"")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_29 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("border:none;\n"
"")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_10.addWidget(self.label_29)
        self.frame_6 = QtWidgets.QFrame(self.frame_13)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_11 = QtWidgets.QFrame(self.frame_6)
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setStyleSheet("border:none;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.verticalSlider = QtWidgets.QSlider(self.frame_11)
        self.verticalSlider.setStyleSheet("QSlider{\n"
"border:none;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"border: 1px solid #bbb;\n"
"background: grey;\n"
"width: 6px;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"background-color:  rgb(85, 170, 255);\n"
"border: 1px solid #777;\n"
"width:: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"background: 474b59;\n"
"border: 1px solid #777;\n"
"width: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"background: #ced7d9;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"margin-right: -5px;\n"
"margin-left: -5px;\n"
"margin-top: -1px;\n"
"border-radius: -5px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_4.addWidget(self.verticalSlider)
        self.verticalLayout.addWidget(self.frame_11, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_10.addWidget(self.frame_6)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(251, 252, 252);\n"
"border: 1px solid rgb(225, 230, 232);\n"
"border-radius:10px;\n"
"")
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setContentsMargins(2, 6, 2, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")


        self.frame_19 = QtWidgets.QFrame(self.tab_2)
        self.frame_19.setStyleSheet("\n"
"border:none;\n"
"")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        # self.label_17 = QtWidgets.QLabel(self.frame_19)
        # self.label_17.setMinimumSize(QtCore.QSize(0, 20))
        # self.label_17.setMaximumSize(QtCore.QSize(16777215, 20))
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI")
        # font.setPointSize(11)
        # font.setBold(False)
        # font.setWeight(50)
        # self.label_17.setFont(font)
        # self.label_17.setStyleSheet("border:none;")
        # self.label_17.setObjectName("label_17")
        # self.verticalLayout_13.addWidget(self.label_17)
        
        '''
        self.frame_2 = QtWidgets.QFrame(self.frame_19)
        self.frame_2.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_2.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_2.setStyleSheet("border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_15.setStyleSheet("border:none;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: none;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(65, 35))
        self.lineEdit.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.verticalLayout_13.addWidget(self.frame_2)
        self.frame_22 = QtWidgets.QFrame(self.frame_19)
        self.frame_22.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_22.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_22.setStyleSheet("border:none;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_25 = QtWidgets.QLabel(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("border: none;")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_7.addWidget(self.label_25)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_22)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(65, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(65, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.label_14 = QtWidgets.QLabel(self.frame_22)
        self.label_14.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_14.setStyleSheet("border:none;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.verticalLayout_13.addWidget(self.frame_22)
        '''

#         # Beginning of vel. displacement
#         self.frame_21 = QtWidgets.QFrame(self.frame_19)
#         self.frame_21.setMinimumSize(QtCore.QSize(230, 55))
#         self.frame_21.setMaximumSize(QtCore.QSize(230, 55))
#         self.frame_21.setStyleSheet("border:none;")
#         self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_21.setObjectName("frame_21")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_21)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.label_23 = QtWidgets.QLabel(self.frame_21)
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         font.setStrikeOut(False)
#         self.label_23.setFont(font)
#         self.label_23.setStyleSheet("border: none;")
#         self.label_23.setObjectName("label_23")
#         self.horizontalLayout_3.addWidget(self.label_23)
#         self.vel_displacement = QtWidgets.QSpinBox(self.frame_21)
#         self.vel_displacement.setMinimumSize(QtCore.QSize(65, 35))
#         self.vel_displacement.setMaximumSize(QtCore.QSize(65, 35))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         self.vel_displacement.setFont(font)
#         self.vel_displacement.setStyleSheet("QSpinBox{\n"
# "    padding-left: 5px;\n"
# "    background: #FFF;\n"
# "    color: rgb(0, 0, 0);\n"
# "    border: 1px solid rgb(225, 230, 232);\n"
# "    border-radius:5px;\n"
# "}\n"
# "\n"
# "QSpinBox:hover{\n"
# "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
# "}\n"
# "\n"
# "\n"
# "QSpinBox:focus{\n"
# "    border:2px solid rgb(85, 170, 255);\n"
# "}")
#         self.vel_displacement.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.vel_displacement.setMaximum(10000)
#         self.vel_displacement.setProperty("value", 2000)
#         self.vel_displacement.setObjectName("vel_displacement")
#         self.horizontalLayout_3.addWidget(self.vel_displacement)
#         # End of Vel displacement
        
#         # Beginning of mm/s after vel deisplacement
#         self.label_13 = QtWidgets.QLabel(self.frame_21)
#         self.label_13.setMaximumSize(QtCore.QSize(30, 20))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(8)
#         self.label_13.setFont(font)
#         self.label_13.setStyleSheet("border:none;")
#         self.label_13.setObjectName("label_13")
#         self.horizontalLayout_3.addWidget(self.label_13)
#         self.verticalLayout_13.addWidget(self.frame_21)
#         # End of mm/s after vel deisplacement
        
#         #  Beginning of Set button
#         self.frame_23 = QtWidgets.QFrame(self.frame_19)
#         self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_23.setObjectName("frame_23")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_23)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.set_btn = QtWidgets.QPushButton(self.frame_23)
#         self.set_btn.setMinimumSize(QtCore.QSize(100, 30))
#         self.set_btn.setStyleSheet("\n"
# "QPushButton{\n"
# "    background-color: rgb(76, 95, 107);\n"
# "    border-bottom: 1px solid  rgb(46, 57, 64);\n"
# "    border-radius:5px;\n"
# "    color: rgb(250, 252, 252);\n"
# "}\n"
# "QPushButton:hover{\n"
# "    background-color: rgb(96, 121, 136);\n"
# "    border-bottom: 1px solid  rgb(46, 57, 64);\n"
# "    border-radius:5px;\n"
# "    color: rgb(250, 252, 252);\n"
# "}\n"
# "QPushButton:pressed{\n"
# "    background-color: rgb(85, 170, 255);\n"
# "}")
#         self.set_btn.setObjectName("set_btn")
#         self.horizontalLayout.addWidget(self.set_btn)
#         self.verticalLayout_13.addWidget(self.frame_23)
#         # End of Set button


#         self.frame_23 = QtWidgets.QFrame(self.frame_19)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
#         self.frame_23.setSizePolicy(sizePolicy)
#         self.frame_23.setMinimumSize(QtCore.QSize(230, 55))
#         self.frame_23.setMaximumSize(QtCore.QSize(230, 55))
#         self.frame_23.setStyleSheet("border:none;")
#         self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_23.setObjectName("frame_23")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_23)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.label_27 = QtWidgets.QLabel(self.frame_23)
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         font.setStrikeOut(False)
#         self.label_27.setFont(font)
#         self.label_27.setStyleSheet("border: none;")
#         self.label_27.setObjectName("label_27")
#         self.horizontalLayout.addWidget(self.label_27)
#         self.vel_laser = QtWidgets.QSpinBox(self.frame_23)
#         self.vel_laser.setMinimumSize(QtCore.QSize(65, 35))
#         self.vel_laser.setMaximumSize(QtCore.QSize(65, 35))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         self.vel_laser.setFont(font)
#         self.vel_laser.setStyleSheet("QSpinBox{\n"
# "    padding-left: 5px;\n"
# "    background: #FFF;\n"
# "    color: rgb(0, 0, 0);\n"
# "    border: 1px solid rgb(225, 230, 232);\n"
# "    border-radius:5px;\n"
# "}\n"
# "\n"
# "QSpinBox:hover{\n"
# "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
# "}\n"
# "\n"
# "\n"
# "QSpinBox:focus{\n"
# "    border:2px solid rgb(85, 170, 255);\n"
# "}")
#         self.vel_laser.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.vel_laser.setMaximum(10000)
#         self.vel_laser.setProperty("value", 50)
#         self.vel_laser.setObjectName("vel_laser")
#         self.horizontalLayout.addWidget(self.vel_laser)
#         self.label_16 = QtWidgets.QLabel(self.frame_23)
#         self.label_16.setMaximumSize(QtCore.QSize(30, 20))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(8)
#         self.label_16.setFont(font)
#         self.label_16.setStyleSheet("border:none;")
#         self.label_16.setObjectName("label_16")
#         self.horizontalLayout.addWidget(self.label_16)
#         self.verticalLayout_13.addWidget(self.frame_23)
        
    
        # Beginning of text input heading
        self.frame_28 = QtWidgets.QFrame(self.tab_2)
        self.frame_28.setStyleSheet("\n"
"border:none;\n"
"")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setMinimumSize(QtCore.QSize(230, 65))
        self.frame_28.setMaximumSize(QtCore.QSize(230, 65))
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")  
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")

        # Radio button for voice
        self.radioButton_voice = QtWidgets.QRadioButton(self.frame_28)
        self.radioButton_voice.setGeometry(QtCore.QRect(180, 120, 95, 20))
        # adding signal and slot 
        # self.radioButton_voice.toggled.connect()
        # self.verticalLayout_13.addWidget(self.radioButton_voice)
        self.verticalLayout_13.addWidget(self.radioButton_voice)
        

        self.label_28 = QtWidgets.QLabel(self.frame_28)
        self.label_28.setMinimumSize(QtCore.QSize(140, 20))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("border:none;")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_21.addWidget(self.label_28)

        self.speak_btn = QtWidgets.QPushButton(self.frame_28)
        self.speak_btn.setMinimumSize(QtCore.QSize(60, 25))
        self.speak_btn.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.speak_btn.setObjectName("speak_btn")
        self.horizontalLayout_21.addWidget(self.speak_btn)
        self.verticalLayout_13.addWidget(self.frame_28)
        # End of text input heading

        
        # Beginning of text
        self.frame_33 = QtWidgets.QFrame(self.frame_28)
        # self.frame_33.setMinimumSize(QtCore.QSize(230, 55))
        # self.frame_33.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_33.setMinimumSize(QtCore.QSize(230, 100))
        # self.frame_33.setMaximumSize(QtCore.QSize(230, 95))
        self.frame_33.setStyleSheet("border:none;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        # Radio button for text
        self.radioButton_text = QtWidgets.QRadioButton(self.frame_28)
        self.radioButton_text.setGeometry(QtCore.QRect(180, 150, 95, 20))
        self.radioButton_text.setChecked(True)
        # adding signal and slot
        # self.radioButton_text.toggled.connect()
        self.verticalLayout_13.addWidget(self.radioButton_text)

        self.label_31 = QtWidgets.QLabel(self.frame_33)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("border: none;")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_17.addWidget(self.label_31)
        self.lineEdit_2 = QtWidgets.QTextEdit(self.frame_33)
        # self.lineEdit_2.setMinimumSize(QtCore.QSize(190, 35))
        # self.lineEdit_2.setMaximumSize(QtCore.QSize(190, 75))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(190, 75))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(190, 95))
        # self.lineEdit_2.setMinimumSize(120, 70)
        self.lineEdit_2.setPlaceholderText("Text Input")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QTextEdit{\n"
"    padding-left: 5px;\n"
"    background: #FFF;\n"
"    height: 1500px;\n"
"    color: rgb(0, 0, 0);\n"
"    border: 1px solid rgb(225, 230, 232);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    border-bottom: 1px solid  rgb(218, 197, 199);\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border:2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_17.addWidget(self.lineEdit_2)
        self.verticalLayout_13.addWidget(self.frame_33)
        # End of text
        
        #  Beginning of font select button
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_34 = QtWidgets.QLabel(self.frame_33)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("border: none;")
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_18.addWidget(self.label_34)
        self.combo_box = QtWidgets.QComboBox(self.frame_29)
        self.combo_box.setGeometry(200, 150, 120, 60)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.combo_box.setFont(font)
        # c_w_d = os.path.join(os.getcwd(),"Fonts")
        c_w_d = os.path.join(os.getcwd(),"cxf_fonts")
        dir_list = os.listdir(c_w_d)
        # geek_list = ["Acquestscript", "Allegrettoscript", "Allegro", "AmerikaSans", "ArtBrush", "ChinacatThin", "ClarendonBT", "ComicScriptOutline", "DeRoosCaps", "Futurami", "GaramondSmallCaps", "MistralRegular", "Shalley_Alegro", "FrenchScript", "MyFont_Nithya", "MyFont_Kalyani", "MyFont_Manivannan"]
        geek_list = dir_list
        self.combo_box.addItems(geek_list)
        self.combo_box.setStyleSheet("QComboBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_18.addWidget(self.combo_box)
        self.verticalLayout_13.addWidget(self.frame_29)
        # End of font select button

        # Beginning of font size
        self.frame_31 = QtWidgets.QFrame(self.frame_28)
        self.frame_31.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_31.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_31.setStyleSheet("border:none;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_24 = QtWidgets.QLabel(self.frame_31)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("border: none;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_20.addWidget(self.label_24)
#         self.user_font_size = QtWidgets.QSpinBox(self.frame_31)
#         self.user_font_size.setMinimumSize(QtCore.QSize(65, 35))
#         self.user_font_size.setMaximumSize(QtCore.QSize(65, 35))
#         font = QtGui.QFont()
#         font.setFamily("Segoe UI")
#         font.setPointSize(10)
#         self.user_font_size.setFont(font)
#         self.user_font_size.setStyleSheet("QSpinBox{\n"
# "    padding-left: 5px;\n"
# "    background: #FFF;\n"
# "    color: rgb(0, 0, 0);\n"
# "    border: 1px solid rgb(225, 230, 232);\n"
# "    border-radius:5px;\n"
# "}\n"
# "\n"
# "QSpinBox:hover{\n"
# "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
# "}\n"
# "\n"
# "\n"
# "QSpinBox:focus{\n"
# "    border:2px solid rgb(85, 170, 255);\n"
# "}")
#         self.user_font_size.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
#         self.user_font_size.setMaximum(1000)
#         self.user_font_size.setProperty("value", 60)
#         self.user_font_size.setObjectName("user_font_size")
        self.font_size_spinbox = QtWidgets.QSpinBox(self.frame_31)
        self.font_size_spinbox.setGeometry(200, 150, 120, 30)
        self.font_size_spinbox.setMinimum(0)
        self.font_size_spinbox.setMaximum(50)
        self.font_size_spinbox.setValue(10)
        self.font_size_spinbox.setStyleSheet("QSpinBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_20.addWidget(self.font_size_spinbox)
        self.verticalLayout_13.addWidget(self.frame_31)
        # End of font size

        # #  Beginning of font size select button
        # self.frame_37 = QtWidgets.QFrame(self.frame_28)
        # self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_37.setObjectName("frame_37")
        # self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_37)
        # self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        # self.font_size_spinbox = QtWidgets.QSpinBox(self.frame_37)
        # self.font_size_spinbox.setGeometry(200, 150, 120, 30)
        # self.font_size_spinbox.setMinimum(0)
        # self.font_size_spinbox.setMaximum(50)
        # self.font_size_spinbox.setValue(10)
        # self.horizontalLayout_25.addWidget(self.font_size_spinbox)
        # self.verticalLayout_13.addWidget(self.frame_37)
        # # End of font size select button

        # Beginning of line spacing
        self.frame_37 = QtWidgets.QFrame(self.frame_28)
        self.frame_37.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_37.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_37.setStyleSheet("border:none;")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_26 = QtWidgets.QLabel(self.frame_37)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("border: none;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_33.addWidget(self.label_26)
        self.line_space_spinbox = QtWidgets.QSpinBox(self.frame_37)
        self.line_space_spinbox.setGeometry(200, 150, 120, 30)
        self.line_space_spinbox.setMinimum(95)
        self.line_space_spinbox.setMaximum(200)
        self.line_space_spinbox.setValue(100)
        self.line_space_spinbox.setStyleSheet("QSpinBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_33.addWidget(self.line_space_spinbox)
        self.verticalLayout_13.addWidget(self.frame_37)
        # End of line spacing

        # Beginning of angle
        self.frame_41 = QtWidgets.QFrame(self.frame_28)
        self.frame_41.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_41.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_41.setStyleSheet("border:none;")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_27 = QtWidgets.QLabel(self.frame_41)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("border: none;")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_32.addWidget(self.label_27)
        self.label_33 = QtWidgets.QLabel(self.frame_41)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("border: none;")
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_32.addWidget(self.label_33)
        self.angle_slider = QtWidgets.QSlider(1,self.frame_41)
        self.angle_slider.setGeometry(200, 150, 120, 30)
        self.angle_slider.setRange(0, 360)
        self.angle_slider.setTickInterval(1)
        self.angle_slider.valueChanged.connect(self.update_angle_val)
        # self.angle_slider.setMinimum(0)
        # self.angle_slider.setMaximum(50)
        self.angle_slider.setValue(0)
        self.angle_slider.setStyleSheet("QSpinBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_32.addWidget(self.angle_slider)
        self.verticalLayout_13.addWidget(self.frame_41)
        # End of angle

        # Beginning of char spacing
        self.frame_40 = QtWidgets.QFrame(self.frame_28)
        self.frame_40.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_40.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_40.setStyleSheet("border:none;")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_30 = QtWidgets.QLabel(self.frame_40)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border: none;")
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_34.addWidget(self.label_30)
        self.char_space_spinbox = QtWidgets.QSpinBox(self.frame_40)
        self.char_space_spinbox.setGeometry(200, 150, 50, 30)
        self.char_space_spinbox.setMinimum(1)
        self.char_space_spinbox.setMaximum(100)
        self.char_space_spinbox.setValue(25)
        self.char_space_spinbox.setStyleSheet("QSpinBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_34.addWidget(self.char_space_spinbox)
        self.verticalLayout_13.addWidget(self.frame_40)
        # End of char spacing

         # Beginning of word spacing
        self.frame_43 = QtWidgets.QFrame(self.frame_28)
        self.frame_43.setMinimumSize(QtCore.QSize(230, 55))
        self.frame_43.setMaximumSize(QtCore.QSize(230, 55))
        self.frame_43.setStyleSheet("border:none;")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_32 = QtWidgets.QLabel(self.frame_43)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border: none;")
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_35.addWidget(self.label_32)
        self.word_space_spinbox = QtWidgets.QSpinBox(self.frame_43)
        self.word_space_spinbox.setGeometry(200, 150, 50, 30)
        self.word_space_spinbox.setMinimum(0)
        self.word_space_spinbox.setMaximum(200)
        self.word_space_spinbox.setValue(100)
        self.word_space_spinbox.setStyleSheet("QSpinBox{\n"
        "    padding-left: 5px;\n"
        "    background: #FFF;\n"
        "    color: rgb(0, 0, 0);\n"
        "    border: 1px solid rgb(225, 230, 232);\n"
        "    border-radius:5px;\n"
        "}\n"
        "\n"
        "QSpinBox:hover{\n"
        "    border-bottom: 1px solid  rgb(218, 197, 199);\n"
        "}\n"
        "\n"
        "\n"
        "QSpinBox:focus{\n"
        "    border:2px solid rgb(85, 170, 255);\n"
        "}")
        self.horizontalLayout_35.addWidget(self.word_space_spinbox)
        self.verticalLayout_13.addWidget(self.frame_43)
        # End of word spacing

        #  Beginning of Preview button
        self.frame_34 = QtWidgets.QFrame(self.frame_28)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.preview_btn_text = QtWidgets.QPushButton(self.frame_34)
        self.preview_btn_text.setMinimumSize(QtCore.QSize(80, 30))
        self.preview_btn_text.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.preview_btn_text.setObjectName("preview_btn_text")
        self.horizontalLayout_19.addWidget(self.preview_btn_text)
        # self.verticalLayout_13.addWidget(self.frame_34)
        # End of Preview button

        
        #  Beginning of generate gcode text button
        # self.frame_32 = QtWidgets.QFrame(self.frame_28)
        # self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_32.setObjectName("frame_32")
        # self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_32)
        # self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        # self.set_btn_text = QtWidgets.QPushButton(self.frame_32)
        self.set_btn_text = QtWidgets.QPushButton(self.frame_34)
        self.set_btn_text.setMinimumSize(QtCore.QSize(90, 30))
        self.set_btn_text.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: rgb(76, 95, 107);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(96, 121, 136);\n"
"    border-bottom: 1px solid  rgb(46, 57, 64);\n"
"    border-radius:5px;\n"
"    color: rgb(250, 252, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.set_btn_text.setObjectName("set_btn_text")
        # self.horizontalLayout_16.addWidget(self.set_btn_text)
        self.horizontalLayout_19.addWidget(self.set_btn_text)
        self.verticalLayout_13.addWidget(self.frame_34)

        # End of generate gcode text button

        #  The end of Text
        spacerItem4 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem4)
        self.verticalLayout_11.addWidget(self.frame_19)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget, 4, 3, 2, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 3, 1, 1, 3)
        self.horizontalLayout_6.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_1)
        self.gridLayout_2.addWidget(self.stackedWidget, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CNC Plotter Robot"))
        self.label_2.setText(_translate("MainWindow", "CNC Plotter Robot"))
        self.btn_toggle.setText(_translate("MainWindow", "Menu"))
        self.btn_home.setText(_translate("MainWindow", "Home"))
        self.btn_info.setText(_translate("MainWindow", "Help"))
        self.load_btn.setText(_translate("MainWindow", "Open image"))
        self.save_btn.setText(_translate("MainWindow", "Save image"))
        self.label_25.setText(_translate("MainWindow", "KPN"))
        self.gcode_btn.setText(_translate("MainWindow", "Generate GCode"))
        self.visualise_btn.setText(_translate("MainWindow", "Visualise"))
        self.print_btn.setText(_translate("MainWindow", "Print"))
        self.label_11.setText(_translate("MainWindow", "Edit image"))
        self.invert_btn.setText(_translate("MainWindow", "Invert"))
        self.sharpness_btn.setText(_translate("MainWindow", "Sharpness"))
        self.label_18.setText(_translate("MainWindow", "Image Dimensions"))
        self.label_35.setText(_translate("MainWindow", "Voice Input"))
        self.speak_btn_img.setText(_translate("MainWindow", "Speak"))
        self.label_5.setText(_translate("MainWindow", "Height  "))
        self.label_21.setText(_translate("MainWindow", "mm"))
        self.label.setText(_translate("MainWindow", "Width"))
        self.label_22.setText(_translate("MainWindow", "mm"))
        self.resize_btn.setText(_translate("MainWindow", "Change"))
        self.label_29.setText(_translate("MainWindow", "Black and white adjustment"))
        self.label_3.setText(_translate("MainWindow", "100 "))
        self.label_6.setText(_translate("MainWindow", "50"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Operation Preferences"))
        self.label_23.setText(_translate("MainWindow", "Speed"))
        self.label_13.setText(_translate("MainWindow", "mm/s"))
        self.set_btn.setText(_translate("MainWindow", "Set"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Image"))
        # self.label_8.setText(_translate("MainWindow", "Laser On"))
        # self.lineEdit.setText(_translate("MainWindow", "M106"))
        # self.label_25.setText(_translate("MainWindow", "Laser Off "))
        # self.lineEdit_2.setText(_translate("MainWindow", "M107"))
        # self.label_27.setText(_translate("MainWindow", "Vel. of laser"))
        # self.label_16.setText(_translate("MainWindow", "mm/s"))
        self.label_28.setText(_translate("MainWindow", "Voice Input"))
        self.speak_btn.setText(_translate("MainWindow", "Speak"))
        # self.label_30.setText(_translate("MainWindow", "Text"))
        self.label_31.setText(_translate("MainWindow", ":"))
        self.label_34.setText(_translate("MainWindow", "Font "))
        # self.combo_box.setText(_translate("MainWindow", "Choose Font"))
        self.label_24.setText(_translate("MainWindow", "Font size"))
        self.label_26.setText(_translate("MainWindow", "Line spacing"))
        self.label_27.setText(_translate("MainWindow", "Angle: "))
        self.label_33.setText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "Char spacing"))
        self.label_32.setText(_translate("MainWindow", "Word spacing"))
        self.preview_btn_text.setText(_translate("MainWindow", "Preview"))
        self.set_btn_text.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Text"))

import file_rc
