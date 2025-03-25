for obj0,url0,nam,geo0 in zip(objector1,data1["url"],data1['name'],geometry1):
    #print(obj1,url1)
    
    pos_x,pos_y,size_x,size_y = [int(r1) for r1 in geo0.split(',')]

    obj0.setGeometry(pos_x,pos_y,size_x,size_y)
    obj0.setWindowTitle(nam)
    obj0.form_new.webEngineView_5.setUrl(url0)
    time.sleep(0.02)
    obj0.show()


'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
from PySide6.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide6.QtCore import QUrl
from PySide6.QtGui import QClipboard

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a browser view
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # Load the initial URL
        self.browser.setUrl(QUrl("https://chatgpt.com"))

        # Get the page and set a custom message handler
        page = self.browser.page()
        page.setWebChannel(QWebChannel())

        # Connect the JavaScript console message signal to the custom handler
        page.javaScriptConsoleMessage = self.on_java_script_console_message

    def on_java_script_console_message(self, level, message, lineNumber, sourceID):
        # Suppress JavaScript errors from being shown in the console
        pass

    def contextMenuEvent(self, event):
        # Create a context menu
        context_menu = QMenu(self)

        # Add a "Copy Text" action to the menu
        copy_action = context_menu.addAction("Copy Text")

        # Connect the action to the copy_text method
        copy_action.triggered.connect(self.copy_text)

        # Show the context menu at the mouse position
        context_menu.exec(event.globalPos())

    def copy_text(self):
        # Get the current clipboard content
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()

        # Check if the clipboard has text
        if mime_data.hasText():
            # Print the copied text
            print("Copied Text:", mime_data.text())
        else:
            print("No text copied.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())
'''

'''import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

def main():
    app = QApplication(sys.argv)

    # Create a QWebEngineView widget
    web_view = QWebEngineView()

    # Load the HTML file
    html_file_path = "C:\\python\\webdev\\index.html"  # Replace with your HTML file path
    web_view.load(QUrl.fromLocalFile(html_file_path))

    # Set window title
    web_view.setWindowTitle("HTML Viewer")

    # Show the web view
    web_view.show()

    # Execute the application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

'''
'''import spacy

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

def differentiate_input(input_text):
    # Process input text with SpaCy
    doc = nlp(input_text)

    # Initialize lists for subjects and objects
    subjects = []
    objects = []

    # Iterate over tokens in the input sentence
    for token in doc:
        # If token is a subject (nsubj or nsubjpass dependency label)
        if token.dep_ in ["nsubj", "nsubjpass"]:
            subjects.append(token.text)
        # If token is an object (dobj or pobj dependency label)
        elif token.dep_ in ["dobj", "pobj"]:
            objects.append(token.text)

    return subjects, objects

def main():
    while True:
        user_input = input("Enter a sentence: ")
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        subjects, objects = differentiate_input(user_input)
        print("Subjects:", subjects)
        print("Objects:", objects)

if __name__ == "__main__":
    main()
'''
'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QPixmap, QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snapshot Window")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        self.snapshot_label = QLabel("Snapshot will be displayed here.")
        layout.addWidget(self.snapshot_label)

        self.snapshot_button = QPushButton("Take Snapshot")
        self.snapshot_button.clicked.connect(self.take_snapshot)
        layout.addWidget(self.snapshot_button)

    def take_snapshot(self):
        # Get the geometry of the central widget
        rect = self.central_widget.rect()

        # Create a pixmap and paint the central widget onto it
        pixmap = QPixmap(rect.size())
        self.central_widget.render(pixmap)

        # Save the pixmap to a file
        pixmap.save("snapshot.png")

        # Display the snapshot
        self.snapshot_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
'''
'''import json

# Sample list of items
data_list = ['item1', 'item2', 'item3', 'item4']

# File path where you want to save the JSON data
file_path = 'abhishek.json'

# Open the file in write mode
with open(file_path, 'w') as json_file:
    # Write the list to the file in JSON format
    json.dump(data_list, json_file)



'''


'''import json

# Sample list of items
data_list = ['item1', 'item2', 'item3', 'item4']
import json

# File path where your JSON data is stored
file_path = 'abhishek.json'

# Open the file in read mode
with open(file_path, 'r') as json_file:
    # Load the JSON data from the file into a Python object
    data = json.load(json_file)

    # Iterate over the items and print them
    for item in data:
        print(item)
'''

'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ComboBox Example")
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        self.comboBox.activated[str].connect(self.on_combobox_item_clicked)
        
        self.setCentralWidget(self.comboBox)
        
    def on_combobox_item_clicked(self, text):
        print("Selected item:", text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
'''
'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ComboBox Example")
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        
        self.setCentralWidget(self.comboBox)
        
    def on_combobox_changed(self, index):
        if index == 1:  # Second item index is 1
            print("Yes")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
'''
'''import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Checkbox Example")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.checkbox1 = QCheckBox("Checkbox 1")
        self.checkbox2 = QCheckBox("Checkbox 2")

        # Connect the clicked signal of checkbox1 to the method that checks checkbox2
        self.checkbox1.clicked.connect(self.check_checkbox2)

        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)

        self.setLayout(layout)

    def check_checkbox2(self):
        # When checkbox1 is clicked, check checkbox2
        if self.checkbox1.isChecked():
            self.checkbox2.setChecked(True)
        else:
            self.checkbox2.setChecked(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())'''

'''import csv
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
import sys

class MyTableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PySide6 Table Widget to CSV Example')
        self.setGeometry(100, 100, 600, 400)

        # Create table widget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        # Fill table widget with dummy data
        for row in range(3):
            for col in range(3):
                item = QTableWidgetItem(f'Row {row}, Col {col}')
                self.tableWidget.setItem(row, col, item)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        
        # Save button
        save_button = QPushButton('Save to CSV')
        save_button.clicked.connect(self.save_to_csv)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_to_csv(self):
        # Get data from table widget
        data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text())
            data.append(row_data)

        # Write data to CSV file
        with open('table_data.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
        
        print("Data saved to 'table_data.csv'")

def main():
    app = QApplication(sys.argv)
    ex = MyTableWidget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
'''

'''import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Save Table Data to JSON")

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a table widget
        self.tableWidget = QTableWidget()
        layout.addWidget(self.tableWidget)

        # Add some items to the table widget for demonstration
        self.populate_table()

        # Create a button to save table data to JSON
        save_button = QPushButton("Save to JSON", self)
        save_button.clicked.connect(self.save_to_json)
        layout.addWidget(save_button)

    def populate_table(self):
        # Adding some sample items to the table widget
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(4)
        for row in range(4):
            for col in range(3):
                item = QTableWidgetItem(f"Data {row}-{col}")
                self.tableWidget.setItem(row, col, item)

    def save_to_json(self):
        data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = {}
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    row_data[f"column_{col}"] = item.text()
            data.append(row_data)

        with open("table_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Table data saved to 'table_data.json'.")
'''

'''if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())'''

'''import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget Example")

        self.table_widget = QTableWidget(0, 3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Class", "Roll"])

        self.button = QPushButton("Add Data")
        self.button.clicked.connect(self.add_data)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_data(self):
        row_count = self.table_widget.rowCount()
        self.table_widget.setRowCount(row_count + 1)

        name_item = QTableWidgetItem("John Doe")
        class_item = QTableWidgetItem("Python Programming")
        roll_item = QTableWidgetItem("12345")

        self.table_widget.setItem(row_count, 0, name_item)
        self.table_widget.setItem(row_count, 1, class_item)
        self.table_widget.setItem(row_count, 2, roll_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

'''

'''from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QScreen
import math

def get_resolution():
    app = QApplication([])
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()
    return screen_width, screen_height

width, height = get_resolution()
print("Screen resolution: {}x{}".format(width, height))



print(math.ceil((height*3.47)/100))
'''








'''
import pyautogui

def gpt_connector():
    text = input('type  = ')
    pyautogui.moveTo(266, 950)
    pyautogui.click()
    pyautogui.typewrite(text)

    pyautogui.moveTo(470, 950)
    pyautogui.click()

gpt_connector()'''
'''
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, QPoint

class MyWindow(QWidget):
    positionChanged = Signal(QPoint)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Move Window Position")
        self.setGeometry(100, 100, 300, 200)

    def moveEvent(self, event):
        self.positionChanged.emit(self.pos())

def print_window_position(position):
    print(f"Window Position - X: {position.x()}, Y: {position.y()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWindow()
    window.positionChanged.connect(print_window_position)
    window.show()

    sys.exit(app.exec())
'''


    

'''
import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class TableWidgetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Table Widget Window')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(2)

        # Set column widths
        tableWidget.setColumnWidth(0, 50)
        tableWidget.setColumnWidth(1, 400)

        # Populate table with some data
        for i in range(5):
            for j in range(2):
                item = QTableWidgetItem("Row {} Column {}".format(i, j))
                tableWidget.setItem(i, j, item)

        layout.addWidget(tableWidget)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWidgetWindow()
    window.show()
    sys.exit(app.execa())'''
