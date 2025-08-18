import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit , QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from logicCode import Question1_from_string, Question2_from_string


class FinallProject(QMainWindow):
    def __init__(self):
        self.Question = 1
        super().__init__()
        self.setWindowTitle("Finall Project")
        self.setGeometry(0,0,800,600)
        self.setFixedSize(800, 600) 

        self.output_box = QTextEdit(self)
        self.output_box.setReadOnly(True)
        self.output_box.setGeometry(150, 370, 400, 180)
        self.output_box.setStyleSheet("background-color: #f0f0f0;")


        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedSize(275, 200)
        self.text_edit.setGeometry(150,120,275, 200)

        self.label_input = QLabel("input:",self)
        self.label_input.setFont(QFont("Arial",11)) 
        self.label_input.setGeometry(100,125,50,30)
        self.label_input.setStyleSheet("""
           QLabel {
               color: #9370DB;
           }
        """)

        self.Qustion_label = QLabel("The least number of train stations",self)
        self.Qustion_label.setFont(QFont("Arial",11)) 
        self.Qustion_label.setGeometry(150,90,350,30)
        self.Qustion_label.setStyleSheet("""
           QLabel {
               color: #9370DB;
           }
        """)

        # دکمه‌های بنفش آبی
        self.btn_close = QPushButton("Close", self)
        self.btn_close.setGeometry(450, 120, 80, 40)
        self.btn_close.clicked.connect(self.Close)
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("""
            QPushButton {
                background-color: #8A70D6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7B68EE;
            }
            QPushButton:pressed {
                background-color: #6A5ACD;
                border: 2px solid #483D8B;
            }
        """)

        self.btn_reset = QPushButton("Reset", self)
        self.btn_reset.setGeometry(450, 170, 80, 40)
        self.btn_reset.clicked.connect(self.Reset)
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset.setStyleSheet("""
            QPushButton {
                background-color: #8A70D6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7B68EE;
            }
            QPushButton:pressed {
                background-color: #6A5ACD;
                border: 2px solid #483D8B;
            }
        """)

        # دکمه‌های طوسی
        self.btn_clear = QPushButton("Clear", self)
        self.btn_clear.setGeometry(450, 220, 80, 40)
        self.btn_clear.clicked.connect(self.Clear_Label)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet("""
            QPushButton {
                background-color: #606060;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #404040;
                border: 2px solid #303030;
            }
        """)

        self.btn_submit = QPushButton("Submit", self)
        self.btn_submit.setGeometry(450, 270, 80, 40)
        self.btn_submit.clicked.connect(self.On_Submit)
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_submit.setStyleSheet("""
            QPushButton {
                background-color: #606060;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #505050;
            }
            QPushButton:pressed {
                background-color: #404040;
                border: 2px solid #303030;
            }
        """)

        # دکمه‌های نارنجی (سوالات)
        self.btn_question1 = QPushButton("Q1",self)
        self.btn_question1.setGeometry(450 + self.btn_reset.width() + 20, 170, 80, 40)
        self.btn_question1.clicked.connect(self.Show_Question1)
        self.btn_question1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_question1.setStyleSheet("""
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF7F00;
            }
            QPushButton:pressed {
                background-color: #FF6500;
                border: 2px solid #E55A00;
            }
        """)

        self.btn_question2 = QPushButton("Q2",self)
        self.btn_question2.setGeometry(450 + self.btn_reset.width() + 20, 220, 80, 40)
        self.btn_question2.clicked.connect(self.Show_Question2)
        self.btn_question2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_question2.setStyleSheet("""
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #FF7F00;
            }
            QPushButton:pressed {
                background-color: #FF6500;
                border: 2px solid #E55A00;
            }
        """)

        self.btn_pasteTestCase = QPushButton("Paste TestCase",self)
        self.btn_pasteTestCase.setGeometry(150+90,330,110,25)
        self.btn_pasteTestCase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pasteTestCase.setStyleSheet("""
           QPushButton {
               background-color: #E91E63;
               color: white;
               border: none;
               border-radius: 3px;
               font-weight: bold;
           }
           QPushButton:hover {
               background-color: #C2185B;
           }
           QPushButton:pressed {
               background-color: #AD1457;
               border: 2px solid #880E4F;
           }
        """)  

        # ComboBox (Select Box)
        self.select_box = QComboBox(self)
        self.select_box.setGeometry(65,300, 75, 20)
        self.select_box.addItem("Them")
        self.select_box.addItem("Light")
        self.select_box.addItem("Dark")
        self.select_box.setStyleSheet("""
            QComboBox {
                background-color: #7A8471;
                color: white;
                border: 1px solid #6A7461;
                border-radius: 3px;
                padding: 3px;
                font-weight: bold;
            }
            QComboBox:hover {
                background-color: #8A9481;
            }
            QComboBox::drop-down {
                border: none;
                background-color: #6A7461;
                width: 15px;
            }
            QComboBox::down-arrow {
                border: 2px solid white;
                border-top: none;
                border-right: none;
                width: 4px;
                height: 4px;
                margin-right: 3px;
            }
            QComboBox QAbstractItemView {
                background-color: #7A8471;
                color: white;
                selection-background-color: #6A7461;
                border: 1px solid #6A7461;
            }
        """)

    def Show_Question1(self):
        self.Question = 1
        self.Qustion_label.setText("The least number of train stations")
        self.Qustion_label.setFont(QFont("Arial",11)) 
        self.Qustion_label.setGeometry(150,90,350,30)
        self.Qustion_label.setStyleSheet("""
           QLabel {
               color: #9370DB;
           }
        """)
    
    def Show_Question2(self):
        self.Question = 2
        self.Qustion_label.setText("The shortest path to the destination station")
        self.Qustion_label.setFont(QFont("Arial",11)) 
        self.Qustion_label.setGeometry(150,90,400,30)
        self.Qustion_label.setStyleSheet("""
           QLabel {
               color: #9370DB;
           }
        """)

    def Clear_Label(self):
            self.text_edit.clear()
    
    def Close(self):
            self.close()

    def On_Submit(self):
        input_text = self.text_edit.toPlainText()
        self.Calculate(input_text)


    def Calculate(self, text):
        if self.Question == 1:
            result = Question1_from_string(text)
        else:
            result = Question2_from_string(text)

        self.output_box.setPlainText(result)

        

    def Reset(self):
        self.text_edit.clear()
        self.select_box.setCurrentIndex(0)
        self.setGeometry(0,0,800,600)
        self.setFixedSize(800, 600)
        self.Question = 1 
        self.Show_Question1()


def main():
  app = QApplication(sys.argv)
  window = FinallProject()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()