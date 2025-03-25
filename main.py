# This Python file uses the following encoding: utf-8
import sys,time,os
import subprocess
#from gc import collect
#os.system('cls')


import json,csv
from threading import Thread

try:
    import speech_recognition as sr
except:
    os.system('pip install SpeechRecognition')

try:
    from googlesearch import search
except:
    os.system('pip install googlesearch-python')
try:

    import pandas as pd
except:
    os.system('pip install pandas')
    
try:
    from PySide6.QtWidgets import QApplication, QMessageBox, QMainWindow, QFileDialog, QCompleter, QTableWidgetItem
    from PySide6.QtPrintSupport import QPrinter
    from PySide6.QtGui import QPainter,QIcon, QMovie,QPixmap
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtWebEngineWidgets import *
    from PySide6.QtWebEngineCore import (qWebEngineChromiumVersion, QWebEngineSettings, QWebEnginePage, QWebEngineProfile)
    
except Exception as e:
    print(e)
    os.system('pip install PySide6')

print("Loading...")

try:
    from reportlab.pdfgen import canvas
except:
    os.system('pip install reportlab')
try:
    import webbrowser
except:
    os.system('pip install webbrowser')
try:
    from PIL import Image
except:
    os.system('pip install pillow')
try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
try:

    from pyautogui import screenshot as script
except:
    os.system('pip install pyautogui')



import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='#'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()

def main23():
    total_iterations = 100

    for i in range(total_iterations + 1):
        time.sleep(0.003)
        print_progress_bar(i, total_iterations, prefix='Importing Modules:', suffix='done', length=50)

main23()
#cmd minimiser
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 2)



layouts_save = []
design1 = []
try:
    with open('layouts.json', 'r') as json_file:
        design1 = json.load(json_file)
except:
    try:
        with open('layouts.json', 'w') as json_file:
            json.dump(layouts_save, json_file)
    except:
        pass
size_x = 1
size_y = 1

def main():
    global screen_height,screen_width,widget_intro,app,size_x,size_y
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    '''[Platforms]
        WindowsArguments = dpiawareness=2'''#save this to qt.conf
    #set QT_SCALE_FACTOR=2 && python main.py      run this in terminal to set dpi
    os.system('set QT_SCALE_FACTOR=2')
    app = QApplication(sys.argv)
    
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()
    size_x = 1920/screen_width
    size_y = 1080/screen_height
    print('Dpi ',screen_width,":",screen_height)
    
    widget_intro = window_intro()
    widget_intro.show()
    
    sys.exit(app.exec())


#Global Controlls
objector1 = []
instancer1 = []
objector = []
editor = True
gpt_talk = False
docker_on = False

defaults1 = [
    "https://www.google.com/search?q=%7Bquery%7D",
    "https://www.google.com/search?q=%7Bquery%7D&udm=2",
    "https://en.wikipedia.org/w/index.php?fulltext=1&search=%7Bquery%7D&title=Special%3ASearch&ns0=1",
    "https://www.youtube.com/results?search_query=%7Bquery%7D",
    "https://www.google.com/search?tbm=bks&q=%7Bquery%7D"
]
if not os.path.exists('data_url.json'):
    try:
        with open('data_url.json', 'w') as json_file01:
            json.dump(defaults1, json_file01, indent=4)
        print("JSON file created successfully.")
    except Exception as e:
        print("Error occurred while saving JSON file:", e)


recognizer = sr.Recognizer()
def alice():
    global widget7,speech
    with sr.Microphone() as source:
        #print("Say something...")
        try:
            audio = recognizer.listen(source)
            speech = recognizer.recognize_google(audio)
            print("You said:", speech)

        except sr.WaitTimeoutError:
            speech =  "Timeout: No speech detected."
            #print(speech)
        except sr.UnknownValueError:
            speech =  "Sorry, I couldn't understand your speech."
            #print(speech)
        except sr.RequestError as e:
            speech =  f"Error requesting speech recognition: {e}"
            #print(speech)

    widget7.form7.lineEdit.setText(speech)

    

def create_pdf_from_images():
    folder_path = "screenshots\\"
    output_pdf = "screenshots\\omni_docs.pdf"
    aspect_ratio = 16 / 9
    page_width = 800  # Arbitrary width, adjust as needed
    page_height = page_width / aspect_ratio
    c = canvas.Canvas(output_pdf, pagesize=(page_width, page_height))
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
    image_files.sort()
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        img = Image.open(image_path)
        img_width, img_height = img.size
        img_aspect_ratio = img_width / img_height
        if img_aspect_ratio > aspect_ratio:
            img_width = page_width
            img_height = page_width / img_aspect_ratio
        else:
            img_height = page_height
            img_width = page_height * img_aspect_ratio
        x_offset = (page_width - img_width) / 2
        c.drawImage(image_path, x_offset, 0, img_width, img_height)
        c.showPage()
    c.save()
    print(f"PDF created successfully: {output_pdf}")
    



def researcher_starter():
    global widget7
    widget7 = window_name7()
    widget7.show()
    



