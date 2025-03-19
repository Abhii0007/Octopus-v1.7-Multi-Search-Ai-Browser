# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutIQDCbz.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextEdit,
    QWidget)

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(530, 399)
        self.textEdit_about = QTextEdit(about)
        self.textEdit_about.setObjectName(u"textEdit_about")
        self.textEdit_about.setGeometry(QRect(0, 0, 530, 401))
        self.textEdit_about.setStyleSheet(u"background-color: rgb(27, 27, 48);")
        self.textEdit_about.setReadOnly(True)
        self.textEdit_about.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About", None))
        self.textEdit_about.setHtml(QCoreApplication.translate("about", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700; color:#45ffc1;\">About</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7895ff;\">Developer:</span><span style=\" color:#7895ff;\"> Abhishek Verma<br /></span><span style=\" font-weight:700; color:#7895ff;\">Project:</span><span"
                        " style=\" color:#7895ff;\"> BTech Project7</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#7895ff;\">Branch</span><span style=\" color:#7895ff;\">: CS-Aiml, 4th Sem April 2024<br /></span><span style=\" font-weight:700; color:#7895ff;\">License:</span><span style=\" color:#7895ff;\"> Open Source GNU</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Description</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">The Multi-Browser Research Tool is a versatile software designed to enhance research productivity and efficiency. Developed by Abhishek Verma as a part of their BTech Minor Project, this tool offers a uniq"
                        "ue approach to conducting research by providing a multi-browser interface.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Features</span></h2>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">Multi-browser functionality: Browse multiple websites simultaneously within a grid interface.</span></li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">External search bar: Easily search across all browsers simultaneously using a centralized search bar.</li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ChatGPT integration: Seamlessly access ChatGPT within the interface for quick information retrieval and assistance.</li>\n"
"<li style=\" color:#7895ff;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enhanced research capabilities: Streamline your research process and maximize productivity.</li></ul>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">License</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">This software is released under the Open Source GNU license, allowing users to Use it freely while ensuring that any derivative works remain open source.</span></p>\n"
"<h2 style=\" margin-top:16px; margin-b"
                        "ottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700; color:#45ffc1;\">Contact</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#7895ff;\">For inquiries or support, please contact us at abhi639679@gmail.com</span></p></body></html>", None))
    # retranslateUi

