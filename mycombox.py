from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
#创建一个新类，继承自QComboBox，为其增加clicked信号
class MyComBox(QComboBox):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        #一定要加上下面这句话，否则父类无法处理本来的点击事件
        super().mousePressEvent(event)
        self.clicked.emit()
        
        
