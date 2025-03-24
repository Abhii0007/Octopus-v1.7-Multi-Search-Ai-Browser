# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'introQxmrIx.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QWidget)

class Ui_intro(object):
    def setupUi(self, intro):
        if not intro.objectName():
            intro.setObjectName(u"intro")
        intro.resize(1120, 600)
        intro.setMinimumSize(QSize(1120, 600))
        intro.setMaximumSize(QSize(1120, 600))
        icon = QIcon()
        icon.addFile(u"../../../Users/abhi/.designer/backup/Designer (2).ico", QSize(), QIcon.Normal, QIcon.Off)
        intro.setWindowIcon(icon)
        intro.setWindowOpacity(1.000000000000000)
        self.tabWidget = QTabWidget(intro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 60, 680, 521))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 680, 521))
        self.widget.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.textEdit_about_2 = QTextEdit(self.widget)
        self.textEdit_about_2.setObjectName(u"textEdit_about_2")
        self.textEdit_about_2.setGeometry(QRect(10, 10, 661, 481))
        self.textEdit_about_2.setStyleSheet(u"background-color: rgb(30, 30, 47);")
        self.textEdit_about_2.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_about_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_about_2.setReadOnly(True)
        self.textEdit_about_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 680, 503))
        self.label_8.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(5, 34, 531, 41))
        font = QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"color: rgb(107, 139, 255);\n"
"background-color: rgb(29, 29, 29);")
        self.pushButton_4 = QPushButton(self.tab_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(8, 71, 70, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(76, 255, 178);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Save_layouts = QPushButton(self.tab_3)
        self.pushButton_Save_layouts.setObjectName(u"pushButton_Save_layouts")
        self.pushButton_Save_layouts.setGeometry(QRect(83, 71, 144, 31))
        self.pushButton_Save_layouts.setFont(font1)
        self.pushButton_Save_layouts.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"\n"
"color: rgb(108, 255, 211);")
        self.pushButton_clear_all = QPushButton(self.tab_3)
        self.pushButton_clear_all.setObjectName(u"pushButton_clear_all")
        self.pushButton_clear_all.setGeometry(QRect(493, 71, 181, 31))
        self.pushButton_clear_all.setFont(font1)
        self.pushButton_clear_all.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"\n"
"color: rgb(108, 255, 211);")
        self.pushButton_new_workspace = QPushButton(self.tab_3)
        self.pushButton_new_workspace.setObjectName(u"pushButton_new_workspace")
        self.pushButton_new_workspace.setGeometry(QRect(8, 10, 145, 31))
        self.pushButton_new_workspace.setFont(font1)
        self.pushButton_new_workspace.setStyleSheet(u"background-color: rgb(76, 255, 178);\n"
"color: rgb(0, 0, 0);")
        self.label_14 = QLabel(self.tab_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(167, 1, 401, 41))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(83, 255, 206);\n"
"background-color: rgb(29, 29, 29);")
        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(232, 71, 255, 28))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setFrame(False)
        self.tabWidget_2 = QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 110, 661, 381))
        self.tabWidget_2.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget_2.setDocumentMode(True)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget = QTableWidget(self.tab_4)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font3 = QFont()
        font3.setPointSize(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 661, 363))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"background-color: rgb(28, 28, 28);\n"
