# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWnd(QWidget):
    def __init__(self, parent=None):
        super(MainWnd, self).__init__(parent)
        # 对字典进行排序，字典默认按照key（升序）进行排序，sorted()函数返回一个列表
        icons = sorted(self.getEnumStrings(QStyle, QStyle.StandardPixmap).items())
        layout = QGridLayout(self)  # 创建栅格布局
        colNums = 4  # 每行显示的图标数目
        for i, iconInfo in enumerate(icons[1:]):
            btn = QPushButton(
                QApplication.style().standardIcon(i), " {} - {}".format(*iconInfo)
            )
            btn.setStyleSheet("QPushButton{text-align:left; height:30}")  # 设置样式表
            layout.addWidget(btn, int(i / colNums), i % colNums)  # 将按钮控件放到栅格布局上
            self.setWindowTitle("Qt内置图标显示")  # 设置窗口标题
            self.setWindowIcon(
                QApplication.style().standardIcon(QStyle.SP_DriveFDIcon)
            )  # 设置窗口图标

    def getEnumStrings(self, cls, enum):
        s = {}
        for key in dir(cls):
            value = getattr(cls, key)
            if isinstance(value, enum):
                s["{:02d}".format(value)] = key
        return s


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWnd()
    w.show()
    sys.exit(app.exec_())
