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
        self.close_file()
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
        close_action.triggered.connect(self.close_file)
        file_menu.addAction(close_action)

        create_action = QAction('Создать', self)
        create_action.triggered.connect(self.create_file)
        file_menu.addAction(create_action)

        # test_action = QAction('test', self)
        # test_action.triggered.connect(self.test_file)
        # file_menu.addAction(test_action)

        self.text_edit.textChanged.connect(self.on_text_changeed)

    def open_file(self):
        """
        Открывает файл для редактирования.
        """
        if self.save_if_changed():
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
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
                    self.is_saved = True
            except Exception as e:
                QMessageBox.critical(self, f"Ошибка при сохранении файла:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        """
        Сохраняет файл как.
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл как", "", "(*.txt);;(*)", options=options)
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
                    self.current_file = file_name
                    self.is_saved = True
            except Exception as e:
                QMessageBox.critical(self, f"Ошибка при сохранении файла:\n{e}")

    def close_file(self):
        """
        Закрывает файл.
        """
        if self.save_if_changed():
            self.current_file = None
            self.text_edit.clear()
            self.text_edit.setReadOnly(True)
            self.setWindowTitle(self.title_text)
            self.is_saved = True

    def save_if_changed(self) -> bool:
        """
        Сохраняет файл, если он был изменен. Возвращает False, если отмена, иначе True.
        """
        if not self.is_saved:
            msgBox = QMessageBox()
            msgBox.setText('Несохраненные изменения')
            msgBox.setInformativeText('Есть несохраненные изменения. Сохранить?')
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            reply = msgBox.exec()
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                return False
            return True

    def create_file(self):
        """
        Создать файл.
        """
        self.close_file()
        self.text_edit.setReadOnly(False)
        self.setWindowTitle(f'Новый файл - {self.title_text}')

    def test_file(self):
        pass

    def on_text_changeed(self):
        """
        Обработчик изменения текста.
        """
        if self.is_saved:
            self.is_saved = False
            self.setWindowTitle(f'*{self.windowTitle()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())