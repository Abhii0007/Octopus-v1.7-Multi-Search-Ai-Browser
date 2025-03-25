# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form4FfBWpM.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QPushButton, QSizePolicy,
    QWidget)

class Ui_window4(object):
    def setupUi(self, window4):
        if not window4.objectName():
            window4.setObjectName(u"window4")
        window4.resize(409, 520)
        window4.setMinimumSize(QSize(409, 520))
        #window4.setMaximumSize(QSize(409, 520))
        self.webEngineView_4 = QWebEngineView(window4)
        self.webEngineView_4.setObjectName(u"webEngineView_4")
        self.webEngineView_4.setGeometry(QRect(0, 0, 409, 520))
        self.webEngineView_4.setMinimumSize(QSize(406, 517))
        self.webEngineView_4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.webEngineView_4.setUrl(QUrl(u"https://chatgpt.com/"))
        self.webEngineView_4.setZoomFactor(0.6)
        self.pushButton = QPushButton(window4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 6, 51, 31))
        font = QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(15, 155, 121);\n"
"background-color: rgb(235, 235, 235);")
        self.checkBox_freeze = QCheckBox(window4)
        self.checkBox_freeze.setObjectName(u"checkBox_freeze")
        self.checkBox_freeze.setGeometry(QRect(76, 9, 61, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.checkBox_freeze.setFont(font1)
        self.checkBox_freeze.setStyleSheet(u"background-color: rgba(0, 0, 0,0.5);\n"
"color: rgb(75, 251, 175);")

        self.retranslateUi(window4)

        QMetaObject.connectSlotsByName(window4)
    # setupUi

    def retranslateUi(self, window4):
        window4.setWindowTitle(QCoreApplication.translate("window4", u"Form", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("window4", u"<html><head/><body><p>Enable, Python Code tester,Code executes when copied</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("window4", u"Enable", None))
        self.checkBox_freeze.setText(QCoreApplication.translate("window4", u"Freeze", None))
    # retranslateUi

