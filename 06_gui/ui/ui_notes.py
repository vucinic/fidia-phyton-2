# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_notes.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Notes(object):
    def setupUi(self, Notes):
        if not Notes.objectName():
            Notes.setObjectName(u"Notes")
        Notes.resize(808, 688)
        self.centralwidget = QWidget(Notes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(19, 560, 291, 81))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 741, 511))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.titoloLabel = QLabel(self.widget)
        self.titoloLabel.setObjectName(u"titoloLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titoloLabel)

        self.titoloLineEdit = QLineEdit(self.widget)
        self.titoloLineEdit.setObjectName(u"titoloLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titoloLineEdit)

        self.testoLabel = QLabel(self.widget)
        self.testoLabel.setObjectName(u"testoLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.testoLabel)

        self.testoLineEdit = QLineEdit(self.widget)
        self.testoLineEdit.setObjectName(u"testoLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.testoLineEdit)

        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.add_button)


        self.verticalLayout.addLayout(self.formLayout)

        self.table = QTableWidget(self.widget)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setSortingEnabled(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table)

        Notes.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Notes)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 808, 23))
        Notes.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Notes)
        self.statusbar.setObjectName(u"statusbar")
        Notes.setStatusBar(self.statusbar)

        self.retranslateUi(Notes)

        QMetaObject.connectSlotsByName(Notes)
    # setupUi

    def retranslateUi(self, Notes):
        Notes.setWindowTitle(QCoreApplication.translate("Notes", u"MainWindow", None))
        self.titoloLabel.setText(QCoreApplication.translate("Notes", u"Titolo", None))
        self.testoLabel.setText(QCoreApplication.translate("Notes", u"Testo", None))
        self.add_button.setText(QCoreApplication.translate("Notes", u"Aggiungi", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Notes", u"titolo", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Notes", u"testo", None));
    # retranslateUi

