from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QStyle, QStyleFactory, QLabel


class CustomButton(QPushButton):

    def __init__(self):
        super().__init__()

        font = QFont()
        font.setBold(True)
        font.setPixelSize(24)
        font.setFamilies('Comic Sans')
        self.setFont(font)

class CustomLabel(QLabel):

    def __init__(self):
        super().__init__()
        font = QFont()
        font.setBold(True)
        font.setPixelSize(24)
        font.setFamilies('Comic Sans')
        self.setFont(font)



global_label = CustomLabel()