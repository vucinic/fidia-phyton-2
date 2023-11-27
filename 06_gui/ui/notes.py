from PySide6.QtWidgets import QWidget, QMainWindow, QTableWidgetItem
from .ui_notes import Ui_Notes

class MainNotes(QMainWindow, Ui_Notes):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Note')
        self.add_button.clicked.connect(self.add_note)

    def add_note(self):
        title = self.titoloLineEdit.text()
        text = self.testoLineEdit.text()
        print(title, text)

        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(title))
        self.table.setItem(row, 1, QTableWidgetItem(text))
        self.titoloLineEdit.clear()
        self.testoLineEdit.clear()

