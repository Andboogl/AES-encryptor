"""
This module creates the main window and handles
the graphical interface of the program
"""


import os
import random
from PyQt6.QtWidgets import QMainWindow
from design import Ui_MainWindow
import utils


class MainWindow(QMainWindow):
    """The class of the main window"""
    def __init__(self):
        QMainWindow.__init__(self)

        self.file = None
        self.result_creation_folder = None

        # Loading the interface
        self.interface = Ui_MainWindow()
        self.interface.setupUi(self)

        # Processing by pressing the buttons
        self.interface.generate_password_btn.clicked.connect(self.generate_password)
        self.interface.chose_file_path_btn.clicked.connect(self.choice_file)
        self.interface.chose_creation_path_btn.clicked.connect(self.choice_folder)
        self.interface.encrypt_btn.clicked.connect(self.encrypt)
        self.interface.decrypt_btn.clicked.connect(self.decrypt)

    def encrypt(self):
        """When the Encrypt file button is pressed"""
        password = self.interface.password.text()

        if self.file:
            if password.strip():
                if self.result_creation_folder:
                    encrypt_file_path = f'{self.result_creation_folder}/{random.randint(1, 10_000)}.aes'

                else:
                    encrypt_file_path = f'{os.path.dirname(self.file)}/{random.randint(1, 10_000)}.aes'

                try:
                    utils.encrypt(self.file, password, encrypt_file_path)
                    utils.show_message(self, f'Зашифрована версія файлу створенна за шляхом {encrypt_file_path}')

                except:
                    utils.show_message(self, 'Невірний пароль або файл невірного формату')

            else:
                utils.show_message(self, 'Введіть або згенеруйте пароль (не вказаний пароль)')

        else:
            utils.show_message(self, 'Ви не вибрали файл')

    def decrypt(self):
        """When the file decryption button is pressed"""
        password = self.interface.password.text()

        if self.file:
            if password.strip():
                if self.result_creation_folder:
                    decrypt_file_path = f'{self.result_creation_folder}/{random.randint(1, 10_000)}.txt'

                else:
                    decrypt_file_path = f'{os.path.dirname(self.file)}/{random.randint(1, 10_000)}.txt'

                try:
                    utils.decrypt(self.file, password, decrypt_file_path)
                    utils.show_message(self, f'Розшифрована версія файлу створенна за шляхом {decrypt_file_path}')

                except ValueError:
                    utils.show_message(self, 'Не вдалося розшифрувати файл (Невірний пароль або невірний формат файлу)')

            else:
                utils.show_message(self, 'Ви не ввели пароль')

        else:
            utils.show_message(self, 'Ви не вибрали файл')

    def choice_file(self):
        """When the Select file button is pressed"""
        file = utils.show_choice_file_window(self)

        if file:
            self.file = file
            self.interface.file_path.setText(self.file)

    def choice_folder(self):
        """When the Select folder button is pressed"""
        folder = utils.show_choice_folder_window(self)

        if folder:
            self.result_creation_folder = folder
            self.interface.creation_dir.setText(self.result_creation_folder)

    def generate_password(self):
        """When the password generation button is pressed"""
        password = utils.generate_password(random.choice([8, 9, 10, 11]))
        self.interface.password.setText(password)
