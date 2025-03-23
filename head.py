# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dock_mainpLbEoL.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMdiArea,
    QSizePolicy, QTabWidget, QWidget)

class Ui_head(object):
    def setupUi(self, head):
        if not head.objectName():
            head.setObjectName(u"head")
        head.resize(1920, 1080)
        head.setMaximumSize(QSize(1920, 1080))
        head.setWindowOpacity(1.000000000000000)
        head.setAutoFillBackground(False)
        self.mdiArea = QMdiArea(head)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(0, 0, 1920, 1080))
        self.mdiArea.setMaximumSize(QSize(1920, 1080))
        self.mdiArea.setFrameShadow(QFrame.Shadow.Plain)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setActivationOrder(QMdiArea.WindowOrder.CreationOrder)
        self.mdiArea.setDocumentMode(False)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setTabPosition(QTabWidget.TabPosition.West)
        self.label = QLabel(head)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setMaximumSize(QSize(1920, 1080))
        self.label.setPixmap(QPixmap(u"../Octopus v1.3/images/wall2.jpg"))
        self.label.setScaledContents(True)
        self.label.raise_()
        self.mdiArea.raise_()

        self.retranslateUi(head)

        QMetaObject.connectSlotsByName(head)
    # setupUi

    def retranslateUi(self, head):
        head.setWindowTitle(QCoreApplication.translate("head", u"OmniSearch workspace v1,1", None))
        self.label.setText("")
    # retranslateUi

