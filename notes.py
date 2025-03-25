# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notesWtTZME.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_notes(object):
    def setupUi(self, notes):
        if not notes.objectName():
            notes.setObjectName(u"notes")
        notes.resize(640, 480)
        self.textEdit = QTextEdit(notes)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 34, 640, 455))
        font = QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.textEdit.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextEditable|Qt.TextInteractionFlag.TextEditorInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.pushButton_save_as_html = QPushButton(notes)
        self.pushButton_save_as_html.setObjectName(u"pushButton_save_as_html")
        self.pushButton_save_as_html.setGeometry(QRect(5, 5, 131, 25))
        self.pushButton_save_as_html.setFont(font)
        self.pushButton_save_as_html.setStyleSheet(u"background-color: rgb(76, 255, 178);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_save_as_pdf = QPushButton(notes)
        self.pushButton_save_as_pdf.setObjectName(u"pushButton_save_as_pdf")
        self.pushButton_save_as_pdf.setGeometry(QRect(145, 5, 131, 25))
        self.pushButton_save_as_pdf.setFont(font)
        self.pushButton_save_as_pdf.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"\n"
"color: rgb(108, 255, 211);")
        self.widget = QWidget(notes)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1920, 34))
        self.widget.setStyleSheet(u"background-color: rgb(43, 43, 43);")
        self.pushButton_change_teme = QPushButton(self.widget)
        self.pushButton_change_teme.setObjectName(u"pushButton_change_teme")
        self.pushButton_change_teme.setGeometry(QRect(506, 5, 131, 25))
        self.pushButton_change_teme.setFont(font)
        self.pushButton_change_teme.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"\n"
"color: rgb(108, 255, 211);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 6, 201, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(75, 251, 175);")
        self.widget.raise_()
        self.textEdit.raise_()
        self.pushButton_save_as_html.raise_()
        self.pushButton_save_as_pdf.raise_()

        self.retranslateUi(notes)

        QMetaObject.connectSlotsByName(notes)
    # setupUi

    def retranslateUi(self, notes):
        notes.setWindowTitle(QCoreApplication.translate("notes", u"Notes Maker", None))
        self.textEdit.setHtml(QCoreApplication.translate("notes", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("notes", u"Type or Just Drag and Drop the websites content here...", None))
        self.pushButton_save_as_html.setText(QCoreApplication.translate("notes", u"Save as HTML", None))
        self.pushButton_save_as_pdf.setText(QCoreApplication.translate("notes", u"Save as PDF", None))
        self.pushButton_change_teme.setText(QCoreApplication.translate("notes", u"Dark Theme", None))
        self.label.setText(QCoreApplication.translate("notes", u"Notes Maker", None))
    # retranslateUi

