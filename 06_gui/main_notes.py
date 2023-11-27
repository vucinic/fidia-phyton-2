import sys

from PySide6.QtWidgets import QApplication
from ui import MainNotes


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainNotes()
    window.show()

    app.exec()