"border-color: rgb(130, 255, 213);\n"
"alternate-background-color: rgb(137, 143, 255);\n"
"selection-background-color: rgb(75, 251, 175);\n"
"selection-color: rgb(0, 0, 0);\n"
"gridline-color: rgb(137, 143, 255);\n"
"color: rgb(75, 251, 175);")
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(213)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.textEdit = QTextEdit(self.tab_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 661, 371))
        self.textEdit.setStyleSheet(u"background-color: rgb(31, 31, 49);")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWidth(0)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 680, 521))
        self.widget_2.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.textEdit_about = QTextEdit(self.widget_2)
        self.textEdit_about.setObjectName(u"textEdit_about")
        self.textEdit_about.setGeometry(QRect(10, 10, 661, 481))
        self.textEdit_about.setStyleSheet(u"background-color: rgb(31, 31, 49);")
        self.textEdit_about.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setCursorWidth(1)
        self.textEdit_about.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.label_16 = QLabel(self.tab_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 680, 503))
        self.label_16.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.label_16.setScaledContents(True)
        self.tabWidget.addTab(self.tab_6, "")
        self.label_6 = QLabel(intro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 1120, 600))
        self.label_6.setStyleSheet(u"background-color: rgb(32, 32, 32);")
        self.label_13 = QLabel(intro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(390, 0, 381, 41))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.label_25 = QLabel(intro)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(418, 30, 401, 41))
        font5 = QFont()
        font5.setPointSize(16)
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"color: rgb(139, 164, 255);")
        self.widget_5 = QWidget(intro)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(710, 77, 399, 503))
        self.widget_5.setStyleSheet(u"background-color: rgb(24, 24, 24);")
        self.label_12 = QLabel(self.widget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(24, 14, 331, 41))
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.comboBox_2 = QComboBox(self.widget_5)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(80, 329, 255, 31))
        font6 = QFont()
        font6.setPointSize(10)
        self.comboBox_2.setFont(font6)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(123, 114, 213);")
        self.comboBox_2.setFrame(False)
        self.label_22 = QLabel(self.widget_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(25, 323, 41, 41))
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.comboBox_3 = QComboBox(self.widget_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(213, 287, 171, 31))
        self.comboBox_3.setFont(font6)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(123, 114, 213);")
        self.comboBox_3.setFrame(False)
        self.label_24 = QLabel(self.widget_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(24, 281, 171, 41))
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 66, 170, 170))
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.label_4.setPixmap(QPixmap(u"../Octopus v1.3/images/Designer 512.png"))
        self.label_4.setScaledContents(True)
        self.label_9 = QLabel(self.widget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(190, 66, 170, 170))
        self.label_9.setStyleSheet(u"\n"
"background-color: rgba(86, 88, 176,0.3);")
        self.label_9.setFrameShape(QFrame.Shape.Box)
        self.label_9.setFrameShadow(QFrame.Shadow.Plain)
        self.label_9.setLineWidth(2)
        self.comboBox = QComboBox(self.widget_5)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(188, 371, 197, 29))
        font7 = QFont()
        font7.setPointSize(11)
        self.comboBox.setFont(font7)
        self.comboBox.setStyleSheet(u"background-color: rgb(239, 239, 239);\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(123, 114, 213);")
        self.comboBox.setFrame(False)
        self.label_23 = QLabel(self.widget_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(15, 363, 171, 41))
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"color: rgb(107, 139, 255);")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(26, 93, 111, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(21, 402, 141, 41))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.checkBox_4 = QCheckBox(self.widget_5)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(167, 414, 21, 20))
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet(u"color: rgb(137, 143, 255);")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(26, 125, 131, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.checkBox_3 = QCheckBox(self.widget_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(159, 135, 21, 20))
        self.checkBox_3.setFont(font6)
        self.checkBox_2 = QCheckBox(self.widget_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(159, 103, 21, 20))
        self.checkBox_2.setFont(font6)
        self.checkBox = QCheckBox(self.widget_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(159, 72, 21, 20))
        self.checkBox.setFont(font6)
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(26, 60, 111, 41))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.checkBox_6 = QCheckBox(self.widget_5)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(159, 202, 21, 20))
        self.checkBox_6.setFont(font6)
        self.label_11 = QLabel(self.widget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(26, 190, 111, 41))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.checkBox_5 = QCheckBox(self.widget_5)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(159, 169, 21, 20))
        self.checkBox_5.setFont(font6)
        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(26, 157, 111, 41))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(120, 149, 255);")
        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(22, 236, 331, 41))
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"color: rgb(83, 255, 206);")
        self.pushButton_delete_workspace = QPushButton(self.widget_5)
        self.pushButton_delete_workspace.setObjectName(u"pushButton_delete_workspace")
        self.pushButton_delete_workspace.setGeometry(QRect(355, 372, 28, 27))
        font8 = QFont()
        font8.setPointSize(26)
        self.pushButton_delete_workspace.setFont(font8)
        self.pushButton_delete_workspace.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_delete_workspace.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(29, 29, 29);")
        self.label_confirm = QLabel(self.widget_5)
        self.label_confirm.setObjectName(u"label_confirm")
        self.label_confirm.setGeometry(QRect(195, 407, 81, 31))
        self.label_confirm.setFont(font5)
        self.label_confirm.setStyleSheet(u"color: rgb(137, 143, 255);")
        self.pushButton_yes = QPushButton(self.widget_5)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        self.pushButton_yes.setGeometry(QRect(277, 413, 51, 24))
        self.pushButton_yes.setFont(font)
        self.pushButton_yes.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(75, 251, 175);")
        self.pushButton_no = QPushButton(self.widget_5)
        self.pushButton_no.setObjectName(u"pushButton_no")
        self.pushButton_no.setGeometry(QRect(336, 413, 51, 24))
        self.pushButton_no.setFont(font)
        self.pushButton_no.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(43, 43, 43);")
        self.toolButton_dpi_set = QToolButton(self.widget_5)
        self.toolButton_dpi_set.setObjectName(u"toolButton_dpi_set")
        self.toolButton_dpi_set.setGeometry(QRect(344, 330, 41, 31))
        self.toolButton_dpi_set.setFont(font)
        self.toolButton_dpi_set.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"color: rgb(75, 251, 175);")
        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(275, 452, 111, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(76, 255, 178);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setCheckable(False)
        self.label_9.raise_()
        self.label_12.raise_()
        self.comboBox_2.raise_()
        self.label_22.raise_()
        self.comboBox_3.raise_()
        self.label_24.raise_()
        self.label_4.raise_()
        self.comboBox.raise_()
        self.label_23.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.checkBox_4.raise_()
        self.label_3.raise_()
        self.checkBox_3.raise_()
        self.checkBox_2.raise_()
        self.checkBox.raise_()
        self.label.raise_()
        self.checkBox_6.raise_()
        self.label_11.raise_()
        self.checkBox_5.raise_()
        self.label_10.raise_()
        self.label_15.raise_()
        self.pushButton_delete_workspace.raise_()
        self.label_confirm.raise_()
        self.pushButton_yes.raise_()
        self.pushButton_no.raise_()
        self.toolButton_dpi_set.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.tabWidget.raise_()
        self.label_13.raise_()
        self.label_25.raise_()
        self.widget_5.raise_()

        self.retranslateUi(intro)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(intro)
    # setupUi

    def retranslateUi(self, intro):
        intro.setWindowTitle(QCoreApplication.translate("intro", u"Octopus v1.1", None))
        self.textEdit_about_2.setHtml(QCoreApplication.translate("intro", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">       </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">   ___________________ /`````````````\\__</span><span style=\" font-size:16pt; text-decoration: underline; color:#53ffce;\">OCTOPUS </span><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">_/`````````````\\__________________________</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9389ff;\">  </span><span style=\" font-size:14pt; color:#9389ff;\">Organised,</span><span style=\" font-size:14pt; font-weight:700; color:#53ffce;\"> </span><span style=\" font-size:14pt; color:#aa95ff;\">Comprehensive, Tool, Offering, Parallel &amp;</span><span style=\" font-size:14pt; font-weight:700; color:#53ffce;\"> </span><span style=\" font-size:14pt; color:#aa95ff;\">Universal, Searches  </span></p>\n"
"<p align=\"justify\" style=\" margin-top"
                        ":12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">   ```````````````````````````````\\___________</span><span style=\" font-size:12pt; color:#53ffce;\">Version1.1</span><span style=\" font-size:12pt; font-weight:700; color:#53ffce;\">__________/````````````````````````````````````````</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:700; color:#53ffce;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#53ffce;\"># How to Use ?</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 1: Launch the Program with suitable Layout</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">Before opning the workspace its recommended to first set the WorkSpace Layout for better experience</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 2: Go to searchbar</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" color:#aa95ff;\">Upon opening, you'll see a searchbar located at the bottom center of screen , it acts like a commander for navigation of all the browser, in other wors when you search it given the order to other browser, and all browsers follow its instruction at the same time. .</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 3: Enter Your Search Query</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">Locate the centralized search bar at the bottom center of the screen.</span></li>\n"
"<li style=\" color:#aa95ff;\" align=\"justify\" style=\" margin-"
                        "top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type your search query into the search bar. and then enter</li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 4: multi-browser matrix Grid with chatgpt integrations</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">you will see the multiple browsers windows representing different search engines such as YouTube, Google, Bing, Wikipedia, Google Books,ChatGPT, etc</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 5: View Results Across Multiple Search Engines</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">Your search query will simultaneously trigger searches across all open search engine windows in the grid view.</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 6: Explore Results</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">Explore the results from various search engines displayed side by side in the grid view.</span></li>\n"
"<li style=\" color:#aa95ff;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compare information, media, and perspectives from different sources quickly and efficiently.</li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 7: Capture Snapshots for PDF </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">While"
                        " researching, if you come across valuable information or media, you can capture snapshots.</span></li>\n"
"<li style=\" color:#aa95ff;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Simply click on the snapshot button within each window to capture the content.</li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   Step 8: Create PDF for information sharing</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\">After capturing snapshots, navigate to the PDF maker feature.</span></li>\n"
"<li style=\" color:#aa95ff;"
                        "\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Compile the captured snapshots into a PDF document by selecting the desired snapshots and arranging them in the desired order.</li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">   # To create your custom browsing instances , check out the Custom WorkSpace Section</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700; color:#53ffce;\">Some Advantages behind the Idea:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Time Efficiency</span><span style=\" font-weight:700;\">:</span> <span style=\" color:#aa95ff;\">By searching across multiple engines simultaneously, you save time on research tasks, increasing productivity. and by comparing the realtime data and information , eventually you wil find that information is reliable when multiple instances or resources shows the similar meaning.</span></li>\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Comprehensive Results</span><span style=\" font-weight:700;\">:</span> <span style=\" color:#aa95ff;\">Accessing results from various search engines allows for a more comprehensive understanding of the topic by aggregating diverse perspectives and information sources.</span></li>\n"
"<li align=\"justify\" style=\" ma"
                        "rgin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Ease of Comparison</span><span style=\" font-weight:700;\">:</span> <span style=\" color:#aa95ff;\">Viewing search results side by side facilitates quick and easy comparison, aiding in decision-making and information evaluation.</span></li>\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Snapshot and PDF Creation</span><span style=\" font-weight:700;\">:</span><span style=\" color:#aa95ff;\"> The ability to capture snapshots and compile them into a PDF streamlines the process of saving and organizing research findings for future reference or sharing.</span></li>\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span"
                        " style=\" font-weight:700; color:#53ffce;\">Customized Workspace</span><span style=\" font-weight:700;\">:</span> <span style=\" color:#aa95ff;\">The grid view layout and centralized search bar provide a tailored and intuitive workspace, optimizing user experience and workflow efficiency.</span></li>\n"
"<li style=\" color:#aa95ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Enhanced Productivity</span><span style=\" font-weight:700;\">:</span> By integrating multiple search engines and PDF creation within a single platform, this custom browser enhances productivity by minimizing the need for switching between multiple applications or tabs.</li>\n"
"<li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#53ffce;\">Versatility</span><span style=\""
                        " font-weight:700;\">:</span> <span style=\" color:#aa95ff;\">Whether you're conducting academic research, gathering market insights, or simply exploring topics of interest, this custom browser adapts to various use cases, offering versatility and flexibility in information retrieval and organization.</span></li></ol>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#aa95ff;\"># Important Note:- Try to Avoid to login in the browsing instances, this project is only for research purposes works and efficient browsing.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("intro", u"How to Use", None))
        self.label_8.setText("")
        self.label_26.setText(QCoreApplication.translate("intro", u"#Tip: To customize the instances position and size, set geometry manually.", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("intro", u"<html><head/><body><p>Its used to initialize browsing instance</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("intro", u"Create", None))
        self.pushButton_Save_layouts.setText(QCoreApplication.translate("intro", u"Save Workspace", None))
#if QT_CONFIG(tooltip)
        self.pushButton_clear_all.setToolTip(QCoreApplication.translate("intro", u"<html><head/><body><p>Delete the last instance</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_clear_all.setText(QCoreApplication.translate("intro", u"Delete Last Instance", None))
        self.pushButton_new_workspace.setText(QCoreApplication.translate("intro", u"New Workspace", None))
        self.label_14.setText(QCoreApplication.translate("intro", u"</Custom Workspace Layout Designer>", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("intro", u"Workspace Name...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("intro", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("intro", u"URL with formatted search {query}", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("intro", u"Geometry", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("intro", u"Layout", None))
        self.textEdit.setHtml(QCoreApplication.translate("intro", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#53f8c3;\">	# Instructions To Create Custom Workspace</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:11pt; color:#898fff;\">1. First, Create New WorkSpace.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">2. Click on 'Create' to create the Intance.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">3. Move window at custom position by dragging or Resizing it.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">4. Enter name for instance.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">5. Enter searching website Url with Formatted search. </span><span style=\" font-size:11pt;"
                        " color:#4cffb2;\">( See Below )</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">6. Click on Add to add the Instance Layout in Workspace.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">7. Click on New to create another Instances.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">8. Click on Finish All to finalize the Workspace setup.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">9. Type Workspace Name.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">10. Save Workspace.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#898fff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#4bfbaf;\">#Important Note to create Formatted Url</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">To create formatted url, you can ask chatgpt to create formatted url of any searching platform or website.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#898fff;"
                        "\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">just ask chatgpt, like this  = </span><span style=\" font-size:11pt; color:#e7e7e7;\"> </span><span style=\" font-size:11pt; color:#4cffb2;\">make formatted Url with search = {query} in these links = wikipedia, youtube, google images, google , google books</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#4cffb2;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">it will give you this- </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:"
                        "#898fff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">Sure! Here\u2019s how you can format a search query for each of the specified links:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#898fff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">1. Wikipedia Url: </span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#ce9178;\">https://en.wikipedia.org/w/index.php fulltext=1&amp;search=</span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\">{query}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">2. Youtube Url: </span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#ce9178;\">https://www.youtube.com/results?search_query=</span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\">{query}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:11pt; color:#898fff;\">3. Google Images Url: </span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#ce9178;\">https://www.google.com/search?tbm=isch&amp;q=</span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\">{query}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">4. Google Search Url: </span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#ce9178;\">https://www.google.com/search?q=</span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\">{query}</span></p>"
                        "\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#898fff;\">5. Google Books Url: </span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#ce9178;\">https://www.google.com/search?tbm=bks&amp;q=</span><span style=\" font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\">{query}</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Consolas','Courier New','monospace'; font-size:15px; color:#569cd6;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#4cffb2;\">Use Urls in this format to perform search in selected Websites.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#4cffb2;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("intro", u"Instructions to Create", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("intro", u"Custom WorkSpace", None))
        self.textEdit_about.setHtml(QCoreApplication.translate("intro", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700; color:#45ffc1;\">About</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7895ff;\">Developer:</span><span style=\" color:#7895ff;\"> Abhishek Verma<br /></span><span style=\" font-weight:700; color:#7895ff;\">Project:</span"
                        "><span style=\" color:#7895ff;\"> BTech Project7</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7895ff;\">Branch</span><span style=\" color:#7895ff;\">: CS-Aiml, 4th Sem April 2024<br /></span><span style=\" font-weight:700; color:#7895ff;\">License:</span><span style=\" color:#7895ff;\"> Open Source GNU</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Description</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">The Multi-Browser Research Tool is a versatile software designed to enhance research productivity and efficiency. Developed by Abhishek Verma as a part of their BTech Minor Project, this tool offers "
                        "a unique approach to conducting research by providing a multi-browser interface.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Features</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">Multi-browser functionality: Browse multiple websites simultaneously within a grid interface.</span></li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">External search bar: Easily search across all browsers simultaneously using a centralized search bar.</li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:0px; m"
                        "argin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ChatGPT integration: Seamlessly access ChatGPT within the interface for quick information retrieval and assistance.</li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enhanced research capabilities: Streamline your research process and maximize productivity.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">License</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">This software is released under the Open Source GNU license, allowing users to Use it freely while ensuring that any derivative works remain open source.</span></p>\n"
"<h2 style=\" margin-top:16px; ma"
                        "rgin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Contact</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">For inquiries or support, please contact us at abhi639679@gmail.com</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("intro", u"About", None))
        self.label_16.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("intro", u"Concept", None))
        self.label_6.setText("")
        self.label_13.setText(QCoreApplication.translate("intro", u"Welcome to the Octopus v1.1", None))
        self.label_25.setText(QCoreApplication.translate("intro", u"A MultiBrowsing WorkSpace </>", None))
        self.label_12.setText(QCoreApplication.translate("intro", u"Default Configurations Settings", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("intro", u"UHD 3840x2160,   Recommended", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("intro", u"FHD 1920x1080,    Scaling:100%", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("intro", u"FHD 1920x1080,    Scaling:125%", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("intro", u"HD   1600x900,      Scaling: 100%", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("intro", u"HD   1366x768,      Scaling: 100%", None))

        self.label_22.setText(QCoreApplication.translate("intro", u"DPI", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("intro", u"Popup Windows", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("intro", u"Docked/Combined", None))

        self.label_24.setText(QCoreApplication.translate("intro", u"WorkSpace Layout", None))
        self.label_4.setText("")
        self.label_9.setText(QCoreApplication.translate("intro", u"TextLabel", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("intro", u"Default/AutoExplore", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("intro", u"Default", None))
        self.label_23.setText(QCoreApplication.translate("intro", u"Select WorkSpace", None))
        self.label_2.setText(QCoreApplication.translate("intro", u"Youtube", None))
        self.label_7.setText(QCoreApplication.translate("intro", u"ChatGPT (Optional)", None))
        self.checkBox_4.setText("")
        self.label_3.setText(QCoreApplication.translate("intro", u"Google Books", None))
        self.checkBox_3.setText("")
        self.checkBox_2.setText("")
        self.checkBox.setText("")
        self.label.setText(QCoreApplication.translate("intro", u"WikiPedia", None))
        self.checkBox_6.setText("")
        self.label_11.setText(QCoreApplication.translate("intro", u"Google Images", None))
        self.checkBox_5.setText("")
        self.label_10.setText(QCoreApplication.translate("intro", u"Google Search", None))
        self.label_15.setText(QCoreApplication.translate("intro", u"Custom Configurations Settings", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete_workspace.setToolTip(QCoreApplication.translate("intro", u"<html><head/><body><p><span style=\" color:#ffffff;\">Delete Selected WorkSpace</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_workspace.setText(QCoreApplication.translate("intro", u"-", None))
        self.label_confirm.setText(QCoreApplication.translate("intro", u"Confirm:", None))
        self.pushButton_yes.setText(QCoreApplication.translate("intro", u"Yes", None))
        self.pushButton_no.setText(QCoreApplication.translate("intro", u"No", None))
        self.toolButton_dpi_set.setText(QCoreApplication.translate("intro", u"Set", None))
        self.pushButton_2.setText(QCoreApplication.translate("intro", u"Connect", None))
    # retranslateUi

