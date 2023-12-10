from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal, Qt


class RightClickButton(QPushButton):
    rightClicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        elif event.buttons() == Qt.MouseButton.RightButton:
            self.rightClicked.emit()


if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = RightClickButton("右键点击我")
    window.clicked.connect(lambda: print("响应左键点击"))
    window.rightClicked.connect(lambda: print("响应右键点击"))
    window.show()
    sys.exit(app.exec())
