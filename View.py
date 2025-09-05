import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from logicCode import Question1_from_string, Question2_from_string



class FinallProject(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Question = 1
        
        # --- تعریف استایل‌شیت‌ها برای تم روشن و تاریک ---
        self.setup_stylesheets()

        self.setWindowTitle("Finall Project")
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)

        self.setup_ui()

        self.change_theme("Light")

    def setup_ui(self):
        """متدی برای ساخت و چیدمان تمام ویجت‌ها"""
        self.output_box = QTextEdit(self)
        self.output_box.setReadOnly(True)
        self.output_box.setGeometry(150, 370, 400, 180)

        self.text_edit = QTextEdit(self)
        self.text_edit.setFixedSize(275, 200)
        self.text_edit.setGeometry(150, 120, 275, 200)

        self.label_input = QLabel("input:", self)
        self.label_input.setFont(QFont("Arial", 11))
        self.label_input.setGeometry(100, 125, 50, 30)

        self.Qustion_label = QLabel("The least number of train stations", self)
        self.Qustion_label.setFont(QFont("Arial", 11))
        self.Qustion_label.setGeometry(150, 90, 350, 30)
        
        # --- دکمه‌ها ---
        self.btn_close = QPushButton("Close", self)
        self.btn_close.setGeometry(450, 120, 80, 40)
        self.btn_close.clicked.connect(self.close)
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setObjectName("purple_button") # نام‌گذاری برای استایل‌دهی

        self.btn_reset = QPushButton("Reset", self)
        self.btn_reset.setGeometry(450, 170, 80, 40)
        self.btn_reset.clicked.connect(self.Reset)
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset.setObjectName("purple_button")

        self.btn_clear = QPushButton("Clear", self)
        self.btn_clear.setGeometry(450, 220, 80, 40)
        self.btn_clear.clicked.connect(self.Clear_Label)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear.setObjectName("gray_button")

        self.btn_submit = QPushButton("Submit", self)
        self.btn_submit.setGeometry(450, 270, 80, 40)
        self.btn_submit.clicked.connect(self.On_Submit)
        self.btn_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_submit.setObjectName("gray_button")

        self.btn_question1 = QPushButton("Q1", self)
        self.btn_question1.setGeometry(450 + self.btn_reset.width() + 20, 170, 80, 40)
        self.btn_question1.clicked.connect(self.Show_Question1)
        self.btn_question1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_question1.setObjectName("orange_button")

        self.btn_question2 = QPushButton("Q2", self)
        self.btn_question2.setGeometry(450 + self.btn_reset.width() + 20, 220, 80, 40)
        self.btn_question2.clicked.connect(self.Show_Question2)
        self.btn_question2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_question2.setObjectName("orange_button")

        self.btn_pasteTestCase = QPushButton("Paste TestCase", self)
        self.btn_pasteTestCase.setGeometry(150 + 90, 330, 110, 25)
        self.btn_pasteTestCase.clicked.connect(self.paste_from_clipboard) # اتصال دکمه به تابع
        self.btn_pasteTestCase.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pasteTestCase.setObjectName("pink_button")

        # --- ComboBox برای انتخاب تم ---
        self.select_box = QComboBox(self)
        self.select_box.setGeometry(65, 300, 75, 20)
        self.select_box.addItems(["Light", "Dark"])
        self.select_box.currentTextChanged.connect(self.change_theme) # اتصال به تابع تغییر تم


    def setup_stylesheets(self):
        """متدی برای تعریف استایل‌شیت‌های مختلف برنامه"""
        self.light_stylesheet = """
            QMainWindow { background-color: #f0f0f0; }
            QLabel { color: #9370DB; }
            QTextEdit { background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 4px; }
            QTextEdit#output_box { background-color: #e9e9e9; }
            QPushButton { border: none; border-radius: 5px; font-weight: bold; color: white; }
            QPushButton#purple_button { background-color: #8A70D6; }
            QPushButton#purple_button:hover { background-color: #7B68EE; }
            QPushButton#purple_button:pressed { background-color: #6A5ACD; border: 2px solid #483D8B; }
            QPushButton#gray_button { background-color: #606060; }
            QPushButton#gray_button:hover { background-color: #505050; }
            QPushButton#gray_button:pressed { background-color: #404040; border: 2px solid #303030; }
            QPushButton#orange_button { background-color: #FF8C00; }
            QPushButton#orange_button:hover { background-color: #FF7F00; }
            QPushButton#orange_button:pressed { background-color: #FF6500; border: 2px solid #E55A00; }
            QPushButton#pink_button { background-color: #E91E63; }
            QPushButton#pink_button:hover { background-color: #C2185B; }
            QPushButton#pink_button:pressed { background-color: #AD1457; border: 2px solid #880E4F; }
            QComboBox { background-color: #7A8471; color: white; border: 1px solid #6A7461; border-radius: 3px; padding: 3px; font-weight: bold; }
            QComboBox QAbstractItemView { background-color: #7A8471; color: white; selection-background-color: #6A7461; }
        """

        self.dark_stylesheet = """
            QMainWindow { background-color: #2E2E2E; }
            QLabel { color: #AFA8D6; } /* رنگ لیبل در حالت دارک کمی روشن‌تر شد */
            QTextEdit { background-color: #3C3C3C; color: #FFFFFF; border: 1px solid #4f4f4f; border-radius: 4px; }
            QTextEdit#output_box { background-color: #333333; }
            QPushButton { border: none; border-radius: 5px; font-weight: bold; color: white; }
            QPushButton#purple_button { background-color: #8A70D6; }
            QPushButton#purple_button:hover { background-color: #7B68EE; }
            QPushButton#purple_button:pressed { background-color: #6A5ACD; border: 2px solid #483D8B; }
            QPushButton#gray_button { background-color: #606060; }
            QPushButton#gray_button:hover { background-color: #505050; }
            QPushButton#gray_button:pressed { background-color: #404040; border: 2px solid #303030; }
            QPushButton#orange_button { background-color: #FF8C00; }
            QPushButton#orange_button:hover { background-color: #FF7F00; }
            QPushButton#orange_button:pressed { background-color: #FF6500; border: 2px solid #E55A00; }
            QPushButton#pink_button { background-color: #E91E63; }
            QPushButton#pink_button:hover { background-color: #C2185B; }
            QPushButton#pink_button:pressed { background-color: #AD1457; border: 2px solid #880E4F; }
            QComboBox { background-color: #555555; color: white; border: 1px solid #666666; border-radius: 3px; padding: 3px; font-weight: bold; }
            QComboBox QAbstractItemView { background-color: #555555; color: white; selection-background-color: #6A6A6A; }
        """

    def change_theme(self, theme_name):
        """بر اساس نام تم، استایل برنامه را تغییر می‌دهد"""
        if theme_name == "Light":
            self.setStyleSheet(self.light_stylesheet)
        elif theme_name == "Dark":
            self.setStyleSheet(self.dark_stylesheet)
        # اگه آیتم Them انتخاب بشه، تم رو به حالت پیش‌فرض برمی‌گردونه
        else:
             self.setStyleSheet("") # پاک کردن استایل کلی

    def paste_from_clipboard(self):
        """متن را از کلیپ‌بورد در تکست‌باکس ورودی قرار می‌دهد"""
        clipboard = QApplication.clipboard()
        self.text_edit.setPlainText(clipboard.text())

    # --- بقیه توابع شما بدون تغییر باقی می‌مانند ---
    def Show_Question1(self):
        self.Question = 1
        self.Qustion_label.setText("The least number of train stations")
        self.Qustion_label.setFont(QFont("Arial", 11))
        self.Qustion_label.setGeometry(150, 90, 350, 30)

    def Show_Question2(self):
        self.Question = 2
        self.Qustion_label.setText("The shortest path to the destination station")
        self.Qustion_label.setFont(QFont("Arial", 11))
        self.Qustion_label.setGeometry(150, 90, 400, 30)

    def Clear_Label(self):
        self.text_edit.clear()

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
        self.output_box.clear()
        self.select_box.setCurrentIndex(0)
        self.Question = 1
        self.Show_Question1()


def main():
    app = QApplication(sys.argv)
    window = FinallProject()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