class window_intro(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from intro import Ui_intro
        self.form_intro = Ui_intro()
        self.form_intro.setupUi(self)
        self.setWindowIcon(QIcon('images\\Designer 128.ico'))

                # Load an image and set it to the label
        self.form_intro.label_4.setPixmap(QPixmap("images\\Designer 512.png"))
        self.form_intro.label_16.setPixmap(QPixmap("images\\intro.jpg"))

        self.form_intro.pushButton_2.clicked.connect(self.starter)
        self.form_intro.pushButton_4.clicked.connect(self.instance_maker)
        self.form_intro.tableWidget.setColumnWidth(0,130)
        self.form_intro.tableWidget.setColumnWidth(1,370)
        self.form_intro.tableWidget.setColumnWidth(2,143)
        self.form_intro.pushButton_clear_all.clicked.connect(self.delete_last_row)
        self.form_intro.pushButton_Save_layouts.clicked.connect(self.save_to_csv)
        self.form_intro.pushButton_new_workspace.clicked.connect(self.resetter)
        self.form_intro.comboBox.currentIndexChanged.connect(self.load_csv)
        self.form_intro.pushButton_delete_workspace.clicked.connect(self.confirmation_show)
        self.form_intro.checkBox.clicked.connect(self.customizer)
        self.form_intro.checkBox_2.clicked.connect(self.customizer)
        self.form_intro.checkBox_3.clicked.connect(self.customizer)
        self.form_intro.pushButton_delete_workspace.setVisible(False)
        self.form_intro.checkBox_5.clicked.connect(self.customizer)
        self.form_intro.checkBox_6.clicked.connect(self.customizer)
        self.form_intro.pushButton_yes.clicked.connect(self.remove_current_item)
        self.form_intro.pushButton_no.clicked.connect(self.confirmation_hide)
        self.form_intro.toolButton_dpi_set.clicked.connect(self.setdpi)
        
        self.form_intro.pushButton_yes.setVisible(False)
        self.form_intro.pushButton_no.setVisible(False)
        self.form_intro.label_confirm.setVisible(False)
        self.workspace_hider()
        self.form_intro.comboBox.setCurrentIndex(1)
        self.defaulter2()
        self.customizer()
        self.anime1 = QMovie("images\\bubble0.gif")
        self.form_intro.label_9.setMovie(self.anime1)
        self.form_intro.label_9.setScaledContents(True)
        self.anime1.start()
        if screen_width==1920 and screen_height==1080:
            self.form_intro.comboBox_2.setItemText(1, "FHD 1920x1080,    Scaling:100% Default")
            self.form_intro.comboBox_2.setCurrentIndex(1)
        elif screen_width==1536 and screen_height==864:
            self.form_intro.comboBox_2.setItemText(2, "FHD 1920x1080,    Scaling:125% Default")
            self.form_intro.comboBox_2.setCurrentIndex(2)
        for works in design1:
            self.form_intro.comboBox.addItem(works)


        self.defaults = {
            'name':[],
            'url':[],
            'geometry':[]
            
        }
      
            

    def setdpi(self):
        
        def scaler(dp):
            os.environ['QT_SCALE_FACTOR'] = str(dp)
            # Command to be executed in another command prompt
            command = 'start cmd /c python main.py'
            # Open a new command prompt window and execute the command
            subprocess.Popen(command, shell=True)
            sys.exit()
        dp1 = self.form_intro.comboBox_2.currentIndex()
        match dp1:
            case 0:
                scaler(2.5)
            case 1:
                scaler(1.25)
            case 2:
                scaler(1)
            case 3:
                scaler(1.042)
            case 4:
                scaler(0.89)
            

    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)

        #QApplication.exit()
        
    def confirmation_show(self):
        self.form_intro.pushButton_yes.setVisible(True)
        self.form_intro.pushButton_no.setVisible(True)
        self.form_intro.label_confirm.setVisible(True)
    def confirmation_hide(self):
        self.form_intro.pushButton_yes.setVisible(False)
        self.form_intro.pushButton_no.setVisible(False)
        self.form_intro.label_confirm.setVisible(False)

    def defaulter2(self):
        global c1,c2,c3,c5,c6
        self.form_intro.checkBox.setChecked(True)
        self.form_intro.checkBox_2.setChecked(True)
        self.form_intro.checkBox_3.setChecked(True)
        self.form_intro.checkBox_4.setChecked(True)
        self.form_intro.checkBox_5.setChecked(True)
        self.form_intro.checkBox_6.setChecked(True)

    def customizer(self):
        global c1,c2,c3,c5,c6
        self.form_intro.comboBox.setCurrentIndex(-1)
        c1 = self.form_intro.checkBox.isChecked()
        c2 = self.form_intro.checkBox_2.isChecked()
        c3 = self.form_intro.checkBox_3.isChecked()
        c5 = self.form_intro.checkBox_5.isChecked()
        c6 = self.form_intro.checkBox_6.isChecked()
        if c1 and c2 and c3 and c5 and c6:
            self.form_intro.comboBox.setPlaceholderText('Default')
       
    def load_csv(self):
        global c1,c2,c3,c5,c6
        if self.form_intro.comboBox.currentIndex() <1:
            self.form_intro.tabWidget_2.setCurrentIndex(1)
            self.form_intro.pushButton_delete_workspace.setVisible(False)
            self.form_intro.comboBox.setGeometry(188,371,197,29)
            self.defaulter2()
        else:
            self.workspace_shower()
            self.form_intro.comboBox.setGeometry(188,371,164,29)
            self.form_intro.tabWidget_2.setCurrentIndex(0)
            self.form_intro.pushButton_delete_workspace.setVisible(True)
            self.form_intro.pushButton_Save_layouts.setVisible(True)
            self.form_intro.lineEdit.setVisible(True)
            self.form_intro.pushButton_clear_all.setVisible(True)
            c1 = self.form_intro.checkBox.setChecked(False)
            c2 = self.form_intro.checkBox_2.setChecked(False)
            c3 = self.form_intro.checkBox_3.setChecked(False)
            c5 = self.form_intro.checkBox_5.setChecked(False)
            c6 = self.form_intro.checkBox_6.setChecked(False)
            self.form_intro.checkBox_4.setChecked(False)
            self.form_intro.label_12.setText("Workspace Configurations Settings")
            self.form_intro.label_12.setStyleSheet('color: rgb(83, 255, 206);')
            
            text1 = "_".join((self.form_intro.comboBox.currentText()).split())+'.csv'
            try:
                df = pd.read_csv(text1)
            except FileNotFoundError:
                print(f"File not found: {text1}")
                return
            except pd.errors.EmptyDataError:
                print(f"Empty file: {text1}")
                return
          
            self.form_intro.tableWidget.setRowCount(df.shape[0])
            self.form_intro.tableWidget.setColumnCount(df.shape[1])
 
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    item = QTableWidgetItem(str(df.iat[i, j]))
                    self.form_intro.tableWidget.setItem(i, j, item)
            self.form_intro.tabWidget.setCurrentIndex(1)
        
    def save_to_csv(self):
        global design1
        if self.form_intro.lineEdit.text() in design1:
            self.form_intro.label_26.setText('Workspace already exists, try different name')
        else:
            workspace_name = "_".join((self.form_intro.lineEdit.text()+'.csv').split(' '))
            with open('layouts.json', 'w') as json_file:
                jk = self.form_intro.lineEdit.text()
                design1.append(jk)
                json.dump(design1, json_file)

            if workspace_name=='.csv':
                self.form_intro.label_26.setText('#Workspace name required!')
            else:

                self.form_intro.comboBox.addItem(f"{self.form_intro.lineEdit.text()}")
                self.form_intro.label_26.setText('#Tip: To customize the instances position and size, set geometry manually.')
                print(workspace_name)
                    
                with open(f"{workspace_name}", 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['name','url','geometry'])
                    data = []
                    for row in range(self.form_intro.tableWidget.rowCount()):
                        row_data = []
                        for col in range(self.form_intro.tableWidget.columnCount()):
                            item = self.form_intro.tableWidget.item(row, col)
                            row_data.append(item.text())
                        data.append(row_data)
                    writer.writerows(data)
                print(f"Data saved to {workspace_name}")
                self.form_intro.pushButton_Save_layouts.setText('#Saved')
            
    def delete_last_row(self):
        num_rows = self.form_intro.tableWidget.rowCount()
        if num_rows > 1:
            self.form_intro.tableWidget.removeRow(num_rows - 1)
        else:
            self.form_intro.tabWidget_2.setCurrentIndex(1)
            self.form_intro.tableWidget.removeRow(num_rows - 1)
            self.form_intro.pushButton_Save_layouts.setVisible(False)
            self.form_intro.lineEdit.setVisible(False)
            self.form_intro.pushButton_clear_all.setVisible(False)
        self.form_intro.pushButton_Save_layouts.setText('Save Layouts')

    def remove_current_item(self):
        self.load_csv()
        current_index = self.form_intro.comboBox.currentIndex()
        if current_index >0:  
            kp = "_".join(self.form_intro.comboBox.currentText().split(' ')) + '.csv'
            print(kp)
            if os.path.exists(kp):
                os.remove(kp)
            with open('layouts.json', 'w') as json_file1:
                design1.remove(self.form_intro.comboBox.currentText())
                json.dump(design1, json_file1)
            self.form_intro.comboBox.removeItem(current_index)
            self.form_intro.label_12.setText('WorkSpace Deleted!')
            self.form_intro.label_12.setStyleSheet('color: rgb(255, 66, 69);')
            self.resetter()
        else:
            self.form_intro.label_12.setText('Select another workspace to delete')
            self.form_intro.label_12.setStyleSheet('color: rgb(255, 66, 69);')
        self.confirmation_hide()

    def resetter(self):
        self.workspace_shower()
        self.form_intro.label_12.setText("Workspace Configurations Settings")
        self.form_intro.label_12.setStyleSheet('color: rgb(83, 255, 206);')
        self.form_intro.lineEdit.clear()
        num_rows1 = self.form_intro.tableWidget.rowCount()
        while num_rows1 > 0:
            self.form_intro.tableWidget.removeRow(num_rows1 - 1)
            num_rows1 = num_rows1-1
        self.form_intro.pushButton_Save_layouts.setText('Save Layouts')

    def workspace_shower(self):
        self.form_intro.pushButton_4.setVisible(True)
        self.form_intro.pushButton_Save_layouts.setVisible(False)
        self.form_intro.lineEdit.setVisible(False)
        self.form_intro.pushButton_clear_all.setVisible(False)

    def workspace_hider(self):
        self.form_intro.pushButton_4.setVisible(False)
        self.form_intro.pushButton_Save_layouts.setVisible(False)
        self.form_intro.lineEdit.setVisible(False)
        self.form_intro.pushButton_clear_all.setVisible(False)
        
    def instance_maker(self):
        global new_browser,instancer1
        if editor:
            new_browser = window_designer()
            new_browser.form_designer.toolButton_up.setVisible(True)
            new_browser.form_designer.toolButton_down.setVisible(True)
            new_browser.form_designer.toolButton_left.setVisible(True)
            new_browser.form_designer.toolButton_right.setVisible(True)
            instancer1.append(new_browser)
            new_browser.show()
        else:
            widget7.maker()
    
    def starter(self):
        print('Generating Browsers...')
        global editor,widget_intro,widget7,widget4,objector,objector1,data1,widget0,geometry1,gpt_talk
        editor = False
      
        if self.form_intro.comboBox.currentIndex() >0:
            text2 = "_".join((self.form_intro.comboBox.currentText()).split())+'.csv'
            try:

                objector1 = []
                data1 = pd.read_csv(text2)
                geometry1 = [u for u in data1["geometry"]]
            except:
                print(f'{text2} not found')         
        else:
            objector1 = []#(409, 520)
            if self.form_intro.checkBox_3.isChecked():
                self.defaults['name'].append('g-search')
                self.defaults['url'].append('https://www.google.com/search?q={query}')
                self.defaults['geometry'].append("410,440,700,380")
            
            if self.form_intro.checkBox_5.isChecked():
                self.defaults['name'].append('images-ref')
                self.defaults['url'].append('https://www.google.com/search?tbm=isch&q={query}')
                self.defaults['geometry'].append("1110,10,426,430")
            if self.form_intro.checkBox_6.isChecked():
                self.defaults['name'].append('wiki')
                self.defaults['url'].append('https://en.wikipedia.org/w/index.php?fulltext=1&search={query}&title=Special%3ASearch&ns0=1')
                self.defaults['geometry'].append("0,10,410,430")
            if self.form_intro.checkBox_2.isChecked():
                self.defaults['name'].append('yt')
                self.defaults['url'].append('https://www.youtube.com/results?search_query={query}')
                self.defaults['geometry'].append("410,10,700,452")
            if self.form_intro.checkBox.isChecked():
                self.defaults['name'].append('g-books')
                self.defaults['url'].append('https://www.google.com/search?tbm=bks&q={query}')
                self.defaults['geometry'].append("1110,300,426,520")
            data1 = pd.DataFrame(self.defaults)
            geometry1 = [u for u in data1["geometry"]]
        if self.form_intro.checkBox_4.isChecked():
            gpt_talk = True
            widget4 = window_name4()
            widget4.show()
        self.maker1()


    def docker(self):
        global widget0
        widget0 = window0()
        widget0.show()

    def maker1(self):
        global new_browser,docker_on
        for a in range(len(data1)):
            new_browser = window_designer()


            new_browser.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
            new_browser.form_designer.lineEdit.setVisible(True)
            new_browser.form_designer.lineEdit.move(125,1)
            new_browser.form_designer.widget_toolbar.setVisible(True)

            new_browser.form_designer.lineEdit_1.setVisible(False)
            new_browser.form_designer.pushButton_add.setVisible(False)
            new_browser.form_designer.pushButton_new.setVisible(False)
 
            new_browser.form_designer.webEngineView_5.move(0,0)
            
            new_browser.form_designer.widget_toolbar.move(0,0)
            new_browser.form_designer.toolButton_aerrow_left.setVisible(True)
            new_browser.form_designer.toolButton_aerrow_left.move(5,0)
            new_browser.form_designer.toolButton_aerrow_right.setVisible(True)
            new_browser.form_designer.toolButton_aerrow_right.move(30,0)
            new_browser.form_designer.toolButton_refresh.setVisible(True)
            new_browser.form_designer.toolButton_refresh.move(55,-1)
            new_browser.form_designer.pushButton_go.setVisible(True)
            new_browser.form_designer.pushButton_go.move(80,0)
            new_browser.form_designer.checkBox_freeze.setVisible(True)
            new_browser.form_designer.checkBox_freeze.move(105,3)
            new_browser.form_designer.pushButton_save_page.setVisible(True)
            new_browser.form_designer.pushButton_maximise.setVisible(True)

            new_browser.form_designer.toolButton_up.setVisible(False)
            new_browser.form_designer.toolButton_down.setVisible(False)
            new_browser.form_designer.toolButton_left.setVisible(False)
            new_browser.form_designer.toolButton_right.setVisible(False)
            objector1.append(new_browser)


        print('Connecting Browsers....')
        try:
                
            for obj0,url0,nam,geo0 in zip(objector1,data1["url"],data1['name'],geometry1):
                pos_x,pos_y,size_x,size_y = [int(r1) for r1 in geo0.split(',')]
                obj0.setGeometry(pos_x,pos_y,size_x,size_y)
                obj0.setMinimumSize(size_x, size_y)
                obj0.setWindowTitle(nam)
                obj0.form_designer.webEngineView_5.setUrl(QUrl(url0))
            if self.form_intro.comboBox_3.currentIndex()==1:
                self.docker()
                docker_on = True
            else:
                for abhi in objector1:
                    abhi.show()
                    time.sleep(0.01)
            print('Connected.') 
        except Exception as err1:
            print('Unable to Connect',err1)

        researcher_starter()
        
    


