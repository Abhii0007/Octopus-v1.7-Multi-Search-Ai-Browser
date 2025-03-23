# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'historyHisxQZ.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTabWidget, QWidget)

class Ui_history(object):
    def setupUi(self, history):
        if not history.objectName():
            history.setObjectName(u"history")
        history.resize(800, 560)
        self.label_6 = QLabel(history)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, -10, 430, 60))
        font = QFont()
        font.setPointSize(24)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(139, 164, 255);")
        self.pushButton = QPushButton(history)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(683, 7, 111, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(139, 164, 255);\n"
"color: rgb(255, 255, 255);")
        self.tabWidget = QTabWidget(history)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(5, 30, 790, 525))
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.listwidget_histories = QListWidget(self.tab2)
        font2 = QFont()
        font2.setPointSize(12)
        __qlistwidgetitem = QListWidgetItem(self.listwidget_histories)
        __qlistwidgetitem.setFont(font2);
        self.listwidget_histories.setObjectName(u"listwidget_histories")
        self.listwidget_histories.setGeometry(QRect(0, 0, 790, 507))
        self.listwidget_histories.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"color: rgb(83, 255, 206);")
        self.tabWidget.addTab(self.tab2, "")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.listwidget_bookmark = QListWidget(self.tab1)
        __qlistwidgetitem1 = QListWidgetItem(self.listwidget_bookmark)
        __qlistwidgetitem1.setFont(font2);
        self.listwidget_bookmark.setObjectName(u"listwidget_bookmark")
        self.listwidget_bookmark.setGeometry(QRect(0, 0, 790, 507))
        self.listwidget_bookmark.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"color: rgb(83, 255, 206);")
        self.tabWidget.addTab(self.tab1, "")
        self.widget = QWidget(history)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 560))
        self.widget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.widget.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(history)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(history)
    # setupUi

    def retranslateUi(self, history):
        history.setWindowTitle(QCoreApplication.translate("history", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("history", u"Octopus WorkSpace v1.59", None))
        self.pushButton.setText(QCoreApplication.translate("history", u"Clear History", None))

        __sortingEnabled = self.listwidget_histories.isSortingEnabled()
        self.listwidget_histories.setSortingEnabled(False)
        ___qlistwidgetitem = self.listwidget_histories.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("history", u"gogle.com", None));
        self.listwidget_histories.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("history", u"BookMarks", None))

        __sortingEnabled1 = self.listwidget_bookmark.isSortingEnabled()
        self.listwidget_bookmark.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listwidget_bookmark.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("history", u"Bookmarks", None));
        self.listwidget_bookmark.setSortingEnabled(__sortingEnabled1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("history", u"Histories", None))
    # retranslateUi

