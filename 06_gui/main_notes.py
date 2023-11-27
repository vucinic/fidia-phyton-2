import sys

from PySide6.QtWidgets import QApplication
from ui import MainNotes

app = QApplication(sys.argv)

window = MainNotes()
window.show()

app.exec()