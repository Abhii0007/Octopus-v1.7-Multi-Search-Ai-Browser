from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QMovie
from PySide6 import QtCore
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QPainter
from PySide6.QtCore import QSize



from notes import Ui_notes
class window_notes(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_notes = Ui_notes()
        self.form_notes.setupUi(self)
        self.resizeEvent = self.on_resize12
        self.form_notes.actionSave_As.triggered.connect(self.save_to_pdf)

    def save_to_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF files (*.pdf)")

        if file_path:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_path)
            printer.setResolution(90)  # Set resolution to 200 DPI
            k = self.geometry()
            # Set paper size to match QTextEdit size
            page_size = QSize(k.width(), k.height())
            printer.setPageSize(page_size)

            painter = QPainter()
            painter.begin(printer)
            self.form_notes.textEdit.document().drawContents(painter)
            painter.end()



    def on_resize12(self, event):
        # Resize the web view widget
        self.form_notes.textEdit.resize(event.size())
        self.form_notes.widget.resize(event.size())
        


# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = window_notes()
    widget.show()
    sys.exit(app.exec())