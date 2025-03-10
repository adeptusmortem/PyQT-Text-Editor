import sys
from PyQt5.QtWidgets import QApplication, QLabel, QTextEdit, QMainWindow, QAction, QFileDialog, QMessageBox

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title_text = 'Текстовый редактор'
        self.setWindowTitle(self.title_text)
        self.setGeometry(100, 100, 800, 600)

        self.is_saved = True
        self.current_file = None


        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        menubar = self.menuBar()

        file_menu = menubar.addMenu('Файл')

        open_action = QAction('Открыть', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('Сохранить', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        save_as_action = QAction('Сохранить как', self)
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        close_action = QAction('Закрыть', self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        create_action = QAction('Создать', self)
        create_action.triggered.connect(self.create_file)
        file_menu.addAction(create_action)
        self.text_edit.textChanged.connect(self.on_text_changeed)

    def open_file(self):
        """
        Открывает файл для редактирования.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файлы", "", "(*.txt);;(*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    self.text_edit.setText(file.read())
                    self.current_file = file_name
                    self.is_saved = True
                    self.setWindowTitle(f'{file_name} - {self.title_text}')
            except Exception as e:
                QMessageBox.critical(self, f"Ошибка при откытии файла:\n{e}")

    def save_file(self):
        """
        Сохраняет файл.
        """
        options = QFileDialog.Options()

    def save_as_file(self):
        """
        Сохраняет файл как.
        """
        options = QFileDialog.Options()

    def close_file(self):
        """
        Закрывает файл.
        """
        options = QFileDialog.Options()

    def create_file(self):
        """
        Создать файл.
        """
        options = QFileDialog.Options()

    def on_text_changeed(self):
        """
        Обработчик изменения текста.
        """
        if self.is_saved:
            self.is_saved = False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())