"""Main module. Launches the program"""


from PyQt6.QtWidgets import QApplication
from app import MainWindow
from sys import argv


def main():
    """Starting the program"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
