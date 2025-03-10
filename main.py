import sys
from PyQt5.QtWidgets import QApplication, QLabel, QTextEdit, QMainWindow, QAction, QFileDialog

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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

        close_action = QAction('Закрыть', self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)


        self.setWindowTitle('Текстовый редактор')
        self.setGeometry(100, 100, 800, 600)

    def open_file(self):
        """
        Открывает файл для редактирования.
        """
        options = QFileDialog.Options()

    def save_file(self):
        """
        Сохраняет файл.
        """
        options = QFileDialog.Options()

    def close_file(self):
        """
        Закрывает файл.
        """
        options = QFileDialog.Options()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())