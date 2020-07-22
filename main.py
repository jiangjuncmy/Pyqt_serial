import sys
import os
from serial_assistant_ui import *
from serial_receive_Thread import *
from SimpleSerial import *
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
from PyQt5.QtCore import QThread,pyqtSignal

import time


class Save_receive_thread(QThread):
    def __init__(self):
        super().__init__()
    def get_new_data(self,data):
        self.new_data = data
        self.start()
    def run(self):
        file_raw_name = "serial_receive_" + time.strftime("%Y%m%d_%H%M", time.localtime()) + ".raw"
        file_raw = open(file_raw_name,"ab")
        file_raw.write(self.new_data)

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.myserial = SimpleSerial()
        self.save_thread = Save_receive_thread()
        
        self.update_coms()
        self.data_comboBox.setCurrentText("8")
        self.receive_textBrowser.setStyleSheet("background-color: black;")
        self.receive_textBrowser.setTextColor(QColor(0,255,0))

        #connect signal and slot
        self.open_pushButton.clicked.connect(self.open_serial)
        self.send_pushButton.clicked.connect(self.serial_send_data)
        self.receive_clear_pushButton.clicked.connect(self.clear_receive_area)
        self.send_clear_pushButton.clicked.connect(self.clear_send_area)
        self.com_comboBox.clicked.connect(self.update_coms)
    def mousePressEvent(self,event):
        print("hhhhhhhhhh")

    def update_coms(self):
        self.coms = self.myserial.get_com_list()
        self.com_comboBox.clear()
        self.com_comboBox.addItems(self.coms)
        print(self.coms)
    def serial_send_data(self,data):
        if self.myserial.IS_OPEN == True:
            data_str = self.send_textEdit.toPlainText()
            if self.send_hex_checkBox.isChecked():
                data_str = data_str.replace(" ","")
                print(data_str)
                try:
                    data_bytes = bytes.fromhex(data_str)
                except:
                    QMessageBox.warning(self,"输入错误!","请正确输入16进制数据！\n数字范围：0~f\n数字个数：偶数个",QMessageBox.Yes)
                    print("hex error!")
                    return
            else:
                try:
                    data_bytes = bytes(data_str,encoding="ascii")
                except:
                    try:
                        data_bytes = bytes(data_str,encoding="gbk")
                    except:
                        print("send error!")
            if self.send_new_line_checkBox.isChecked():
                data_bytes += b"\r\n"
            self.myserial.send(data_bytes)
    def clear_receive_area(self):
        self.receive_textBrowser.setText("")
        self.receive_data_len = 0
        self.label_10.setText(str(self.receive_data_len))
    def clear_send_area(self):
        self.send_textEdit.setText("")
    def update_receive_area(self,data):
        if(self.save_checkBox.isChecked()):
            self.save_thread.get_new_data(data)
        self.receive_data_len += len(data)
        
        if self.receive_hex_radioButton.isChecked():
            str_data = ""
            for i in data:
                str_data += str("%02x"%i) + " "
            self.receive_textBrowser.append(str_data)
        else:
            try:
                self.receive_textBrowser.append(str(data,encoding="ascii"))
            except:
                try:
                    self.receive_textBrowser.append(str(data,encoding="gbk"))
                except:
                    str_data = ""
                    for i in data:
                        str_data += hex(i)[2:] + " "
                    self.receive_textBrowser.append(str_data)
        self.label_10.setText(str(self.receive_data_len))
    def update_com_paras(self):
        self.port = self.com_comboBox.currentText()
        self.baudrate = int(self.baudrate_comboBox.currentText())
        self.parity= self.parity_comboBox.currentText()
        if self.parity == "无校验":
            self.parity = "N"
        elif self.parity == "奇校验":
            self.parity = "E"
        elif self.parity == "偶校验":
            self.parity = "O"
        else:
            print("parity error!: ",self.parity)
        self.stopbits= float(self.stopbit_comboBox.currentText())
        self.bytesize = int(self.data_comboBox.currentText())
        self.com_paras_dic = {
            "port":self.port,
            "baudrate":self.baudrate,
            "parity":self.parity,
            "stopbits":self.stopbits,
            "bytesize":self.bytesize
        }
        print(self.com_paras_dic)

    def open_serial(self):
        # print(self.open_pushButton.text())
        print("open id: ",threading.current_thread().ident)
        if self.open_pushButton.text() == "打开串口":
            self.update_com_paras()
            self.myserial.open(**self.com_paras_dic)
            if self.myserial.IS_OPEN == True:
                self.com_comboBox.setEnabled(False)
                self.data_comboBox.setEnabled(False)
                self.stopbit_comboBox.setEnabled(False)
                self.parity_comboBox.setEnabled(False)
                self.baudrate_comboBox.setEnabled(False)
                self.receive_data_len = 0
                self.serial_thread = Serial_receive_thread()
                self.serial_thread.start_receive_data(self.myserial)
                self.serial_thread.signal_have_data.connect(self.update_receive_area)
                self.serial_thread.signal_receive_error.connect(self.close_serial)
                self.open_pushButton.setText("关闭串口")
                self.statusBar().showMessage("串口打开成功！",5000)
            else:
                self.statusBar().showMessage("串口打开失败！",5000)
        else:
            self.close_serial()
            
    def close_serial(self):
        self.myserial.close()
        self.com_comboBox.setEnabled(True)
        self.data_comboBox.setEnabled(True)
        self.stopbit_comboBox.setEnabled(True)
        self.parity_comboBox.setEnabled(True)
        self.baudrate_comboBox.setEnabled(True)
        self.statusBar().showMessage("串口关闭成功！",5000)
        self.open_pushButton.setText("打开串口")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = MyMainWindow()
    print("main id: ",threading.current_thread().ident)
    my_window.show()
    sys.exit(app.exec_())
        