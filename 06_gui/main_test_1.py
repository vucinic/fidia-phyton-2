import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMainWindow
from components import CustomButton, CustomLabel

class FidiaMain(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = FidiaWidget()
        self.setCentralWidget(widget)

        file_menu = self.menuBar().addMenu('&File')

        act1 = QAction('&Apri', self)
        act1.triggered.connect(lambda x: print(x))
        file_menu.addAction(act1)

        act2 = file_menu.addAction('&Nuovo')
        act2.triggered.connect(lambda x: print(x))

        act3 = file_menu.addAction('&Salva')
        act4 = file_menu.addAction('&Salva senza nome')
        act5 = file_menu.addAction('&Chiudi')




class FidiaWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Titolo della finestra')

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.label = CustomLabel()
        self.label.setText('1')
        layout.addWidget(self.label)

        self.button = CustomButton()
        self.button.setText('Push me!')
        self.button.clicked.connect(self.button_clicked)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def button_clicked(self):
        self.label.setText(str(int(self.label.text()) + 1))

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main_window = FidiaMain()

    main_window.show()

    app.exec()
