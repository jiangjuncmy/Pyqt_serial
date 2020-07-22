# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\serial_assistant.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(50, 20))
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.com_comboBox = MyComBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_comboBox.sizePolicy().hasHeightForWidth())
        self.com_comboBox.setSizePolicy(sizePolicy)
        self.com_comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.com_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.com_comboBox.setObjectName("com_comboBox")
        self.gridLayout.addWidget(self.com_comboBox, 1, 0, 1, 2)
        self.baudrate_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baudrate_comboBox.sizePolicy().hasHeightForWidth())
        self.baudrate_comboBox.setSizePolicy(sizePolicy)
        self.baudrate_comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.baudrate_comboBox.setObjectName("baudrate_comboBox")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.gridLayout.addWidget(self.baudrate_comboBox, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.data_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_comboBox.sizePolicy().hasHeightForWidth())
        self.data_comboBox.setSizePolicy(sizePolicy)
        self.data_comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.data_comboBox.setObjectName("data_comboBox")
        self.data_comboBox.addItem("")
        self.data_comboBox.addItem("")
        self.data_comboBox.addItem("")
        self.data_comboBox.addItem("")
        self.gridLayout.addWidget(self.data_comboBox, 4, 1, 1, 1)
        self.open_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_pushButton.sizePolicy().hasHeightForWidth())
        self.open_pushButton.setSizePolicy(sizePolicy)
        self.open_pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.open_pushButton.setMaximumSize(QtCore.QSize(70, 20))
        self.open_pushButton.setObjectName("open_pushButton")
        self.gridLayout.addWidget(self.open_pushButton, 6, 1, 1, 1)
        self.stopbit_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopbit_comboBox.sizePolicy().hasHeightForWidth())
        self.stopbit_comboBox.setSizePolicy(sizePolicy)
        self.stopbit_comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.stopbit_comboBox.setObjectName("stopbit_comboBox")
        self.stopbit_comboBox.addItem("")
        self.stopbit_comboBox.addItem("")
        self.stopbit_comboBox.addItem("")
        self.gridLayout.addWidget(self.stopbit_comboBox, 3, 1, 1, 1)
        self.parity_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parity_comboBox.sizePolicy().hasHeightForWidth())
        self.parity_comboBox.setSizePolicy(sizePolicy)
        self.parity_comboBox.setMinimumSize(QtCore.QSize(80, 0))
        self.parity_comboBox.setObjectName("parity_comboBox")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.parity_comboBox.addItem("")
        self.gridLayout.addWidget(self.parity_comboBox, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(80, 20))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 1, 1, 1)
        self.receive_hex_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.receive_hex_radioButton.setAcceptDrops(False)
        self.receive_hex_radioButton.setChecked(False)
        self.receive_hex_radioButton.setObjectName("receive_hex_radioButton")
        self.gridLayout.addWidget(self.receive_hex_radioButton, 8, 0, 1, 1)
        self.receive_auto_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.receive_auto_radioButton.setChecked(True)
        self.receive_auto_radioButton.setObjectName("receive_auto_radioButton")
        self.gridLayout.addWidget(self.receive_auto_radioButton, 8, 1, 1, 1)
        self.save_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.save_checkBox.setObjectName("save_checkBox")
        self.gridLayout.addWidget(self.save_checkBox, 9, 0, 1, 1)
        self.receive_clear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.receive_clear_pushButton.setSizePolicy(sizePolicy)
        self.receive_clear_pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.receive_clear_pushButton.setObjectName("receive_clear_pushButton")
        self.gridLayout.addWidget(self.receive_clear_pushButton, 9, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.receive_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_textBrowser.sizePolicy().hasHeightForWidth())
        self.receive_textBrowser.setSizePolicy(sizePolicy)
        self.receive_textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.receive_textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.receive_textBrowser.setCursorWidth(1)
        self.receive_textBrowser.setObjectName("receive_textBrowser")
        self.gridLayout_2.addWidget(self.receive_textBrowser, 0, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.send_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_textEdit.sizePolicy().hasHeightForWidth())
        self.send_textEdit.setSizePolicy(sizePolicy)
        self.send_textEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.send_textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.send_textEdit.setObjectName("send_textEdit")
        self.horizontalLayout.addWidget(self.send_textEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.send_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_pushButton.sizePolicy().hasHeightForWidth())
        self.send_pushButton.setSizePolicy(sizePolicy)
        self.send_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.send_pushButton.setObjectName("send_pushButton")
        self.verticalLayout_2.addWidget(self.send_pushButton)
        self.send_new_line_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.send_new_line_checkBox.setObjectName("send_new_line_checkBox")
        self.verticalLayout_2.addWidget(self.send_new_line_checkBox)
        self.send_hex_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.send_hex_checkBox.setTabletTracking(False)
        self.send_hex_checkBox.setAcceptDrops(False)
        self.send_hex_checkBox.setAutoFillBackground(False)
        self.send_hex_checkBox.setChecked(False)
        self.send_hex_checkBox.setAutoRepeat(False)
        self.send_hex_checkBox.setTristate(False)
        self.send_hex_checkBox.setObjectName("send_hex_checkBox")
        self.verticalLayout_2.addWidget(self.send_hex_checkBox)
        self.send_clear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_clear_pushButton.sizePolicy().hasHeightForWidth())
        self.send_clear_pushButton.setSizePolicy(sizePolicy)
        self.send_clear_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.send_clear_pushButton.setObjectName("send_clear_pushButton")
        self.verticalLayout_2.addWidget(self.send_clear_pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionhello1 = QtWidgets.QAction(MainWindow)
        self.actionhello1.setObjectName("actionhello1")
        self.actionhello2 = QtWidgets.QAction(MainWindow)
        self.actionhello2.setObjectName("actionhello2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口调试助手"))
        self.label_8.setText(_translate("MainWindow", "串口操作"))
        self.label.setText(_translate("MainWindow", "串口选择"))
        self.baudrate_comboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrate_comboBox.setItemText(1, _translate("MainWindow", "14400"))
        self.baudrate_comboBox.setItemText(2, _translate("MainWindow", "19200"))
        self.baudrate_comboBox.setItemText(3, _translate("MainWindow", "38400"))
        self.baudrate_comboBox.setItemText(4, _translate("MainWindow", "57600"))
        self.baudrate_comboBox.setItemText(5, _translate("MainWindow", "78600"))
        self.baudrate_comboBox.setItemText(6, _translate("MainWindow", "115200"))
        self.label_6.setText(_translate("MainWindow", "奇偶校验"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.label_3.setText(_translate("MainWindow", "停止位"))
        self.data_comboBox.setCurrentText(_translate("MainWindow", "5"))
        self.data_comboBox.setItemText(0, _translate("MainWindow", "5"))
        self.data_comboBox.setItemText(1, _translate("MainWindow", "6"))
        self.data_comboBox.setItemText(2, _translate("MainWindow", "7"))
        self.data_comboBox.setItemText(3, _translate("MainWindow", "8"))
        self.open_pushButton.setText(_translate("MainWindow", "打开串口"))
        self.stopbit_comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.stopbit_comboBox.setItemText(1, _translate("MainWindow", "1.5"))
        self.stopbit_comboBox.setItemText(2, _translate("MainWindow", "2"))
        self.parity_comboBox.setItemText(0, _translate("MainWindow", "无校验"))
        self.parity_comboBox.setItemText(1, _translate("MainWindow", "奇校验"))
        self.parity_comboBox.setItemText(2, _translate("MainWindow", "偶校验"))
        self.label_5.setText(_translate("MainWindow", "数据位"))
        self.label_9.setText(_translate("MainWindow", "接收数目"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.receive_hex_radioButton.setText(_translate("MainWindow", "Hex"))
        self.receive_auto_radioButton.setText(_translate("MainWindow", "Auto"))
        self.save_checkBox.setText(_translate("MainWindow", "保存接收"))
        self.receive_clear_pushButton.setText(_translate("MainWindow", "清除接收"))
        self.receive_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.send_pushButton.setText(_translate("MainWindow", "发送"))
        self.send_new_line_checkBox.setText(_translate("MainWindow", "New line"))
        self.send_hex_checkBox.setText(_translate("MainWindow", "Hex"))
        self.send_clear_pushButton.setText(_translate("MainWindow", "清除发送"))
        self.actionhello1.setText(_translate("MainWindow", "hello1"))
        self.actionhello2.setText(_translate("MainWindow", "hello2"))
from mycombox import MyComBox
