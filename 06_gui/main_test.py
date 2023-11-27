import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QToolBar

from components import CustomButton


def quit():
    ret = QMessageBox.warning(app.parent(),
                               'Chiudi',
                               'Sei sicuro?',
                               QMessageBox.StandardButton.Yes |
                               QMessageBox.StandardButton.No
                               )
    if ret == QMessageBox.StandardButton.Yes:
        app.quit()


def button_clicked(data):
    print(data)
    msg_box = QMessageBox()
    msg_box.setText("AAAAAAAH.")
    msg_box.exec()

    ret = QMessageBox.information(app.parent(),
                                  'information',
                                  'information text',
                                  QMessageBox.StandardButton.Ok |
                                  QMessageBox.StandardButton.Discard |
                                  QMessageBox.StandardButton.LastButton |
                                  QMessageBox.StandardButton.Apply |
                                  QMessageBox.StandardButton.Abort)
    print(ret)
    ret = QMessageBox.warning(app.parent(), 'warning', 'warning text', QMessageBox.StandardButton.Ok)
    ret = QMessageBox.critical(app.parent(), 'critical', 'critical text', QMessageBox.StandardButton.Ok)

    ret = QMessageBox.about(app.parent(), 'about', 'about text')
    ret = QMessageBox.question(app.parent(), 'question', 'question text', QMessageBox.StandardButton.Ok)


app = QApplication(sys.argv)
main_panel = QWidget()

layout = QVBoxLayout()
layout.setAlignment(Qt.AlignmentFlag.AlignBottom)

button = QPushButton()
button.setText('Click me!')
button.clicked.connect(button_clicked)
layout.addWidget(button)

button2 = QPushButton()
button2.setText('Exit')
button2.clicked.connect(quit)
layout.addWidget(button2)

button3 = CustomButton()
button3.setText('CUSTOM')
button3.clicked.connect(lambda: button_clicked)
layout.addWidget(button3)

main_panel.setLayout(layout)


main_window = QMainWindow()
main_window.setMinimumWidth(800)
main_window.setMinimumHeight(400)

menu = main_window.menuBar().addMenu('&Menu')
act = QAction('&New')
act.setShortcut('Ctrl+N')
act.triggered.connect(button_clicked)
menu.addAction(act)

toolbar = QToolBar('Toolbar')
toolbar.setAllowedAreas(Qt.ToolBarArea.TopToolBarArea)
main_window.addToolBar(Qt.ToolBarArea.TopToolBarArea, toolbar)

toolbar2 = QToolBar('Toolbar2')
toolbar2.setAllowedAreas(Qt.ToolBarArea.BottomToolBarArea)
main_window.addToolBar(Qt.ToolBarArea.BottomToolBarArea, toolbar2)

toolbar.addAction(act)
toolbar2.addAction(act)

main_window.setCentralWidget(main_panel)


#
main_window.show()

# main_panel.show()

# button2.show()


app.exec()