file_exists22 = os.path.isfile('searches_list.csv')
with open('searches_list.csv', mode='a', newline='') as file43:
    writer = csv.writer(file43)
    if not file_exists22:
        writer.writerow(['search_data'])


class window_name7(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

      
        from researcher import Ui_researcher
        self.setWindowOpacity(0.7)
        self.form7 = Ui_researcher()
        self.form7.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.form7.toolButton_mic.setIcon(QIcon('images\\mic.ico'))
        self.form7.toolButton.setIcon(QIcon('images\\search.ico'))
        

        self.form7.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid rgb(137, 143, 255); /* Custom border color */
                border-radius: 12px; /* Optional: Make the corners rounded */
                
                                          
                background-color: rgb(29, 29, 29); /* Background color */
                alternate-background-color: rgb(225, 225, 225); /* Alternate background color */
                selection-background-color: rgb(137, 143, 255); /* Selected text background color */
                selection-color: rgb(0, 0, 0); /* Selected text color */
                color: rgb(83, 248, 195); /* Text color */
            }
        """)


        self.model = QStringListModel()
        
        # Create a QCompleter and set the model
        self.completer = QCompleter(self.model)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.form7.lineEdit.setCompleter(self.completer)

        self.form7.lineEdit.returnPressed.connect(self.search)
        self.setWindowIcon(QIcon('Designer.ico'))
        self.form7.actionExit.triggered.connect(self.exit)
        self.form7.actionLast_Saved.triggered.connect(self.lastsaved)
        self.form7.actionTake.triggered.connect(self.taker)
        self.form7.actionOpen_Folder.triggered.connect(self.opener)
        self.form7.actionReset_Url.triggered.connect(self.defaulter)
        self.form7.actionInfo.triggered.connect(self.abouts)
        self.form7.actionNew_Browser.triggered.connect(self.maker)
        self.form7.action_Hide.triggered.connect(self.showMinimized)
        self.form7.action_search_withoutgpt.triggered.connect(self.search)
        self.form7.actionHide_minimise.triggered.connect(self.minimiser)
        self.form7.actionhistory.triggered.connect(self.history_view)
        self.form7.actionGenerate_PDF.triggered.connect(create_pdf_from_images)
        self.form7.actionArrange_Windows.triggered.connect(self.organiser)
        self.form7.actionDrag_Notes_maker.triggered.connect(self.notes_maker)
        self.form7.actionPython_Code_Tester.triggered.connect(self.tester)
        self.form7.toolButton.clicked.connect(self.google_connector)
        self.form7.toolButton_2.clicked.connect(self.minimiser)
        self.installEventFilter(self)
        self.form7.lineEdit.textChanged.connect(self.adjust_window_size)
        self.adjust_window_size()
        self.form7.actionHide_Borders.triggered.connect(self.hide_border)
        self.form7.toolButton_mic.clicked.connect(self.listener)
        self.form7.actionShare.triggered.connect(self.uploader)
        self.lastsaved()
       
        #self.form7.action_clearcache.triggered.connect(self.refresher)
        self.form7.actionClear_History.triggered.connect(self.clear_mem)
      
        self.snap1=0
        self.txt3=''
        self.min1 = False
        self.border = True

        self.searches = []
        self.list_view = self.completer.popup()  # Use popup() to get the QListView
        self.list_view.setStyleSheet("""
            QListView {
                background-color: rgb(43, 43, 43);
                color: rgb(83, 248, 195);
                border: 1px solid gray;
            }
            QListView::item {
                padding: 5px;
            }
            QListView::item:selected {
                background-color: rgb(20, 20, 20);
                color: rgb(255, 255, 255);
            }
        """)
    

        
        '''def refresher(self):
            for caches in objector1:
                caches.form_designer.webEngineView_5.history().clear()

                caches.form_designer.webEngineView_5.page().profile().clearHttpCache()'''
        
        
        self.intro_obj_delete()
       
        self.refresher()


    def uploader(self):
        import requests

        # Open file dialog to select a file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "All Files (*)")
        
        if file_path:
            # Print the full file path (location), name, and format in one line
            print(f"File Path: {file_path}")



            TOKEN = '5910714156:AAEJdmAsoi6wR0MfqKMae0iTtq0Ib1--xzE'
            CHAT_ID = 1309636266
            #for sending File to telegram bot from computer
            #start--------------------------------------------------------------------
            #for Sending file to telegram bot
            url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
            #file_path = input('just drag and drop here = ').strip('"')


            file_name = os.path.basename(file_path)     # Get the file name
            file_format = file_name.split('.')[-1]

            try:

                with open(file_path, "rb") as f:
                    response = requests.post(url, data={"chat_id": CHAT_ID}, files={"document": f})
                    #print(response.json())
                print('File Saved.')

                self.form7.lineEdit.setText(str(file_name +' is Saved'))
            except:
                print('File Not saved')
                
                self.form7.lineEdit.setText(str(file_name +' is Saved'))


    def clear_mem(self):
        for obx in objector1:
            obx.form_designer.webEngineView_5.page().profile().clearHttpCache()
            obx.form_designer.webEngineView_5.page().profile().cookieStore().deleteAllCookies()
            obx.form_designer.webEngineView_5.page().history().clear()
            os.system('cls')
            print('memory cleared')

    def intro_obj_delete(self):
        global widget_intro
        widget_intro.deleteLater()
        
        del widget_intro


    def refresher(self):
        global df2
        df2 = pd.read_csv('searches_list.csv')
        self.searches = df2['search_data']
        self.set_suggestions(self.searches)


    def listener(self):
        self.form7.lineEdit.setText('Say something...')
        Thread(target=alice).start()
        
        

    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)

    def hide_border(self):
       
        if self.border:
            for obj4 in objector1:
                obj4.setWindowFlags(Qt.FramelessWindowHint)
                obj4.show()
            self.form7.actionHide_Borders.setText('Show Borders')
            if gpt_talk:
                widget4.setWindowFlags(Qt.FramelessWindowHint)
                widget4.show()
            self.border = False
        else:
            for obj4 in objector1:
                obj4.setWindowFlags(Qt.Window)
                
                obj4.show()
                #obj4.setGeometry(int(obj4.geometry().x())+30,int(obj4.geometry().y())-30,obj4.geometry().width(),obj4.geometry().height())#today
            self.form7.actionHide_Borders.setText('Hide Borders')
            if gpt_talk:
                widget4.setWindowFlags(Qt.Window)
                widget4.show()
            self.border = True

    def print_page_text(self):
        widget4.form.webEngineView_4.page().toPlainText(self.process_text)

    def process_text(self, text):
        lines = text.splitlines()  # Split lines without any arguments
        filtered_lines = lines[7:10]  # Skip the first 6 lines
        filtered_text = '\n'.join(filtered_lines)
        print(filtered_text)

        pyttsx3.speak(filtered_text)



    def adjust_window_size(self):
        self.setWindowOpacity(1)
        text_width = self.form7.lineEdit.fontMetrics().boundingRect(self.form7.lineEdit.text()).width() + 95
        min_width = 600
        new_width = max(min_width, text_width)

        if text_width>=600:
            self.form7.toolButton_2.move(text_width-35,4)
            self.form7.toolButton.move(text_width-60,4)
            self.form7.toolButton_mic.move(text_width-90,4)
        elif text_width==95:
            self.form7.toolButton_2.move(570,4)
            self.form7.toolButton.move(550,6)
            self.form7.toolButton_mic.move(524,6)
        self.form7.lineEdit.setFixedWidth(new_width)  
        self.setFixedSize(new_width, 70)
        self.center_window()
        

    def center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - 80)
        self.move(x, y)

    def eventFilter(self, source, event):
        if event.type() == QEvent.HoverMove:
            self.setWindowOpacity(1)
        elif event.type() == QEvent.Leave:
            self.setWindowOpacity(0.5)
        return super(window_name7, self).eventFilter(source, event)

    def tester(self):
        os.system('start python tester.py')
        widget4.form.pushButton.setStyleSheet('background-color: rgb(16, 163, 127);color: rgb(255, 255, 255);')
    
    def notes_maker(self):
        global widget_notes
        widget_notes = window_notes()
        widget_notes.show()

    def organiser(self):
        for obj3,geo3 in zip(objector1,geometry1):
            x4,y4,width4,hight4 = [int(k) for k in geo3.split(',')]
            obj3.setGeometry(x4,y4,width4,hight4)

    def history_view(self):
        global widget_hist
        widget_hist = window_history()
        widget_hist.show()
              
    def minimiser(self):

        if docker_on:
            if self.min1==False:

                widget0.hide()
                self.min1 = True
            else:
                widget0.show()
                self.min1 = False
        else:



            if self.min1==False:
                if gpt_talk:
                    widget4.hide()
                for obj2 in objector1:
                    obj2.hide()
                self.form7.actionHide_minimise.setText('Maximize')
                if len(objector)==0:
                    pass
                else:
                    for obj3 in objector:
                        obj3.hide()
                self.min1 = True
            else:
                if gpt_talk:
                    widget4.show()
                for obj2 in objector1:
                
                    obj2.show()
                self.form7.actionHide_minimise.setText('Minimize')
                if len(objector)==0:
                    pass
                else:
                    for obj3 in objector:
                        obj3.show()
                self.min1 = False

    def maker(self):
        global new_browser
        new_browser = window_designer()
        
        new_browser.form_designer.lineEdit_1.setVisible(False)
        new_browser.form_designer.pushButton_add.setVisible(False)
        new_browser.form_designer.pushButton_new.setVisible(False)
        new_browser.form_designer.toolButton_up.setVisible(False)
        new_browser.form_designer.toolButton_down.setVisible(False)
        new_browser.form_designer.toolButton_left.setVisible(False)
        new_browser.form_designer.toolButton_right.setVisible(False)
  


        new_browser.form_designer.lineEdit.setVisible(True)
        new_browser.form_designer.lineEdit.move(125,1)
        new_browser.form_designer.widget_toolbar.setVisible(True)

        new_browser.form_designer.lineEdit_1.setVisible(False)

        new_browser.form_designer.webEngineView_5.move(0,0)
        
        new_browser.form_designer.widget_toolbar.move(0,0)
        new_browser.form_designer.toolButton_aerrow_left.setVisible(True)
        new_browser.form_designer.toolButton_aerrow_left.move(5,0)
        new_browser.form_designer.toolButton_aerrow_right.setVisible(True)
        new_browser.form_designer.toolButton_aerrow_right.move(30,0)
        new_browser.form_designer.toolButton_refresh.setVisible(True)
        new_browser.form_designer.toolButton_refresh.move(55,-1)
        new_browser.form_designer.pushButton_go.setVisible(True)
        new_browser.form_designer.pushButton_go.move(80,0)
        new_browser.form_designer.checkBox_freeze.setVisible(True)
        new_browser.form_designer.checkBox_freeze.move(105,3)
        new_browser.form_designer.pushButton_save_page.setVisible(True)
        new_browser.form_designer.pushButton_maximise.setVisible(True)

        new_browser.form_designer.toolButton_up.setVisible(False)
        new_browser.form_designer.toolButton_down.setVisible(False)
        new_browser.form_designer.toolButton_left.setVisible(False)
        new_browser.form_designer.toolButton_right.setVisible(False)

        
        new_browser.show()
        objector.append(new_browser)
        

    def abouts(self):
        global widget9
        widget9 = window_name9()
        widget9.show()

    def defaulter(self):
        for new1,new2 in zip(objector1,data1["url"]):
            new1.form_designer.webEngineView_5.setUrl(QUrl(new2))
        print('Url reset')
        

    
    def opener(self):

        os.system('start screenshots')
    
    def taker(self):
       
        save_path = r'screenshots\\'
        txt2 = self.form7.lineEdit.text()
        if txt2==self.txt3:
            self.snap1+=1
            txt2 = txt2 + str(self.snap1)
        else:
            self.txt3=txt2
            self.snap1=0
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        screenshot = script()
        screenshot.save(os.path.join(save_path, f'{txt2}.jpg'))

    def lastsaved(self):
        global data_url
        with open('data_url.json', 'r') as json_file1:
            data_url = json.load(json_file1)
            for obj5,url5 in zip(objector1,data_url):
            #print(obj1,url1)
                obj5.form_designer.webEngineView_5.setUrl(QUrl(url5))
       
    def exit(self):
        self.save()
        QApplication.exit()

    def save(self):
        new2 = []
        for obj1 in objector1:
            k23 = obj1.form_designer.webEngineView_5.url().toString()
            new2.append(k23)
        try:
            with open('data_url.json', 'w') as json_file:
                json.dump(new2, json_file, indent=4)
            print("JSON file created successfully.")
        except Exception as e:
            print("Error occurred while saving JSON file:", e)
    
    def search(self):
       
        

        query = self.form7.lineEdit.text()
        if query.lower()=='close':
            QApplication.exit()
        elif query=='':
            self.form7.lineEdit.setPlaceholderText('Search & Enter...or click play button ')
        else:
            for obj1,url1 in zip(objector1,data1["url"]):
                #print(obj1,url1)
                link_new = url1.replace("{query}",query)
                if obj1.form_designer.checkBox_freeze.isChecked():
                    pass
                else:

                    obj1.form_designer.webEngineView_5.setUrl(QUrl(link_new))
                    obj1.form_designer.lineEdit.setText(link_new)
                    obj1.show()
                   
                if len(objector)>0:
                    self.browser_extender(query)

        if gpt_talk:
            widget4.showNormal()
       
        self.form7.actionHide_minimise.setText('Minimize')
        if len(objector)==0:
            pass
        else:
            for obj3 in objector:
                obj3.showNormal()
        self.min1 = False



        if gpt_talk:
            
            if widget4.form.checkBox_freeze.isChecked():
                pass
            else:
                self.type_and_press_button()

        with open('searches_list.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([query])

        #print(query)
        self.refresher()
        
        #collected_objects = collect()
        #print(f"Garbage collector collected {collected_objects} objects.")
        

    def set_suggestions(self, suggestions):
        # Update the model with the new suggestions
        self.model.setStringList(suggestions)


    def browser_extender(self,query1):
        for abhishek in objector:
            link1 = abhishek.form_designer.lineEdit.text()
            link_new = link1.replace("{query}",query1)
            if abhishek.form_designer.checkBox_freeze.isChecked():
                pass
            else:
                abhishek.form_designer.webEngineView_5.setUrl(QUrl(f"{link_new}"))
                abhishek.raise_()

                
    def google_connector(self):
        global response2
        response2 = list(search(self.form7.lineEdit.text(),30))[:len(objector1)+len(objector)]

        for a,b in enumerate(response2):
            
            
            if a!=len(objector1):
                if objector1[a].form_designer.checkBox_freeze.isChecked()==False:
                    
                    objector1[a].form_designer.webEngineView_5.setUrl(QUrl(b))
                    #print(a,b)
            else:
                break


           

        '''for objx,urlx in zip(objector1,response2):
            if objx.form_designer.checkBox_freeze.isChecked()==False:
                objx.form_designer.webEngineView_5.setUrl(QUrl(urlx))'''
                
        if gpt_talk:
                
            if widget4.form.checkBox_freeze.isChecked():
                pass
            else:
                self.type_and_press_button()

        if len(objector)>0:
            for objx2,urlx2 in zip(objector,response2[len(objector1):]):
                if objx2.form_designer.checkBox_freeze.isChecked():
                    pass
                else:
                    objx2.form_designer.webEngineView_5.setUrl(QUrl(f"{urlx2}"))
                    objx2.raise_()
        
    @Slot()
    def type_and_press_button(self):
        #print('clicked\n\n\n')
        
        # JavaScript to type in the search bar and click the button
        new_text = self.form7.lineEdit.text()

        script = f"""
        var element = document.getElementById("prompt-textarea");
        if (element) {{
            element.innerHTML = "<p>{new_text}</p>";
        }}
        """
        widget4.form.webEngineView_4.page().runJavaScript(script)

        script = """
        var button = document.querySelector('button[aria-label="Send prompt"]');
        if (button) {
            button.click();
        }
        """
        # Run the JavaScript in the context of the current webpage
        
        widget4.form.webEngineView_4.page().runJavaScript(script)
    
  



class window_history(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from form_history import Ui_history
        self.form = Ui_history()
        self.form.setupUi(self)
        self.setWindowIcon(QIcon('images\\Designer 128.ico'))
    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)

class window0(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from head import Ui_head
        self.form = Ui_head()
        self.form.setupUi(self)
        self.setWindowIcon(QIcon('images\\Designer 128.ico'))
        self.setMaximumSize(screen_width,screen_height)
        self.form.label.setMaximumSize(screen_width,screen_height)
        self.form.mdiArea.setMaximumSize(screen_width,screen_height)
        from PySide6.QtCore import Qt
        self.setWindowFlags(Qt.FramelessWindowHint)
        for obj in objector1:
            self.form.mdiArea.addSubWindow(obj)

        if gpt_talk ==True:
            self.form.mdiArea.addSubWindow(widget4)
        self.showNormal()
        
    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)


class window_name9(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from about import Ui_about 
        self.form9 = Ui_about()
        self.form9.setupUi(self)
        self.setWindowIcon(QIcon('images\\Designer 128.ico'))
        #self.setWindowOpacity(0.8)

    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)
#--------------------------------------------------------------------\
# To handle webpage headers js client hints 
'''class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceID):
        if "ch-ua-form-factors" in message:
            return
        #print(f"Console message: {message} (Line: {lineNumber})")'''
#---------------------------------------------------------------------/


class window_designer(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from designer import Ui_designer
        self.form_designer = Ui_designer()
        self.form_designer.setupUi(self)
        
        self.setWindowIcon(QIcon('images\\Designer 128.ico'))
        self.resizeEvent = self.on_resize10
        
                
        self.form_designer.toolButton_aerrow_left.setIcon(QIcon('images\\aerrow_left.ico'))
        self.form_designer.toolButton_aerrow_right.setIcon(QIcon('images\\aerrow_right.ico'))
        self.form_designer.toolButton_refresh.setIcon(QIcon('images\\refresh.ico'))
        self.form_designer.pushButton_go.setIcon(QIcon('images\\redirect.ico'))
        self.form_designer.pushButton_save_page.setIcon(QIcon('images\\save_page.ico'))
        self.form_designer.pushButton_maximise.setIcon(QIcon('images\\maximise.ico'))

        self.form_designer.lineEdit_1.setGeometry(2,0,128,22)

        self.form_designer.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid rgb(0, 0, 0); /* Custom border color */
                border-radius: 8px; /* Optional: Make the corners rounded */
                
                                          
                background-color: rgb(240, 240, 240); /* Background color */
                alternate-background-color: rgb(100, 100, 100); /* Alternate background color */
                selection-background-color: rgb(137, 143, 255); /* Selected text background color */
                selection-color: rgb(0, 0, 0); /* Selected text color */
                color: rgb(0, 0, 0); /* Text color */
            }
        """)

        self.form_designer.lineEdit_1.setStyleSheet("""
            QLineEdit {
                border: 2px solid rgb(0, 0, 0); /* Custom border color */
                border-radius: 8px; /* Optional: Make the corners rounded */
                
                                          
                background-color: rgb(240, 240, 240); /* Background color */
                alternate-background-color: rgb(100, 100, 100); /* Alternate background color */
                selection-background-color: rgb(137, 143, 255); /* Selected text background color */
                selection-color: rgb(0, 0, 0); /* Selected text color */
                color: rgb(0, 0, 0); /* Text color */
            }
        """)
        self.form_designer.pushButton_add.clicked.connect(self.add_data)
        self.form_designer.lineEdit.returnPressed.connect(self.navigate)
        self.form_designer.pushButton_new.clicked.connect(self.creator)
        self.form_designer.pushButton_setup.clicked.connect(self.final_setup)
        self.form_designer.pushButton_setup.setVisible(False)
        self.form_designer.pushButton_go.clicked.connect(self.opener)

        self.form_designer.toolButton_aerrow_left.setVisible(False)
        self.form_designer.toolButton_aerrow_left.move(5,5)
        self.form_designer.toolButton_aerrow_right.setVisible(False)
        self.form_designer.toolButton_aerrow_right.move(30,5)
        self.form_designer.toolButton_refresh.setVisible(False)
        self.form_designer.toolButton_refresh.move(55,5)
        self.form_designer.pushButton_go.setVisible(False)
        self.form_designer.pushButton_go.move(80,5)
        self.form_designer.checkBox_freeze.setVisible(False)
        self.form_designer.checkBox_freeze.move(105,6)
        self.form_designer.widget_toolbar.setVisible(False)
        self.form_designer.pushButton_maximise.setVisible(False)
        self.form_designer.checkBox_freeze.clicked.connect(self.freezer_effect)

        #self.settings = self.form_designer.webEngineView_5.page().profile()
        #self.settings.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.form_designer.pushButton_save_page.setVisible(False)
        
     

        self.profile = self.form_designer.webEngineView_5.page().profile()
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, True)
        self.profile.settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanPaste, True)
        #profile.downloadRequested.connect(self.on_downloadRequested)

        #self.form_designer.webEngineView_5.setPage(CustomWebEnginePage(self))
        self.form_designer.webEngineView_5.setZoomFactor(0.8)
       
        profile1 = QWebEngineProfile.defaultProfile()
        profile1.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")

        self.form_designer.toolButton_up.clicked.connect(self.upper)
        self.form_designer.toolButton_down.clicked.connect(self.downer)
        self.form_designer.toolButton_left.clicked.connect(self.lefter)
        self.form_designer.toolButton_right.clicked.connect(self.righter)


        self.form_designer.toolButton_aerrow_left.clicked.connect(self.form_designer.webEngineView_5.back)
        self.form_designer.toolButton_aerrow_right.clicked.connect(self.form_designer.webEngineView_5.forward)
        self.form_designer.toolButton_refresh.clicked.connect(self.form_designer.webEngineView_5.reload)    
        self.form_designer.pushButton_save_page.clicked.connect(self.save_html)
        self.form_designer.pushButton_maximise.clicked.connect(self.fulldisplay)
        self.fullscreen = False

    def freezer_effect(self):
        if self.form_designer.checkBox_freeze.isChecked():
            self.form_designer.widget_toolbar.setStyleSheet("background-color: rgb(0, 39, 89);")
            self.setStyleSheet("background-color: rgb(0, 39, 89);")
        else:
            self.form_designer.widget_toolbar.setStyleSheet("background-color: rgb(32, 32, 32);")
            self.setStyleSheet("background-color: rgb(32, 32, 32);")

    def fulldisplay(self):
        
        if self.fullscreen:
            self.showNormal()
            self.fullscreen = False
        else:
            self.showFullScreen()
            self.fullscreen = True

    def save_html(self):
        # Open a file dialog to select where to save the HTML file
        file_path, _ = QFileDialog.getSaveFileName(self, "Save HTML Page", "", "HTML Files (*.html);;All Files (*)")

        # If a valid path is selected, proceed to save the HTML
        if file_path:
            # Fetch the HTML content
            self.form_designer.webEngineView_5.page().toHtml(lambda html: self.handle_html_save(html, file_path))

    def handle_html_save(self, html_content, file_path):
        # Save the HTML content to the selected file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML content saved to '{file_path}'")



    def enterEvent(self, event):
        
        # Focus the window when the mouse enters
        self.activateWindow()  # Bring window to the front
        self.setFocus(Qt.OtherFocusReason)  # Set focus explicitly
        super().enterEvent(event)


  

    def upper(self):
        self.move(self.geometry().x(),self.geometry().y()-40)
    def downer(self):
        self.move(self.geometry().x(),self.geometry().y()-5)
    def lefter(self):
        self.move(self.geometry().x()-10,self.geometry().y()-30)
    def righter(self):
        self.move(self.geometry().x()+10,self.geometry().y()-30)


    def opener(self):
        my_url = self.form_designer.webEngineView_5.url().toString()
        webbrowser.open_new_tab(my_url)

    def closeEvent(self, event):
        for loc in objector1:
            if self==loc:
                objector1.remove(self)
        self.deleteLater()
        super().closeEvent(event)
    '''def on_downloadRequested(self, download: QWebEngineDownloadRequest):
        # Open file dialog to select download location
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", download.suggestedFileName())
        
        if file_path:
            # Print debug info
            print(f"Download path selected: {file_path}")
            directory = QFileInfo(file_path).absolutePath()
            file_name = QFileInfo(file_path).fileName()

            print(f"Directory: {directory}")
            print(f"File Name: {file_name}")

            if QDir(directory).exists():
                print("Directory exists, proceeding with download.")
            else:
                print("Directory does not exist, creating directory.")
                if QDir().mkpath(directory):
                    print("Directory created successfully.")
                else:
                    print("Failed to create directory.")
                    QMessageBox.critical(self, "Error", f"Failed to create directory: {directory}")
                    return
            
            # Set the download directory and file name
            download.setDownloadDirectory(directory)
            download.setDownloadFileName(file_name)
            download.accept()

            print("Download accepted.")
        else:
            download.cancel()
            print("Download was canceled by the user.")'''

       
    def final_setup(self):
        if len(instancer1)>0:
            for inst1 in instancer1:
                inst1.close()
                inst1.deleteLater()
            
            instancer1.clear()
        
    def creator(self):
            widget_intro.instance_maker()

    def navigate(self):
        self.form_designer.webEngineView_5.setUrl(QUrl(self.form_designer.lineEdit.text()))
        
    def add_data(self):
        widget_intro.form_intro.tabWidget_2.setCurrentIndex(0)
        widget_intro.form_intro.pushButton_Save_layouts.setVisible(True)
        widget_intro.form_intro.lineEdit.setVisible(True)
        widget_intro.form_intro.pushButton_clear_all.setVisible(True)
        self.form_designer.pushButton_add.setVisible(False)
        self.form_designer.pushButton_new.setStyleSheet("background-color: rgb(76, 255, 178); color: black;")
        self.form_designer.pushButton_new.move(8,68)
        self.form_designer.pushButton_setup.move(62,68)
        row_count = widget_intro.form_intro.tableWidget.rowCount()
        widget_intro.form_intro.tableWidget.setRowCount(row_count + 1)
        name_item = QTableWidgetItem(self.form_designer.lineEdit_1.text())
        class_item = QTableWidgetItem(self.form_designer.lineEdit.text())
        geometry = self.geometry()
        self_info = QTableWidgetItem(f"{geometry.x()},{geometry.y()},{geometry.width()},{geometry.height()}")
        widget_intro.form_intro.tableWidget.setItem(row_count, 0, name_item)
        widget_intro.form_intro.tableWidget.setItem(row_count, 1, class_item)
        widget_intro.form_intro.tableWidget.setItem(row_count, 2, self_info)
        widget_intro.form_intro.pushButton_Save_layouts.setText('Save Layouts')
        self.form_designer.pushButton_setup.setVisible(True)

    def on_resize10(self, event):
        x,y = self.geometry().width(),self.geometry().height()
        self.form_designer.webEngineView_5.setGeometry(1,23,x-3,y-26)
        self.form_designer.widget_toolbar.setGeometry(0,0,x-2,23)
        self.form_designer.lineEdit.setGeometry(130,0,x-260,22)
        self.form_designer.pushButton_save_page.setGeometry(x-130,1,22,22)
        self.form_designer.pushButton_maximise.setGeometry(x-105,-1,22,22)

class WebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        print(f"\n\nJavaScript console message: {message} (source: {sourceId}, line: {lineNumber})")
        pass

class window_name4(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from window4 import Ui_window4
        self.form = Ui_window4()
        self.form.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('Designer.ico'))
        self.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.move(0,280)
        web_engine_page = WebEnginePage(self.form.webEngineView_4)  # Instantiate WebEnginePage
        self.form.webEngineView_4.setPage(web_engine_page)  # Pass WebEnginePage instance to setPage
        self.form.webEngineView_4.setUrl(QUrl("https://chatgpt.com/"))
        self.resizeEvent = self.on_resize4
        
        self.form.webEngineView_4.setZoomFactor(0.9)
        
        #self.setCentralWidget(self.form.webEngineView_4)
        self.form.webEngineView_4.page().profile().settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanAccessClipboard, True)
        self.form.webEngineView_4.page().profile().settings().setAttribute(QWebEngineSettings.WebAttribute.JavascriptCanPaste, True)
        self.form.checkBox_freeze.setChecked(False)

    def enterEvent(self, event):
        # Focus the window when the mouse enters
        self.activateWindow()  # Bring window to the front
        self.setFocus(Qt.OtherFocusReason)  # Set focus explicitly
        super().enterEvent(event)

    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)


        

    def on_resize4(self, event):
        x,y = self.geometry().width(),self.geometry().height()
        self.form.webEngineView_4.setGeometry(2,2,x-2,y-2)
        


class window_notes(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        from notes import Ui_notes
        self.form_notes = Ui_notes()
        self.form_notes.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.resizeEvent = self.on_resize12
        self.form_notes.pushButton_save_as_pdf.clicked.connect(self.save_to_pdf)
        self.form_notes.pushButton_save_as_html.clicked.connect(self.save_html)
        self.form_notes.pushButton_change_teme.clicked.connect(self.theme)

        self.dark = False
        self.theme()

    def theme(self):
     
        if self.dark==False:

            self.form_notes.textEdit.setStyleSheet('background-color: rgb(27, 27, 27);color: rgb(240, 240, 240);')
            self.form_notes.pushButton_change_teme.setText('Light theme')
            self.dark=True
        else:
            self.form_notes.textEdit.setStyleSheet('background-color: rgb(240, 240, 240);color: rgb(0, 0, 0);')
            self.form_notes.pushButton_change_teme.setText('self.dark theme')
            self.dark = False

    def closeEvent(self, event):
        self.deleteLater()
        super().closeEvent(event)

    def save_html(self):
        html_content = self.form_notes.textEdit.toHtml()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save HTML File", "", "HTML Files (*.html)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(html_content)
                self.form_notes.label.setText('Html Docs Saved.')
                #QMessageBox.information(self, "Saved", "HTML content saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save HTML content: {e}")
                self.form_notes.label.setText('Html Docs Failed to save.')

    def save_to_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF files (*.pdf)")
        try:
            if file_path:
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(file_path)
                printer.setResolution(90)  # Set resolution to 200 DPI
            
                page_size = QSize(self.geometry().width(), self.geometry().height())
                printer.setPageSize(page_size)
                painter = QPainter()
                painter.begin(printer)
                self.form_notes.textEdit.document().drawContents(painter)
                painter.end()
                self.form_notes.label.setText('PDF Saved.')
                #QMessageBox.information(self, "Saved", "PDF content saved successfully.")
        except Exception as e:  
            QMessageBox.critical(self, "Error", f"Failed to save HTML content: {e}")
            self.form_notes.label.setText('PDF failed to Save!')

    def on_resize12(self, event):
        self.form_notes.textEdit.setGeometry(5,34,self.geometry().width()-10,self.geometry().height()-39)
        self.form_notes.widget.setGeometry(0,0,self.geometry().width(),self.geometry().height())

        

if __name__ == '__main__':
    main()
    
